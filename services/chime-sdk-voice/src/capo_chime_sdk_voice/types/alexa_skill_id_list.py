"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#AlexaSkillIdList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.alexa_skill_id

AlexaSkillIdList: TypeAlias = list[
    "capo_chime_sdk_voice.types.alexa_skill_id.AlexaSkillId"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlexaSkillIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AlexaSkillIdList:
    return [item for item in data if item is not None]


def redact_sensitive(value: AlexaSkillIdList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
