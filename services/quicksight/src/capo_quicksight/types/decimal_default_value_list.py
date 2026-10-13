"""Generated from Smithy shape ``com.amazonaws.quicksight#DecimalDefaultValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double_object

DecimalDefaultValueList: TypeAlias = list[
    "capo_quicksight.types.sensitive_double_object.SensitiveDoubleObject"
]


# --- restJson1 ser/de ---
def serialize_json(value: DecimalDefaultValueList) -> list:
    return [
        (
            "NaN"
            if item != item
            else "Infinity"
            if item == float("inf")
            else "-Infinity"
            if item == float("-inf")
            else item
        )
        for item in value
    ]


def deserialize_json(data: list) -> DecimalDefaultValueList:
    return [float(item) for item in data if item is not None]


def redact_sensitive(value: DecimalDefaultValueList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
