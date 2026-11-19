"""Generated from Smithy shape ``com.amazonaws.fms#FailedItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.failed_item

FailedItemList: TypeAlias = list["capo_fms.types.failed_item.FailedItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItemList) -> list:
    import capo_fms.types.failed_item

    out: list = []
    for item in value:
        out.append(capo_fms.types.failed_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> FailedItemList:
    import capo_fms.types.failed_item

    out: FailedItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.failed_item.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedItemList) -> list:
    import capo_fms.types.failed_item

    out: list = []
    for item in value:
        out.append(capo_fms.types.failed_item.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FailedItemList:
    import capo_fms.types.failed_item

    out: FailedItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.failed_item.deserialize_cbor(item))
    return out
