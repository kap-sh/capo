"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AutomationStream``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.automation_stream_status
    import capo_bedrock_agentcore.types.browser_stream_endpoint


class AutomationStream(TypedDict, closed=True):
    stream_endpoint: (
        "capo_bedrock_agentcore.types.browser_stream_endpoint.BrowserStreamEndpoint"
    )
    """<p>The endpoint URL for the automation stream. This URL is used to establish a WebSocket connection to the stream for sending commands and receiving responses.</p>"""
    stream_status: (
        "capo_bedrock_agentcore.types.automation_stream_status.AutomationStreamStatus"
    )
    """<p>The current status of the automation stream. This indicates whether the stream is available for use. Possible values include ACTIVE, CONNECTING, and DISCONNECTED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationStream) -> dict:
    out: dict = {}
    out["streamEndpoint"] = value["stream_endpoint"]
    import capo_bedrock_agentcore.types.automation_stream_status

    out["streamStatus"] = (
        capo_bedrock_agentcore.types.automation_stream_status.serialize_json(
            value["stream_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomationStream:
    out: AutomationStream = {}  # type: ignore[typeddict-item]
    if data.get("streamEndpoint") is not None:
        out["stream_endpoint"] = data["streamEndpoint"]
    else:
        out["stream_endpoint"] = ""
    if data.get("streamStatus") is not None:
        import capo_bedrock_agentcore.types.automation_stream_status

        out["stream_status"] = (
            capo_bedrock_agentcore.types.automation_stream_status.deserialize_json(
                data["streamStatus"]
            )
        )
    else:
        import typing

        out["stream_status"] = typing.cast(
            "capo_bedrock_agentcore.types.automation_stream_status.AutomationStreamStatus",
            "",
        )
    return out
