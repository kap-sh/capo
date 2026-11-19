"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportGroupTrendStats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class ReportGroupTrendStats(TypedDict, closed=True):
    average: NotRequired["capo_codebuild.types.string.String"]
    """<p>Contains the average of all values analyzed.</p>"""
    max: NotRequired["capo_codebuild.types.string.String"]
    """<p>Contains the maximum value analyzed.</p>"""
    min: NotRequired["capo_codebuild.types.string.String"]
    """<p>Contains the minimum value analyzed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportGroupTrendStats) -> dict:
    out: dict = {}
    if "average" in value:
        out["average"] = value["average"]
    if "max" in value:
        out["max"] = value["max"]
    if "min" in value:
        out["min"] = value["min"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportGroupTrendStats:
    out: ReportGroupTrendStats = {}  # type: ignore[typeddict-item]
    if data.get("average") is not None:
        out["average"] = data["average"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    if data.get("min") is not None:
        out["min"] = data["min"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportGroupTrendStats) -> dict:
    out: dict = {}
    if "average" in value:
        out["average"] = value["average"]
    if "max" in value:
        out["max"] = value["max"]
    if "min" in value:
        out["min"] = value["min"]
    return out


def deserialize_cbor(data: dict) -> ReportGroupTrendStats:
    out: ReportGroupTrendStats = {}  # type: ignore[typeddict-item]
    if data.get("average") is not None:
        out["average"] = data["average"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    if data.get("min") is not None:
        out["min"] = data["min"]
    return out
