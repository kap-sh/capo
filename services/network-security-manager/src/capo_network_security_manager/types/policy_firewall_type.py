"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicyFirewallType``."""

from typing import Literal, TypeAlias, cast

PolicyFirewallType: TypeAlias = Literal[
    "WAF",
    "SHIELD_ADVANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyFirewallType) -> str:
    return value


def deserialize_json(data: str) -> PolicyFirewallType:
    return cast(PolicyFirewallType, data)
