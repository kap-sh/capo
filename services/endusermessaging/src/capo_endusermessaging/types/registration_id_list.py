"""Generated from Smithy shape ``com.amazonaws.endusermessaging#RegistrationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_endusermessaging.types.registration_id_or_arn

RegistrationIdList: TypeAlias = list[
    "capo_endusermessaging.types.registration_id_or_arn.RegistrationIdOrArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistrationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegistrationIdList:
    return [item for item in data if item is not None]
