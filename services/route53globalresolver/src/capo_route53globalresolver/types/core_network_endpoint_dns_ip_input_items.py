"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CoreNetworkEndpointDnsIpInputItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item

CoreNetworkEndpointDnsIpInputItems: TypeAlias = list[
    "capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item.CoreNetworkEndpointDnsIpInputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEndpointDnsIpInputItems) -> list:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkEndpointDnsIpInputItems:
    import capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item

    out: CoreNetworkEndpointDnsIpInputItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route53globalresolver.types.core_network_endpoint_dns_ip_input_item.deserialize_json(
                item
            )
        )
    return out
