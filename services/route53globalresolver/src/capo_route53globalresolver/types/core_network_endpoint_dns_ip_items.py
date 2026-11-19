"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CoreNetworkEndpointDnsIpItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_item

CoreNetworkEndpointDnsIpItems: TypeAlias = list[
    "capo_route53globalresolver.types.core_network_endpoint_dns_ip_item.CoreNetworkEndpointDnsIpItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEndpointDnsIpItems) -> list:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkEndpointDnsIpItems:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_item

    out: CoreNetworkEndpointDnsIpItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_item.deserialize_json(
                item
            )
        )
    return out
