"""Generated from Smithy shape ``com.amazonaws.acmpca#AccessMethodType``."""

from typing import Literal, TypeAlias, cast

AccessMethodType: TypeAlias = Literal[
    "CA_REPOSITORY",
    "RESOURCE_PKI_MANIFEST",
    "RESOURCE_PKI_NOTIFY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessMethodType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessMethodType:
    return cast(AccessMethodType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AccessMethodType) -> str:
    return value


def deserialize_cbor(data: str) -> AccessMethodType:
    return cast(AccessMethodType, data)
