"""Generated from Smithy shape ``com.amazonaws.mediaconnect#StandardSourceEndpointProtocolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.rist_standard_source_endpoint_configuration
    import capo_mediaconnect.types.rtp_standard_source_endpoint_configuration
    import capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration
    import capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration


class _StandardSourceEndpointProtocolConfiguration_Rist(TypedDict, closed=True):
    Rist: "capo_mediaconnect.types.rist_standard_source_endpoint_configuration.RistStandardSourceEndpointConfiguration"


class _StandardSourceEndpointProtocolConfiguration_SrtListener(TypedDict, closed=True):
    SrtListener: "capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration.SrtListenerStandardSourceEndpointConfiguration"


class _StandardSourceEndpointProtocolConfiguration_SrtCaller(TypedDict, closed=True):
    SrtCaller: "capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration.SrtCallerStandardSourceEndpointConfiguration"


class _StandardSourceEndpointProtocolConfiguration_Rtp(TypedDict, closed=True):
    Rtp: "capo_mediaconnect.types.rtp_standard_source_endpoint_configuration.RtpStandardSourceEndpointConfiguration"


StandardSourceEndpointProtocolConfiguration: TypeAlias = (
    _StandardSourceEndpointProtocolConfiguration_Rist
    | _StandardSourceEndpointProtocolConfiguration_SrtListener
    | _StandardSourceEndpointProtocolConfiguration_SrtCaller
    | _StandardSourceEndpointProtocolConfiguration_Rtp
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: StandardSourceEndpointProtocolConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StandardSourceEndpointProtocolConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Rist" in value:
        import capo_mediaconnect.types.rist_standard_source_endpoint_configuration

        return {
            "rist": capo_mediaconnect.types.rist_standard_source_endpoint_configuration.serialize_json(
                value["Rist"]
            )
        }
    elif "SrtListener" in value:
        import capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration

        return {
            "srtListener": capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration.serialize_json(
                value["SrtListener"]
            )
        }
    elif "SrtCaller" in value:
        import capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration

        return {
            "srtCaller": capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration.serialize_json(
                value["SrtCaller"]
            )
        }
    elif "Rtp" in value:
        import capo_mediaconnect.types.rtp_standard_source_endpoint_configuration

        return {
            "rtp": capo_mediaconnect.types.rtp_standard_source_endpoint_configuration.serialize_json(
                value["Rtp"]
            )
        }
    else:
        raise SerializationError(
            "StandardSourceEndpointProtocolConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> StandardSourceEndpointProtocolConfiguration:
    if data.get("rist") is not None:
        import capo_mediaconnect.types.rist_standard_source_endpoint_configuration

        return {
            "Rist": capo_mediaconnect.types.rist_standard_source_endpoint_configuration.deserialize_json(
                data["rist"]
            )
        }
    elif data.get("srtListener") is not None:
        import capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration

        return {
            "SrtListener": capo_mediaconnect.types.srt_listener_standard_source_endpoint_configuration.deserialize_json(
                data["srtListener"]
            )
        }
    elif data.get("srtCaller") is not None:
        import capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration

        return {
            "SrtCaller": capo_mediaconnect.types.srt_caller_standard_source_endpoint_configuration.deserialize_json(
                data["srtCaller"]
            )
        }
    elif data.get("rtp") is not None:
        import capo_mediaconnect.types.rtp_standard_source_endpoint_configuration

        return {
            "Rtp": capo_mediaconnect.types.rtp_standard_source_endpoint_configuration.deserialize_json(
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
            "StandardSourceEndpointProtocolConfiguration: no recognized variant key"
        )
