"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyPressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_action_status


class KeyPressResult(TypedDict, closed=True):
    status: "capo_bedrock_agentcore.types.browser_action_status.BrowserActionStatus"
    """<p>The status of the action execution.</p>"""
    error: NotRequired["str"]
    """<p>The error message. Present only when the action failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPressResult) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.browser_action_status

    out["status"] = capo_bedrock_agentcore.types.browser_action_status.serialize_json(
        value["status"]
    )
    if "error" in value:
        out["error"] = value["error"]
    return out


def deserialize_json(data: dict) -> KeyPressResult:
    out: KeyPressResult = {}  # type: ignore[typeddict-item]
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
    return out
