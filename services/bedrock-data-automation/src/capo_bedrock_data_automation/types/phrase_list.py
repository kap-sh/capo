"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#PhraseList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.phrase

PhraseList: TypeAlias = list["capo_bedrock_data_automation.types.phrase.Phrase"]


# --- restJson1 ser/de ---
def serialize_json(value: PhraseList) -> list:
    import capo_bedrock_data_automation.types.phrase

    out: list = []
    for item in value:
        out.append(capo_bedrock_data_automation.types.phrase.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhraseList:
    import capo_bedrock_data_automation.types.phrase

    out: PhraseList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_data_automation.types.phrase.deserialize_json(item))
    return out


def redact_sensitive(value: PhraseList) -> list[Any]:
    import capo_bedrock_data_automation.types.phrase

    return [
        capo_bedrock_data_automation.types.phrase.redact_sensitive(item)
        for item in value
    ]
