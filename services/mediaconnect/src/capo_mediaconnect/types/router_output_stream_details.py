"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputStreamDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_connect_flow_router_output_stream_details
    import capo_mediaconnect.types.media_live_input_router_output_stream_details
    import capo_mediaconnect.types.source_endpoint_router_output_stream_details
    import capo_mediaconnect.types.standard_router_output_stream_details


class RouterOutputStreamDetailsStandardMember(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_router_output_stream_details.StandardRouterOutputStreamDetails"


class RouterOutputStreamDetailsMediaConnectFlowMember(TypedDict, closed=True):
    MediaConnectFlow: "capo_mediaconnect.types.media_connect_flow_router_output_stream_details.MediaConnectFlowRouterOutputStreamDetails"


class RouterOutputStreamDetailsMediaLiveInputMember(TypedDict, closed=True):
    MediaLiveInput: "capo_mediaconnect.types.media_live_input_router_output_stream_details.MediaLiveInputRouterOutputStreamDetails"


class RouterOutputStreamDetailsSourceEndpointMember(TypedDict, closed=True):
    SourceEndpoint: "capo_mediaconnect.types.source_endpoint_router_output_stream_details.SourceEndpointRouterOutputStreamDetails"


RouterOutputStreamDetails: TypeAlias = (
    RouterOutputStreamDetailsStandardMember
    | RouterOutputStreamDetailsMediaConnectFlowMember
    | RouterOutputStreamDetailsMediaLiveInputMember
    | RouterOutputStreamDetailsSourceEndpointMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputStreamDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterOutputStreamDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_router_output_stream_details

        return {
            "standard": capo_mediaconnect.types.standard_router_output_stream_details.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaConnectFlow" in value:
        import capo_mediaconnect.types.media_connect_flow_router_output_stream_details

        return {
            "mediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_output_stream_details.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "MediaLiveInput" in value:
        import capo_mediaconnect.types.media_live_input_router_output_stream_details

        return {
            "mediaLiveInput": capo_mediaconnect.types.media_live_input_router_output_stream_details.serialize_json(
                value["MediaLiveInput"]
            )
        }
    elif "SourceEndpoint" in value:
        import capo_mediaconnect.types.source_endpoint_router_output_stream_details

        return {
            "sourceEndpoint": capo_mediaconnect.types.source_endpoint_router_output_stream_details.serialize_json(
                value["SourceEndpoint"]
            )
        }
    else:
        raise SerializationError("RouterOutputStreamDetails: no variant present")


def deserialize_json(data: dict) -> RouterOutputStreamDetails:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_router_output_stream_details

        return {
            "Standard": capo_mediaconnect.types.standard_router_output_stream_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("mediaConnectFlow") is not None:
        import capo_mediaconnect.types.media_connect_flow_router_output_stream_details

        return {
            "MediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_output_stream_details.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif data.get("mediaLiveInput") is not None:
        import capo_mediaconnect.types.media_live_input_router_output_stream_details

        return {
            "MediaLiveInput": capo_mediaconnect.types.media_live_input_router_output_stream_details.deserialize_json(
                data["mediaLiveInput"]
            )
        }
    elif data.get("sourceEndpoint") is not None:
        import capo_mediaconnect.types.source_endpoint_router_output_stream_details

        return {
            "SourceEndpoint": capo_mediaconnect.types.source_endpoint_router_output_stream_details.deserialize_json(
                data["sourceEndpoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RouterOutputStreamDetails: no recognized variant key"
        )
