"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpsertEntityInfo``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.vocabulary_entity_info


class _UpsertEntityInfo_vocabulary(TypedDict, closed=True):
    vocabulary: (
        "capo_bedrock_data_automation.types.vocabulary_entity_info.VocabularyEntityInfo"
    )


UpsertEntityInfo: TypeAlias = _UpsertEntityInfo_vocabulary


# --- restJson1 ser/de ---
def serialize_json(value: UpsertEntityInfo) -> dict:
    if "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity_info

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity_info.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError("UpsertEntityInfo: no variant present")


def deserialize_json(data: dict) -> UpsertEntityInfo:
    if data.get("vocabulary") is not None:
        import capo_bedrock_data_automation.types.vocabulary_entity_info

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity_info.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        raise DeserializationError("UpsertEntityInfo: no recognized variant key")


def redact_sensitive(value: UpsertEntityInfo) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity_info

        out["vocabulary"] = (
            capo_bedrock_data_automation.types.vocabulary_entity_info.redact_sensitive(
                value["vocabulary"]
            )
        )
    return out
