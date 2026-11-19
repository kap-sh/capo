"""Generated from Smithy shape ``com.amazonaws.comprehend#Point``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float


class Point(TypedDict, closed=True):
    x: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The value of the X coordinate for a point on a polygon</p>"""
    y: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The value of the Y coordinate for a point on a polygon</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Point) -> dict:
    out: dict = {}
    if "x" in value:
        out["X"] = (
            "NaN"
            if value["x"] != value["x"]
            else "Infinity"
            if value["x"] == float("inf")
            else "-Infinity"
            if value["x"] == float("-inf")
            else value["x"]
        )
    if "y" in value:
        out["Y"] = (
            "NaN"
            if value["y"] != value["y"]
            else "Infinity"
            if value["y"] == float("inf")
            else "-Infinity"
            if value["y"] == float("-inf")
            else value["y"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if data.get("X") is not None:
        out["x"] = float(data["X"])
    if data.get("Y") is not None:
        out["y"] = float(data["Y"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Point) -> dict:
    out: dict = {}
    if "x" in value:
        out["X"] = value["x"]
    if "y" in value:
        out["Y"] = value["y"]
    return out


def deserialize_cbor(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if data.get("X") is not None:
        out["x"] = float(data["X"])
    if data.get("Y") is not None:
        out["y"] = float(data["Y"])
    return out
