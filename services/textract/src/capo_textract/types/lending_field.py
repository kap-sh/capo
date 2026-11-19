"""Generated from Smithy shape ``com.amazonaws.textract#LendingField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.lending_detection
    import capo_textract.types.lending_detection_list
    import capo_textract.types.string


class LendingField(TypedDict, closed=True):
    type: NotRequired["capo_textract.types.string.String"]
    """<p>The type of the lending document.</p>"""
    key_detection: NotRequired["capo_textract.types.lending_detection.LendingDetection"]
    value_detections: NotRequired[
        "capo_textract.types.lending_detection_list.LendingDetectionList"
    ]
    """<p>An array of LendingDetection objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingField) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "key_detection" in value:
        import capo_textract.types.lending_detection

        out["KeyDetection"] = (
            capo_textract.types.lending_detection.serialize_aws_json_1_1(
                value["key_detection"]
            )
        )
    if "value_detections" in value:
        import capo_textract.types.lending_detection_list

        out["ValueDetections"] = (
            capo_textract.types.lending_detection_list.serialize_aws_json_1_1(
                value["value_detections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LendingField:
    out: LendingField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("KeyDetection") is not None:
        import capo_textract.types.lending_detection

        out["key_detection"] = (
            capo_textract.types.lending_detection.deserialize_aws_json_1_1(
                data["KeyDetection"]
            )
        )
    if data.get("ValueDetections") is not None:
        import capo_textract.types.lending_detection_list

        out["value_detections"] = (
            capo_textract.types.lending_detection_list.deserialize_aws_json_1_1(
                data["ValueDetections"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingField) -> dict:
    out: dict = {}
    if "type" in value:
        out["Type"] = value["type"]
    if "key_detection" in value:
        import capo_textract.types.lending_detection

        out["KeyDetection"] = capo_textract.types.lending_detection.serialize_cbor(
            value["key_detection"]
        )
    if "value_detections" in value:
        import capo_textract.types.lending_detection_list

        out["ValueDetections"] = (
            capo_textract.types.lending_detection_list.serialize_cbor(
                value["value_detections"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LendingField:
    out: LendingField = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("KeyDetection") is not None:
        import capo_textract.types.lending_detection

        out["key_detection"] = capo_textract.types.lending_detection.deserialize_cbor(
            data["KeyDetection"]
        )
    if data.get("ValueDetections") is not None:
        import capo_textract.types.lending_detection_list

        out["value_detections"] = (
            capo_textract.types.lending_detection_list.deserialize_cbor(
                data["ValueDetections"]
            )
        )
    return out
