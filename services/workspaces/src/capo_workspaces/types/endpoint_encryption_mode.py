"""Generated from Smithy shape ``com.amazonaws.workspaces#EndpointEncryptionMode``."""

from typing import Literal, TypeAlias, cast

EndpointEncryptionMode: TypeAlias = Literal[
    "STANDARD_TLS",
    "FIPS_VALIDATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointEncryptionMode:
    return cast(EndpointEncryptionMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EndpointEncryptionMode) -> str:
    return value


def deserialize_cbor(data: str) -> EndpointEncryptionMode:
    return cast(EndpointEncryptionMode, data)
