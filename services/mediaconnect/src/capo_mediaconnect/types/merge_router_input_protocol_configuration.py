"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rist_router_input_configuration
    import capo_mediaconnect.types.rtp_router_input_configuration
    import capo_mediaconnect.types.srt_caller_router_input_configuration
    import capo_mediaconnect.types.srt_listener_router_input_configuration


class MergeRouterInputProtocolConfigurationRtpMember(TypedDict, closed=True):
    Rtp: "capo_mediaconnect.types.rtp_router_input_configuration.RtpRouterInputConfiguration"


class MergeRouterInputProtocolConfigurationRistMember(TypedDict, closed=True):
    Rist: "capo_mediaconnect.types.rist_router_input_configuration.RistRouterInputConfiguration"


class MergeRouterInputProtocolConfigurationSrtListenerMember(TypedDict, closed=True):
    SrtListener: "capo_mediaconnect.types.srt_listener_router_input_configuration.SrtListenerRouterInputConfiguration"


class MergeRouterInputProtocolConfigurationSrtCallerMember(TypedDict, closed=True):
    SrtCaller: "capo_mediaconnect.types.srt_caller_router_input_configuration.SrtCallerRouterInputConfiguration"


MergeRouterInputProtocolConfiguration: TypeAlias = (
    MergeRouterInputProtocolConfigurationRtpMember
    | MergeRouterInputProtocolConfigurationRistMember
    | MergeRouterInputProtocolConfigurationSrtListenerMember
    | MergeRouterInputProtocolConfigurationSrtCallerMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputProtocolConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MergeRouterInputProtocolConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Rtp" in value:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "rtp": capo_mediaconnect.types.rtp_router_input_configuration.serialize_json(
                value["Rtp"]
            )
        }
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
    else:
        raise SerializationError(
            "MergeRouterInputProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MergeRouterInputProtocolConfiguration:
    if data.get("rtp") is not None:
        import capo_mediaconnect.types.rtp_router_input_configuration

        return {
            "Rtp": capo_mediaconnect.types.rtp_router_input_configuration.deserialize_json(
                data["rtp"]
            )
        }
    elif data.get("rist") is not None:
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
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MergeRouterInputProtocolConfiguration: no recognized variant key"
        )
