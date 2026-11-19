"""Generated from Smithy shape ``com.amazonaws.textract#LendingResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.lending_result

LendingResultList: TypeAlias = list["capo_textract.types.lending_result.LendingResult"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingResultList) -> list:
    import capo_textract.types.lending_result

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LendingResultList:
    import capo_textract.types.lending_result

    out: LendingResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_result.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingResultList) -> list:
    import capo_textract.types.lending_result

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_result.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LendingResultList:
    import capo_textract.types.lending_result

    out: LendingResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_result.deserialize_cbor(item))
    return out
