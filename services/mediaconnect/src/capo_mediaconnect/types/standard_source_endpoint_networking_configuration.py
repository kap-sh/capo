"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardSourceEndpointNetworkingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_source_endpoint_networking_configuration
    import capo_mediaconnect.types.vpc_source_endpoint_networking_configuration


class StandardSourceEndpointNetworkingConfigurationPublicMember(TypedDict, closed=True):
    Public: "capo_mediaconnect.types.public_source_endpoint_networking_configuration.PublicSourceEndpointNetworkingConfiguration"


class StandardSourceEndpointNetworkingConfigurationVpcMember(TypedDict, closed=True):
    Vpc: "capo_mediaconnect.types.vpc_source_endpoint_networking_configuration.VpcSourceEndpointNetworkingConfiguration"


StandardSourceEndpointNetworkingConfiguration: TypeAlias = (
    StandardSourceEndpointNetworkingConfigurationPublicMember
    | StandardSourceEndpointNetworkingConfigurationVpcMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: StandardSourceEndpointNetworkingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StandardSourceEndpointNetworkingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Public" in value:
        import capo_mediaconnect.types.public_source_endpoint_networking_configuration

        return {
            "public": capo_mediaconnect.types.public_source_endpoint_networking_configuration.serialize_json(
                value["Public"]
            )
        }
    elif "Vpc" in value:
        import capo_mediaconnect.types.vpc_source_endpoint_networking_configuration

        return {
            "vpc": capo_mediaconnect.types.vpc_source_endpoint_networking_configuration.serialize_json(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError(
            "StandardSourceEndpointNetworkingConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> StandardSourceEndpointNetworkingConfiguration:
    if data.get("public") is not None:
        import capo_mediaconnect.types.public_source_endpoint_networking_configuration

        return {
            "Public": capo_mediaconnect.types.public_source_endpoint_networking_configuration.deserialize_json(
                data["public"]
            )
        }
    elif data.get("vpc") is not None:
        import capo_mediaconnect.types.vpc_source_endpoint_networking_configuration

        return {
            "Vpc": capo_mediaconnect.types.vpc_source_endpoint_networking_configuration.deserialize_json(
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
            "StandardSourceEndpointNetworkingConfiguration: no recognized variant key"
        )
