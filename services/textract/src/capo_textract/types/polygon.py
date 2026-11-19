"""Generated from Smithy shape ``com.amazonaws.textract#Polygon``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_textract.types.point

Polygon: TypeAlias = list["capo_textract.types.point.Point"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Polygon) -> list:
    import capo_textract.types.point

    out: list = []
    for item in value:
        out.append(capo_textract.types.point.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Polygon:
    import capo_textract.types.point

    out: Polygon = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.point.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Polygon) -> list:
    import capo_textract.types.point

    out: list = []
    for item in value:
        out.append(capo_textract.types.point.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Polygon:
    import capo_textract.types.point

    out: Polygon = []
    for item in data:
        if item is None:
            continue
        out.append(capo_textract.types.point.deserialize_cbor(item))
    return out
