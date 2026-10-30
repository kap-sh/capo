"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampleTokenUsage``."""

from typing_extensions import TypedDict


class SampleTokenUsage(TypedDict, closed=True):
    prefill: "int"
    """<p>The number of tokens in the input prompt (prefill phase).</p>"""
    decode: "int"
    """<p>The number of tokens generated (decode phase).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SampleTokenUsage) -> dict:
    out: dict = {}
    out["prefill"] = value["prefill"]
    out["decode"] = value["decode"]
    return out


def deserialize_json(data: dict) -> SampleTokenUsage:
    out: SampleTokenUsage = {}  # type: ignore[typeddict-item]
    if data.get("prefill") is not None:
        out["prefill"] = data["prefill"]
    else:
        out["prefill"] = 0
    if data.get("decode") is not None:
        out["decode"] = data["decode"]
    else:
        out["decode"] = 0
    return out
