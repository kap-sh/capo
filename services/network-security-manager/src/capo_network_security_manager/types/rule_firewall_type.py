"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RuleFirewallType``."""

from typing import Literal, TypeAlias, cast

RuleFirewallType: TypeAlias = Literal["WAF",]


# --- restJson1 ser/de ---
def serialize_json(value: RuleFirewallType) -> str:
    return value


def deserialize_json(data: str) -> RuleFirewallType:
    return cast(RuleFirewallType, data)
