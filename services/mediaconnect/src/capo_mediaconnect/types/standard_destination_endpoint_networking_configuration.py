"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardDestinationEndpointNetworkingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_destination_endpoint_networking_configuration
    import capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration


class StandardDestinationEndpointNetworkingConfigurationPublicMember(
    TypedDict, closed=True
):
    Public: "capo_mediaconnect.types.public_destination_endpoint_networking_configuration.PublicDestinationEndpointNetworkingConfiguration"


class StandardDestinationEndpointNetworkingConfigurationVpcMember(
    TypedDict, closed=True
):
    Vpc: "capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration.VpcDestinationEndpointNetworkingConfiguration"


StandardDestinationEndpointNetworkingConfiguration: TypeAlias = (
    StandardDestinationEndpointNetworkingConfigurationPublicMember
    | StandardDestinationEndpointNetworkingConfigurationVpcMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: StandardDestinationEndpointNetworkingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StandardDestinationEndpointNetworkingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Public" in value:
        import capo_mediaconnect.types.public_destination_endpoint_networking_configuration

        return {
            "public": capo_mediaconnect.types.public_destination_endpoint_networking_configuration.serialize_json(
                value["Public"]
            )
        }
    elif "Vpc" in value:
        import capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration

        return {
            "vpc": capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration.serialize_json(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError(
            "StandardDestinationEndpointNetworkingConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> StandardDestinationEndpointNetworkingConfiguration:
    if data.get("public") is not None:
        import capo_mediaconnect.types.public_destination_endpoint_networking_configuration

        return {
            "Public": capo_mediaconnect.types.public_destination_endpoint_networking_configuration.deserialize_json(
                data["public"]
            )
        }
    elif data.get("vpc") is not None:
        import capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration

        return {
            "Vpc": capo_mediaconnect.types.vpc_destination_endpoint_networking_configuration.deserialize_json(
                data["vpc"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "StandardDestinationEndpointNetworkingConfiguration: no recognized variant key"
        )
