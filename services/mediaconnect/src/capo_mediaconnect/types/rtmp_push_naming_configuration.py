"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtmpPushNamingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.automatic_rtmp_push_naming_configuration
    import capo_mediaconnect.types.manual_rtmp_push_naming_configuration


class RtmpPushNamingConfigurationManualMember(TypedDict, closed=True):
    Manual: "capo_mediaconnect.types.manual_rtmp_push_naming_configuration.ManualRtmpPushNamingConfiguration"


class RtmpPushNamingConfigurationAutomaticMember(TypedDict, closed=True):
    Automatic: "capo_mediaconnect.types.automatic_rtmp_push_naming_configuration.AutomaticRtmpPushNamingConfiguration"


RtmpPushNamingConfiguration: TypeAlias = (
    RtmpPushNamingConfigurationManualMember
    | RtmpPushNamingConfigurationAutomaticMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RtmpPushNamingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RtmpPushNamingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Manual" in value:
        import capo_mediaconnect.types.manual_rtmp_push_naming_configuration

        return {
            "manual": capo_mediaconnect.types.manual_rtmp_push_naming_configuration.serialize_json(
                value["Manual"]
            )
        }
    elif "Automatic" in value:
        import capo_mediaconnect.types.automatic_rtmp_push_naming_configuration

        return {
            "automatic": capo_mediaconnect.types.automatic_rtmp_push_naming_configuration.serialize_json(
                value["Automatic"]
            )
        }
    else:
        raise SerializationError("RtmpPushNamingConfiguration: no variant present")


def deserialize_json(data: dict) -> RtmpPushNamingConfiguration:
    if data.get("manual") is not None:
        import capo_mediaconnect.types.manual_rtmp_push_naming_configuration

        return {
            "Manual": capo_mediaconnect.types.manual_rtmp_push_naming_configuration.deserialize_json(
                data["manual"]
            )
        }
    elif data.get("automatic") is not None:
        import capo_mediaconnect.types.automatic_rtmp_push_naming_configuration

        return {
            "Automatic": capo_mediaconnect.types.automatic_rtmp_push_naming_configuration.deserialize_json(
                data["automatic"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RtmpPushNamingConfiguration: no recognized variant key"
        )
