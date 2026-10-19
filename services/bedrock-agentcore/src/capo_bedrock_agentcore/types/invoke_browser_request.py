"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeBrowserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.browser_action
    import capo_bedrock_agentcore.types.browser_session_id


class InvokeBrowserRequest(TypedDict, closed=True):
    browser_identifier: "str"
    """<p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>"""
    session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId"
    """<p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>"""
    action: "capo_bedrock_agentcore.types.browser_action.BrowserAction"
    """<p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeBrowserRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.browser_action

    out["action"] = capo_bedrock_agentcore.types.browser_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> InvokeBrowserRequest:
    out: InvokeBrowserRequest = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_bedrock_agentcore.types.browser_action

        out["action"] = capo_bedrock_agentcore.types.browser_action.deserialize_json(
            data["action"]
        )
    else:
        import capo_bedrock_agentcore.types._unknown

        out["action"] = capo_bedrock_agentcore.types._unknown.UnknownUnionMember("")
    return out
