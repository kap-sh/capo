"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ComputeConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.ec2_configuration


class _ComputeConfiguration_ec2Configuration(TypedDict, closed=True):
    ec2Configuration: (
        "capo_bedrock_agentcore_control.types.ec2_configuration.Ec2Configuration"
    )


ComputeConfiguration: TypeAlias = (
    _ComputeConfiguration_ec2Configuration | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ComputeConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ComputeConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "ec2Configuration" in value:
        import capo_bedrock_agentcore_control.types.ec2_configuration

        return {
            "ec2Configuration": capo_bedrock_agentcore_control.types.ec2_configuration.serialize_json(
                value["ec2Configuration"]
            )
        }
    else:
        raise SerializationError("ComputeConfiguration: no variant present")


def deserialize_json(data: dict) -> ComputeConfiguration:
    if data.get("ec2Configuration") is not None:
        import capo_bedrock_agentcore_control.types.ec2_configuration

        return {
            "ec2Configuration": capo_bedrock_agentcore_control.types.ec2_configuration.deserialize_json(
                data["ec2Configuration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ComputeConfiguration: no recognized variant key")
