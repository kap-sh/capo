"""Generated from Smithy shape ``com.amazonaws.pi#DimensionDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.dimension_detail

DimensionDetailList: TypeAlias = list["capo_pi.types.dimension_detail.DimensionDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionDetailList) -> list:
    import capo_pi.types.dimension_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionDetailList:
    import capo_pi.types.dimension_detail

    out: DimensionDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_detail.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionDetailList) -> list:
    import capo_pi.types.dimension_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DimensionDetailList:
    import capo_pi.types.dimension_detail

    out: DimensionDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_detail.deserialize_cbor(item))
    return out
