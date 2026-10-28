"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordRightExpression``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_metadata_value


class MemoryRecordRightExpressionMetadataValueMember(TypedDict, closed=True):
    metadataValue: "capo_bedrock_agentcore.types.memory_record_metadata_value.MemoryRecordMetadataValue"


MemoryRecordRightExpression: TypeAlias = (
    MemoryRecordRightExpressionMetadataValueMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordRightExpression) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemoryRecordRightExpression: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "metadataValue" in value:
        import capo_bedrock_agentcore.types.memory_record_metadata_value

        return {
            "metadataValue": capo_bedrock_agentcore.types.memory_record_metadata_value.serialize_json(
                value["metadataValue"]
            )
        }
    else:
        raise SerializationError("MemoryRecordRightExpression: no variant present")


def deserialize_json(data: dict) -> MemoryRecordRightExpression:
    if data.get("metadataValue") is not None:
        import capo_bedrock_agentcore.types.memory_record_metadata_value

        return {
            "metadataValue": capo_bedrock_agentcore.types.memory_record_metadata_value.deserialize_json(
                data["metadataValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MemoryRecordRightExpression: no recognized variant key"
        )
