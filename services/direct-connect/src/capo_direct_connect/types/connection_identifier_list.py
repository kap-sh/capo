"""Generated from Smithy shape ``com.amazonaws.directconnect#ConnectionIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.connection_identifier

ConnectionIdentifierList: TypeAlias = list[
    "capo_direct_connect.types.connection_identifier.ConnectionIdentifier"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectionIdentifierList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConnectionIdentifierList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ConnectionIdentifierList:
    return [item for item in data if item is not None]
