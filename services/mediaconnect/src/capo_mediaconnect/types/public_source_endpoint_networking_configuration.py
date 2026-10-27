"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicSourceEndpointNetworkingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list


class PublicSourceEndpointNetworkingConfiguration(TypedDict, closed=True):
    source_allow_rules: "capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list.PublicSourceEndpointNetworkingConfigurationAllowRuleList"
    """<p>The rules that specify which CIDR blocks can connect to the source endpoint. You can specify up to 10 rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicSourceEndpointNetworkingConfiguration) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list

    out["sourceAllowRules"] = (
        capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list.serialize_json(
            value["source_allow_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> PublicSourceEndpointNetworkingConfiguration:
    out: PublicSourceEndpointNetworkingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("sourceAllowRules") is not None:
        import capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list

        out["source_allow_rules"] = (
            capo_mediaconnect.types.public_source_endpoint_networking_configuration_allow_rule_list.deserialize_json(
                data["sourceAllowRules"]
            )
        )
    else:
        out["source_allow_rules"] = []
    return out
