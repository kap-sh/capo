"""Generated from Smithy shape ``com.amazonaws.textract#Warnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.warning

Warnings: TypeAlias = list["capo_textract.types.warning.Warning"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Warnings) -> list:
    import capo_textract.types.warning

    out: list = []
    for item in value:
        out.append(capo_textract.types.warning.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Warnings:
    import capo_textract.types.warning

    out: Warnings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.warning.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Warnings) -> list:
    import capo_textract.types.warning

    out: list = []
    for item in value:
        out.append(capo_textract.types.warning.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Warnings:
    import capo_textract.types.warning

    out: Warnings = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.warning.deserialize_cbor(item))
    return out
