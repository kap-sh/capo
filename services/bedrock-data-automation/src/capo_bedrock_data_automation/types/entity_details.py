"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EntityDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError
from capo_bedrock_data_automation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.vocabulary_entity


class EntityDetailsVocabularyMember(TypedDict, closed=True):
    vocabulary: "capo_bedrock_data_automation.types.vocabulary_entity.VocabularyEntity"


EntityDetails: TypeAlias = EntityDetailsVocabularyMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: EntityDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntityDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError("EntityDetails: no variant present")


def deserialize_json(data: dict) -> EntityDetails:
    if data.get("vocabulary") is not None:
        import capo_bedrock_data_automation.types.vocabulary_entity

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntityDetails: no recognized variant key")


def redact_sensitive(value: EntityDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity

        out["vocabulary"] = (
            capo_bedrock_data_automation.types.vocabulary_entity.redact_sensitive(
                value["vocabulary"]
            )
        )
    return out
