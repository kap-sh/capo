"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordLeftExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.metadata_key


class _MemoryRecordLeftExpression_metadataKey(TypedDict, closed=True):
    metadataKey: "capo_bedrock_agentcore.types.metadata_key.MetadataKey"


MemoryRecordLeftExpression: TypeAlias = (
    _MemoryRecordLeftExpression_metadataKey | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordLeftExpression) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MemoryRecordLeftExpression: cannot serialize unknown variant {value.name!r}"
        )
    elif "metadataKey" in value:
        return {"metadataKey": value["metadataKey"]}
    else:
        raise SerializationError("MemoryRecordLeftExpression: no variant present")


def deserialize_json(data: dict) -> MemoryRecordLeftExpression:
    if data.get("metadataKey") is not None:
        return {"metadataKey": data["metadataKey"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "MemoryRecordLeftExpression: no recognized variant key"
        )
