"""Generated from Smithy shape ``com.amazonaws.directconnect#LagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.lag

LagList: TypeAlias = list["capo_direct_connect.types.lag.Lag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LagList) -> list:
    import capo_direct_connect.types.lag

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.lag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LagList:
    import capo_direct_connect.types.lag

    out: LagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.lag.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LagList) -> list:
    import capo_direct_connect.types.lag

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.lag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LagList:
    import capo_direct_connect.types.lag

    out: LagList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.lag.deserialize_cbor(item))
    return out
