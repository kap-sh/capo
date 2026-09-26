"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TemplateAndRuleReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.template_or_rule_reference

TemplateAndRuleReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.template_or_rule_reference.TemplateOrRuleReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateAndRuleReferenceList) -> list:
    import capo_network_security_manager.types.template_or_rule_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.template_or_rule_reference.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TemplateAndRuleReferenceList:
    import capo_network_security_manager.types.template_or_rule_reference

    out: TemplateAndRuleReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.template_or_rule_reference.deserialize_json(
                item
            )
        )
    return out
