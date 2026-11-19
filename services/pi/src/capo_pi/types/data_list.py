"""Generated from Smithy shape ``com.amazonaws.pi#DataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.data

DataList: TypeAlias = list["capo_pi.types.data.Data"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataList) -> list:
    import capo_pi.types.data

    out: list = []
    for item in value:
        out.append(capo_pi.types.data.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataList:
    import capo_pi.types.data

    out: DataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.data.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataList) -> list:
    import capo_pi.types.data

    out: list = []
    for item in value:
        out.append(capo_pi.types.data.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> DataList:
    import capo_pi.types.data

    out: DataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_pi.types.data.deserialize_cbor(item))
    return out
