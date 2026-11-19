"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationSelectionRecord``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_filters
    import capo_bedrock_agentcore.types.generation_identifier_counts


class GenerationSelectionRecordFiltersMember(TypedDict, closed=True):
    filters: "capo_bedrock_agentcore.types.generation_filters.GenerationFilters"


class GenerationSelectionRecordIdentifiersMember(TypedDict, closed=True):
    identifiers: "capo_bedrock_agentcore.types.generation_identifier_counts.GenerationIdentifierCounts"


GenerationSelectionRecord: TypeAlias = (
    GenerationSelectionRecordFiltersMember
    | GenerationSelectionRecordIdentifiersMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSelectionRecord) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GenerationSelectionRecord: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "filters" in value:
        import capo_bedrock_agentcore.types.generation_filters

        return {
            "filters": capo_bedrock_agentcore.types.generation_filters.serialize_json(
                value["filters"]
            )
        }
    elif "identifiers" in value:
        import capo_bedrock_agentcore.types.generation_identifier_counts

        return {
            "identifiers": capo_bedrock_agentcore.types.generation_identifier_counts.serialize_json(
                value["identifiers"]
            )
        }
    else:
        raise SerializationError("GenerationSelectionRecord: no variant present")


def deserialize_json(data: dict) -> GenerationSelectionRecord:
    if data.get("filters") is not None:
        import capo_bedrock_agentcore.types.generation_filters

        return {
            "filters": capo_bedrock_agentcore.types.generation_filters.deserialize_json(
                data["filters"]
            )
        }
    elif data.get("identifiers") is not None:
        import capo_bedrock_agentcore.types.generation_identifier_counts

        return {
            "identifiers": capo_bedrock_agentcore.types.generation_identifier_counts.deserialize_json(
                data["identifiers"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "GenerationSelectionRecord: no recognized variant key"
        )
