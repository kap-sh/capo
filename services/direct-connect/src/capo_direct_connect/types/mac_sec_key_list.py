"""Generated from Smithy shape ``com.amazonaws.directconnect#MacSecKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.mac_sec_key

MacSecKeyList: TypeAlias = list["capo_direct_connect.types.mac_sec_key.MacSecKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacSecKeyList) -> list:
    import capo_direct_connect.types.mac_sec_key

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.mac_sec_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MacSecKeyList:
    import capo_direct_connect.types.mac_sec_key

    out: MacSecKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.mac_sec_key.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MacSecKeyList) -> list:
    import capo_direct_connect.types.mac_sec_key

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.mac_sec_key.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> MacSecKeyList:
    import capo_direct_connect.types.mac_sec_key

    out: MacSecKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.mac_sec_key.deserialize_cbor(item))
    return out
