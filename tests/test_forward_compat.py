"""Forward compatibility: a client keeps working after the service model grows.

AWS adds union members, enum values and event-stream events to a service
without a new API version, so a client generated before the change must
neither fail on them in a reply nor refuse to send a value it doesn't know.
Each test fakes a reply (or captures the request) carrying a name this client
was not generated with, once per protocol that has the shape:

* restJson1 - bedrock-runtime
* restXml - s3
* rpcv2Cbor - eventbridgev2 (skipped on Pyodide, which has no cbor2)
* awsQuery - iam
* ec2Query - ec2

All offline (mocked HTTP), so free. ``ry`` generates the sync twins.
"""

from __future__ import annotations

import json
from typing import Any

import pytest
from capo_bedrock_runtime import AsyncBedrockRuntimeClient, BedrockRuntimeClient
from capo_ec2 import AsyncEC2Client, EC2Client
from capo_iam import AsyncIAMClient, IAMClient
from capo_s3 import AsyncS3Client, S3Client
from capo_s3._protocol.eventstream import Message
from zapros import Request, Response
from zapros.matchers import method
from zapros.mock import Mock, MockMiddleware, MockRouter

CREDENTIALS = {"access_key": "AKIDEXAMPLE", "secret_key": "secret"}

# a value of an enum that the service added after this client was generated
FUTURE: Any = "FUTURE_VALUE"

USER_MESSAGE = [{"role": "user", "content": [{"text": "hi"}]}]
CONVERSE_USAGE = {"inputTokens": 1, "outputTokens": 1, "totalTokens": 2}
SELECT_QUERY: dict[str, Any] = {
    "expression": "SELECT * FROM S3Object",
    "expression_type": "SQL",
    "input_serialization": {"csv": {}},
    "output_serialization": {"csv": {}},
}
CBOR_HEADERS = {"smithy-protocol": "rpc-v2-cbor", "content-type": "application/cbor"}


def offline(
    client_cls: Any,
    http_method: str,
    response: Response,
    sent: list[Request] | None = None,
) -> Any:
    """A ``client_cls`` whose only request is answered with ``response``; it is appended to ``sent``."""

    def answer(request: Request) -> Response:
        if sent is not None:
            sent.append(request)
        return response

    router = MockRouter().add(Mock.given(method(http_method)).callback(answer).once())
    return client_cls(region="us-east-1", credentials=CREDENTIALS, http_handler=MockMiddleware(router))


def json_reply(body: Any) -> Response:
    return Response(200, {"content-type": "application/json"}, content=json.dumps(body).encode())


def xml_reply(body: str) -> Response:
    return Response(200, {"content-type": "text/xml"}, content=body.encode())


def converse_reply(output: Any = None, stop_reason: Any = "end_turn") -> Response:
    """A Converse reply; the default output is an empty assistant message."""
    if output is None:
        output = {"message": {"role": "assistant", "content": []}}
    body = {
        "output": output,
        "stopReason": stop_reason,
        "usage": CONVERSE_USAGE,
        "metrics": {"latencyMs": 1},
    }
    return json_reply(body)


def cbor_reply(body: Any) -> Response:
    cbor2 = pytest.importorskip("cbor2")
    return Response(200, CBOR_HEADERS, content=cbor2.dumps(body))


def event_stream(*events: tuple[str, str, bytes]) -> Response:
    """An event-stream reply of ``(event type, content type, payload)`` events."""
    frames = [
        Message(
            {":message-type": "event", ":event-type": name, ":content-type": ctype},
            payload,
        ).encode()
        for name, ctype, payload in events
    ]
    return Response(
        200,
        {"content-type": "application/vnd.amazon.eventstream"},
        content=b"".join(frames),
    )


def json_event(name: str, payload: Any) -> tuple[str, str, bytes]:
    return name, "application/json", json.dumps(payload).encode()


def body_of(request: Request) -> bytes:
    assert isinstance(request.body, bytes)
    return request.body


