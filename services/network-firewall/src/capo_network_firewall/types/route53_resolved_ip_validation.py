"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Route53ResolvedIPValidation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.dns_expiry_exception_policy
    import capo_network_firewall.types.dns_firewall_rule_group_id
    import capo_network_firewall.types.route53_resolved_ip_validation_action
    import capo_network_firewall.types.route53_resolved_ip_validation_addresses


class Route53ResolvedIPValidation(TypedDict, closed=True):
    action: "capo_network_firewall.types.route53_resolved_ip_validation_action.Route53ResolvedIPValidationAction"
    """<p>The action that Network Firewall takes for a connection whose destination IP address fails resolved IP validation. A destination IP address fails validation when the Route 53 Resolver didn't return it in a DNS response in an associated VPC. Valid values are the following:</p> <ul> <li> <p> <code>ALERT</code> – Tags the matching connection in the firewall's flow logs without blocking it, when you enable logging. Use this to observe the effect of resolved IP validation before you enforce it.</p> </li> <li> <p> <code>DROP</code> – Silently blocks the connection without sending any response to the client.</p> </li> <li> <p> <code>REJECT</code> – Blocks the connection and sends a TCP reset (RST) to the client. Because a TCP reset applies only to TCP connections, Network Firewall drops non-TCP traffic instead of resetting it.</p> </li> </ul>"""
    dns_firewall_rule_group_id: (
        "capo_network_firewall.types.dns_firewall_rule_group_id.DNSFirewallRuleGroupId"
    )
    """<p>The ID of the Route 53 Resolver DNS Firewall rule group that determines which VPCs' DNS resolutions count for resolved IP validation. A destination IP address counts as resolved for a domain only when the Route 53 Resolver returned it in a DNS response within a VPC that's associated with this rule group. Associate the rule group with the VPCs that send traffic to the firewall. The ID must match the pattern <code>^rslvr-frg-[0-9a-f]+$</code>. It must also exist and be accessible from your account. Network Firewall validates this when you create or update the policy.</p> <p>Changing this value swaps the managed rule group association. Network Firewall processes the swap asynchronously. Each policy can have only one managed Route 53 Resolver DNS Firewall association. While a swap is in progress, Network Firewall rejects further changes to this setting. Wait until the swap completes, then retry.</p>"""
    dns_expiry_exception_policy: "capo_network_firewall.types.dns_expiry_exception_policy.DNSExpiryExceptionPolicy"
    """<p>The action that Network Firewall takes when the DNS resolution recorded for a destination IP address has expired from the resolved IP cache. This applies when Network Firewall still sees traffic to that IP address after the expiry. Network Firewall keeps a resolution for longer than the DNS record's time to live (TTL). Valid values are the following:</p> <ul> <li> <p> <code>CONTINUE</code> – Treats the expired resolution as still valid and doesn't block the connection because of expiry.</p> </li> <li> <p> <code>DROP</code> – Silently blocks traffic to the IP address after its resolution has expired, without sending any response to the client.</p> </li> <li> <p> <code>REJECT</code> – Blocks traffic to the IP address after its resolution has expired and sends a TCP reset (RST) to the client. Network Firewall drops non-TCP traffic instead of resetting it.</p> </li> </ul>"""
    bypass_destination_validation_ip_ranges: NotRequired[
        "capo_network_firewall.types.route53_resolved_ip_validation_addresses.Route53ResolvedIPValidationAddresses"
    ]
    """<p>The destination IP address ranges that are exempt from the policy-level resolved IP check. Network Firewall doesn't apply the <code>Action</code> in this configuration to a connection whose destination falls in these ranges, even if the Route 53 Resolver didn't return that IP address in an associated VPC. Specify each entry as an IPv4 or IPv6 address or CIDR range, up to 100 entries.</p> <p>This exemption applies only to the policy-level check. Stateful rules that use the <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> target type or the <code>aws_route_53_resolved_domain</code> keyword still evaluate connections to these destinations and match them independently of this list.</p>"""
    source_ip_ranges: NotRequired[
        "capo_network_firewall.types.route53_resolved_ip_validation_addresses.Route53ResolvedIPValidationAddresses"
    ]
    """<p>The client source IP address ranges whose connections are subject to resolved IP validation. Specify each entry as an IPv4 or IPv6 address or CIDR range, up to 100 entries. If you omit this field, resolved IP validation applies to the CIDR ranges of the firewall's VPC and of any additional VPCs attached to the firewall. Specifying an empty list is not the same as omitting the field: an empty list means that Network Firewall doesn't validate any source addresses.</p> <p>This scope applies to the policy-level check only. Stateful rules that use the <code>AWS_ROUTE_53_RESOLVED_DOMAIN</code> target type or the <code>aws_route_53_resolved_domain</code> keyword still evaluate their destinations regardless of <code>SourceIPRanges</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Route53ResolvedIPValidation) -> dict:
    out: dict = {}
    import capo_network_firewall.types.route53_resolved_ip_validation_action

    out["Action"] = (
        capo_network_firewall.types.route53_resolved_ip_validation_action.serialize_aws_json_1_0(
            value["action"]
        )
    )
    out["DNSFirewallRuleGroupId"] = value["dns_firewall_rule_group_id"]
    import capo_network_firewall.types.dns_expiry_exception_policy

    out["DNSExpiryExceptionPolicy"] = (
        capo_network_firewall.types.dns_expiry_exception_policy.serialize_aws_json_1_0(
            value["dns_expiry_exception_policy"]
        )
    )
    if "bypass_destination_validation_ip_ranges" in value:
        import capo_network_firewall.types.route53_resolved_ip_validation_addresses

        out["BypassDestinationValidationIPRanges"] = (
            capo_network_firewall.types.route53_resolved_ip_validation_addresses.serialize_aws_json_1_0(
                value["bypass_destination_validation_ip_ranges"]
            )
        )
    if "source_ip_ranges" in value:
        import capo_network_firewall.types.route53_resolved_ip_validation_addresses

        out["SourceIPRanges"] = (
            capo_network_firewall.types.route53_resolved_ip_validation_addresses.serialize_aws_json_1_0(
                value["source_ip_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Route53ResolvedIPValidation:
    out: Route53ResolvedIPValidation = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_network_firewall.types.route53_resolved_ip_validation_action

        out["action"] = (
            capo_network_firewall.types.route53_resolved_ip_validation_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_network_firewall.types.route53_resolved_ip_validation_action.Route53ResolvedIPValidationAction",
            "",
        )
    if data.get("DNSFirewallRuleGroupId") is not None:
        out["dns_firewall_rule_group_id"] = data["DNSFirewallRuleGroupId"]
    else:
        out["dns_firewall_rule_group_id"] = ""
    if data.get("DNSExpiryExceptionPolicy") is not None:
        import capo_network_firewall.types.dns_expiry_exception_policy

        out["dns_expiry_exception_policy"] = (
            capo_network_firewall.types.dns_expiry_exception_policy.deserialize_aws_json_1_0(
                data["DNSExpiryExceptionPolicy"]
            )
        )
    else:
        import typing

        out["dns_expiry_exception_policy"] = typing.cast(
            "capo_network_firewall.types.dns_expiry_exception_policy.DNSExpiryExceptionPolicy",
            "",
        )
    if data.get("BypassDestinationValidationIPRanges") is not None:
        import capo_network_firewall.types.route53_resolved_ip_validation_addresses

        out["bypass_destination_validation_ip_ranges"] = (
            capo_network_firewall.types.route53_resolved_ip_validation_addresses.deserialize_aws_json_1_0(
                data["BypassDestinationValidationIPRanges"]
            )
        )
    if data.get("SourceIPRanges") is not None:
        import capo_network_firewall.types.route53_resolved_ip_validation_addresses

        out["source_ip_ranges"] = (
            capo_network_firewall.types.route53_resolved_ip_validation_addresses.deserialize_aws_json_1_0(
                data["SourceIPRanges"]
            )
        )
    return out
