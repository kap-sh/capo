"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilterRight``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value


class AgenticRetrieveMemoryMetadataFilterRightMetadataValueMember(
    TypedDict, closed=True
):
    metadataValue: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.AgenticRetrieveMemoryMetadataValue"


AgenticRetrieveMemoryMetadataFilterRight: TypeAlias = (
    AgenticRetrieveMemoryMetadataFilterRightMetadataValueMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilterRight) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgenticRetrieveMemoryMetadataFilterRight: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "metadataValue" in value:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value

        return {
            "metadataValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.serialize_json(
                value["metadataValue"]
            )
        }
    else:
        raise SerializationError(
            "AgenticRetrieveMemoryMetadataFilterRight: no variant present"
        )


def deserialize_json(data: dict) -> AgenticRetrieveMemoryMetadataFilterRight:
    if data.get("metadataValue") is not None:
        import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value

        return {
            "metadataValue": capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_value.deserialize_json(
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
            "AgenticRetrieveMemoryMetadataFilterRight: no recognized variant key"
        )
