"""Generated from Smithy shape ``com.amazonaws.endusermessaging#RegistrationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.registration_type

RegistrationTypeList: TypeAlias = list[
    "capo_endusermessaging.types.registration_type.RegistrationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegistrationTypeList:
    return [item for item in data if item is not None]