class TestAsyncUnknownUnionVariant:  # unasync: generate
    """A variant this client doesn't know comes back as ``{"$unknown": {"name": <wire name>}}``."""

    async def test_rest_json(self):
        reply = converse_reply(
            {
                "message": {
                    "role": "assistant",
                    "content": [{"text": "hi"}, {"hologram": {"x": 1}}],
                }
            }
        )
        async with offline(AsyncBedrockRuntimeClient, "POST", reply) as client:
            out = await client.converse("model", messages=USER_MESSAGE)
        unknown = {"$unknown": {"name": "hologram"}}
        assert out["output"]["message"]["content"] == [{"text": "hi"}, unknown]

    async def test_rest_json_top_level(self):
        async with offline(AsyncBedrockRuntimeClient, "POST", converse_reply({"hologram": {}})) as client:
            out = await client.converse("model", messages=USER_MESSAGE)
        assert out["output"] == {"$unknown": {"name": "hologram"}}

    async def test_rest_xml(self):
        body = "<MetricsConfiguration><Id>m</Id><Filter><Hologram><X>1</X></Hologram></Filter></MetricsConfiguration>"
        async with offline(AsyncS3Client, "GET", xml_reply(body)) as client:
            out = await client.get_bucket_metrics_configuration("bucket", "m")
        assert out["metrics_configuration"] == {
            "id": "m",
            "filter": {"$unknown": {"name": "Hologram"}},
        }

    async def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        reply = cbor_reply({"Name": "source", "Configuration": {"HologramConfiguration": {"X": 1}}})
        async with offline(eventbridgev2.AsyncEventBridgeV2Client, "POST", reply) as client:
            out = await client.describe_event_source("arn:aws:events:us-east-1:123456789012:event-source/source")
        unknown = {"$unknown": {"name": "HologramConfiguration"}}
        assert out == {"name": "source", "configuration": unknown}

    async def test_inside_an_event(self):
        reply = event_stream(json_event("contentBlockDelta", {"contentBlockIndex": 0, "delta": {"hologram": {}}}))
        async with offline(AsyncBedrockRuntimeClient, "POST", reply) as client:
            async with client.converse_stream("model", messages=USER_MESSAGE) as out:
                events = [e async for e in out["stream"]]
        unknown = {"$unknown": {"name": "hologram"}}
        assert events == [{"contentBlockDelta": {"content_block_index": 0, "delta": unknown}}]


class TestUnknownUnionVariant:  # unasync: generated
    """A variant this client doesn't know comes back as ``{"$unknown": {"name": <wire name>}}``."""

    def test_rest_json(self):
        reply = converse_reply(
            {
                "message": {
                    "role": "assistant",
                    "content": [{"text": "hi"}, {"hologram": {"x": 1}}],
                }
            }
        )
        with offline(BedrockRuntimeClient, "POST", reply) as client:
            out = client.converse("model", messages=USER_MESSAGE)
        unknown = {"$unknown": {"name": "hologram"}}
        assert out["output"]["message"]["content"] == [{"text": "hi"}, unknown]

    def test_rest_json_top_level(self):
        with offline(BedrockRuntimeClient, "POST", converse_reply({"hologram": {}})) as client:
            out = client.converse("model", messages=USER_MESSAGE)
        assert out["output"] == {"$unknown": {"name": "hologram"}}

    def test_rest_xml(self):
        body = "<MetricsConfiguration><Id>m</Id><Filter><Hologram><X>1</X></Hologram></Filter></MetricsConfiguration>"
        with offline(S3Client, "GET", xml_reply(body)) as client:
            out = client.get_bucket_metrics_configuration("bucket", "m")
        assert out["metrics_configuration"] == {
            "id": "m",
            "filter": {"$unknown": {"name": "Hologram"}},
        }

    def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        reply = cbor_reply({"Name": "source", "Configuration": {"HologramConfiguration": {"X": 1}}})
        with offline(eventbridgev2.EventBridgeV2Client, "POST", reply) as client:
            out = client.describe_event_source("arn:aws:events:us-east-1:123456789012:event-source/source")
        unknown = {"$unknown": {"name": "HologramConfiguration"}}
        assert out == {"name": "source", "configuration": unknown}

    def test_inside_an_event(self):
        reply = event_stream(json_event("contentBlockDelta", {"contentBlockIndex": 0, "delta": {"hologram": {}}}))
        with offline(BedrockRuntimeClient, "POST", reply) as client:
            with client.converse_stream("model", messages=USER_MESSAGE) as out:
                events = [e for e in out["stream"]]
        unknown = {"$unknown": {"name": "hologram"}}
        assert events == [{"contentBlockDelta": {"content_block_index": 0, "delta": unknown}}]


