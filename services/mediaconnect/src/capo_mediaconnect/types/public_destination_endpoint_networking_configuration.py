"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicDestinationEndpointNetworkingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list


class PublicDestinationEndpointNetworkingConfiguration(TypedDict, closed=True):
    destination_allow_rules: "capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list.PublicDestinationEndpointNetworkingConfigurationAllowRuleList"
    """<p>The rules that specify which CIDR blocks can connect to the destination endpoint. You can specify up to 10 rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicDestinationEndpointNetworkingConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list

    out["destinationAllowRules"] = (
        capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list.serialize_json(
            value["destination_allow_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> PublicDestinationEndpointNetworkingConfiguration:
    out: PublicDestinationEndpointNetworkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAllowRules") is not None:
        import capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list

        out["destination_allow_rules"] = (
            capo_mediaconnect.types.public_destination_endpoint_networking_configuration_allow_rule_list.deserialize_json(
                data["destinationAllowRules"]
            )
        )
    else:
        out["destination_allow_rules"] = []
    return out
