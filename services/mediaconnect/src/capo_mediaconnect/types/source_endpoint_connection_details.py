"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SourceEndpointConnectionDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_output_source_endpoint_connection_details
    import capo_mediaconnect.types.standard_source_endpoint_connection_details


class _SourceEndpointConnectionDetails_Standard(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_source_endpoint_connection_details.StandardSourceEndpointConnectionDetails"


class _SourceEndpointConnectionDetails_RouterOutput(TypedDict, closed=True):
    RouterOutput: "capo_mediaconnect.types.router_output_source_endpoint_connection_details.RouterOutputSourceEndpointConnectionDetails"


SourceEndpointConnectionDetails: TypeAlias = (
    _SourceEndpointConnectionDetails_Standard
    | _SourceEndpointConnectionDetails_RouterOutput
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceEndpointConnectionDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceEndpointConnectionDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_source_endpoint_connection_details

        return {
            "standard": capo_mediaconnect.types.standard_source_endpoint_connection_details.serialize_json(
                value["Standard"]
            )
        }
    elif "RouterOutput" in value:
        import capo_mediaconnect.types.router_output_source_endpoint_connection_details

        return {
            "routerOutput": capo_mediaconnect.types.router_output_source_endpoint_connection_details.serialize_json(
                value["RouterOutput"]
            )
        }
    else:
        raise SerializationError("SourceEndpointConnectionDetails: no variant present")


def deserialize_json(data: dict) -> SourceEndpointConnectionDetails:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_source_endpoint_connection_details

        return {
            "Standard": capo_mediaconnect.types.standard_source_endpoint_connection_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("routerOutput") is not None:
        import capo_mediaconnect.types.router_output_source_endpoint_connection_details

        return {
            "RouterOutput": capo_mediaconnect.types.router_output_source_endpoint_connection_details.deserialize_json(
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
            "SourceEndpointConnectionDetails: no recognized variant key"
        )
