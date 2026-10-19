"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateFirewallRuleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.block_override_dns_query_type
    import capo_route53globalresolver.types.block_override_ttl
    import capo_route53globalresolver.types.confidence_threshold
    import capo_route53globalresolver.types.cr_resource_status
    import capo_route53globalresolver.types.dns_advanced_protection
    import capo_route53globalresolver.types.dns_query_type
    import capo_route53globalresolver.types.domain
    import capo_route53globalresolver.types.firewall_block_response
    import capo_route53globalresolver.types.firewall_rule_action
    import capo_route53globalresolver.types.firewall_rule_priority
    import capo_route53globalresolver.types.iso8601_time_string
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name


class CreateFirewallRuleOutput(TypedDict, closed=True):
    action: "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction"
    """<p>The action that DNS Firewall takes on DNS queries that match this rule.</p>"""
    block_override_dns_type: NotRequired[
        "capo_route53globalresolver.types.block_override_dns_query_type.BlockOverrideDnsQueryType"
    ]
    """<p>The DNS record type for the custom response when blockResponse is OVERRIDE.</p>"""
    block_override_domain: NotRequired["capo_route53globalresolver.types.domain.Domain"]
    """<p>The custom domain to return when the action is BLOCK and blockResponse is OVERRIDE.</p>"""
    block_override_ttl: NotRequired[
        "capo_route53globalresolver.types.block_override_ttl.BlockOverrideTtl"
    ]
    """<p>The time-to-live (TTL) value for the custom response when blockResponse is OVERRIDE.</p>"""
    block_response: NotRequired[
        "capo_route53globalresolver.types.firewall_block_response.FirewallBlockResponse"
    ]
    """<p>The response to return when the action is BLOCK.</p>"""
    confidence_threshold: NotRequired[
        "capo_route53globalresolver.types.confidence_threshold.ConfidenceThreshold"
    ]
    """<p>The confidence threshold for advanced threat detection.</p>"""
    created_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the firewall rule was created.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the firewall rule.</p>"""
    dns_advanced_protection: NotRequired[
        "capo_route53globalresolver.types.dns_advanced_protection.DnsAdvancedProtection"
    ]
    """<p>Whether advanced DNS threat protection is enabled for this rule.</p>"""
    firewall_domain_list_id: NotRequired[
        "capo_route53globalresolver.types.resource_id.ResourceId"
    ]
    """<p>The ID of the firewall domain list used in this rule.</p>"""
    id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The unique identifier for the firewall rule.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>The name of the firewall rule.</p>"""
    priority: (
        "capo_route53globalresolver.types.firewall_rule_priority.FirewallRulePriority"
    )
    """<p>The priority of the firewall rule.</p>"""
    dns_view_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the DNS view associated with this firewall rule.</p>"""
    query_type: NotRequired[
        "capo_route53globalresolver.types.dns_query_type.DnsQueryType"
    ]
    """<p>The DNS query type that this rule matches.</p>"""
    status: "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus"
    """<p>The operational status of the firewall rule.</p>"""
    updated_at: "capo_route53globalresolver.types.iso8601_time_string.ISO8601TimeString"
    """<p>The date and time when the firewall rule was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFirewallRuleOutput) -> dict:
    out: dict = {}
    import capo_route53globalresolver.types.firewall_rule_action

    out["action"] = (
        capo_route53globalresolver.types.firewall_rule_action.serialize_json(
            value["action"]
        )
    )
    if "block_override_dns_type" in value:
        import capo_route53globalresolver.types.block_override_dns_query_type

        out["blockOverrideDnsType"] = (
            capo_route53globalresolver.types.block_override_dns_query_type.serialize_json(
                value["block_override_dns_type"]
            )
        )
    if "block_override_domain" in value:
        out["blockOverrideDomain"] = value["block_override_domain"]
    if "block_override_ttl" in value:
        out["blockOverrideTtl"] = value["block_override_ttl"]
    if "block_response" in value:
        import capo_route53globalresolver.types.firewall_block_response

        out["blockResponse"] = (
            capo_route53globalresolver.types.firewall_block_response.serialize_json(
                value["block_response"]
            )
        )
    if "confidence_threshold" in value:
        import capo_route53globalresolver.types.confidence_threshold

        out["confidenceThreshold"] = (
            capo_route53globalresolver.types.confidence_threshold.serialize_json(
                value["confidence_threshold"]
            )
        )
    import capo_route53globalresolver.types.iso8601_time_string

    out["createdAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["created_at"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "dns_advanced_protection" in value:
        import capo_route53globalresolver.types.dns_advanced_protection

        out["dnsAdvancedProtection"] = (
            capo_route53globalresolver.types.dns_advanced_protection.serialize_json(
                value["dns_advanced_protection"]
            )
        )
    if "firewall_domain_list_id" in value:
        out["firewallDomainListId"] = value["firewall_domain_list_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["priority"] = value["priority"]
    out["dnsViewId"] = value["dns_view_id"]
    if "query_type" in value:
        out["queryType"] = value["query_type"]
    import capo_route53globalresolver.types.cr_resource_status

    out["status"] = capo_route53globalresolver.types.cr_resource_status.serialize_json(
        value["status"]
    )
    import capo_route53globalresolver.types.iso8601_time_string

    out["updatedAt"] = (
        capo_route53globalresolver.types.iso8601_time_string.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateFirewallRuleOutput:
    out: CreateFirewallRuleOutput = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_route53globalresolver.types.firewall_rule_action

        out["action"] = (
            capo_route53globalresolver.types.firewall_rule_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_route53globalresolver.types.firewall_rule_action.FirewallRuleAction",
            "",
        )
    if data.get("blockOverrideDnsType") is not None:
        import capo_route53globalresolver.types.block_override_dns_query_type

        out["block_override_dns_type"] = (
            capo_route53globalresolver.types.block_override_dns_query_type.deserialize_json(
                data["blockOverrideDnsType"]
            )
        )
    if data.get("blockOverrideDomain") is not None:
        out["block_override_domain"] = data["blockOverrideDomain"]
    if data.get("blockOverrideTtl") is not None:
        out["block_override_ttl"] = data["blockOverrideTtl"]
    if data.get("blockResponse") is not None:
        import capo_route53globalresolver.types.firewall_block_response

        out["block_response"] = (
            capo_route53globalresolver.types.firewall_block_response.deserialize_json(
                data["blockResponse"]
            )
        )
    if data.get("confidenceThreshold") is not None:
        import capo_route53globalresolver.types.confidence_threshold

        out["confidence_threshold"] = (
            capo_route53globalresolver.types.confidence_threshold.deserialize_json(
                data["confidenceThreshold"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["created_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("dnsAdvancedProtection") is not None:
        import capo_route53globalresolver.types.dns_advanced_protection

        out["dns_advanced_protection"] = (
            capo_route53globalresolver.types.dns_advanced_protection.deserialize_json(
                data["dnsAdvancedProtection"]
            )
        )
    if data.get("firewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["firewallDomainListId"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        out["priority"] = 0
    if data.get("dnsViewId") is not None:
        out["dns_view_id"] = data["dnsViewId"]
    else:
        out["dns_view_id"] = ""
    if data.get("queryType") is not None:
        out["query_type"] = data["queryType"]
    if data.get("status") is not None:
        import capo_route53globalresolver.types.cr_resource_status

        out["status"] = (
            capo_route53globalresolver.types.cr_resource_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_route53globalresolver.types.cr_resource_status.CRResourceStatus", ""
        )
    if data.get("updatedAt") is not None:
        import capo_route53globalresolver.types.iso8601_time_string

        out["updated_at"] = (
            capo_route53globalresolver.types.iso8601_time_string.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
