"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_router_network_interface_configuration
    import capo_mediaconnect.types.vpc_router_network_interface_configuration


class _RouterNetworkInterfaceConfiguration_Public(TypedDict, closed=True):
    Public: "capo_mediaconnect.types.public_router_network_interface_configuration.PublicRouterNetworkInterfaceConfiguration"


class _RouterNetworkInterfaceConfiguration_Vpc(TypedDict, closed=True):
    Vpc: "capo_mediaconnect.types.vpc_router_network_interface_configuration.VpcRouterNetworkInterfaceConfiguration"


RouterNetworkInterfaceConfiguration: TypeAlias = (
    _RouterNetworkInterfaceConfiguration_Public
    | _RouterNetworkInterfaceConfiguration_Vpc
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RouterNetworkInterfaceConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "Public" in value:
        import capo_mediaconnect.types.public_router_network_interface_configuration

        return {
            "public": capo_mediaconnect.types.public_router_network_interface_configuration.serialize_json(
                value["Public"]
            )
        }
    elif "Vpc" in value:
        import capo_mediaconnect.types.vpc_router_network_interface_configuration

        return {
            "vpc": capo_mediaconnect.types.vpc_router_network_interface_configuration.serialize_json(
                value["Vpc"]
            )
        }
    else:
        raise SerializationError(
            "RouterNetworkInterfaceConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterNetworkInterfaceConfiguration:
    if data.get("public") is not None:
        import capo_mediaconnect.types.public_router_network_interface_configuration

        return {
            "Public": capo_mediaconnect.types.public_router_network_interface_configuration.deserialize_json(
                data["public"]
            )
        }
    elif data.get("vpc") is not None:
        import capo_mediaconnect.types.vpc_router_network_interface_configuration

        return {
            "Vpc": capo_mediaconnect.types.vpc_router_network_interface_configuration.deserialize_json(
                data["vpc"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RouterNetworkInterfaceConfiguration: no recognized variant key"
        )
