"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ConverseStreamMetadataEvent``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime._protocol.eventstream import HeaderValue, Message
from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.converse_stream_metrics
    import capo_bedrock_runtime.types.converse_stream_trace
    import capo_bedrock_runtime.types.performance_configuration
    import capo_bedrock_runtime.types.service_tier
    import capo_bedrock_runtime.types.token_usage


class ConverseStreamMetadataEvent(TypedDict, closed=True):
    usage: "capo_bedrock_runtime.types.token_usage.TokenUsage"
    """<p>Usage information for the conversation stream event.</p>"""
    metrics: "capo_bedrock_runtime.types.converse_stream_metrics.ConverseStreamMetrics"
    """<p>The metrics for the conversation stream metadata event.</p>"""
    trace: NotRequired[
        "capo_bedrock_runtime.types.converse_stream_trace.ConverseStreamTrace"
    ]
    r"""<p>The trace object in the response from <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html\">ConverseStream</a> that contains information about the guardrail behavior.</p>"""
    performance_config: NotRequired[
        "capo_bedrock_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>Model performance configuration metadata for the conversation stream event.</p>"""
    service_tier: NotRequired["capo_bedrock_runtime.types.service_tier.ServiceTier"]
    """<p>Specifies the processing tier configuration used for serving the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConverseStreamMetadataEvent) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.token_usage

    out["usage"] = capo_bedrock_runtime.types.token_usage.serialize_json(value["usage"])
    import capo_bedrock_runtime.types.converse_stream_metrics

    out["metrics"] = capo_bedrock_runtime.types.converse_stream_metrics.serialize_json(
        value["metrics"]
    )
    if "trace" in value:
        import capo_bedrock_runtime.types.converse_stream_trace

        out["trace"] = capo_bedrock_runtime.types.converse_stream_trace.serialize_json(
            value["trace"]
        )
    if "performance_config" in value:
        import capo_bedrock_runtime.types.performance_configuration

        out["performanceConfig"] = (
            capo_bedrock_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    if "service_tier" in value:
        import capo_bedrock_runtime.types.service_tier

        out["serviceTier"] = capo_bedrock_runtime.types.service_tier.serialize_json(
            value["service_tier"]
        )
    return out


def deserialize_json(data: dict) -> ConverseStreamMetadataEvent:
    out: ConverseStreamMetadataEvent = {}  # type: ignore[typeddict-item]
    if data.get("usage") is not None:
        import capo_bedrock_runtime.types.token_usage

        out["usage"] = capo_bedrock_runtime.types.token_usage.deserialize_json(
            data["usage"]
        )
    else:
        raise DeserializationError("ConverseStreamMetadataEvent.usage required")
    if data.get("metrics") is not None:
        import capo_bedrock_runtime.types.converse_stream_metrics

        out["metrics"] = (
            capo_bedrock_runtime.types.converse_stream_metrics.deserialize_json(
                data["metrics"]
            )
        )
    else:
        raise DeserializationError("ConverseStreamMetadataEvent.metrics required")
    if data.get("trace") is not None:
        import capo_bedrock_runtime.types.converse_stream_trace

        out["trace"] = (
            capo_bedrock_runtime.types.converse_stream_trace.deserialize_json(
                data["trace"]
            )
        )
    if data.get("performanceConfig") is not None:
        import capo_bedrock_runtime.types.performance_configuration

        out["performance_config"] = (
            capo_bedrock_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    if data.get("serviceTier") is not None:
        import capo_bedrock_runtime.types.service_tier

        out["service_tier"] = capo_bedrock_runtime.types.service_tier.deserialize_json(
            data["serviceTier"]
        )
    return out


def serialize_event_json(value: ConverseStreamMetadataEvent) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "metadata",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ConverseStreamMetadataEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ConverseStreamMetadataEvent = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
