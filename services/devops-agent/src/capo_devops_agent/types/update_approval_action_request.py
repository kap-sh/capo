"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateApprovalActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space_identifier
    import capo_devops_agent.types.approval_action_type
    import capo_devops_agent.types.approval_id
    import capo_devops_agent.types.approval_pattern
    import capo_devops_agent.types.approval_reason


class UpdateApprovalActionRequest(TypedDict, closed=True):
    agent_space_id: (
        "capo_devops_agent.types.agent_space_identifier.AgentSpaceIdentifier"
    )
    """<p>The agent space identifier — multi-tenant workspace scope. Bound from the request URI.</p>"""
    approval_id: "capo_devops_agent.types.approval_id.ApprovalId"
    """<p>Identifier of the approval request being resolved. A UUID. Bound from the request URI.</p>"""
    action: "capo_devops_agent.types.approval_action_type.ApprovalActionType"
    """<p>The action to take on the approval request — APPROVED or REJECTED.</p>"""
    final_pattern: NotRequired[
        "capo_devops_agent.types.approval_pattern.ApprovalPattern"
    ]
    """<p>The finalized pattern (tool + argumentPins) that scopes the approval. Required when `action` is APPROVED; must be absent when `action` is REJECTED. The pattern narrows, and must not widen, the invocation originally requested by the agent. This cross-field invariant is enforced by service-side validation.</p>"""
    reason: NotRequired["capo_devops_agent.types.approval_reason.ApprovalReason"]
    """<p>Optional free-text rationale for the decision. Permitted when `action` is REJECTED; ignored when `action` is APPROVED.</p>"""
    ttl_seconds: NotRequired["int"]
    """<p>Approval lifetime in seconds, starting from when the decision is submitted. Required when `action` is APPROVED AND `singleUse` is false; must be absent when `action` is REJECTED or when `singleUse` is true (a single-use approval backs one executed action and the redemption window collapses). Cross-field invariants are enforced by service-side validation; the @range bound here is the operation-boundary check that always applies (a maximum of 4 hours).</p>"""
    single_use: NotRequired["bool"]
    """<p>Whether the approved action backs a single executed tool call (true) or is reusable within ttlSeconds (false). Required when `action` is APPROVED; must be absent when `action` is REJECTED. When true, ttlSeconds must be absent (the redemption window collapses to the single use). When false, ttlSeconds is required and bounds the reuse window. Cross-field invariants are enforced by service-side validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApprovalActionRequest) -> dict:
    out: dict = {}
    import capo_devops_agent.types.approval_action_type

    out["action"] = capo_devops_agent.types.approval_action_type.serialize_json(
        value["action"]
    )
    if "final_pattern" in value:
        import capo_devops_agent.types.approval_pattern

        out["finalPattern"] = capo_devops_agent.types.approval_pattern.serialize_json(
            value["final_pattern"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    if "ttl_seconds" in value:
        out["ttlSeconds"] = value["ttl_seconds"]
    if "single_use" in value:
        out["singleUse"] = value["single_use"]
    return out


def deserialize_json(data: dict) -> UpdateApprovalActionRequest:
    out: UpdateApprovalActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_devops_agent.types.approval_action_type

        out["action"] = capo_devops_agent.types.approval_action_type.deserialize_json(
            data["action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_devops_agent.types.approval_action_type.ApprovalActionType", ""
        )
    if data.get("finalPattern") is not None:
        import capo_devops_agent.types.approval_pattern

        out["final_pattern"] = (
            capo_devops_agent.types.approval_pattern.deserialize_json(
                data["finalPattern"]
            )
        )
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("ttlSeconds") is not None:
        out["ttl_seconds"] = data["ttlSeconds"]
    if data.get("singleUse") is not None:
        out["single_use"] = data["singleUse"]
    return out
