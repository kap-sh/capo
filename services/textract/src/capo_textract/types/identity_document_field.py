"""Generated from Smithy shape ``com.amazonaws.textract#IdentityDocumentField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.analyze_id_detections


class IdentityDocumentField(TypedDict, closed=True):
    type: NotRequired["capo_textract.types.analyze_id_detections.AnalyzeIDDetections"]
    value_detection: NotRequired[
        "capo_textract.types.analyze_id_detections.AnalyzeIDDetections"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityDocumentField) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.analyze_id_detections

        out["Type"] = capo_textract.types.analyze_id_detections.serialize_aws_json_1_1(
            value["type"]
        )
    if "value_detection" in value:
        import capo_textract.types.analyze_id_detections

        out["ValueDetection"] = (
            capo_textract.types.analyze_id_detections.serialize_aws_json_1_1(
                value["value_detection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityDocumentField:
    out: IdentityDocumentField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.analyze_id_detections

        out["type"] = (
            capo_textract.types.analyze_id_detections.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("ValueDetection") is not None:
        import capo_textract.types.analyze_id_detections

        out["value_detection"] = (
            capo_textract.types.analyze_id_detections.deserialize_aws_json_1_1(
                data["ValueDetection"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdentityDocumentField) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_textract.types.analyze_id_detections

        out["Type"] = capo_textract.types.analyze_id_detections.serialize_cbor(
            value["type"]
        )
    if "value_detection" in value:
        import capo_textract.types.analyze_id_detections

        out["ValueDetection"] = (
            capo_textract.types.analyze_id_detections.serialize_cbor(
                value["value_detection"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> IdentityDocumentField:
    out: IdentityDocumentField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_textract.types.analyze_id_detections

        out["type"] = capo_textract.types.analyze_id_detections.deserialize_cbor(
            data["Type"]
        )
    if data.get("ValueDetection") is not None:
        import capo_textract.types.analyze_id_detections

        out["value_detection"] = (
            capo_textract.types.analyze_id_detections.deserialize_cbor(
                data["ValueDetection"]
            )
        )
    return out
