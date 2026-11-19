"""Generated from Smithy shape ``com.amazonaws.textract#BoundingBox``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_textract.types.float


class BoundingBox(TypedDict, closed=True):
    width: "capo_textract.types.float.Float"
    """<p>The width of the bounding box as a ratio of the overall document page width.</p>"""
    height: "capo_textract.types.float.Float"
    """<p>The height of the bounding box as a ratio of the overall document page height.</p>"""
    left: "capo_textract.types.float.Float"
    """<p>The left coordinate of the bounding box as a ratio of overall document page width.</p>"""
    top: "capo_textract.types.float.Float"
    """<p>The top coordinate of the bounding box as a ratio of overall document page height.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BoundingBox) -> dict:
    out: dict = {}
    out["Width"] = (
        "NaN"
        if value.get("width", 0) != value.get("width", 0)
        else "Infinity"
        if value.get("width", 0) == float("inf")
        else "-Infinity"
        if value.get("width", 0) == float("-inf")
        else value.get("width", 0)
    )
    out["Height"] = (
        "NaN"
        if value.get("height", 0) != value.get("height", 0)
        else "Infinity"
        if value.get("height", 0) == float("inf")
        else "-Infinity"
        if value.get("height", 0) == float("-inf")
        else value.get("height", 0)
    )
    out["Left"] = (
        "NaN"
        if value.get("left", 0) != value.get("left", 0)
        else "Infinity"
        if value.get("left", 0) == float("inf")
        else "-Infinity"
        if value.get("left", 0) == float("-inf")
        else value.get("left", 0)
    )
    out["Top"] = (
        "NaN"
        if value.get("top", 0) != value.get("top", 0)
        else "Infinity"
        if value.get("top", 0) == float("inf")
        else "-Infinity"
        if value.get("top", 0) == float("-inf")
        else value.get("top", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    else:
        out["width"] = 0
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    else:
        out["height"] = 0
    if data.get("Left") is not None:
        out["left"] = float(data["Left"])
    else:
        out["left"] = 0
    if data.get("Top") is not None:
        out["top"] = float(data["Top"])
    else:
        out["top"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BoundingBox) -> dict:
    out: dict = {}
    out["Width"] = value.get("width", 0)
    out["Height"] = value.get("height", 0)
    out["Left"] = value.get("left", 0)
    out["Top"] = value.get("top", 0)
    return out


def deserialize_cbor(data: dict) -> BoundingBox:
    out: BoundingBox = {}  # type: ignore[typeddict-item]
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    else:
        out["width"] = 0
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    else:
        out["height"] = 0
    if data.get("Left") is not None:
        out["left"] = float(data["Left"])
    else:
        out["left"] = 0
    if data.get("Top") is not None:
        out["top"] = float(data["Top"])
    else:
        out["top"] = 0
    return out
