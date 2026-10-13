"""Generated from Smithy shape ``com.amazonaws.qconnect#SuggestedMessagesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.non_empty_sensitive_string

SuggestedMessagesList: TypeAlias = list[
    "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuggestedMessagesList) -> list:
    return list(value)


def deserialize_json(data: list) -> SuggestedMessagesList:
    return [item for item in data if item is not None]


def redact_sensitive(value: SuggestedMessagesList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
