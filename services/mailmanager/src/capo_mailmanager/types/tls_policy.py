"""Generated from Smithy shape ``com.amazonaws.mailmanager#TlsPolicy``."""

from typing import Literal, TypeAlias, cast

TlsPolicy: TypeAlias = Literal[
    "REQUIRED",
    "OPTIONAL",
    "FIPS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TlsPolicy:
    return cast(TlsPolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TlsPolicy) -> str:
    return value


def deserialize_cbor(data: str) -> TlsPolicy:
    return cast(TlsPolicy, data)
