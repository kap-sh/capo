"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageServerProtocol``."""

from typing import Literal, TypeAlias, cast

ObjectStorageServerProtocol: TypeAlias = Literal[
    "HTTPS",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectStorageServerProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectStorageServerProtocol:
    return cast(ObjectStorageServerProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ObjectStorageServerProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> ObjectStorageServerProtocol:
    return cast(ObjectStorageServerProtocol, data)
