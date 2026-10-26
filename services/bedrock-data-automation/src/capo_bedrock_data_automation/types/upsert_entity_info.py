"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpsertEntityInfo``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError
from capo_bedrock_data_automation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.vocabulary_entity_info


class _UpsertEntityInfo_vocabulary(TypedDict, closed=True):
    vocabulary: (
        "capo_bedrock_data_automation.types.vocabulary_entity_info.VocabularyEntityInfo"
    )


UpsertEntityInfo: TypeAlias = _UpsertEntityInfo_vocabulary | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: UpsertEntityInfo) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpsertEntityInfo: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "vocabulary" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
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
