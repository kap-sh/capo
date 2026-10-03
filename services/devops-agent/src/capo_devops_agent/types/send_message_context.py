"""Generated from Smithy shape ``com.amazonaws.devopsagent#SendMessageContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.approval_action


class SendMessageContext(TypedDict, closed=True):
    current_page: NotRequired["str"]
    """<p>The current page or view the user is on</p>"""
    last_message: NotRequired["str"]
    """<p>The ID of the last message in the conversation</p>"""
    user_action_response: NotRequired["str"]
    """<p>Response to a UI prompt (not a text conversation message). Set this to the sentinel value `"APPROVAL_ACTION"` when the request is resuming a paused execution after an approval decision; in that case the structured decision is provided on the sibling `approvalAction` member. Preserved as a String for backward compatibility: clients that predate the typed approval field may still encode UI-prompt responses as JSON in this field.</p>"""
    approval_action: NotRequired[
        "capo_devops_agent.types.approval_action.ApprovalAction"
    ]
    """<p>An approval decision supplied when resuming a paused agent execution. When an agent execution pauses to request approval for an elevated action, SendMessage streams an approval request carrying interrupt identifiers. To resume the paused execution, call SendMessage again with `userActionResponse` set to `"APPROVAL_ACTION"` and this member populated with those identifiers and the decision (APPROVED or REJECTED). Optional; omit it for messages that are not resuming an approval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageContext) -> dict:
    out: dict = {}
    if "current_page" in value:
        out["currentPage"] = value["current_page"]
    if "last_message" in value:
        out["lastMessage"] = value["last_message"]
    if "user_action_response" in value:
        out["userActionResponse"] = value["user_action_response"]
    if "approval_action" in value:
        import capo_devops_agent.types.approval_action

        out["approvalAction"] = capo_devops_agent.types.approval_action.serialize_json(
            value["approval_action"]
        )
    return out


def deserialize_json(data: dict) -> SendMessageContext:
    out: SendMessageContext = {}  # type: ignore[typeddict-item]
    if data.get("currentPage") is not None:
        out["current_page"] = data["currentPage"]
    if data.get("lastMessage") is not None:
        out["last_message"] = data["lastMessage"]
    if data.get("userActionResponse") is not None:
        out["user_action_response"] = data["userActionResponse"]
    if data.get("approvalAction") is not None:
        import capo_devops_agent.types.approval_action

        out["approval_action"] = (
            capo_devops_agent.types.approval_action.deserialize_json(
                data["approvalAction"]
            )
        )
    return out
