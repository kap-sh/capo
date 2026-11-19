"""Generated from Smithy shape ``com.amazonaws.textract#SignatureDetectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.signature_detection

SignatureDetectionList: TypeAlias = list[
    "capo_textract.types.signature_detection.SignatureDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignatureDetectionList) -> list:
    import capo_textract.types.signature_detection

    out: list = []
    for item in value:
        out.append(capo_textract.types.signature_detection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SignatureDetectionList:
    import capo_textract.types.signature_detection

    out: SignatureDetectionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.signature_detection.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SignatureDetectionList) -> list:
    import capo_textract.types.signature_detection

    out: list = []
    for item in value:
        out.append(capo_textract.types.signature_detection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SignatureDetectionList:
    import capo_textract.types.signature_detection

    out: SignatureDetectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.signature_detection.deserialize_cbor(item))
    return out
