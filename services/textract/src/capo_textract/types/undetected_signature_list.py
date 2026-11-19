"""Generated from Smithy shape ``com.amazonaws.textract#UndetectedSignatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.undetected_signature

UndetectedSignatureList: TypeAlias = list[
    "capo_textract.types.undetected_signature.UndetectedSignature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndetectedSignatureList) -> list:
    import capo_textract.types.undetected_signature

    out: list = []
    for item in value:
        out.append(
            capo_textract.types.undetected_signature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UndetectedSignatureList:
    import capo_textract.types.undetected_signature

    out: UndetectedSignatureList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_textract.types.undetected_signature.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UndetectedSignatureList) -> list:
    import capo_textract.types.undetected_signature

    out: list = []
    for item in value:
        out.append(capo_textract.types.undetected_signature.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UndetectedSignatureList:
    import capo_textract.types.undetected_signature

    out: UndetectedSignatureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.undetected_signature.deserialize_cbor(item))
    return out
