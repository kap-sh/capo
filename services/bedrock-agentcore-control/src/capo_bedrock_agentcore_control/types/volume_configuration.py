"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VolumeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ebs_volume_configuration


class _VolumeConfiguration_ebsConfiguration(TypedDict, closed=True):
    ebsConfiguration: "capo_bedrock_agentcore_control.types.ebs_volume_configuration.EbsVolumeConfiguration"


VolumeConfiguration: TypeAlias = (
    _VolumeConfiguration_ebsConfiguration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VolumeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VolumeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ebsConfiguration" in value:
        import capo_bedrock_agentcore_control.types.ebs_volume_configuration

        return {
            "ebsConfiguration": capo_bedrock_agentcore_control.types.ebs_volume_configuration.serialize_json(
                value["ebsConfiguration"]
            )
        }
    else:
        raise SerializationError("VolumeConfiguration: no variant present")


def deserialize_json(data: dict) -> VolumeConfiguration:
    if data.get("ebsConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.ebs_volume_configuration

        return {
            "ebsConfiguration": capo_bedrock_agentcore_control.types.ebs_volume_configuration.deserialize_json(
                data["ebsConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("VolumeConfiguration: no recognized variant key")
