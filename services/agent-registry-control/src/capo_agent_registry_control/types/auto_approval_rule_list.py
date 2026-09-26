"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AutoApprovalRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_approval_rule

AutoApprovalRuleList: TypeAlias = list[
    "capo_agent_registry_control.types.auto_approval_rule.AutoApprovalRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoApprovalRuleList) -> list:
    import capo_agent_registry_control.types.auto_approval_rule

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.auto_approval_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutoApprovalRuleList:
    import capo_agent_registry_control.types.auto_approval_rule

    out: AutoApprovalRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.auto_approval_rule.deserialize_json(item)
        )
    return out
