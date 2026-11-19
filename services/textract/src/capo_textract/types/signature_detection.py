"""Generated from Smithy shape ``com.amazonaws.textract#SignatureDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.geometry
    import capo_textract.types.percent


class SignatureDetection(TypedDict, closed=True):
    confidence: NotRequired["capo_textract.types.percent.Percent"]
    """<p>The confidence, from 0 to 100, in the predicted values for a detected signature.</p>"""
    geometry: NotRequired["capo_textract.types.geometry.Geometry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignatureDetection) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = (
            "NaN"
            if value["confidence"] != value["confidence"]
            else "Infinity"
            if value["confidence"] == float("inf")
            else "-Infinity"
            if value["confidence"] == float("-inf")
            else value["confidence"]
        )
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_aws_json_1_1(
            value["geometry"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SignatureDetection:
    out: SignatureDetection = {}  # type: ignore[typeddict-item]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Geometry") is not None:
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_aws_json_1_1(
            data["Geometry"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SignatureDetection) -> dict:
    out: dict = {}
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "geometry" in value:
        import capo_textract.types.geometry

        out["Geometry"] = capo_textract.types.geometry.serialize_cbor(value["geometry"])
    return out


def deserialize_cbor(data: dict) -> SignatureDetection:
    out: SignatureDetection = {}  # type: ignore[typeddict-item]
    if data.get("Confidence") is not None:
        out["confidence"] = float(data["Confidence"])
    if data.get("Geometry") is not None:
        import capo_textract.types.geometry

        out["geometry"] = capo_textract.types.geometry.deserialize_cbor(
            data["Geometry"]
        )
    return out
