"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallRuleEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.qtype
    import capo_route53resolver.types.resource_id


class DeleteFirewallRuleEntry(TypedDict, closed=True):
    firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group for the rule.</p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the domain list that's used in the rule.</p>"""
    firewall_threat_protection_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the DNS Firewall Advanced rule.</p>"""
    qtype: NotRequired["capo_route53resolver.types.qtype.Qtype"]
    """<p>The DNS query type that the rule evaluates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallRuleEntry) -> dict:
    out: dict = {}
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "firewall_domain_list_id" in value:
        out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    if "firewall_threat_protection_id" in value:
        out["FirewallThreatProtectionId"] = value["firewall_threat_protection_id"]
    if "qtype" in value:
        out["Qtype"] = value["qtype"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallRuleEntry:
    out: DeleteFirewallRuleEntry = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        out["firewall_rule_group_id"] = ""
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    if data.get("FirewallThreatProtectionId") is not None:
        out["firewall_threat_protection_id"] = data["FirewallThreatProtectionId"]
    if data.get("Qtype") is not None:
        out["qtype"] = data["Qtype"]
    return out
