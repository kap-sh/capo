"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicDestinationEndpointNetworkingConfigurationAllowRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule

PublicDestinationEndpointNetworkingConfigurationAllowRuleList: TypeAlias = list[
    "capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule.PublicDestinationEndpointNetworkingConfigurationAllowRule"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: PublicDestinationEndpointNetworkingConfigurationAllowRuleList,
) -> list:
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule

    out: list = []
    for item in value:
        out.append(
            capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> PublicDestinationEndpointNetworkingConfigurationAllowRuleList:
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule

    out: PublicDestinationEndpointNetworkingConfigurationAllowRuleList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule.deserialize_json(
                item
            )
        )
    return out
