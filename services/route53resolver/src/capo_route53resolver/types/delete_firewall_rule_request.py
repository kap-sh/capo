"""Generated from Smithy shape ``com.amazonaws.route53resolver#DeleteFirewallRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53resolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53resolver.types.qtype
    import capo_route53resolver.types.resource_id


class DeleteFirewallRuleRequest(TypedDict, closed=True):
    firewall_rule_group_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The unique identifier of the firewall rule group that you want to delete the rule from. </p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the domain list that's used in the rule. </p>"""
    firewall_threat_protection_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p> The ID that is created for a DNS Firewall Advanced rule. </p>"""
    qtype: NotRequired["capo_route53resolver.types.qtype.Qtype"]
    """<p> The DNS query type that the rule you are deleting evaluates. Allowed values are; </p> <ul> <li> <p> A: Returns an IPv4 address.</p> </li> <li> <p>AAAA: Returns an Ipv6 address.</p> </li> <li> <p>CAA: Restricts CAs that can create SSL/TLS certifications for the domain.</p> </li> <li> <p>CNAME: Returns another domain name.</p> </li> <li> <p>DS: Record that identifies the DNSSEC signing key of a delegated zone.</p> </li> <li> <p>MX: Specifies mail servers.</p> </li> <li> <p>NAPTR: Regular-expression-based rewriting of domain names.</p> </li> <li> <p>NS: Authoritative name servers.</p> </li> <li> <p>PTR: Maps an IP address to a domain name.</p> </li> <li> <p>SOA: Start of authority record for the zone.</p> </li> <li> <p>SPF: Lists the servers authorized to send emails from a domain.</p> </li> <li> <p>SRV: Application specific values that identify servers.</p> </li> <li> <p>TXT: Verifies email senders and application-specific values.</p> </li> <li> <p>A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">List of DNS record types</a>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFirewallRuleRequest) -> dict:
    out: dict = {}
    out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "firewall_domain_list_id" in value:
        out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    if "firewall_threat_protection_id" in value:
        out["FirewallThreatProtectionId"] = value["firewall_threat_protection_id"]
    if "qtype" in value:
        out["Qtype"] = value["qtype"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFirewallRuleRequest:
    out: DeleteFirewallRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    else:
        raise DeserializationError(
            "DeleteFirewallRuleRequest.firewall_rule_group_id required"
        )
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    if data.get("FirewallThreatProtectionId") is not None:
        out["firewall_threat_protection_id"] = data["FirewallThreatProtectionId"]
    if data.get("Qtype") is not None:
        out["qtype"] = data["Qtype"]
    return out
