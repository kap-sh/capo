"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessMetadataEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore._protocol.eventstream import HeaderValue, Message
from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_stream_metrics
    import capo_bedrock_agentcore.types.harness_token_usage


class HarnessMetadataEvent(TypedDict, closed=True):
    usage: "capo_bedrock_agentcore.types.harness_token_usage.HarnessTokenUsage"
    """<p>Token usage counts.</p>"""
    metrics: "capo_bedrock_agentcore.types.harness_stream_metrics.HarnessStreamMetrics"
    """<p>Latency metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessMetadataEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.harness_token_usage

    out["usage"] = capo_bedrock_agentcore.types.harness_token_usage.serialize_json(
        value["usage"]
    )
    import capo_bedrock_agentcore.types.harness_stream_metrics

    out["metrics"] = capo_bedrock_agentcore.types.harness_stream_metrics.serialize_json(
        value["metrics"]
    )
    return out


def deserialize_json(data: dict) -> HarnessMetadataEvent:
    out: HarnessMetadataEvent = {}  # type: ignore[typeddict-item]
    if data.get("usage") is not None:
        import capo_bedrock_agentcore.types.harness_token_usage

        out["usage"] = (
            capo_bedrock_agentcore.types.harness_token_usage.deserialize_json(
                data["usage"]
            )
        )
    else:
        raise DeserializationError("HarnessMetadataEvent.usage required")
    if data.get("metrics") is not None:
        import capo_bedrock_agentcore.types.harness_stream_metrics

        out["metrics"] = (
            capo_bedrock_agentcore.types.harness_stream_metrics.deserialize_json(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("HarnessMetadataEvent.metrics required")
    return out


def serialize_event_json(value: HarnessMetadataEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "metadata",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> HarnessMetadataEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: HarnessMetadataEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
