"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ParticipantPhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.e164_phone_number

ParticipantPhoneNumberList: TypeAlias = list[
    "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantPhoneNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParticipantPhoneNumberList:
    return [item for item in data if item is not None]


def redact_sensitive(value: ParticipantPhoneNumberList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
