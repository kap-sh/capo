"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LaunchTemplateSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.launch_parameters


class _LaunchTemplateSource_launchParameters(TypedDict, closed=True):
    launchParameters: (
        "capo_bedrock_agentcore_control.types.launch_parameters.LaunchParameters"
    )


LaunchTemplateSource: TypeAlias = (
    _LaunchTemplateSource_launchParameters | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LaunchTemplateSource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"LaunchTemplateSource: cannot serialize unknown variant {value.name!r}"
        )
    elif "launchParameters" in value:
        import capo_bedrock_agentcore_control.types.launch_parameters

        return {
            "launchParameters": capo_bedrock_agentcore_control.types.launch_parameters.serialize_json(
                value["launchParameters"]
            )
        }
    else:
        raise SerializationError("LaunchTemplateSource: no variant present")


def deserialize_json(data: dict) -> LaunchTemplateSource:
    if data.get("launchParameters") is not None:
        import capo_bedrock_agentcore_control.types.launch_parameters

        return {
            "launchParameters": capo_bedrock_agentcore_control.types.launch_parameters.deserialize_json(
                data["launchParameters"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("LaunchTemplateSource: no recognized variant key")
