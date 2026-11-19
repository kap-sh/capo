"""Generated from Smithy shape ``com.amazonaws.textract#Geometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.angle
    import capo_textract.types.bounding_box
    import capo_textract.types.polygon


class Geometry(TypedDict, closed=True):
    bounding_box: NotRequired["capo_textract.types.bounding_box.BoundingBox"]
    """<p>An axis-aligned coarse representation of the location of the recognized item on the document page.</p>"""
    polygon: NotRequired["capo_textract.types.polygon.Polygon"]
    """<p>Within the bounding box, a fine-grained polygon around the recognized item.</p>"""
    rotation_angle: NotRequired["capo_textract.types.angle.Angle"]
    """<p>Provides a numerical value corresponding to the rotation of the WORD block. Possible values are 0, 90, 180, and 270.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_textract.types.bounding_box

        out["BoundingBox"] = capo_textract.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_textract.types.polygon

        out["Polygon"] = capo_textract.types.polygon.serialize_aws_json_1_1(
            value["polygon"]
        )
    if "rotation_angle" in value:
        out["RotationAngle"] = (
            "NaN"
            if value["rotation_angle"] != value["rotation_angle"]
            else "Infinity"
            if value["rotation_angle"] == float("inf")
            else "-Infinity"
            if value["rotation_angle"] == float("-inf")
            else value["rotation_angle"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_textract.types.bounding_box

        out["bounding_box"] = capo_textract.types.bounding_box.deserialize_aws_json_1_1(
            data["BoundingBox"]
        )
    if data.get("Polygon") is not None:
        import capo_textract.types.polygon

        out["polygon"] = capo_textract.types.polygon.deserialize_aws_json_1_1(
            data["Polygon"]
        )
    if data.get("RotationAngle") is not None:
        out["rotation_angle"] = float(data["RotationAngle"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_textract.types.bounding_box

        out["BoundingBox"] = capo_textract.types.bounding_box.serialize_cbor(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_textract.types.polygon

        out["Polygon"] = capo_textract.types.polygon.serialize_cbor(value["polygon"])
    if "rotation_angle" in value:
        out["RotationAngle"] = value["rotation_angle"]
    return out


def deserialize_cbor(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_textract.types.bounding_box

        out["bounding_box"] = capo_textract.types.bounding_box.deserialize_cbor(
            data["BoundingBox"]
        )
    if data.get("Polygon") is not None:
        import capo_textract.types.polygon

        out["polygon"] = capo_textract.types.polygon.deserialize_cbor(data["Polygon"])
    if data.get("RotationAngle") is not None:
        out["rotation_angle"] = float(data["RotationAngle"])
    return out
