"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#UnmappedAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.unmapped_attribute

UnmappedAttributeList: TypeAlias = list[
    "capo_comprehendmedical.types.unmapped_attribute.UnmappedAttribute"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnmappedAttributeList) -> list:
    import capo_comprehendmedical.types.unmapped_attribute

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.unmapped_attribute.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UnmappedAttributeList:
    import capo_comprehendmedical.types.unmapped_attribute

    out: UnmappedAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.unmapped_attribute.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UnmappedAttributeList) -> list:
    import capo_comprehendmedical.types.unmapped_attribute

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.unmapped_attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> UnmappedAttributeList:
    import capo_comprehendmedical.types.unmapped_attribute

    out: UnmappedAttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.unmapped_attribute.deserialize_cbor(item)
        )
    return out
