"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CoreNetworkEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53globalresolver.types.core_network_endpoints_item

CoreNetworkEndpoints: TypeAlias = list[
    "capo_route53globalresolver.types.core_network_endpoints_item.CoreNetworkEndpointsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEndpoints) -> list:
    import capo_route53globalresolver.types.core_network_endpoints_item

    out: list = []
    for item in value:
        out.append(
            capo_route53globalresolver.types.core_network_endpoints_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkEndpoints:
    import capo_route53globalresolver.types.core_network_endpoints_item

    out: CoreNetworkEndpoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_route53globalresolver.types.core_network_endpoints_item.deserialize_json(
                item
            )
        )
    return out
