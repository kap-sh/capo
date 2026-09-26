"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ApprovalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.auto_approval_rule_list


class ApprovalConfiguration(TypedDict, closed=True):
    auto_approval_rules: NotRequired[
        "capo_agent_registry_control.types.auto_approval_rule_list.AutoApprovalRuleList"
    ]
    """<p>The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApprovalConfiguration) -> dict:
    out: dict = {}
    if "auto_approval_rules" in value:
        import capo_agent_registry_control.types.auto_approval_rule_list

        out["autoApprovalRules"] = (
            capo_agent_registry_control.types.auto_approval_rule_list.serialize_json(
                value["auto_approval_rules"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApprovalConfiguration:
    out: ApprovalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("autoApprovalRules") is not None:
        import capo_agent_registry_control.types.auto_approval_rule_list

        out["auto_approval_rules"] = (
            capo_agent_registry_control.types.auto_approval_rule_list.deserialize_json(
                data["autoApprovalRules"]
            )
        )
    return out
