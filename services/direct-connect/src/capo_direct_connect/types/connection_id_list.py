"""Generated from Smithy shape ``com.amazonaws.directconnect#ConnectionIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_id

ConnectionIdList: TypeAlias = list[
    "capo_direct_connect.types.connection_id.ConnectionId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectionIdList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ConnectionIdList:
    return [item for item in data if item is not None]
