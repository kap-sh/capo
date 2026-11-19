"""Generated from Smithy shape ``com.amazonaws.fms#StatefulRuleGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.network_firewall_resource_name
    import capo_fms.types.network_firewall_stateful_rule_group_override
    import capo_fms.types.priority_number
    import capo_fms.types.resource_id


class StatefulRuleGroup(TypedDict, closed=True):
    rule_group_name: NotRequired[
        "capo_fms.types.network_firewall_resource_name.NetworkFirewallResourceName"
    ]
    """<p>The name of the rule group.</p>"""
    resource_id: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The resource ID of the rule group.</p>"""
    priority: NotRequired["capo_fms.types.priority_number.PriorityNumber"]
    """<p>An integer setting that indicates the order in which to run the stateful rule groups in a single Network Firewall firewall policy. This setting only applies to firewall policies that specify the <code>STRICT_ORDER</code> rule order in the stateful engine options settings.</p> <p> Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy. For information about </p> <p> You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on. </p>"""
    override: NotRequired[
        "capo_fms.types.network_firewall_stateful_rule_group_override.NetworkFirewallStatefulRuleGroupOverride"
    ]
    """<p>The action that allows the policy owner to override the behavior of the rule group within a policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatefulRuleGroup) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "override" in value:
        import capo_fms.types.network_firewall_stateful_rule_group_override

        out["Override"] = (
            capo_fms.types.network_firewall_stateful_rule_group_override.serialize_aws_json_1_1(
                value["override"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StatefulRuleGroup:
    out: StatefulRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("Override") is not None:
        import capo_fms.types.network_firewall_stateful_rule_group_override

        out["override"] = (
            capo_fms.types.network_firewall_stateful_rule_group_override.deserialize_aws_json_1_1(
                data["Override"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatefulRuleGroup) -> dict:
    out: dict = {}
    if "rule_group_name" in value:
        out["RuleGroupName"] = value["rule_group_name"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "override" in value:
        import capo_fms.types.network_firewall_stateful_rule_group_override

        out["Override"] = (
            capo_fms.types.network_firewall_stateful_rule_group_override.serialize_cbor(
                value["override"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> StatefulRuleGroup:
    out: StatefulRuleGroup = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupName") is not None:
        out["rule_group_name"] = data["RuleGroupName"]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("Override") is not None:
        import capo_fms.types.network_firewall_stateful_rule_group_override

        out["override"] = (
            capo_fms.types.network_firewall_stateful_rule_group_override.deserialize_cbor(
                data["Override"]
            )
        )
    return out