class TestAsyncUnknownEnumValue:  # unasync: generate
    """An enum value this client doesn't know comes back as the plain string."""

    async def test_rest_json(self):
        async with offline(AsyncBedrockRuntimeClient, "POST", converse_reply(stop_reason=FUTURE)) as client:
            out = await client.converse("model", messages=USER_MESSAGE)
        assert out["stop_reason"] == FUTURE

    async def test_rest_xml(self):
        body = f"<VersioningConfiguration><Status>{FUTURE}</Status></VersioningConfiguration>"
        async with offline(AsyncS3Client, "GET", xml_reply(body)) as client:
            out = await client.get_bucket_versioning("bucket")
        assert out == {"status": FUTURE}

    async def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        reply = cbor_reply({"Name": "source", "State": FUTURE})
        async with offline(eventbridgev2.AsyncEventBridgeV2Client, "POST", reply) as client:
            out = await client.describe_event_source("arn:aws:events:us-east-1:123456789012:event-source/source")
        assert out == {"name": "source", "state": FUTURE}

    async def test_aws_query(self):
        body = (
            "<ListAccessKeysResponse><ListAccessKeysResult><AccessKeyMetadata><member>"
            f"<AccessKeyId>AKID</AccessKeyId><Status>{FUTURE}</Status>"
            "</member></AccessKeyMetadata><IsTruncated>false</IsTruncated></ListAccessKeysResult></ListAccessKeysResponse>"
        )
        async with offline(AsyncIAMClient, "POST", xml_reply(body)) as client:
            out = await client.list_access_keys()
        assert out["access_key_metadata"] == [{"access_key_id": "AKID", "status": FUTURE}]

    async def test_ec2_query(self):
        body = (
            "<DescribeInstanceTypesResponse><instanceTypeSet><item>"
            f"<instanceType>{FUTURE}</instanceType><hypervisor>{FUTURE}</hypervisor>"
            "</item></instanceTypeSet></DescribeInstanceTypesResponse>"
        )
        async with offline(AsyncEC2Client, "POST", xml_reply(body)) as client:
            out = await client.describe_instance_types()
        assert out["instance_types"] == [{"instance_type": FUTURE, "hypervisor": FUTURE}]


class TestUnknownEnumValue:  # unasync: generated
    """An enum value this client doesn't know comes back as the plain string."""

    def test_rest_json(self):
        with offline(BedrockRuntimeClient, "POST", converse_reply(stop_reason=FUTURE)) as client:
            out = client.converse("model", messages=USER_MESSAGE)
        assert out["stop_reason"] == FUTURE

    def test_rest_xml(self):
        body = f"<VersioningConfiguration><Status>{FUTURE}</Status></VersioningConfiguration>"
        with offline(S3Client, "GET", xml_reply(body)) as client:
            out = client.get_bucket_versioning("bucket")
        assert out == {"status": FUTURE}

    def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        reply = cbor_reply({"Name": "source", "State": FUTURE})
        with offline(eventbridgev2.EventBridgeV2Client, "POST", reply) as client:
            out = client.describe_event_source("arn:aws:events:us-east-1:123456789012:event-source/source")
        assert out == {"name": "source", "state": FUTURE}

    def test_aws_query(self):
        body = (
            "<ListAccessKeysResponse><ListAccessKeysResult><AccessKeyMetadata><member>"
            f"<AccessKeyId>AKID</AccessKeyId><Status>{FUTURE}</Status>"
            "</member></AccessKeyMetadata><IsTruncated>false</IsTruncated></ListAccessKeysResult></ListAccessKeysResponse>"
        )
        with offline(IAMClient, "POST", xml_reply(body)) as client:
            out = client.list_access_keys()
        assert out["access_key_metadata"] == [{"access_key_id": "AKID", "status": FUTURE}]

    def test_ec2_query(self):
        body = (
            "<DescribeInstanceTypesResponse><instanceTypeSet><item>"
            f"<instanceType>{FUTURE}</instanceType><hypervisor>{FUTURE}</hypervisor>"
            "</item></instanceTypeSet></DescribeInstanceTypesResponse>"
        )
        with offline(EC2Client, "POST", xml_reply(body)) as client:
            out = client.describe_instance_types()
        assert out["instance_types"] == [{"instance_type": FUTURE, "hypervisor": FUTURE}]


