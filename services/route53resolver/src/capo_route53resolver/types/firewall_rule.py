"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.action
    import capo_route53resolver.types.block_override_dns_type
    import capo_route53resolver.types.block_override_domain
    import capo_route53resolver.types.block_response
    import capo_route53resolver.types.confidence_threshold
    import capo_route53resolver.types.creator_request_id
    import capo_route53resolver.types.dns_threat_protection
    import capo_route53resolver.types.firewall_domain_redirection_action
    import capo_route53resolver.types.firewall_rule_status
    import capo_route53resolver.types.firewall_rule_status_message
    import capo_route53resolver.types.firewall_rule_type
    import capo_route53resolver.types.name
    import capo_route53resolver.types.priority
    import capo_route53resolver.types.qtype
    import capo_route53resolver.types.resource_id
    import capo_route53resolver.types.rfc3339_time_string
    import capo_route53resolver.types.unsigned


class FirewallRule(TypedDict, closed=True):
    firewall_rule_group_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the Firewall rule group of the rule. </p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the domain list that's used in the rule. </p>"""
    firewall_threat_protection_id: NotRequired[
        "capo_route53resolver.types.resource_id.ResourceId"
    ]
    """<p> ID of the DNS Firewall Advanced rule. </p>"""
    name: NotRequired["capo_route53resolver.types.name.Name"]
    """<p>The name of the rule. </p>"""
    priority: NotRequired["capo_route53resolver.types.priority.Priority"]
    """<p>The priority of the rule in the rule group. This value must be unique within the rule group. DNS Firewall processes the rules in a rule group by order of priority, starting from the lowest setting.</p>"""
    action: NotRequired["capo_route53resolver.types.action.Action"]
    """<p>The action that DNS Firewall should take on a DNS query when it matches one of the domains in the rule's domain list, or a threat in a DNS Firewall Advanced rule:</p> <ul> <li> <p> <code>ALLOW</code> - Permit the request to go through. Not available for DNS Firewall Advanced rules.</p> </li> <li> <p> <code>ALERT</code> - Permit the request to go through but send an alert to the logs.</p> </li> <li> <p> <code>BLOCK</code> - Disallow the request. If this is specified, additional handling details are provided in the rule's <code>BlockResponse</code> setting. </p> </li> </ul>"""
    block_response: NotRequired[
        "capo_route53resolver.types.block_response.BlockResponse"
    ]
    """<p>The way that you want DNS Firewall to block the request. Used for the rule action setting <code>BLOCK</code>.</p> <ul> <li> <p> <code>NODATA</code> - Respond indicating that the query was successful, but no response is available for it.</p> </li> <li> <p> <code>NXDOMAIN</code> - Respond indicating that the domain name that's in the query doesn't exist.</p> </li> <li> <p> <code>OVERRIDE</code> - Provide a custom override in the response. This option requires custom handling details in the rule's <code>BlockOverride*</code> settings. </p> </li> </ul>"""
    block_override_domain: NotRequired[
        "capo_route53resolver.types.block_override_domain.BlockOverrideDomain"
    ]
    """<p>The custom DNS record to send back in response to the query. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    block_override_dns_type: NotRequired[
        "capo_route53resolver.types.block_override_dns_type.BlockOverrideDnsType"
    ]
    """<p>The DNS record's type. This determines the format of the record value that you provided in <code>BlockOverrideDomain</code>. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    block_override_ttl: NotRequired["capo_route53resolver.types.unsigned.Unsigned"]
    """<p>The recommended amount of time, in seconds, for the DNS resolver or web browser to cache the provided override record. Used for the rule action <code>BLOCK</code> with a <code>BlockResponse</code> setting of <code>OVERRIDE</code>.</p>"""
    creator_request_id: NotRequired[
        "capo_route53resolver.types.creator_request_id.CreatorRequestId"
    ]
    """<p>A unique string defined by you to identify the request. This allows you to retry failed requests without the risk of executing the operation twice. This can be any unique string, for example, a timestamp. </p>"""
    creation_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the rule was created, in Unix time format and Coordinated Universal Time (UTC). </p>"""
    modification_time: NotRequired[
        "capo_route53resolver.types.rfc3339_time_string.Rfc3339TimeString"
    ]
    """<p>The date and time that the rule was last modified, in Unix time format and Coordinated Universal Time (UTC).</p>"""
    firewall_domain_redirection_action: NotRequired[
        "capo_route53resolver.types.firewall_domain_redirection_action.FirewallDomainRedirectionAction"
    ]
    """<p> How you want the the rule to evaluate DNS redirection in the DNS redirection chain, such as CNAME or DNAME. </p> <p> <code>INSPECT_REDIRECTION_DOMAIN</code>: (Default) inspects all domains in the redirection chain. The individual domains in the redirection chain must be added to the domain list.</p> <p> <code>TRUST_REDIRECTION_DOMAIN</code>: Inspects only the first domain in the redirection chain. You don't need to add the subsequent domains in the domain in the redirection list to the domain list.</p>"""
    qtype: NotRequired["capo_route53resolver.types.qtype.Qtype"]
    """<p> The DNS query type you want the rule to evaluate. Allowed values are; </p> <ul> <li> <p> A: Returns an IPv4 address.</p> </li> <li> <p>AAAA: Returns an Ipv6 address.</p> </li> <li> <p>CAA: Restricts CAs that can create SSL/TLS certifications for the domain.</p> </li> <li> <p>CNAME: Returns another domain name.</p> </li> <li> <p>DS: Record that identifies the DNSSEC signing key of a delegated zone.</p> </li> <li> <p>MX: Specifies mail servers.</p> </li> <li> <p>NAPTR: Regular-expression-based rewriting of domain names.</p> </li> <li> <p>NS: Authoritative name servers.</p> </li> <li> <p>PTR: Maps an IP address to a domain name.</p> </li> <li> <p>SOA: Start of authority record for the zone.</p> </li> <li> <p>SPF: Lists the servers authorized to send emails from a domain.</p> </li> <li> <p>SRV: Application specific values that identify servers.</p> </li> <li> <p>TXT: Verifies email senders and application-specific values.</p> </li> <li> <p>A query type you define by using the DNS type ID, for example 28 for AAAA. The values must be defined as TYPENUMBER, where the NUMBER can be 1-65534, for example, TYPE28. For more information, see <a href="https://en.wikipedia.org/wiki/List_of_DNS_record_types">List of DNS record types</a>.</p> </li> </ul>"""
    dns_threat_protection: NotRequired[
        "capo_route53resolver.types.dns_threat_protection.DnsThreatProtection"
    ]
    """<p> The type of the DNS Firewall Advanced rule. Valid values are: </p> <ul> <li> <p> <code>DGA</code>: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.</p> </li> <li> <p> <code>DNS_TUNNELING</code>: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.</p> </li> <li> <p> <code>DICTIONARY_DGA</code>: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.</p> </li> </ul>"""
    confidence_threshold: NotRequired[
        "capo_route53resolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p> The confidence threshold for DNS Firewall Advanced. You must provide this value when you create a DNS Firewall Advanced rule. The confidence level values mean: </p> <ul> <li> <p> <code>LOW</code>: Provides the highest detection rate for threats, but also increases false positives.</p> </li> <li> <p> <code>MEDIUM</code>: Provides a balance between detecting threats and false positives.</p> </li> <li> <p> <code>HIGH</code>: Detects only the most well corroborated threats with a low rate of false positives. </p> </li> </ul>"""
    firewall_rule_type: NotRequired[
        "capo_route53resolver.types.firewall_rule_type.FirewallRuleType"
    ]
    """<p>The rule type configuration for the firewall rule. This is a tagged union — exactly one of its members will be populated. Possible members are:</p> <ul> <li> <p> <code>FirewallAdvancedContentCategory</code> — an Amazon Web Services-managed content category (for example, <code>VIOLENCE_AND_HATE_SPEECH</code>).</p> </li> <li> <p> <code>FirewallAdvancedThreatCategory</code> — an Amazon Web Services-managed advanced threat category (for example, <code>PHISHING</code>).</p> </li> <li> <p> <code>DnsThreatProtection</code> — a built-in DNS Firewall Advanced threat detector (<code>DGA</code>, <code>DNS_TUNNELING</code>, or <code>DICTIONARY_DGA</code>).</p> </li> <li> <p> <code>PartnerThreatProtection</code> — a third-party threat feed delivered through Amazon Web Services Marketplace.</p> </li> </ul> <p>To enumerate the values supported in your account, call <a>ListFirewallRuleTypes</a>.</p>"""
    status: NotRequired[
        "capo_route53resolver.types.firewall_rule_status.FirewallRuleStatus"
    ]
    """<p>The lifecycle state of the firewall rule. Possible values:</p> <ul> <li> <p> <code>CREATING</code> — DNS Firewall is provisioning the rule. Rules created with the <code>PartnerThreatProtection</code> rule type begin in this state while DNS Firewall verifies the calling account's Amazon Web Services Marketplace entitlement.</p> </li> <li> <p> <code>COMPLETE</code> — The rule is provisioned and enforcing matches.</p> </li> <li> <p> <code>CREATION_FAILED</code> — Provisioning failed. <code>StatusMessage</code> contains a human-readable reason. A rule in this state is immutable: <a>UpdateFirewallRule</a> rejects the request, and the rule must be removed with <a>DeleteFirewallRule</a>.</p> </li> </ul> <p>For rules that do not require asynchronous provisioning, this field may be absent.</p>"""
    status_message: NotRequired[
        "capo_route53resolver.types.firewall_rule_status_message.FirewallRuleStatusMessage"
    ]
    """<p>An additional message about the rule's lifecycle state. Populated when <code>Status</code> is <code>CREATION_FAILED</code> to describe why provisioning failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallRule) -> dict:
    out: dict = {}
    if "firewall_rule_group_id" in value:
        out["FirewallRuleGroupId"] = value["firewall_rule_group_id"]
    if "firewall_domain_list_id" in value:
        out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    if "firewall_threat_protection_id" in value:
        out["FirewallThreatProtectionId"] = value["firewall_threat_protection_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "action" in value:
        import capo_route53resolver.types.action

        out["Action"] = capo_route53resolver.types.action.serialize_aws_json_1_1(
            value["action"]
        )
    if "block_response" in value:
        import capo_route53resolver.types.block_response

        out["BlockResponse"] = (
            capo_route53resolver.types.block_response.serialize_aws_json_1_1(
                value["block_response"]
            )
        )
    if "block_override_domain" in value:
        out["BlockOverrideDomain"] = value["block_override_domain"]
    if "block_override_dns_type" in value:
        import capo_route53resolver.types.block_override_dns_type

        out["BlockOverrideDnsType"] = (
            capo_route53resolver.types.block_override_dns_type.serialize_aws_json_1_1(
                value["block_override_dns_type"]
            )
        )
    if "block_override_ttl" in value:
        out["BlockOverrideTtl"] = value["block_override_ttl"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "modification_time" in value:
        out["ModificationTime"] = value["modification_time"]
    if "firewall_domain_redirection_action" in value:
        import capo_route53resolver.types.firewall_domain_redirection_action

        out["FirewallDomainRedirectionAction"] = (
            capo_route53resolver.types.firewall_domain_redirection_action.serialize_aws_json_1_1(
                value["firewall_domain_redirection_action"]
            )
        )
    if "qtype" in value:
        out["Qtype"] = value["qtype"]
    if "dns_threat_protection" in value:
        import capo_route53resolver.types.dns_threat_protection

        out["DnsThreatProtection"] = (
            capo_route53resolver.types.dns_threat_protection.serialize_aws_json_1_1(
                value["dns_threat_protection"]
            )
        )
    if "confidence_threshold" in value:
        import capo_route53resolver.types.confidence_threshold

        out["ConfidenceThreshold"] = (
            capo_route53resolver.types.confidence_threshold.serialize_aws_json_1_1(
                value["confidence_threshold"]
            )
        )
    if "firewall_rule_type" in value:
        import capo_route53resolver.types.firewall_rule_type

        out["FirewallRuleType"] = (
            capo_route53resolver.types.firewall_rule_type.serialize_aws_json_1_1(
                value["firewall_rule_type"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallRule:
    out: FirewallRule = {}  # type: ignore[typeddict-item]
    if data.get("FirewallRuleGroupId") is not None:
        out["firewall_rule_group_id"] = data["FirewallRuleGroupId"]
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    if data.get("FirewallThreatProtectionId") is not None:
        out["firewall_threat_protection_id"] = data["FirewallThreatProtectionId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("Action") is not None:
        import capo_route53resolver.types.action

        out["action"] = capo_route53resolver.types.action.deserialize_aws_json_1_1(
            data["Action"]
        )
    if data.get("BlockResponse") is not None:
        import capo_route53resolver.types.block_response

        out["block_response"] = (
            capo_route53resolver.types.block_response.deserialize_aws_json_1_1(
                data["BlockResponse"]
            )
        )
    if data.get("BlockOverrideDomain") is not None:
        out["block_override_domain"] = data["BlockOverrideDomain"]
    if data.get("BlockOverrideDnsType") is not None:
        import capo_route53resolver.types.block_override_dns_type

        out["block_override_dns_type"] = (
            capo_route53resolver.types.block_override_dns_type.deserialize_aws_json_1_1(
                data["BlockOverrideDnsType"]
            )
        )
    if data.get("BlockOverrideTtl") is not None:
        out["block_override_ttl"] = data["BlockOverrideTtl"]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("CreationTime") is not None:
        out["creation_time"] = data["CreationTime"]
    if data.get("ModificationTime") is not None:
        out["modification_time"] = data["ModificationTime"]
    if data.get("FirewallDomainRedirectionAction") is not None:
        import capo_route53resolver.types.firewall_domain_redirection_action

        out["firewall_domain_redirection_action"] = (
            capo_route53resolver.types.firewall_domain_redirection_action.deserialize_aws_json_1_1(
                data["FirewallDomainRedirectionAction"]
            )
        )
    if data.get("Qtype") is not None:
        out["qtype"] = data["Qtype"]
    if data.get("DnsThreatProtection") is not None:
        import capo_route53resolver.types.dns_threat_protection

        out["dns_threat_protection"] = (
            capo_route53resolver.types.dns_threat_protection.deserialize_aws_json_1_1(
                data["DnsThreatProtection"]
            )
        )
    if data.get("ConfidenceThreshold") is not None:
        import capo_route53resolver.types.confidence_threshold

        out["confidence_threshold"] = (
            capo_route53resolver.types.confidence_threshold.deserialize_aws_json_1_1(
                data["ConfidenceThreshold"]
            )
        )
    if data.get("FirewallRuleType") is not None:
        import capo_route53resolver.types.firewall_rule_type

        out["firewall_rule_type"] = (
            capo_route53resolver.types.firewall_rule_type.deserialize_aws_json_1_1(
                data["FirewallRuleType"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
