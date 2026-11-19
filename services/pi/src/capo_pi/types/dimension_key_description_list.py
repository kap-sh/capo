"""Generated from Smithy shape ``com.amazonaws.pi#DimensionKeyDescriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.dimension_key_description

DimensionKeyDescriptionList: TypeAlias = list[
    "capo_pi.types.dimension_key_description.DimensionKeyDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DimensionKeyDescriptionList) -> list:
    import capo_pi.types.dimension_key_description

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_key_description.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DimensionKeyDescriptionList:
    import capo_pi.types.dimension_key_description

    out: DimensionKeyDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_pi.types.dimension_key_description.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DimensionKeyDescriptionList) -> list:
    import capo_pi.types.dimension_key_description

    out: list = []
    for item in value:
        out.append(capo_pi.types.dimension_key_description.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DimensionKeyDescriptionList:
    import capo_pi.types.dimension_key_description

    out: DimensionKeyDescriptionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.dimension_key_description.deserialize_cbor(item))
    return out