class TestAsyncUnknownEvent:  # unasync: generate
    """An event this client doesn't know comes back keyed by ``$unknown``, and the stream goes on."""

    async def test_rest_json(self):
        reply = event_stream(
            json_event("messageStart", {"role": "assistant"}),
            json_event("hologramDelta", {"x": 1}),
            json_event("messageStop", {"stopReason": "end_turn"}),
        )
        async with offline(AsyncBedrockRuntimeClient, "POST", reply) as client:
            async with client.converse_stream("model", messages=USER_MESSAGE) as out:
                events = [e async for e in out["stream"]]
        assert events[0] == {"messageStart": {"role": "assistant"}}
        unknown = events[1]["$unknown"]
        assert unknown["name"] == "hologramDelta"
        assert unknown["message"].payload == b'{"x": 1}'
        assert events[2] == {"messageStop": {"stop_reason": "end_turn"}}

    async def test_rest_xml(self):
        reply = event_stream(
            ("Records", "application/octet-stream", b"1,ann\n"),
            ("Hologram", "text/xml", b"<Hologram><X>1</X></Hologram>"),
            ("End", "text/xml", b""),
        )
        async with offline(AsyncS3Client, "POST", reply) as client:
            async with client.select_object_content("bucket", "key.csv", **SELECT_QUERY) as out:
                events = [e async for e in out["payload"]]
        assert events[0] == {"Records": {"payload": b"1,ann\n"}}
        unknown = events[1]["$unknown"]
        assert unknown["name"] == "Hologram"
        assert unknown["message"].payload == b"<Hologram><X>1</X></Hologram>"
        assert events[2] == {"End": {}}


class TestUnknownEvent:  # unasync: generated
    """An event this client doesn't know comes back keyed by ``$unknown``, and the stream goes on."""

    def test_rest_json(self):
        reply = event_stream(
            json_event("messageStart", {"role": "assistant"}),
            json_event("hologramDelta", {"x": 1}),
            json_event("messageStop", {"stopReason": "end_turn"}),
        )
        with offline(BedrockRuntimeClient, "POST", reply) as client:
            with client.converse_stream("model", messages=USER_MESSAGE) as out:
                events = [e for e in out["stream"]]
        assert events[0] == {"messageStart": {"role": "assistant"}}
        unknown = events[1]["$unknown"]
        assert unknown["name"] == "hologramDelta"
        assert unknown["message"].payload == b'{"x": 1}'
        assert events[2] == {"messageStop": {"stop_reason": "end_turn"}}

    def test_rest_xml(self):
        reply = event_stream(
            ("Records", "application/octet-stream", b"1,ann\n"),
            ("Hologram", "text/xml", b"<Hologram><X>1</X></Hologram>"),
            ("End", "text/xml", b""),
        )
        with offline(S3Client, "POST", reply) as client:
            with client.select_object_content("bucket", "key.csv", **SELECT_QUERY) as out:
                events = [e for e in out["payload"]]
        assert events[0] == {"Records": {"payload": b"1,ann\n"}}
        unknown = events[1]["$unknown"]
        assert unknown["name"] == "Hologram"
        assert unknown["message"].payload == b"<Hologram><X>1</X></Hologram>"
        assert events[2] == {"End": {}}


