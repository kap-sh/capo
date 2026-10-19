"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateDNSViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route53globalresolver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.dns_sec_validation_type
    import capo_route53globalresolver.types.edns_client_subnet_type
    import capo_route53globalresolver.types.firewall_rules_fail_open_type
    import capo_route53globalresolver.types.resource_description
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.tags


class CreateDNSViewInput(TypedDict, closed=True):
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver to associate with this DNS view.</p>"""
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique string that identifies the request and ensures idempotency.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>A descriptive name for the DNS view.</p>"""
    dnssec_validation: NotRequired[
        "capo_route53globalresolver.types.dns_sec_validation_type.DnsSecValidationType"
    ]
    """<p>Whether to enable DNSSEC validation for DNS queries in this DNS view. When enabled, the resolver verifies the authenticity and integrity of DNS responses from public name servers for DNSSEC-signed domains.</p>"""
    edns_client_subnet: NotRequired[
        "capo_route53globalresolver.types.edns_client_subnet_type.EdnsClientSubnetType"
    ]
    """<p>Whether to enable EDNS Client Subnet injection for DNS queries in this DNS view. When enabled, client subnet information is forwarded to provide more accurate geographic-based DNS responses.</p>"""
    firewall_rules_fail_open: NotRequired[
        "capo_route53globalresolver.types.firewall_rules_fail_open_type.FirewallRulesFailOpenType"
    ]
    """<p>Determines the behavior when Route 53 Global Resolver cannot apply DNS firewall rules due to service impairment. When enabled, DNS queries are allowed through; when disabled, queries are blocked.</p>"""
    description: NotRequired[
        "capo_route53globalresolver.types.resource_description.ResourceDescription"
    ]
    """<p>An optional description for the DNS view.</p>"""
    tags: NotRequired["capo_route53globalresolver.types.tags.Tags"]
    """<p>Tags to associate with the DNS view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDNSViewInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "dnssec_validation" in value:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssecValidation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.serialize_json(
                value["dnssec_validation"]
            )
        )
    if "edns_client_subnet" in value:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["ednsClientSubnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.serialize_json(
                value["edns_client_subnet"]
            )
        )
    if "firewall_rules_fail_open" in value:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewallRulesFailOpen"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.serialize_json(
                value["firewall_rules_fail_open"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDNSViewInput:
    out: CreateDNSViewInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDNSViewInput.name required")
    if data.get("dnssecValidation") is not None:
        import capo_route53globalresolver.types.dns_sec_validation_type

        out["dnssec_validation"] = (
            capo_route53globalresolver.types.dns_sec_validation_type.deserialize_json(
                data["dnssecValidation"]
            )
        )
    if data.get("ednsClientSubnet") is not None:
        import capo_route53globalresolver.types.edns_client_subnet_type

        out["edns_client_subnet"] = (
            capo_route53globalresolver.types.edns_client_subnet_type.deserialize_json(
                data["ednsClientSubnet"]
            )
        )
    if data.get("firewallRulesFailOpen") is not None:
        import capo_route53globalresolver.types.firewall_rules_fail_open_type

        out["firewall_rules_fail_open"] = (
            capo_route53globalresolver.types.firewall_rules_fail_open_type.deserialize_json(
                data["firewallRulesFailOpen"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
