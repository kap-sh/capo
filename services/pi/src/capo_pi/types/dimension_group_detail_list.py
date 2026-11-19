"""Generated from Smithy shape ``com.amazonaws.pi#DimensionGroupDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.dimension_group_detail

DimensionGroupDetailList: TypeAlias = list[
    "capo_pi.types.dimension_group_detail.DimensionGroupDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionGroupDetailList) -> list:
    import capo_pi.types.dimension_group_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_group_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionGroupDetailList:
    import capo_pi.types.dimension_group_detail

    out: DimensionGroupDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_group_detail.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionGroupDetailList) -> list:
    import capo_pi.types.dimension_group_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_group_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DimensionGroupDetailList:
    import capo_pi.types.dimension_group_detail

    out: DimensionGroupDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_group_detail.deserialize_cbor(item))
    return out
