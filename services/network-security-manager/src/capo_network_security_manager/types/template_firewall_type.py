"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TemplateFirewallType``."""

from typing import Literal, TypeAlias, cast

TemplateFirewallType: TypeAlias = Literal["WAF",]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateFirewallType) -> str:
    return value


def deserialize_json(data: str) -> TemplateFirewallType:
    return cast(TemplateFirewallType, data)
