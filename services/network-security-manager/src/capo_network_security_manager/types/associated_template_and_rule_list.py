"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedTemplateAndRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_template_or_rule

AssociatedTemplateAndRuleList: TypeAlias = list[
    "capo_network_security_manager.types.associated_template_or_rule.AssociatedTemplateOrRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedTemplateAndRuleList) -> list:
    import capo_network_security_manager.types.associated_template_or_rule

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.associated_template_or_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AssociatedTemplateAndRuleList:
    import capo_network_security_manager.types.associated_template_or_rule

    out: AssociatedTemplateAndRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.associated_template_or_rule.deserialize_json(
                item
            )
        )
    return out
