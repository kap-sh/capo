"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RuleReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.rule_reference

RuleReferenceList: TypeAlias = list[
    "capo_network_security_manager.types.rule_reference.RuleReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleReferenceList) -> list:
    import capo_network_security_manager.types.rule_reference

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.rule_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RuleReferenceList:
    import capo_network_security_manager.types.rule_reference

    out: RuleReferenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.rule_reference.deserialize_json(item)
        )
    return out
