"""Generated from Smithy shape ``com.amazonaws.devopsagent#UsageMetric``."""

from typing_extensions import TypedDict


class UsageMetric(TypedDict, closed=True):
    limit: "int"
    """<p>Configured limit for this metric. A value of -1 indicates no limit is enforced.</p>"""
    usage: "float"
    """<p>Current usage for this metric</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsageMetric) -> dict:
    out: dict = {}
    out["limit"] = value["limit"]
    out["usage"] = (
        "NaN"
        if value["usage"] != value["usage"]
        else "Infinity"
        if value["usage"] == float("inf")
        else "-Infinity"
        if value["usage"] == float("-inf")
        else value["usage"]
    )
    return out


def deserialize_json(data: dict) -> UsageMetric:
    out: UsageMetric = {}  # type: ignore[typeddict-item]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    else:
        out["limit"] = 0
    if data.get("usage") is not None:
        out["usage"] = float(data["usage"])
    else:
        out["usage"] = 0.0
    return out
