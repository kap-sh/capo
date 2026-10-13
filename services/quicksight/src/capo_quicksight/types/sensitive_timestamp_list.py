"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveTimestampList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_timestamp

SensitiveTimestampList: TypeAlias = list[
    "capo_quicksight.types.sensitive_timestamp.SensitiveTimestamp"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveTimestampList) -> list:
    import capo_quicksight.types.sensitive_timestamp

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sensitive_timestamp.serialize_json(item))
    return out


def deserialize_json(data: list) -> SensitiveTimestampList:
    import capo_quicksight.types.sensitive_timestamp

    out: SensitiveTimestampList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.sensitive_timestamp.deserialize_json(item))
    return out


def redact_sensitive(value: SensitiveTimestampList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
