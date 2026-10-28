"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_destination_endpoint_configuration
    import capo_mediaconnect.types.standard_destination_endpoint_configuration


class DestinationEndpointConfigurationStandardMember(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_destination_endpoint_configuration.StandardDestinationEndpointConfiguration"


class DestinationEndpointConfigurationRouterInputMember(TypedDict, closed=True):
    RouterInput: "capo_mediaconnect.types.router_input_destination_endpoint_configuration.RouterInputDestinationEndpointConfiguration"


DestinationEndpointConfiguration: TypeAlias = (
    DestinationEndpointConfigurationStandardMember
    | DestinationEndpointConfigurationRouterInputMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationEndpointConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_destination_endpoint_configuration

        return {
            "standard": capo_mediaconnect.types.standard_destination_endpoint_configuration.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterInput" in value:
        import capo_mediaconnect.types.router_input_destination_endpoint_configuration

        return {
            "routerInput": capo_mediaconnect.types.router_input_destination_endpoint_configuration.serialize_json(
                value["RouterInput"]
            )
        }
    else:
        raise SerializationError("DestinationEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> DestinationEndpointConfiguration:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_destination_endpoint_configuration

        return {
            "Standard": capo_mediaconnect.types.standard_destination_endpoint_configuration.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerInput") is not None:
        import capo_mediaconnect.types.router_input_destination_endpoint_configuration

        return {
            "RouterInput": capo_mediaconnect.types.router_input_destination_endpoint_configuration.deserialize_json(
                data["routerInput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DestinationEndpointConfiguration: no recognized variant key"
        )
