"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.dimension_key_detail

DimensionKeyDetailList: TypeAlias = list[
    "capo_pi.types.dimension_key_detail.DimensionKeyDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDetailList) -> list:
    import capo_pi.types.dimension_key_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_key_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionKeyDetailList:
    import capo_pi.types.dimension_key_detail

    out: DimensionKeyDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_key_detail.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionKeyDetailList) -> list:
    import capo_pi.types.dimension_key_detail

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_key_detail.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DimensionKeyDetailList:
    import capo_pi.types.dimension_key_detail

    out: DimensionKeyDetailList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_key_detail.deserialize_cbor(item))
    return out
