"""Generated from Smithy shape ``com.amazonaws.textract#LendingDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.lending_field_list
    import capo_textract.types.signature_detection_list


class LendingDocument(TypedDict, closed=True):
    lending_fields: NotRequired[
        "capo_textract.types.lending_field_list.LendingFieldList"
    ]
    """<p>An array of LendingField objects.</p>"""
    signature_detections: NotRequired[
        "capo_textract.types.signature_detection_list.SignatureDetectionList"
    ]
    """<p>A list of signatures detected in a lending document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingDocument) -> dict:
    out: dict = {}
    if "lending_fields" in value:
        import capo_textract.types.lending_field_list

        out["LendingFields"] = (
            capo_textract.types.lending_field_list.serialize_aws_json_1_1(
                value["lending_fields"]
            )
        )
    if "signature_detections" in value:
        import capo_textract.types.signature_detection_list

        out["SignatureDetections"] = (
            capo_textract.types.signature_detection_list.serialize_aws_json_1_1(
                value["signature_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingDocument:
    out: LendingDocument = {}  # type: ignore[typeddict-item]
    if data.get("LendingFields") is not None:
        import capo_textract.types.lending_field_list

        out["lending_fields"] = (
            capo_textract.types.lending_field_list.deserialize_aws_json_1_1(
                data["LendingFields"]
            )
        )
    if data.get("SignatureDetections") is not None:
        import capo_textract.types.signature_detection_list

        out["signature_detections"] = (
            capo_textract.types.signature_detection_list.deserialize_aws_json_1_1(
                data["SignatureDetections"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingDocument) -> dict:
    out: dict = {}
    if "lending_fields" in value:
        import capo_textract.types.lending_field_list

        out["LendingFields"] = capo_textract.types.lending_field_list.serialize_cbor(
            value["lending_fields"]
        )
    if "signature_detections" in value:
        import capo_textract.types.signature_detection_list

        out["SignatureDetections"] = (
            capo_textract.types.signature_detection_list.serialize_cbor(
                value["signature_detections"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LendingDocument:
    out: LendingDocument = {}  # type: ignore[typeddict-item]
    if data.get("LendingFields") is not None:
        import capo_textract.types.lending_field_list

        out["lending_fields"] = capo_textract.types.lending_field_list.deserialize_cbor(
            data["LendingFields"]
        )
    if data.get("SignatureDetections") is not None:
        import capo_textract.types.signature_detection_list

        out["signature_detections"] = (
            capo_textract.types.signature_detection_list.deserialize_cbor(
                data["SignatureDetections"]
            )
        )
    return out
