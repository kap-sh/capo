"""Generated from Smithy shape ``com.amazonaws.quicksight#DateTimeDefaultValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_timestamp

DateTimeDefaultValueList: TypeAlias = list[
    "capo_quicksight.types.sensitive_timestamp.SensitiveTimestamp"
]


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeDefaultValueList) -> list:
    import capo_quicksight.types.sensitive_timestamp

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sensitive_timestamp.serialize_json(item))
    return out


def deserialize_json(data: list) -> DateTimeDefaultValueList:
    import capo_quicksight.types.sensitive_timestamp

    out: DateTimeDefaultValueList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.sensitive_timestamp.deserialize_json(item))
    return out


def redact_sensitive(value: DateTimeDefaultValueList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
