"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#CountPercent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.float
    import capo_lookoutequipment.types.integer


class CountPercent(TypedDict, closed=True):
    count: "capo_lookoutequipment.types.integer.Integer"
    """<p> Indicates the count of occurences of the given statistic. </p>"""
    percentage: "capo_lookoutequipment.types.float.Float"
    """<p> Indicates the percentage of occurances of the given statistic. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CountPercent) -> dict:
    out: dict = {}
    out["Count"] = value["count"]
    out["Percentage"] = (
        "NaN"
        if value.get("percentage", 0) != value.get("percentage", 0)
        else "Infinity"
        if value.get("percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("percentage", 0) == float("-inf")
        else value.get("percentage", 0)
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CountPercent:
    out: CountPercent = {}  # type: ignore[typeddict-item]
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if data.get("Percentage") is not None:
        out["percentage"] = float(data["Percentage"])
    else:
        out["percentage"] = 0
    return out
