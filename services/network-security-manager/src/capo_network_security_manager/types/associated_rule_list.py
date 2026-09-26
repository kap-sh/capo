"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#AssociatedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_rule

AssociatedRuleList: TypeAlias = list[
    "capo_network_security_manager.types.associated_rule.AssociatedRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedRuleList) -> list:
    import capo_network_security_manager.types.associated_rule

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.associated_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AssociatedRuleList:
    import capo_network_security_manager.types.associated_rule

    out: AssociatedRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.associated_rule.deserialize_json(item)
        )
    return out
