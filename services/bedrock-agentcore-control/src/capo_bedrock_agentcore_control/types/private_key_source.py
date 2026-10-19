"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PrivateKeySource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.kms_key_source_type


class _PrivateKeySource_kmsKeySource(TypedDict, closed=True):
    kmsKeySource: (
        "capo_bedrock_agentcore_control.types.kms_key_source_type.KmsKeySourceType"
    )


PrivateKeySource: TypeAlias = _PrivateKeySource_kmsKeySource | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeySource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrivateKeySource: cannot serialize unknown variant {value.name!r}"
        )
    elif "kmsKeySource" in value:
        import capo_bedrock_agentcore_control.types.kms_key_source_type

        return {
            "kmsKeySource": capo_bedrock_agentcore_control.types.kms_key_source_type.serialize_json(
                value["kmsKeySource"]
            )
        }
    else:
        raise SerializationError("PrivateKeySource: no variant present")


def deserialize_json(data: dict) -> PrivateKeySource:
    if data.get("kmsKeySource") is not None:
        import capo_bedrock_agentcore_control.types.kms_key_source_type

        return {
            "kmsKeySource": capo_bedrock_agentcore_control.types.kms_key_source_type.deserialize_json(
                data["kmsKeySource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PrivateKeySource: no recognized variant key")
