"""Bidirectional event streams are full duplex.

Bedrock ``InvokeModelWithBidirectionalStream`` (Nova Sonic) is a conversation:
the client keeps sending input events while the model answers, and what it
sends next often depends on what came back. The local echo server here answers
the request at once and echoes every input event the moment its frame is
complete; the client sends a turn only after the echo of the previous one came
back. A client that writes the whole request body before it reads the response
never sees the first echo, so the test fails on a timeout instead of hanging.

The client is the default one: the generated request switches itself to
cleartext HTTP/2 (prior knowledge) and full duplex through
``context["handler_overrides"]``, while other operations stay on HTTP/1.1. The
server speaks both protocols on one port and records which one each request
came over.

Offline (a server on a thread on localhost), so free.
"""

from __future__ import annotations

import socket
import threading
from collections.abc import Iterator

import anyio
import h2.config
import h2.connection
import h2.events
import h2.exceptions
import h11
import pytest
from capo_bedrock_runtime import AsyncBedrockRuntimeClient, Credentials
from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message, MessageDecoder

from tests.conftest import needs_threads

CREDENTIALS = Credentials(access_key="AKIDEXAMPLE", secret_key="secret")
EVENT_STREAM = b"application/vnd.amazon.eventstream"
H2_PREFACE = b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"
MODEL = "amazon.nova-sonic-v1:0"
TURNS = 5
# How long one turn may wait for its echo; a half-duplex client never gets it.
TURN_TIMEOUT = 5


def echo_events(decoder: MessageDecoder, data: bytes) -> Iterator[bytes]:
    """The output ``chunk`` events echoing the signed input frames completed by ``data``."""
    for signed_frame in decoder.feed(data):
        if not signed_frame.payload:  # the empty frame that closes the stream
            continue
        (event,) = MessageDecoder().feed(signed_frame.payload)
        assert event.headers[":event-type"] == "chunk"
        headers: dict[str, HeaderValue] = {
            ":message-type": "event",
            ":event-type": "chunk",
            ":content-type": "application/json",
        }
        # BidirectionalInputPayloadPart and BidirectionalOutputPayloadPart are both {"bytes": <base64>}
        yield Message(headers, event.payload).encode()


class EchoServer:
    """Echoes event-stream request bodies as they arrive, over HTTP/1.1 or HTTP/2 on one port."""

    def __init__(self) -> None:
        self.listener = socket.create_server(("127.0.0.1", 0))
        self.endpoint = f"http://127.0.0.1:{self.listener.getsockname()[1]}"
        # the protocol of every request, in the order they arrived
        self.protocols: list[str] = []

    def accept_loop(self) -> None:
        while True:
            try:
                conn, _ = self.listener.accept()
            except OSError:  # listener closed
                return
            threading.Thread(target=self.serve, args=(conn,), daemon=True).start()

    def serve(self, conn: socket.socket) -> None:
        """HTTP/2 when the client opens with the prior-knowledge preface, HTTP/1.1 otherwise."""
        with conn:
            try:
                head = conn.recv(len(H2_PREFACE), socket.MSG_PEEK | socket.MSG_WAITALL)
                (self.serve_http2 if head == H2_PREFACE else self.serve_http1)(conn)
            except (OSError, h2.exceptions.StreamClosedError):  # the client hung up or reset the stream
                pass

    def serve_http1(self, conn: socket.socket) -> None:
        """Answer requests; an event-stream body is echoed as it arrives, any other is dropped."""
        h11conn = h11.Connection(h11.SERVER)
        decoder: MessageDecoder | None = None
        while data := conn.recv(65536):
            h11conn.receive_data(data)
            while (event := h11conn.next_event()) is not h11.NEED_DATA:
                if isinstance(event, h11.Request):
                    self.protocols.append("HTTP/1.1")
                    decoder = MessageDecoder() if dict(event.headers).get(b"content-type") == EVENT_STREAM else None
                    headers = [(b"content-type", EVENT_STREAM), (b"transfer-encoding", b"chunked")]
                    conn.sendall(h11conn.send(h11.Response(status_code=200, headers=headers)))
                elif isinstance(event, h11.Data) and decoder is not None:
                    for echo in echo_events(decoder, event.data):
                        conn.sendall(h11conn.send(h11.Data(data=echo)))
                elif isinstance(event, h11.EndOfMessage):
                    conn.sendall(h11conn.send(h11.EndOfMessage()))
                    h11conn.start_next_cycle()

    def serve_http2(self, conn: socket.socket) -> None:
        h2conn = h2.connection.H2Connection(h2.config.H2Configuration(client_side=False, header_encoding=None))
        h2conn.initiate_connection()
        conn.sendall(h2conn.data_to_send())
        decoders: dict[int, MessageDecoder] = {}
        while data := conn.recv(65536):
            for event in h2conn.receive_data(data):
                if isinstance(event, h2.events.RequestReceived):
                    self.protocols.append("HTTP/2")
                    decoders[event.stream_id] = MessageDecoder()
                    h2conn.send_headers(event.stream_id, [(b":status", b"200"), (b"content-type", EVENT_STREAM)])
                elif isinstance(event, h2.events.DataReceived):
                    h2conn.acknowledge_received_data(event.flow_controlled_length, event.stream_id)
                    for echo in echo_events(decoders[event.stream_id], event.data):
                        h2conn.send_data(event.stream_id, echo)
                elif isinstance(event, h2.events.StreamEnded):
                    h2conn.end_stream(event.stream_id)
            conn.sendall(h2conn.data_to_send())


