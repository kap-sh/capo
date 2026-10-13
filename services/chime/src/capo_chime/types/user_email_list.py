"""Generated from Smithy shape ``com.amazonaws.chime#UserEmailList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime.types.email_address

UserEmailList: TypeAlias = list["capo_chime.types.email_address.EmailAddress"]


# --- restJson1 ser/de ---
def serialize_json(value: UserEmailList) -> list:
    return list(value)


def deserialize_json(data: list) -> UserEmailList:
    return [item for item in data if item is not None]


def redact_sensitive(value: UserEmailList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
