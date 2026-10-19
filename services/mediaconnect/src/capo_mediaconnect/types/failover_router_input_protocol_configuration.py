"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FailoverRouterInputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rist_router_input_configuration
    import capo_mediaconnect.types.rtp_router_input_configuration
    import capo_mediaconnect.types.srt_caller_router_input_configuration
    import capo_mediaconnect.types.srt_listener_router_input_configuration


class _FailoverRouterInputProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "capo_mediaconnect.types.rist_router_input_configuration.RistRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_SrtListener(TypedDict, closed=True):
    SrtListener: "capo_mediaconnect.types.srt_listener_router_input_configuration.SrtListenerRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_SrtCaller(TypedDict, closed=True):
    SrtCaller: "capo_mediaconnect.types.srt_caller_router_input_configuration.SrtCallerRouterInputConfiguration"


class _FailoverRouterInputProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "capo_mediaconnect.types.rtp_router_input_configuration.RtpRouterInputConfiguration"


FailoverRouterInputProtocolConfiguration: TypeAlias = (
    _FailoverRouterInputProtocolConfiguration_Rist
    | _FailoverRouterInputProtocolConfiguration_SrtListener
    | _FailoverRouterInputProtocolConfiguration_SrtCaller
    | _FailoverRouterInputProtocolConfiguration_Rtp
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FailoverRouterInputProtocolConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FailoverRouterInputProtocolConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "Rist" in value:
        import capo_mediaconnect.types.rist_router_input_configuration

        return {
            "rist": capo_mediaconnect.types.rist_router_input_configuration.serialize_json(
                value["Rist"]
            )
        }
    elif "SrtListener" in value:
        import capo_mediaconnect.types.srt_listener_router_input_configuration

        return {
            "srtListener": capo_mediaconnect.types.srt_listener_router_input_configuration.serialize_json(
                value["SrtListener"]
            )
        }
    elif "SrtCaller" in value:
        import capo_mediaconnect.types.srt_caller_router_input_configuration

        return {
            "srtCaller": capo_mediaconnect.types.srt_caller_router_input_configuration.serialize_json(
                value["SrtCaller"]
            )
        }
    elif "Rtp" in value:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "rtp": capo_mediaconnect.types.rtp_router_input_configuration.serialize_json(
                value["Rtp"]
            )
        }
    else:
        raise SerializationError(
            "FailoverRouterInputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> FailoverRouterInputProtocolConfiguration:
    if data.get("rist") is not None:
        import capo_mediaconnect.types.rist_router_input_configuration

        return {
            "Rist": capo_mediaconnect.types.rist_router_input_configuration.deserialize_json(
                data["rist"]
            )
        }
    elif data.get("srtListener") is not None:
        import capo_mediaconnect.types.srt_listener_router_input_configuration

        return {
            "SrtListener": capo_mediaconnect.types.srt_listener_router_input_configuration.deserialize_json(
                data["srtListener"]
            )
        }
    elif data.get("srtCaller") is not None:
        import capo_mediaconnect.types.srt_caller_router_input_configuration

        return {
            "SrtCaller": capo_mediaconnect.types.srt_caller_router_input_configuration.deserialize_json(
                data["srtCaller"]
            )
        }
    elif data.get("rtp") is not None:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "Rtp": capo_mediaconnect.types.rtp_router_input_configuration.deserialize_json(
                data["rtp"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "FailoverRouterInputProtocolConfiguration: no recognized variant key"
        )
