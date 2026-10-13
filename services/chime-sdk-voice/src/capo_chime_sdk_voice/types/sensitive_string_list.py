"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SensitiveStringList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.sensitive_string

SensitiveStringList: TypeAlias = list[
    "capo_chime_sdk_voice.types.sensitive_string.SensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> SensitiveStringList:
    return [item for item in data if item is not None]


def redact_sensitive(value: SensitiveStringList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
