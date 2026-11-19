"""Generated from Smithy shape ``com.amazonaws.textract#LendingDetectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.lending_detection

LendingDetectionList: TypeAlias = list[
    "capo_textract.types.lending_detection.LendingDetection"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LendingDetectionList) -> list:
    import capo_textract.types.lending_detection

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_detection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LendingDetectionList:
    import capo_textract.types.lending_detection

    out: LendingDetectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_detection.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LendingDetectionList) -> list:
    import capo_textract.types.lending_detection

    out: list = []
    for item in value:
        out.append(capo_textract.types.lending_detection.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LendingDetectionList:
    import capo_textract.types.lending_detection

    out: LendingDetectionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.lending_detection.deserialize_cbor(item))
    return out
