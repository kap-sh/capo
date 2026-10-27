"""Generated from Smithy shape ``com.amazonaws.deadline#ConsumedUsages``."""

from typing_extensions import TypedDict


class ConsumedUsages(TypedDict, closed=True):
    approximate_dollar_usage: "float"
    """The amount of the budget consumed."""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumedUsages) -> dict:
    out: dict = {}
    out["approximateDollarUsage"] = (
        "NaN"
        if value["approximate_dollar_usage"] != value["approximate_dollar_usage"]
        else "Infinity"
        if value["approximate_dollar_usage"] == float("inf")
        else "-Infinity"
        if value["approximate_dollar_usage"] == float("-inf")
        else value["approximate_dollar_usage"]
    )
    return out


def deserialize_json(data: dict) -> ConsumedUsages:
    out: ConsumedUsages = {}  # type: ignore[typeddict-item]
    if data.get("approximateDollarUsage") is not None:
        out["approximate_dollar_usage"] = float(data["approximateDollarUsage"])
    else:
        out["approximate_dollar_usage"] = 0.0
    return out
