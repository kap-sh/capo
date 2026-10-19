"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryEntitySummary``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError
from capo_bedrock_data_automation.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.vocabulary_entity_summary


class _DataAutomationLibraryEntitySummary_vocabulary(TypedDict, closed=True):
    vocabulary: "capo_bedrock_data_automation.types.vocabulary_entity_summary.VocabularyEntitySummary"


DataAutomationLibraryEntitySummary: TypeAlias = (
    _DataAutomationLibraryEntitySummary_vocabulary | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryEntitySummary) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DataAutomationLibraryEntitySummary: cannot serialize unknown variant {value.name!r}"
        )
    elif "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity_summary

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity_summary.serialize_json(
                value["vocabulary"]
            )
        }
    else:
        raise SerializationError(
            "DataAutomationLibraryEntitySummary: no variant present"
        )


def deserialize_json(data: dict) -> DataAutomationLibraryEntitySummary:
    if data.get("vocabulary") is not None:
        import capo_bedrock_data_automation.types.vocabulary_entity_summary

        return {
            "vocabulary": capo_bedrock_data_automation.types.vocabulary_entity_summary.deserialize_json(
                data["vocabulary"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "DataAutomationLibraryEntitySummary: no recognized variant key"
        )


def redact_sensitive(
    value: DataAutomationLibraryEntitySummary,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity_summary

        out["vocabulary"] = (
            capo_bedrock_data_automation.types.vocabulary_entity_summary.redact_sensitive(
                value["vocabulary"]
            )
        )
    return out
