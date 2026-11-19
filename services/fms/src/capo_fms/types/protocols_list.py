"""Generated from Smithy shape ``com.amazonaws.fms#ProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.protocol

ProtocolsList: TypeAlias = list["capo_fms.types.protocol.Protocol"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ProtocolsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ProtocolsList:
    return [item for item in data if item is not None]
