"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ControlStats``."""

from typing_extensions import TypedDict


class ControlStats(TypedDict, closed=True):
    variant_name: "str"
    """<p>The name of the control variant.</p>"""
    sample_size: "int"
    """<p>The number of sessions evaluated for the control variant.</p>"""
    mean: "float"
    """<p>The mean evaluation score for the control variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlStats) -> dict:
    out: dict = {}
    out["variantName"] = value["variant_name"]
    out["sampleSize"] = value["sample_size"]
    out["mean"] = (
        "NaN"
        if value["mean"] != value["mean"]
        else "Infinity"
        if value["mean"] == float("inf")
        else "-Infinity"
        if value["mean"] == float("-inf")
        else value["mean"]
    )
    return out


def deserialize_json(data: dict) -> ControlStats:
    out: ControlStats = {}  # type: ignore[typeddict-item]
    if data.get("variantName") is not None:
        out["variant_name"] = data["variantName"]
    else:
        out["variant_name"] = ""
    if data.get("sampleSize") is not None:
        out["sample_size"] = data["sampleSize"]
    else:
        out["sample_size"] = 0
    if data.get("mean") is not None:
        out["mean"] = float(data["mean"])
    else:
        out["mean"] = 0.0
    return out
