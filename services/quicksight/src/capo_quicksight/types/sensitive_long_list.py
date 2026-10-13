"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveLongList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_long

SensitiveLongList: TypeAlias = list[
    "capo_quicksight.types.sensitive_long.SensitiveLong"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveLongList) -> list:
    return list(value)


def deserialize_json(data: list) -> SensitiveLongList:
    return [item for item in data if item is not None]


def redact_sensitive(value: SensitiveLongList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
