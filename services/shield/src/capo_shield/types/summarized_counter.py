"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedCounter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.double
    import capo_shield.types.integer
    import capo_shield.types.string


class SummarizedCounter(TypedDict, closed=True):
    name: NotRequired["capo_shield.types.string.String"]
    """<p>The counter name.</p>"""
    max: "capo_shield.types.double.Double"
    """<p>The maximum value of the counter for a specified time period.</p>"""
    average: "capo_shield.types.double.Double"
    """<p>The average value of the counter for a specified time period.</p>"""
    sum: "capo_shield.types.double.Double"
    """<p>The total of counter values for a specified time period.</p>"""
    n: "capo_shield.types.integer.Integer"
    """<p>The number of counters for a specified time period.</p>"""
    unit: NotRequired["capo_shield.types.string.String"]
    """<p>The unit of the counters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedCounter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Max"] = (
        "NaN"
        if value.get("max", 0) != value.get("max", 0)
        else "Infinity"
        if value.get("max", 0) == float("inf")
        else "-Infinity"
        if value.get("max", 0) == float("-inf")
        else value.get("max", 0)
    )
    out["Average"] = (
        "NaN"
        if value.get("average", 0) != value.get("average", 0)
        else "Infinity"
        if value.get("average", 0) == float("inf")
        else "-Infinity"
        if value.get("average", 0) == float("-inf")
        else value.get("average", 0)
    )
    out["Sum"] = (
        "NaN"
        if value.get("sum", 0) != value.get("sum", 0)
        else "Infinity"
        if value.get("sum", 0) == float("inf")
        else "-Infinity"
        if value.get("sum", 0) == float("-inf")
        else value.get("sum", 0)
    )
    out["N"] = value.get("n", 0)
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SummarizedCounter:
    out: SummarizedCounter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    else:
        out["max"] = 0
    if data.get("Average") is not None:
        out["average"] = float(data["Average"])
    else:
        out["average"] = 0
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    else:
        out["sum"] = 0
    if data.get("N") is not None:
        out["n"] = data["N"]
    else:
        out["n"] = 0
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummarizedCounter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    out["Max"] = value.get("max", 0)
    out["Average"] = value.get("average", 0)
    out["Sum"] = value.get("sum", 0)
    out["N"] = value.get("n", 0)
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_cbor(data: dict) -> SummarizedCounter:
    out: SummarizedCounter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    else:
        out["max"] = 0
    if data.get("Average") is not None:
        out["average"] = float(data["Average"])
    else:
        out["average"] = 0
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    else:
        out["sum"] = 0
    if data.get("N") is not None:
        out["n"] = data["N"]
    else:
        out["n"] = 0
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out
