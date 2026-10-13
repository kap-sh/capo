"""Generated from Smithy shape ``com.amazonaws.quicksight#SensitiveDoubleList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sensitive_double

SensitiveDoubleList: TypeAlias = list[
    "capo_quicksight.types.sensitive_double.SensitiveDouble"
]


# --- restJson1 ser/de ---
def serialize_json(value: SensitiveDoubleList) -> list:
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


def deserialize_json(data: list) -> SensitiveDoubleList:
    return [float(item) for item in data if item is not None]


def redact_sensitive(value: SensitiveDoubleList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
