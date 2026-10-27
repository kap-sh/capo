"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpointAssociatedResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details
    import capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details


class _DestinationEndpointAssociatedResourceDetails_Standard(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details.StandardDestinationEndpointAssociatedResourceDetails"


class _DestinationEndpointAssociatedResourceDetails_RouterInput(TypedDict, closed=True):
    RouterInput: "capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details.RouterInputDestinationEndpointAssociatedResourceDetails"


DestinationEndpointAssociatedResourceDetails: TypeAlias = (
    _DestinationEndpointAssociatedResourceDetails_Standard
    | _DestinationEndpointAssociatedResourceDetails_RouterInput
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpointAssociatedResourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DestinationEndpointAssociatedResourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details

        return {
            "standard": capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterInput" in value:
        import capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details

        return {
            "routerInput": capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details.serialize_json(
                value["RouterInput"]
            )
        }
    else:
        raise SerializationError(
            "DestinationEndpointAssociatedResourceDetails: no variant present"
        )


def deserialize_json(data: dict) -> DestinationEndpointAssociatedResourceDetails:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details

        return {
            "Standard": capo_mediaconnect.types.standard_destination_endpoint_associated_resource_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerInput") is not None:
        import capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details

        return {
            "RouterInput": capo_mediaconnect.types.router_input_destination_endpoint_associated_resource_details.deserialize_json(
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
            "DestinationEndpointAssociatedResourceDetails: no recognized variant key"
        )
