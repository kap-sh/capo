"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputStreamDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.destination_endpoint_router_input_stream_details
    import capo_mediaconnect.types.failover_router_input_stream_details
    import capo_mediaconnect.types.media_connect_flow_router_input_stream_details
    import capo_mediaconnect.types.media_live_channel_router_input_stream_details
    import capo_mediaconnect.types.merge_router_input_stream_details
    import capo_mediaconnect.types.standard_router_input_stream_details


class RouterInputStreamDetailsDestinationEndpointMember(TypedDict, closed=True):
    DestinationEndpoint: "capo_mediaconnect.types.destination_endpoint_router_input_stream_details.DestinationEndpointRouterInputStreamDetails"


class RouterInputStreamDetailsStandardMember(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_router_input_stream_details.StandardRouterInputStreamDetails"


class RouterInputStreamDetailsMediaLiveChannelMember(TypedDict, closed=True):
    MediaLiveChannel: "capo_mediaconnect.types.media_live_channel_router_input_stream_details.MediaLiveChannelRouterInputStreamDetails"


class RouterInputStreamDetailsFailoverMember(TypedDict, closed=True):
    Failover: "capo_mediaconnect.types.failover_router_input_stream_details.FailoverRouterInputStreamDetails"


class RouterInputStreamDetailsMediaConnectFlowMember(TypedDict, closed=True):
    MediaConnectFlow: "capo_mediaconnect.types.media_connect_flow_router_input_stream_details.MediaConnectFlowRouterInputStreamDetails"


class RouterInputStreamDetailsMergeMember(TypedDict, closed=True):
    Merge: "capo_mediaconnect.types.merge_router_input_stream_details.MergeRouterInputStreamDetails"


RouterInputStreamDetails: TypeAlias = (
    RouterInputStreamDetailsDestinationEndpointMember
    | RouterInputStreamDetailsStandardMember
    | RouterInputStreamDetailsMediaLiveChannelMember
    | RouterInputStreamDetailsFailoverMember
    | RouterInputStreamDetailsMediaConnectFlowMember
    | RouterInputStreamDetailsMergeMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputStreamDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterInputStreamDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DestinationEndpoint" in value:
        import capo_mediaconnect.types.destination_endpoint_router_input_stream_details

        return {
            "destinationEndpoint": capo_mediaconnect.types.destination_endpoint_router_input_stream_details.serialize_json(
                value["DestinationEndpoint"]
            )
        }
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_router_input_stream_details

        return {
            "standard": capo_mediaconnect.types.standard_router_input_stream_details.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaLiveChannel" in value:
        import capo_mediaconnect.types.media_live_channel_router_input_stream_details

        return {
            "mediaLiveChannel": capo_mediaconnect.types.media_live_channel_router_input_stream_details.serialize_json(
                value["MediaLiveChannel"]
            )
        }
    elif "Failover" in value:
        import capo_mediaconnect.types.failover_router_input_stream_details

        return {
            "failover": capo_mediaconnect.types.failover_router_input_stream_details.serialize_json(
                value["Failover"]
            )
        }
    elif "MediaConnectFlow" in value:
        import capo_mediaconnect.types.media_connect_flow_router_input_stream_details

        return {
            "mediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_input_stream_details.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "Merge" in value:
        import capo_mediaconnect.types.merge_router_input_stream_details

        return {
            "merge": capo_mediaconnect.types.merge_router_input_stream_details.serialize_json(
                value["Merge"]
            )
        }
    else:
        raise SerializationError("RouterInputStreamDetails: no variant present")


def deserialize_json(data: dict) -> RouterInputStreamDetails:
    if data.get("destinationEndpoint") is not None:
        import capo_mediaconnect.types.destination_endpoint_router_input_stream_details

        return {
            "DestinationEndpoint": capo_mediaconnect.types.destination_endpoint_router_input_stream_details.deserialize_json(
                data["destinationEndpoint"]
            )
        }
    elif data.get("standard") is not None:
        import capo_mediaconnect.types.standard_router_input_stream_details

        return {
            "Standard": capo_mediaconnect.types.standard_router_input_stream_details.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("mediaLiveChannel") is not None:
        import capo_mediaconnect.types.media_live_channel_router_input_stream_details

        return {
            "MediaLiveChannel": capo_mediaconnect.types.media_live_channel_router_input_stream_details.deserialize_json(
                data["mediaLiveChannel"]
            )
        }
    elif data.get("failover") is not None:
        import capo_mediaconnect.types.failover_router_input_stream_details

        return {
            "Failover": capo_mediaconnect.types.failover_router_input_stream_details.deserialize_json(
                data["failover"]
            )
        }
    elif data.get("mediaConnectFlow") is not None:
        import capo_mediaconnect.types.media_connect_flow_router_input_stream_details

        return {
            "MediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_input_stream_details.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif data.get("merge") is not None:
        import capo_mediaconnect.types.merge_router_input_stream_details

        return {
            "Merge": capo_mediaconnect.types.merge_router_input_stream_details.deserialize_json(
                data["merge"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RouterInputStreamDetails: no recognized variant key"
        )
