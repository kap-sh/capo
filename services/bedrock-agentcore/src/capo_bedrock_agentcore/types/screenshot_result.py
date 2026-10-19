"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ScreenshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_action_status


class ScreenshotResult(TypedDict, closed=True):
    status: "capo_bedrock_agentcore.types.browser_action_status.BrowserActionStatus"
    """<p>The status of the action execution.</p>"""
    error: NotRequired["str"]
    """<p>The error message. Present only when the action failed.</p>"""
    data: NotRequired["bytes"]
    """<p>The base64-encoded image data. Present only when the action succeeded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScreenshotResult) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.browser_action_status

    out["status"] = capo_bedrock_agentcore.types.browser_action_status.serialize_json(
        value["status"]
    )
    if "error" in value:
        out["error"] = value["error"]
    if "data" in value:
        import capo_bedrock_agentcore.types._prelude.blob

        out["data"] = capo_bedrock_agentcore.types._prelude.blob.serialize_json(
            value["data"]
        )
    return out


def deserialize_json(data: dict) -> ScreenshotResult:
    out: ScreenshotResult = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.browser_action_status

        out["status"] = (
            capo_bedrock_agentcore.types.browser_action_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.browser_action_status.BrowserActionStatus", ""
        )
    if data.get("error") is not None:
        out["error"] = data["error"]
    if data.get("data") is not None:
        import capo_bedrock_agentcore.types._prelude.blob

        out["data"] = capo_bedrock_agentcore.types._prelude.blob.deserialize_json(
            data["data"]
        )
    return out
