"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemoryMetadataFilterLeft``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_key


class AgenticRetrieveMemoryMetadataFilterLeftMetadataKeyMember(TypedDict, closed=True):
    metadataKey: "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_metadata_key.AgenticRetrieveMemoryMetadataKey"


AgenticRetrieveMemoryMetadataFilterLeft: TypeAlias = (
    AgenticRetrieveMemoryMetadataFilterLeftMetadataKeyMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemoryMetadataFilterLeft) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgenticRetrieveMemoryMetadataFilterLeft: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "metadataKey" in value:
        return {"metadataKey": value["metadataKey"]}
    else:
        raise SerializationError(
            "AgenticRetrieveMemoryMetadataFilterLeft: no variant present"
        )


def deserialize_json(data: dict) -> AgenticRetrieveMemoryMetadataFilterLeft:
    if data.get("metadataKey") is not None:
        return {"metadataKey": data["metadataKey"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AgenticRetrieveMemoryMetadataFilterLeft: no recognized variant key"
        )
