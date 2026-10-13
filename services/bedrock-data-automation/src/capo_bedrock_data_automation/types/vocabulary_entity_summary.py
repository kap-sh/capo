"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#VocabularyEntitySummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.entity_description
    import capo_bedrock_data_automation.types.entity_id
    import capo_bedrock_data_automation.types.language


class VocabularyEntitySummary(TypedDict, closed=True):
    entity_id: NotRequired["capo_bedrock_data_automation.types.entity_id.EntityId"]
    description: NotRequired[
        "capo_bedrock_data_automation.types.entity_description.EntityDescription"
    ]
    language: NotRequired["capo_bedrock_data_automation.types.language.Language"]
    num_of_phrases: NotRequired["int"]
    """num of phrases in the entity"""
    last_modified_time: NotRequired[
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: VocabularyEntitySummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "language" in value:
        import capo_bedrock_data_automation.types.language

        out["language"] = capo_bedrock_data_automation.types.language.serialize_json(
            value["language"]
        )
    if "num_of_phrases" in value:
        out["numOfPhrases"] = value["num_of_phrases"]
    if "last_modified_time" in value:
        import capo_bedrock_data_automation.types.date_timestamp

        out["lastModifiedTime"] = (
            capo_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> VocabularyEntitySummary:
    out: VocabularyEntitySummary = {}  # type: ignore[typeddict-item]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("language") is not None:
        import capo_bedrock_data_automation.types.language

        out["language"] = capo_bedrock_data_automation.types.language.deserialize_json(
            data["language"]
        )
    if data.get("numOfPhrases") is not None:
        out["num_of_phrases"] = data["numOfPhrases"]
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out


def redact_sensitive(value: VocabularyEntitySummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
