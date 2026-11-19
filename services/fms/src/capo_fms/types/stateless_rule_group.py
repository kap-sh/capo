"""Generated from Smithy shape ``com.amazonaws.fms#StatelessRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.network_firewall_resource_name
    import capo_fms.types.resource_id
    import capo_fms.types.stateless_rule_group_priority


class StatelessRuleGroup(TypedDict, closed=True):
    rule_group_name: NotRequired[
        "capo_fms.types.network_firewall_resource_name.NetworkFirewallResourceName"
    ]
    """<p>The name of the rule group.</p>"""
    resource_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the rule group.</p>"""
    priority: NotRequired[
        "capo_fms.types.stateless_rule_group_priority.StatelessRuleGroupPriority"
    ]
    """<p>The priority of the rule group. Network Firewall evaluates the stateless rule groups in a firewall policy starting from the lowest priority setting. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatelessRuleGroup) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StatelessRuleGroup:
    out: StatelessRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatelessRuleGroup) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_cbor(data: dict) -> StatelessRuleGroup:
    out: StatelessRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    return out
