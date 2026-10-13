"""Generated from Smithy shape ``com.amazonaws.chime#E164PhoneNumberList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.e164_phone_number

E164PhoneNumberList: TypeAlias = list[
    "capo_chime.types.e164_phone_number.E164PhoneNumber"
]


# --- restJson1 ser/de ---
def serialize_json(value: E164PhoneNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> E164PhoneNumberList:
    return [item for item in data if item is not None]


def redact_sensitive(value: E164PhoneNumberList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
