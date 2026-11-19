"""Generated from Smithy shape ``com.amazonaws.mgn#SecurityGroupRuleConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class SecurityGroupRuleConfiguration(TypedDict, closed=True):
    enable_referencing: NotRequired["bool"]
    """<p>Whether automatic conversion of CIDR-based sources and destinations to security group references applies to this rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupRuleConfiguration) -> dict:
    out: dict = {}
    if "enable_referencing" in value:
        out["enableReferencing"] = value["enable_referencing"]
    return out


def deserialize_json(data: dict) -> SecurityGroupRuleConfiguration:
    out: SecurityGroupRuleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enableReferencing") is not None:
        out["enable_referencing"] = data["enableReferencing"]
    return out
