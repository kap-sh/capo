"""Generated from Smithy shape ``com.amazonaws.deadline#Stats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.double


class Stats(TypedDict, closed=True):
    min: NotRequired["capo_deadline.types.double.Double"]
    """The minimum of the usage statistics."""
    max: NotRequired["capo_deadline.types.double.Double"]
    """The maximum among the usage statistics."""
    avg: NotRequired["capo_deadline.types.double.Double"]
    """The average of the usage statistics."""
    sum: NotRequired["capo_deadline.types.double.Double"]
    """The sum of the usage statistics."""


# --- restJson1 ser/de ---
def serialize_json(value: Stats) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = (
            "NaN"
            if value["min"] != value["min"]
            else "Infinity"
            if value["min"] == float("inf")
            else "-Infinity"
            if value["min"] == float("-inf")
            else value["min"]
        )
    if "max" in value:
        out["max"] = (
            "NaN"
            if value["max"] != value["max"]
            else "Infinity"
            if value["max"] == float("inf")
            else "-Infinity"
            if value["max"] == float("-inf")
            else value["max"]
        )
    if "avg" in value:
        out["avg"] = (
            "NaN"
            if value["avg"] != value["avg"]
            else "Infinity"
            if value["avg"] == float("inf")
            else "-Infinity"
            if value["avg"] == float("-inf")
            else value["avg"]
        )
    if "sum" in value:
        out["sum"] = (
            "NaN"
            if value["sum"] != value["sum"]
            else "Infinity"
            if value["sum"] == float("inf")
            else "-Infinity"
            if value["sum"] == float("-inf")
            else value["sum"]
        )
    return out


def deserialize_json(data: dict) -> Stats:
    out: Stats = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = float(data["min"])
    if data.get("max") is not None:
        out["max"] = float(data["max"])
    if data.get("avg") is not None:
        out["avg"] = float(data["avg"])
    if data.get("sum") is not None:
        out["sum"] = float(data["sum"])
    return out
