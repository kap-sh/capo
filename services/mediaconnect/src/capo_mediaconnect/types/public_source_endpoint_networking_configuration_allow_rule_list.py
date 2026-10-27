"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicSourceEndpointNetworkingConfigurationAllowRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule

PublicSourceEndpointNetworkingConfigurationAllowRuleList: TypeAlias = list[
    "capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule.PublicSourceEndpointNetworkingConfigurationAllowRule"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: PublicSourceEndpointNetworkingConfigurationAllowRuleList,
) -> list:
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> PublicSourceEndpointNetworkingConfigurationAllowRuleList:
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule

    out: PublicSourceEndpointNetworkingConfigurationAllowRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule.deserialize_json(
                item
            )
        )
    return out
