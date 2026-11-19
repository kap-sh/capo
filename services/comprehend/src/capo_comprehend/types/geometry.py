"""Generated from Smithy shape ``com.amazonaws.comprehend#Geometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.bounding_box
    import capo_comprehend.types.polygon


class Geometry(TypedDict, closed=True):
    bounding_box: NotRequired["capo_comprehend.types.bounding_box.BoundingBox"]
    """<p>An axis-aligned coarse representation of the location of the recognized item on the document page.</p>"""
    polygon: NotRequired["capo_comprehend.types.polygon.Polygon"]
    """<p>Within the bounding box, a fine-grained polygon around the recognized item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_comprehend.types.bounding_box

        out["BoundingBox"] = capo_comprehend.types.bounding_box.serialize_aws_json_1_1(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_comprehend.types.polygon

        out["Polygon"] = capo_comprehend.types.polygon.serialize_aws_json_1_1(
            value["polygon"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_comprehend.types.bounding_box

        out["bounding_box"] = (
            capo_comprehend.types.bounding_box.deserialize_aws_json_1_1(
                data["BoundingBox"]
            )
        )
    if data.get("Polygon") is not None:
        import capo_comprehend.types.polygon

        out["polygon"] = capo_comprehend.types.polygon.deserialize_aws_json_1_1(
            data["Polygon"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Geometry) -> dict:
    out: dict = {}
    if "bounding_box" in value:
        import capo_comprehend.types.bounding_box

        out["BoundingBox"] = capo_comprehend.types.bounding_box.serialize_cbor(
            value["bounding_box"]
        )
    if "polygon" in value:
        import capo_comprehend.types.polygon

        out["Polygon"] = capo_comprehend.types.polygon.serialize_cbor(value["polygon"])
    return out


def deserialize_cbor(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if data.get("BoundingBox") is not None:
        import capo_comprehend.types.bounding_box

        out["bounding_box"] = capo_comprehend.types.bounding_box.deserialize_cbor(
            data["BoundingBox"]
        )
    if data.get("Polygon") is not None:
        import capo_comprehend.types.polygon

        out["polygon"] = capo_comprehend.types.polygon.deserialize_cbor(data["Polygon"])
    return out
