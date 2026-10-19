"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.failover_router_input_configuration
    import capo_mediaconnect.types.media_connect_flow_router_input_configuration
    import capo_mediaconnect.types.media_live_channel_router_input_configuration
    import capo_mediaconnect.types.merge_router_input_configuration
    import capo_mediaconnect.types.standard_router_input_configuration


class _RouterInputConfiguration_Standard(TypedDict, closed=True):
    Standard: "capo_mediaconnect.types.standard_router_input_configuration.StandardRouterInputConfiguration"


class _RouterInputConfiguration_MediaLiveChannel(TypedDict, closed=True):
    MediaLiveChannel: "capo_mediaconnect.types.media_live_channel_router_input_configuration.MediaLiveChannelRouterInputConfiguration"


class _RouterInputConfiguration_Failover(TypedDict, closed=True):
    Failover: "capo_mediaconnect.types.failover_router_input_configuration.FailoverRouterInputConfiguration"


class _RouterInputConfiguration_MediaConnectFlow(TypedDict, closed=True):
    MediaConnectFlow: "capo_mediaconnect.types.media_connect_flow_router_input_configuration.MediaConnectFlowRouterInputConfiguration"


class _RouterInputConfiguration_Merge(TypedDict, closed=True):
    Merge: "capo_mediaconnect.types.merge_router_input_configuration.MergeRouterInputConfiguration"


RouterInputConfiguration: TypeAlias = (
    _RouterInputConfiguration_Standard
    | _RouterInputConfiguration_MediaLiveChannel
    | _RouterInputConfiguration_Failover
    | _RouterInputConfiguration_MediaConnectFlow
    | _RouterInputConfiguration_Merge
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RouterInputConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "Standard" in value:
        import capo_mediaconnect.types.standard_router_input_configuration

        return {
            "standard": capo_mediaconnect.types.standard_router_input_configuration.serialize_json(
                value["Standard"]
            )
        }
    elif "MediaLiveChannel" in value:
        import capo_mediaconnect.types.media_live_channel_router_input_configuration

        return {
            "mediaLiveChannel": capo_mediaconnect.types.media_live_channel_router_input_configuration.serialize_json(
                value["MediaLiveChannel"]
            )
        }
    elif "Failover" in value:
        import capo_mediaconnect.types.failover_router_input_configuration

        return {
            "failover": capo_mediaconnect.types.failover_router_input_configuration.serialize_json(
                value["Failover"]
            )
        }
    elif "MediaConnectFlow" in value:
        import capo_mediaconnect.types.media_connect_flow_router_input_configuration

        return {
            "mediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_input_configuration.serialize_json(
                value["MediaConnectFlow"]
            )
        }
    elif "Merge" in value:
        import capo_mediaconnect.types.merge_router_input_configuration

        return {
            "merge": capo_mediaconnect.types.merge_router_input_configuration.serialize_json(
                value["Merge"]
            )
        }
    else:
        raise SerializationError("RouterInputConfiguration: no variant present")


def deserialize_json(data: dict) -> RouterInputConfiguration:
    if data.get("standard") is not None:
        import capo_mediaconnect.types.standard_router_input_configuration

        return {
            "Standard": capo_mediaconnect.types.standard_router_input_configuration.deserialize_json(
                data["standard"]
            )
        }
    elif data.get("mediaLiveChannel") is not None:
        import capo_mediaconnect.types.media_live_channel_router_input_configuration

        return {
            "MediaLiveChannel": capo_mediaconnect.types.media_live_channel_router_input_configuration.deserialize_json(
                data["mediaLiveChannel"]
            )
        }
    elif data.get("failover") is not None:
        import capo_mediaconnect.types.failover_router_input_configuration

        return {
            "Failover": capo_mediaconnect.types.failover_router_input_configuration.deserialize_json(
                data["failover"]
            )
        }
    elif data.get("mediaConnectFlow") is not None:
        import capo_mediaconnect.types.media_connect_flow_router_input_configuration

        return {
            "MediaConnectFlow": capo_mediaconnect.types.media_connect_flow_router_input_configuration.deserialize_json(
                data["mediaConnectFlow"]
            )
        }
    elif data.get("merge") is not None:
        import capo_mediaconnect.types.merge_router_input_configuration

        return {
            "Merge": capo_mediaconnect.types.merge_router_input_configuration.deserialize_json(
                data["merge"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RouterInputConfiguration: no recognized variant key"
        )
