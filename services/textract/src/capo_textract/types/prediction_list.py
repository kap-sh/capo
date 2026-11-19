"""Generated from Smithy shape ``com.amazonaws.textract#PredictionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.prediction

PredictionList: TypeAlias = list["capo_textract.types.prediction.Prediction"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictionList) -> list:
    import capo_textract.types.prediction

    out: list = []
    for item in value:
        out.append(capo_textract.types.prediction.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredictionList:
    import capo_textract.types.prediction

    out: PredictionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.prediction.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PredictionList) -> list:
    import capo_textract.types.prediction

    out: list = []
    for item in value:
        out.append(capo_textract.types.prediction.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PredictionList:
    import capo_textract.types.prediction

    out: PredictionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.prediction.deserialize_cbor(item))
    return out
