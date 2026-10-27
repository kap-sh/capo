"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointConnectionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_destination_endpoint_connection_details
    import capo_mediaconnect.types.standard_destination_endpoint_connection_details


class _DestinationEndpointConnectionDetails_Standard(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_destination_endpoint_connection_details.StandardDestinationEndpointConnectionDetails"


class _DestinationEndpointConnectionDetails_RouterInput(TypedDict, closed=True):
    RouterInput: "capo_mediaconnect.types.router_input_destination_endpoint_connection_details.RouterInputDestinationEndpointConnectionDetails"


DestinationEndpointConnectionDetails: TypeAlias = (
    _DestinationEndpointConnectionDetails_Standard
    | _DestinationEndpointConnectionDetails_RouterInput
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointConnectionDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationEndpointConnectionDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_destination_endpoint_connection_details

        return {
            "standard": capo_mediaconnect.types.standard_destination_endpoint_connection_details.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterInput" in value:
        import capo_mediaconnect.types.router_input_destination_endpoint_connection_details

        return {
            "routerInput": capo_mediaconnect.types.router_input_destination_endpoint_connection_details.serialize_json(
                value["RouterInput"]
            )
        }
    else:
        raise SerializationError(
            "DestinationEndpointConnectionDetails: no variant present"
        )


def deserialize_json(data: dict) -> DestinationEndpointConnectionDetails:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_destination_endpoint_connection_details

        return {
            "Standard": capo_mediaconnect.types.standard_destination_endpoint_connection_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerInput") is not None:
        import capo_mediaconnect.types.router_input_destination_endpoint_connection_details

        return {
            "RouterInput": capo_mediaconnect.types.router_input_destination_endpoint_connection_details.deserialize_json(
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
            "DestinationEndpointConnectionDetails: no recognized variant key"
        )
