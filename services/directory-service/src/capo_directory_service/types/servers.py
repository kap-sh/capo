"""Generated from Smithy shape ``com.amazonaws.directoryservice#Servers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.server

Servers: TypeAlias = list["capo_directory_service.types.server.Server"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Servers) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Servers:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Servers) -> list:
    return list(value)


def deserialize_cbor(data: list) -> Servers:
    return [item for item in data if item is not None]
