"""Generated from Smithy shape ``com.amazonaws.textract#DetectedSignatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.detected_signature

DetectedSignatureList: TypeAlias = list[
    "capo_textract.types.detected_signature.DetectedSignature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectedSignatureList) -> list:
    import capo_textract.types.detected_signature

    out: list = []
    for item in value:
        out.append(capo_textract.types.detected_signature.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DetectedSignatureList:
    import capo_textract.types.detected_signature

    out: DetectedSignatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.detected_signature.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectedSignatureList) -> list:
    import capo_textract.types.detected_signature

    out: list = []
    for item in value:
        out.append(capo_textract.types.detected_signature.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DetectedSignatureList:
    import capo_textract.types.detected_signature

    out: DetectedSignatureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.detected_signature.deserialize_cbor(item))
    return out
