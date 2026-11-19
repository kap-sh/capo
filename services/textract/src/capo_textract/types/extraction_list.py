"""Generated from Smithy shape ``com.amazonaws.textract#ExtractionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.extraction

ExtractionList: TypeAlias = list["capo_textract.types.extraction.Extraction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtractionList) -> list:
    import capo_textract.types.extraction

    out: list = []
    for item in value:
        out.append(capo_textract.types.extraction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExtractionList:
    import capo_textract.types.extraction

    out: ExtractionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.extraction.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExtractionList) -> list:
    import capo_textract.types.extraction

    out: list = []
    for item in value:
        out.append(capo_textract.types.extraction.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ExtractionList:
    import capo_textract.types.extraction

    out: ExtractionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.extraction.deserialize_cbor(item))
    return out