@pytest.fixture
def echo_server() -> Iterator[EchoServer]:
    server = EchoServer()
    threading.Thread(target=server.accept_loop, daemon=True).start()
    try:
        yield server
    finally:
        server.listener.close()


def make_client(server: EchoServer) -> AsyncBedrockRuntimeClient:
    return AsyncBedrockRuntimeClient(endpoint=server.endpoint, region="us-east-1", credentials=CREDENTIALS)


class TestAsyncBidirectionalStream:
    # No sync twin: the sync client drives the request body and the response from one thread.

    @needs_threads
    async def test_input_waits_for_output(self, echo_server: EchoServer):
        client = make_client(echo_server)
        send_echo, receive_echo = anyio.create_memory_object_stream[bytes](TURNS)

        async def conversation():
            for i in range(TURNS):
                said = b"turn %d" % i
                yield {"chunk": {"bytes": said}}
                with anyio.move_on_after(TURN_TIMEOUT) as wait:
                    heard = await receive_echo.receive()
                if wait.cancelled_caught:
                    pytest.fail(f"no echo of turn {i} while the request was open: the stream is not full duplex")
                assert heard == said

        echoes = []
        with anyio.fail_after(TURNS * TURN_TIMEOUT):
            async with send_echo, receive_echo, client:
                async with client.invoke_model_with_bidirectional_stream(MODEL, conversation()) as out:
                    async for event in out["body"]:
                        match event:
                            case {"chunk": {"bytes": bytes() as echo}}:
                                echoes.append(echo)
                                await send_echo.send(echo)
                            case _:
                                pytest.fail(f"unexpected event {event!r}")
        assert echoes == [b"turn %d" % i for i in range(TURNS)]
        assert echo_server.protocols == ["HTTP/2"]

    @needs_threads
    async def test_other_requests_stay_on_http1(self, echo_server: EchoServer):
        client = make_client(echo_server)

        async def one_turn():
            yield {"chunk": {"bytes": b"hi"}}

        with anyio.fail_after(TURN_TIMEOUT):
            async with client:
                await client.invoke_model(MODEL, body=b"{}")
                async with client.invoke_model_with_bidirectional_stream(MODEL, one_turn()) as out:
                    events = [event async for event in out["body"]]
                # the pooled HTTP/2 connection to the same host is not reused for it
                await client.invoke_model(MODEL, body=b"{}")
        assert events == [{"chunk": {"bytes": b"hi"}}]
        assert echo_server.protocols == ["HTTP/1.1", "HTTP/2", "HTTP/1.1"]
