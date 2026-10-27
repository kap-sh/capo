"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatRuleRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.nat_rule_request

NatRuleRequestList: TypeAlias = list[
    "capo_networkmanager.types.nat_rule_request.NatRuleRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: NatRuleRequestList) -> list:
    import capo_networkmanager.types.nat_rule_request

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.nat_rule_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> NatRuleRequestList:
    import capo_networkmanager.types.nat_rule_request

    out: NatRuleRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.nat_rule_request.deserialize_json(item))
    return out
