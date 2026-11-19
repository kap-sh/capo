"""Generated from Smithy shape ``com.amazonaws.comprehend#BoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.float


class BoundingBox(TypedDict, closed=True):
    height: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The height of the bounding box as a ratio of the overall document page height.</p>"""
    left: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The left coordinate of the bounding box as a ratio of overall document page width.</p>"""
    top: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The top coordinate of the bounding box as a ratio of overall document page height.</p>"""
    width: NotRequired["capo_comprehend.types.float.Float"]
    """<p>The width of the bounding box as a ratio of the overall document page width.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    if "height" in value:
        out["Height"] = (
            "NaN"
            if value["height"] != value["height"]
            else "Infinity"
            if value["height"] == float("inf")
            else "-Infinity"
            if value["height"] == float("-inf")
            else value["height"]
        )
    if "left" in value:
        out["Left"] = (
            "NaN"
            if value["left"] != value["left"]
            else "Infinity"
            if value["left"] == float("inf")
            else "-Infinity"
            if value["left"] == float("-inf")
            else value["left"]
        )
    if "top" in value:
        out["Top"] = (
            "NaN"
            if value["top"] != value["top"]
            else "Infinity"
            if value["top"] == float("inf")
            else "-Infinity"
            if value["top"] == float("-inf")
            else value["top"]
        )
    if "width" in value:
        out["Width"] = (
            "NaN"
            if value["width"] != value["width"]
            else "Infinity"
            if value["width"] == float("inf")
            else "-Infinity"
            if value["width"] == float("-inf")
            else value["width"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    if data.get("Left") is not None:
        out["left"] = float(data["Left"])
    if data.get("Top") is not None:
        out["top"] = float(data["Top"])
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BoundingBox) -> dict:
    out: dict = {}
    if "height" in value:
        out["Height"] = value["height"]
    if "left" in value:
        out["Left"] = value["left"]
    if "top" in value:
        out["Top"] = value["top"]
    if "width" in value:
        out["Width"] = value["width"]
    return out


def deserialize_cbor(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    if data.get("Left") is not None:
        out["left"] = float(data["Left"])
    if data.get("Top") is not None:
        out["top"] = float(data["Top"])
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    return out
