"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRuleItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.ip_rule
    import capo_workspaces.types.ip_rule_desc


class IpRuleItem(TypedDict, closed=True):
    ip_rule: NotRequired["capo_workspaces.types.ip_rule.IpRule"]
    """<p>The IP address range, in CIDR notation.</p>"""
    rule_desc: NotRequired["capo_workspaces.types.ip_rule_desc.IpRuleDesc"]
    """<p>The description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRuleItem) -> dict:
    out: dict = {}
    if "ip_rule" in value:
        out["ipRule"] = value["ip_rule"]
    if "rule_desc" in value:
        out["ruleDesc"] = value["rule_desc"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpRuleItem:
    out: IpRuleItem = {}  # type: ignore[typeddict-item]
    if data.get("ipRule") is not None:
        out["ip_rule"] = data["ipRule"]
    if data.get("ruleDesc") is not None:
        out["rule_desc"] = data["ruleDesc"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRuleItem) -> dict:
    out: dict = {}
    if "ip_rule" in value:
        out["ipRule"] = value["ip_rule"]
    if "rule_desc" in value:
        out["ruleDesc"] = value["rule_desc"]
    return out


def deserialize_cbor(data: dict) -> IpRuleItem:
    out: IpRuleItem = {}  # type: ignore[typeddict-item]
    if data.get("ipRule") is not None:
        out["ip_rule"] = data["ipRule"]
    if data.get("ruleDesc") is not None:
        out["rule_desc"] = data["ruleDesc"]
    return out
