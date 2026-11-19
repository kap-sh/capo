"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GenerationSelection``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.generation_filters
    import capo_bedrock_agentcore.types.generation_identifiers


class GenerationSelectionFiltersMember(TypedDict, closed=True):
    filters: "capo_bedrock_agentcore.types.generation_filters.GenerationFilters"


class GenerationSelectionIdentifiersMember(TypedDict, closed=True):
    identifiers: (
        "capo_bedrock_agentcore.types.generation_identifiers.GenerationIdentifiers"
    )


GenerationSelection: TypeAlias = (
    GenerationSelectionFiltersMember
    | GenerationSelectionIdentifiersMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GenerationSelection) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GenerationSelection: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "filters" in value:
        import capo_bedrock_agentcore.types.generation_filters

        return {
            "filters": capo_bedrock_agentcore.types.generation_filters.serialize_json(
                value["filters"]
            )
        }
    elif "identifiers" in value:
        import capo_bedrock_agentcore.types.generation_identifiers

        return {
            "identifiers": capo_bedrock_agentcore.types.generation_identifiers.serialize_json(
                value["identifiers"]
            )
        }
    else:
        raise SerializationError("GenerationSelection: no variant present")


def deserialize_json(data: dict) -> GenerationSelection:
    if data.get("filters") is not None:
        import capo_bedrock_agentcore.types.generation_filters

        return {
            "filters": capo_bedrock_agentcore.types.generation_filters.deserialize_json(
                data["filters"]
            )
        }
    elif data.get("identifiers") is not None:
        import capo_bedrock_agentcore.types.generation_identifiers

        return {
            "identifiers": capo_bedrock_agentcore.types.generation_identifiers.deserialize_json(
                data["identifiers"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GenerationSelection: no recognized variant key")
