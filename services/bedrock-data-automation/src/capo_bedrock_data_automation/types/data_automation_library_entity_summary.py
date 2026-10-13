"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryEntitySummary``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.vocabulary_entity_summary


class _DataAutomationLibraryEntitySummary_vocabulary(TypedDict, closed=True):
    vocabulary: "capo_bedrock_data_automation.types.vocabulary_entity_summary.VocabularyEntitySummary"


DataAutomationLibraryEntitySummary: TypeAlias = (
    _DataAutomationLibraryEntitySummary_vocabulary
)


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryEntitySummary) -> dict:
    if "vocabulary" in value:
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
        raise DeserializationError(
            "DataAutomationLibraryEntitySummary: no recognized variant key"
        )


def redact_sensitive(value: DataAutomationLibraryEntitySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "vocabulary" in value:
        import capo_bedrock_data_automation.types.vocabulary_entity_summary

        out["vocabulary"] = (
            capo_bedrock_data_automation.types.vocabulary_entity_summary.redact_sensitive(
                value["vocabulary"]
            )
        )
    return out
