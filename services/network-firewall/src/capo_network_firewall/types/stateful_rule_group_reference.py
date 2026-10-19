"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleGroupReference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.deep_threat_inspection
    import capo_network_firewall.types.priority
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.stateful_rule_group_override


class StatefulRuleGroupReference(TypedDict, closed=True):
    resource_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the stateful rule group.</p>"""
    priority: NotRequired["capo_network_firewall.types.priority.Priority"]
    """<p>An integer setting that indicates the order in which to run the stateful rule groups in a single <a>FirewallPolicy</a>. This setting only applies to firewall policies that specify the <code>STRICT_ORDER</code> rule order in the stateful engine options settings.</p> <p>Network Firewall evalutes each stateful rule group against a packet starting with the group that has the lowest priority setting. You must ensure that the priority settings are unique within each policy.</p> <p>You can change the priority settings of your rule groups at any time. To make it easier to insert rule groups later, number them so there's a wide range in between, for example use 100, 200, and so on. </p>"""
    override: NotRequired[
        "capo_network_firewall.types.stateful_rule_group_override.StatefulRuleGroupOverride"
    ]
    """<p>The action that allows the policy owner to override the behavior of the rule group within a policy.</p>"""
    deep_threat_inspection: NotRequired[
        "capo_network_firewall.types.deep_threat_inspection.DeepThreatInspection"
    ]
    """<p>Network Firewall plans to augment the active threat defense managed rule group with an additional deep threat inspection capability. When this capability is released, Amazon Web Services will analyze service logs of network traffic processed by these rule groups to identify threat indicators across customers. Amazon Web Services will use these threat indicators to improve the active threat defense managed rule groups and protect the security of Amazon Web Services customers and services.</p> <note> <p>Customers can opt-out of deep threat inspection at any time through the Network Firewall console or API. When customers opt out, Network Firewall will not use the network traffic processed by those customers' active threat defense rule groups for rule group improvement.</p> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleGroupReference) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "override" in value:
        import capo_network_firewall.types.stateful_rule_group_override

        out["Override"] = (
            capo_network_firewall.types.stateful_rule_group_override.serialize_aws_json_1_0(
                value["override"]
            )
        )
    if "deep_threat_inspection" in value:
        out["DeepThreatInspection"] = value["deep_threat_inspection"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StatefulRuleGroupReference:
    out: StatefulRuleGroupReference = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("Override") is not None:
        import capo_network_firewall.types.stateful_rule_group_override

        out["override"] = (
            capo_network_firewall.types.stateful_rule_group_override.deserialize_aws_json_1_0(
                data["Override"]
            )
        )
    if data.get("DeepThreatInspection") is not None:
        out["deep_threat_inspection"] = data["DeepThreatInspection"]
    return out
