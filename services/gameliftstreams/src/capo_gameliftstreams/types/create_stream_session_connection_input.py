"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamSessionConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.signal_request


class CreateStreamSessionConnectionInput(TypedDict, closed=True):
    client_token: NotRequired["capo_gameliftstreams.types.client_token.ClientToken"]
    """<p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>"""
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p> The stream group that you want to run this stream session with. The stream group must be in <code>ACTIVE</code> status. </p>"""
    stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p> <p> The stream session must be in <code>PENDING_CLIENT_RECONNECTION</code> or <code>ACTIVE</code> status. </p>"""
    signal_request: "capo_gameliftstreams.types.signal_request.SignalRequest"
    """<p>A WebRTC ICE offer string to use when initializing a WebRTC connection. The offer is a very long JSON string. Provide the string as a text value in quotes. The offer must be newly generated, not the same offer provided to <code>StartStreamSession</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamSessionConnectionInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["SignalRequest"] = value["signal_request"]
    return out


def deserialize_json(data: dict) -> CreateStreamSessionConnectionInput:
    out: CreateStreamSessionConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("SignalRequest") is not None:
        out["signal_request"] = data["SignalRequest"]
    else:
        raise DeserializationError(
            "CreateStreamSessionConnectionInput.signal_request required"
        )
    return out
