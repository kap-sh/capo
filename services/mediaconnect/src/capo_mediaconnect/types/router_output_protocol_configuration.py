"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rist_router_output_configuration
    import capo_mediaconnect.types.rtmp_push_router_output_configuration
    import capo_mediaconnect.types.rtp_router_output_configuration
    import capo_mediaconnect.types.srt_caller_router_output_configuration
    import capo_mediaconnect.types.srt_listener_router_output_configuration


class _RouterOutputProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "capo_mediaconnect.types.rist_router_output_configuration.RistRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_SrtListener(TypedDict, closed=True):
    SrtListener: "capo_mediaconnect.types.srt_listener_router_output_configuration.SrtListenerRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_RtmpPush(TypedDict, closed=True):
    RtmpPush: "capo_mediaconnect.types.rtmp_push_router_output_configuration.RtmpPushRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_SrtCaller(TypedDict, closed=True):
    SrtCaller: "capo_mediaconnect.types.srt_caller_router_output_configuration.SrtCallerRouterOutputConfiguration"


class _RouterOutputProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "capo_mediaconnect.types.rtp_router_output_configuration.RtpRouterOutputConfiguration"


RouterOutputProtocolConfiguration: TypeAlias = (
    _RouterOutputProtocolConfiguration_Rist
    | _RouterOutputProtocolConfiguration_SrtListener
    | _RouterOutputProtocolConfiguration_RtmpPush
    | _RouterOutputProtocolConfiguration_SrtCaller
    | _RouterOutputProtocolConfiguration_Rtp
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputProtocolConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterOutputProtocolConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Rist" in value:
        import capo_mediaconnect.types.rist_router_output_configuration

        return {
            "rist": capo_mediaconnect.types.rist_router_output_configuration.serialize_json(
                value["Rist"]
            )
        }
    elif "SrtListener" in value:
        import capo_mediaconnect.types.srt_listener_router_output_configuration

        return {
            "srtListener": capo_mediaconnect.types.srt_listener_router_output_configuration.serialize_json(
                value["SrtListener"]
            )
        }
    elif "RtmpPush" in value:
        import capo_mediaconnect.types.rtmp_push_router_output_configuration

        return {
            "rtmpPush": capo_mediaconnect.types.rtmp_push_router_output_configuration.serialize_json(
                value["RtmpPush"]
            )
        }
    elif "SrtCaller" in value:
        import capo_mediaconnect.types.srt_caller_router_output_configuration

        return {
            "srtCaller": capo_mediaconnect.types.srt_caller_router_output_configuration.serialize_json(
                value["SrtCaller"]
            )
        }
    elif "Rtp" in value:
        import capo_mediaconnect.types.rtp_router_output_configuration

        return {
            "rtp": capo_mediaconnect.types.rtp_router_output_configuration.serialize_json(
                value["Rtp"]
            )
        }
    else:
        raise SerializationError(
            "RouterOutputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterOutputProtocolConfiguration:
    if data.get("rist") is not None:
        import capo_mediaconnect.types.rist_router_output_configuration

        return {
            "Rist": capo_mediaconnect.types.rist_router_output_configuration.deserialize_json(
                data["rist"]
            )
        }
    elif data.get("srtListener") is not None:
        import capo_mediaconnect.types.srt_listener_router_output_configuration

        return {
            "SrtListener": capo_mediaconnect.types.srt_listener_router_output_configuration.deserialize_json(
                data["srtListener"]
            )
        }
    elif data.get("rtmpPush") is not None:
        import capo_mediaconnect.types.rtmp_push_router_output_configuration

        return {
            "RtmpPush": capo_mediaconnect.types.rtmp_push_router_output_configuration.deserialize_json(
                data["rtmpPush"]
            )
        }
    elif data.get("srtCaller") is not None:
        import capo_mediaconnect.types.srt_caller_router_output_configuration

        return {
            "SrtCaller": capo_mediaconnect.types.srt_caller_router_output_configuration.deserialize_json(
                data["srtCaller"]
            )
        }
    elif data.get("rtp") is not None:
        import capo_mediaconnect.types.rtp_router_output_configuration

        return {
            "Rtp": capo_mediaconnect.types.rtp_router_output_configuration.deserialize_json(
                data["rtp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RouterOutputProtocolConfiguration: no recognized variant key"
        )
