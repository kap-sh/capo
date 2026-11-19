"""Generated from Smithy shape ``com.amazonaws.mediaconnect#FabricSwitchingConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.immediate_fabric_switching_configuration
    import capo_mediaconnect.types.key_frame_fabric_switching_configuration


class FabricSwitchingConfigurationImmediateMember(TypedDict, closed=True):
    Immediate: "capo_mediaconnect.types.immediate_fabric_switching_configuration.ImmediateFabricSwitchingConfiguration"


class FabricSwitchingConfigurationKeyFrameMember(TypedDict, closed=True):
    KeyFrame: "capo_mediaconnect.types.key_frame_fabric_switching_configuration.KeyFrameFabricSwitchingConfiguration"


FabricSwitchingConfiguration: TypeAlias = (
    FabricSwitchingConfigurationImmediateMember
    | FabricSwitchingConfigurationKeyFrameMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FabricSwitchingConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FabricSwitchingConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Immediate" in value:
        import capo_mediaconnect.types.immediate_fabric_switching_configuration

        return {
            "immediate": capo_mediaconnect.types.immediate_fabric_switching_configuration.serialize_json(
                value["Immediate"]
            )
        }
    elif "KeyFrame" in value:
        import capo_mediaconnect.types.key_frame_fabric_switching_configuration

        return {
            "keyFrame": capo_mediaconnect.types.key_frame_fabric_switching_configuration.serialize_json(
                value["KeyFrame"]
            )
        }
    else:
        raise SerializationError("FabricSwitchingConfiguration: no variant present")


def deserialize_json(data: dict) -> FabricSwitchingConfiguration:
    if data.get("immediate") is not None:
        import capo_mediaconnect.types.immediate_fabric_switching_configuration

        return {
            "Immediate": capo_mediaconnect.types.immediate_fabric_switching_configuration.deserialize_json(
                data["immediate"]
            )
        }
    elif data.get("keyFrame") is not None:
        import capo_mediaconnect.types.key_frame_fabric_switching_configuration

        return {
            "KeyFrame": capo_mediaconnect.types.key_frame_fabric_switching_configuration.deserialize_json(
                data["keyFrame"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "FabricSwitchingConfiguration: no recognized variant key"
        )
