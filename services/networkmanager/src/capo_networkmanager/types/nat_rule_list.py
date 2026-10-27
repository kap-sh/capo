"""Generated from Smithy shape ``com.amazonaws.networkmanager#NatRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.nat_rule

NatRuleList: TypeAlias = list["capo_networkmanager.types.nat_rule.NatRule"]


# --- restJson1 ser/de ---
def serialize_json(value: NatRuleList) -> list:
    import capo_networkmanager.types.nat_rule

    out: list = []
    for item in value:
        out.append(capo_networkmanager.types.nat_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> NatRuleList:
    import capo_networkmanager.types.nat_rule

    out: NatRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_networkmanager.types.nat_rule.deserialize_json(item))
    return out
