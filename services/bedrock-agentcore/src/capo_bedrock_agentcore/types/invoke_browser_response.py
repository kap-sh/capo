"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeBrowserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_action_result
    import capo_bedrock_agentcore.types.browser_session_id


class InvokeBrowserResponse(TypedDict, closed=True):
    result: "capo_bedrock_agentcore.types.browser_action_result.BrowserActionResult"
    """<p>The result of the browser action. The member set in the result corresponds to the action that was performed.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session on which the action was performed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeBrowserResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.browser_action_result

    out["result"] = capo_bedrock_agentcore.types.browser_action_result.serialize_json(
        value["result"]
    )
    return out


def deserialize_json(data: dict) -> InvokeBrowserResponse:
    out: InvokeBrowserResponse = {}  # type: ignore[typeddict-item]
    if data.get("result") is not None:
        import capo_bedrock_agentcore.types.browser_action_result

        out["result"] = (
            capo_bedrock_agentcore.types.browser_action_result.deserialize_json(
                data["result"]
            )
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["result"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    return out
