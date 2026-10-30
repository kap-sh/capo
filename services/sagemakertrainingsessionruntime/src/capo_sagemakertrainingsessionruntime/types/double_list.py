"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#DoubleList``."""

from typing import TypeAlias

DoubleList: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: DoubleList) -> list:
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


def deserialize_json(data: list) -> DoubleList:
    return [float(item) for item in data if item is not None]
