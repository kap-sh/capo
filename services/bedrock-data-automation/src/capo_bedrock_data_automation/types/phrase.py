"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Phrase``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.phrase_display_as_text
    import capo_bedrock_data_automation.types.phrase_text


class Phrase(TypedDict, closed=True):
    text: "capo_bedrock_data_automation.types.phrase_text.PhraseText"
    display_as_text: NotRequired[
        "capo_bedrock_data_automation.types.phrase_display_as_text.PhraseDisplayAsText"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Phrase) -> dict:
    out: dict = {}
    out["text"] = value["text"]
    if "display_as_text" in value:
        out["displayAsText"] = value["display_as_text"]
    return out


def deserialize_json(data: dict) -> Phrase:
    out: Phrase = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        raise DeserializationError("Phrase.text required")
    if data.get("displayAsText") is not None:
        out["display_as_text"] = data["displayAsText"]
    return out


def redact_sensitive(value: Phrase) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "display_as_text" in value:
        out["display_as_text"] = "*** Sensitive Data Redacted ***"
    return out
