"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointAssociatedResourceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details
    import capo_mediaconnect.types.standard_source_endpoint_associated_resource_details


class SourceEndpointAssociatedResourceDetailsStandardMember(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_source_endpoint_associated_resource_details.StandardSourceEndpointAssociatedResourceDetails"


class SourceEndpointAssociatedResourceDetailsRouterOutputMember(TypedDict, closed=True):
    RouterOutput: "capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details.RouterOutputSourceEndpointAssociatedResourceDetails"


SourceEndpointAssociatedResourceDetails: TypeAlias = (
    SourceEndpointAssociatedResourceDetailsStandardMember
    | SourceEndpointAssociatedResourceDetailsRouterOutputMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointAssociatedResourceDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceEndpointAssociatedResourceDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_source_endpoint_associated_resource_details

        return {
            "standard": capo_mediaconnect.types.standard_source_endpoint_associated_resource_details.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterOutput" in value:
        import capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details

        return {
            "routerOutput": capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details.serialize_json(
                value["RouterOutput"]
            )
        }
    else:
        raise SerializationError(
            "SourceEndpointAssociatedResourceDetails: no variant present"
        )


def deserialize_json(data: dict) -> SourceEndpointAssociatedResourceDetails:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_source_endpoint_associated_resource_details

        return {
            "Standard": capo_mediaconnect.types.standard_source_endpoint_associated_resource_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerOutput") is not None:
        import capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details

        return {
            "RouterOutput": capo_mediaconnect.types.router_output_source_endpoint_associated_resource_details.deserialize_json(
                data["routerOutput"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SourceEndpointAssociatedResourceDetails: no recognized variant key"
        )
