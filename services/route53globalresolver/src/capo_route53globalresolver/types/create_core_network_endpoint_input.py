"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CreateCoreNetworkEndpointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.client_token
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_id
    import capo_route53globalresolver.types.resource_name
    import capo_route53globalresolver.types.tags


class CreateCoreNetworkEndpointInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_route53globalresolver.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that ensures the request is idempotent. Making the same request multiple times with the same <code>clientToken</code> produces the same result every time.</p>"""
    core_network_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Cloud WAN core network to connect to this endpoint.</p>"""
    global_resolver_id: "capo_route53globalresolver.types.resource_id.ResourceId"
    """<p>The ID of the Route 53 Global Resolver to associate with this core network endpoint.</p>"""
    ip_addresses: "capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items.CoreNetworkEndpointDnsIpInputItems"
    """<p>The IP addresses that the core network endpoint uses to resolve DNS queries within the Amazon Web Services Cloud WAN core network.</p>"""
    name: NotRequired["capo_route53globalresolver.types.resource_name.ResourceName"]
    """<p>A descriptive name for the core network endpoint.</p>"""
    tags: NotRequired["capo_route53globalresolver.types.tags.Tags"]
    """<p>An array of user-defined keys and optional values that you can use to categorize and organize the core network endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreNetworkEndpointInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["coreNetworkArn"] = value["core_network_arn"]
    out["globalResolverId"] = value["global_resolver_id"]
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items

    out["ipAddresses"] = (
        capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items.serialize_json(
            value["ip_addresses"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCoreNetworkEndpointInput:
    out: CreateCoreNetworkEndpointInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("coreNetworkArn") is not None:
        out["core_network_arn"] = data["coreNetworkArn"]
    else:
        out["core_network_arn"] = ""
    if data.get("globalResolverId") is not None:
        out["global_resolver_id"] = data["globalResolverId"]
    else:
        out["global_resolver_id"] = ""
    if data.get("ipAddresses") is not None:
        import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items

        out["ip_addresses"] = (
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_items.deserialize_json(
                data["ipAddresses"]
            )
        )
    else:
        out["ip_addresses"] = []
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("tags") is not None:
        import capo_route53globalresolver.types.tags

        out["tags"] = capo_route53globalresolver.types.tags.deserialize_json(
            data["tags"]
        )
    return out
