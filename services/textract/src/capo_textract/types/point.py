"""Generated from Smithy shape ``com.amazonaws.textract#Point``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.float


class Point(TypedDict, closed=True):
    x: "capo_textract.types.float.Float"
    """<p>The value of the X coordinate for a point on a <code>Polygon</code>.</p>"""
    y: "capo_textract.types.float.Float"
    """<p>The value of the Y coordinate for a point on a <code>Polygon</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Point) -> dict:
    out: dict = {}
    out["X"] = (
        "NaN"
        if value.get("x", 0) != value.get("x", 0)
        else "Infinity"
        if value.get("x", 0) == float("inf")
        else "-Infinity"
        if value.get("x", 0) == float("-inf")
        else value.get("x", 0)
    )
    out["Y"] = (
        "NaN"
        if value.get("y", 0) != value.get("y", 0)
        else "Infinity"
        if value.get("y", 0) == float("inf")
        else "-Infinity"
        if value.get("y", 0) == float("-inf")
        else value.get("y", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if data.get("X") is not None:
        out["x"] = float(data["X"])
    else:
        out["x"] = 0
    if data.get("Y") is not None:
        out["y"] = float(data["Y"])
    else:
        out["y"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Point) -> dict:
    out: dict = {}
    out["X"] = value.get("x", 0)
    out["Y"] = value.get("y", 0)
    return out


def deserialize_cbor(data: dict) -> Point:
    out: Point = {}  # type: ignore[typeddict-item]
    if data.get("X") is not None:
        out["x"] = float(data["X"])
    else:
        out["x"] = 0
    if data.get("Y") is not None:
        out["y"] = float(data["Y"])
    else:
        out["y"] = 0
    return out
