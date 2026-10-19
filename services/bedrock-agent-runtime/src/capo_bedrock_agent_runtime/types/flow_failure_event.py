"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowFailureEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.flow_error_code


class FlowFailureEvent(TypedDict, closed=True):
    timestamp: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the failure occurred.</p>"""
    error_code: "capo_bedrock_agent_runtime.types.flow_error_code.FlowErrorCode"
    """<p>The error code that identifies the type of failure that occurred.</p>"""
    error_message: "str"
    """<p>A descriptive message that provides details about the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowFailureEvent) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["timestamp"] = capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_bedrock_agent_runtime.types.flow_error_code

    out["errorCode"] = capo_bedrock_agent_runtime.types.flow_error_code.serialize_json(
        value["error_code"]
    )
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FlowFailureEvent:
    out: FlowFailureEvent = {}  # type: ignore[typeddict-item]
    if data.get("timestamp") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["timestamp"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("errorCode") is not None:
        import capo_bedrock_agent_runtime.types.flow_error_code

        out["error_code"] = (
            capo_bedrock_agent_runtime.types.flow_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_bedrock_agent_runtime.types.flow_error_code.FlowErrorCode", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
