"""Generated from Smithy shape ``com.amazonaws.devopsagent#ApprovalAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.approval_action_type
    import capo_devops_agent.types.approval_id
    import capo_devops_agent.types.button_text
    import capo_devops_agent.types.interrupt_id
    import capo_devops_agent.types.tool_use_id


class ApprovalAction(TypedDict, closed=True):
    tool_use_id: NotRequired["capo_devops_agent.types.tool_use_id.ToolUseId"]
    """<p>Identifier of the specific paused tool invocation that requested approval. Correlates the approval decision back to the paused invocation.</p>"""
    interrupt_id: NotRequired["capo_devops_agent.types.interrupt_id.InterruptId"]
    """<p>An opaque resume identifier issued by the service when an agent execution pauses for approval. Provide it when resuming so the service can resume the correct paused execution.</p>"""
    approval_id: NotRequired["capo_devops_agent.types.approval_id.ApprovalId"]
    """<p>Identifier of the approval request being resolved.</p>"""
    button_text: NotRequired["capo_devops_agent.types.button_text.ButtonText"]
    """<p>Optional display text of the UI control the user chose (for example, "Approve Exact", "Approve Broader", or "Reject"), provided as auxiliary decision context.</p>"""
    action: NotRequired[
        "capo_devops_agent.types.approval_action_type.ApprovalActionType"
    ]
    """<p>The action taken on the approval request — APPROVED or REJECTED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalAction) -> dict:
    out: dict = {}
    if "tool_use_id" in value:
        out["toolUseId"] = value["tool_use_id"]
    if "interrupt_id" in value:
        out["interruptId"] = value["interrupt_id"]
    if "approval_id" in value:
        out["approvalId"] = value["approval_id"]
    if "button_text" in value:
        out["buttonText"] = value["button_text"]
    if "action" in value:
        import capo_devops_agent.types.approval_action_type

        out["action"] = capo_devops_agent.types.approval_action_type.serialize_json(
            value["action"]
        )
    return out


def deserialize_json(data: dict) -> ApprovalAction:
    out: ApprovalAction = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    if data.get("interruptId") is not None:
        out["interrupt_id"] = data["interruptId"]
    if data.get("approvalId") is not None:
        out["approval_id"] = data["approvalId"]
    if data.get("buttonText") is not None:
        out["button_text"] = data["buttonText"]
    if data.get("action") is not None:
        import capo_devops_agent.types.approval_action_type

        out["action"] = capo_devops_agent.types.approval_action_type.deserialize_json(
            data["action"]
        )
    return out
