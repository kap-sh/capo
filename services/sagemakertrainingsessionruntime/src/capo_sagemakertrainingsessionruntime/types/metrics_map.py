"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#MetricsMap``."""

from typing import TypeAlias

MetricsMap: TypeAlias = dict["str", "float"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MetricsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = (
            "NaN"
            if value != value
            else "Infinity"
            if value == float("inf")
            else "-Infinity"
            if value == float("-inf")
            else value
        )
    return out


def deserialize_json(data: dict) -> MetricsMap:
    out: MetricsMap = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = float(value)
    return out
