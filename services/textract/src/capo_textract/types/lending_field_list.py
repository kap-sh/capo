"""Generated from Smithy shape ``com.amazonaws.textract#LendingFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.lending_field

LendingFieldList: TypeAlias = list["capo_textract.types.lending_field.LendingField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingFieldList) -> list:
    import capo_textract.types.lending_field

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LendingFieldList:
    import capo_textract.types.lending_field

    out: LendingFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_field.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingFieldList) -> list:
    import capo_textract.types.lending_field

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_field.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LendingFieldList:
    import capo_textract.types.lending_field

    out: LendingFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_field.deserialize_cbor(item))
    return out