class TestAsyncSendNewEnumValue:  # unasync: generate
    """An enum value newer than this client goes on the wire as given."""

    async def test_rest_json(self):
        sent: list[Request] = []
        async with offline(AsyncBedrockRuntimeClient, "POST", converse_reply(), sent) as client:
            await client.converse("model", messages=USER_MESSAGE, performance_config={"latency": FUTURE})
        assert json.loads(body_of(sent[0]))["performanceConfig"] == {"latency": FUTURE}

    async def test_rest_xml_body(self):
        sent: list[Request] = []
        async with offline(AsyncS3Client, "PUT", Response(200), sent) as client:
            await client.put_bucket_versioning("bucket", versioning_configuration={"status": FUTURE})
        expected = f"<VersioningConfiguration><Status>{FUTURE}</Status></VersioningConfiguration>"
        assert body_of(sent[0]) == expected.encode()

    async def test_rest_xml_header(self):
        sent: list[Request] = []
        async with offline(AsyncS3Client, "PUT", Response(200), sent) as client:
            await client.put_object("bucket", "key", body=b"data", storage_class=FUTURE)
        assert sent[0].headers["x-amz-storage-class"] == FUTURE

    async def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        cbor2 = pytest.importorskip("cbor2")
        sent: list[Request] = []
        async with offline(eventbridgev2.AsyncEventBridgeV2Client, "POST", cbor_reply({}), sent) as client:
            await client.update_subscriber("arn:aws:events:us-east-1:123456789012:subscriber/s", state=FUTURE)
        assert cbor2.loads(body_of(sent[0]))["State"] == FUTURE

    async def test_aws_query(self):
        sent: list[Request] = []
        body = (
            "<ListPoliciesResponse><ListPoliciesResult><IsTruncated>false</IsTruncated>"
            "</ListPoliciesResult></ListPoliciesResponse>"
        )
        async with offline(AsyncIAMClient, "POST", xml_reply(body), sent) as client:
            await client.list_policies(scope=FUTURE)
        assert f"Scope={FUTURE}".encode() in body_of(sent[0])

    async def test_ec2_query(self):
        sent: list[Request] = []
        body = "<DescribeInstanceTypesResponse><instanceTypeSet/></DescribeInstanceTypesResponse>"
        async with offline(AsyncEC2Client, "POST", xml_reply(body), sent) as client:
            await client.describe_instance_types(instance_types=[FUTURE])
        assert f"InstanceType.1={FUTURE}".encode() in body_of(sent[0])


class TestSendNewEnumValue:  # unasync: generated
    """An enum value newer than this client goes on the wire as given."""

    def test_rest_json(self):
        sent: list[Request] = []
        with offline(BedrockRuntimeClient, "POST", converse_reply(), sent) as client:
            client.converse("model", messages=USER_MESSAGE, performance_config={"latency": FUTURE})
        assert json.loads(body_of(sent[0]))["performanceConfig"] == {"latency": FUTURE}

    def test_rest_xml_body(self):
        sent: list[Request] = []
        with offline(S3Client, "PUT", Response(200), sent) as client:
            client.put_bucket_versioning("bucket", versioning_configuration={"status": FUTURE})
        expected = f"<VersioningConfiguration><Status>{FUTURE}</Status></VersioningConfiguration>"
        assert body_of(sent[0]) == expected.encode()

    def test_rest_xml_header(self):
        sent: list[Request] = []
        with offline(S3Client, "PUT", Response(200), sent) as client:
            client.put_object("bucket", "key", body=b"data", storage_class=FUTURE)
        assert sent[0].headers["x-amz-storage-class"] == FUTURE

    def test_rpc_v2_cbor(self):
        eventbridgev2 = pytest.importorskip("capo_eventbridgev2")
        cbor2 = pytest.importorskip("cbor2")
        sent: list[Request] = []
        with offline(eventbridgev2.EventBridgeV2Client, "POST", cbor_reply({}), sent) as client:
            client.update_subscriber("arn:aws:events:us-east-1:123456789012:subscriber/s", state=FUTURE)
        assert cbor2.loads(body_of(sent[0]))["State"] == FUTURE

    def test_aws_query(self):
        sent: list[Request] = []
        body = (
            "<ListPoliciesResponse><ListPoliciesResult><IsTruncated>false</IsTruncated>"
            "</ListPoliciesResult></ListPoliciesResponse>"
        )
        with offline(IAMClient, "POST", xml_reply(body), sent) as client:
            client.list_policies(scope=FUTURE)
        assert f"Scope={FUTURE}".encode() in body_of(sent[0])

    def test_ec2_query(self):
        sent: list[Request] = []
        body = "<DescribeInstanceTypesResponse><instanceTypeSet/></DescribeInstanceTypesResponse>"
        with offline(EC2Client, "POST", xml_reply(body), sent) as client:
            client.describe_instance_types(instance_types=[FUTURE])
        assert f"InstanceType.1={FUTURE}".encode() in body_of(sent[0])
