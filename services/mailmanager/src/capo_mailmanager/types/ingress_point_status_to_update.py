"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointStatusToUpdate``."""

from typing import Literal, TypeAlias, cast

IngressPointStatusToUpdate: TypeAlias = Literal[
    "ACTIVE",
    "CLOSED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointStatusToUpdate) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointStatusToUpdate:
    return cast(IngressPointStatusToUpdate, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressPointStatusToUpdate) -> str:
    return value


def deserialize_cbor(data: str) -> IngressPointStatusToUpdate:
    return cast(IngressPointStatusToUpdate, data)
