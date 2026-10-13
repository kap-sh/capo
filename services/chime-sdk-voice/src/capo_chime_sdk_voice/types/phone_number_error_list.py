"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PhoneNumberErrorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.phone_number_error

PhoneNumberErrorList: TypeAlias = list[
    "capo_chime_sdk_voice.types.phone_number_error.PhoneNumberError"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberErrorList) -> list:
    import capo_chime_sdk_voice.types.phone_number_error

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.phone_number_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhoneNumberErrorList:
    import capo_chime_sdk_voice.types.phone_number_error

    out: PhoneNumberErrorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_voice.types.phone_number_error.deserialize_json(item))
    return out


def redact_sensitive(value: PhoneNumberErrorList) -> list[Any]:
    import capo_chime_sdk_voice.types.phone_number_error

    return [
        capo_chime_sdk_voice.types.phone_number_error.redact_sensitive(item)
        for item in value
    ]
