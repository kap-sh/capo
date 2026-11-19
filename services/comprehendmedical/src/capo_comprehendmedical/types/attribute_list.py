"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#AttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.attribute

AttributeList: TypeAlias = list["capo_comprehendmedical.types.attribute.Attribute"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeList) -> list:
    import capo_comprehendmedical.types.attribute

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.attribute.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AttributeList:
    import capo_comprehendmedical.types.attribute

    out: AttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.attribute.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttributeList) -> list:
    import capo_comprehendmedical.types.attribute

    out: list = []
    for item in value:
        out.append(capo_comprehendmedical.types.attribute.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> AttributeList:
    import capo_comprehendmedical.types.attribute

    out: AttributeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_comprehendmedical.types.attribute.deserialize_cbor(item))
    return out
