"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TlsInterceptMode``."""

from typing import Literal, TypeAlias, cast

TlsInterceptMode: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TlsInterceptMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TlsInterceptMode:
    return cast(TlsInterceptMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TlsInterceptMode) -> str:
    return value


def deserialize_cbor(data: str) -> TlsInterceptMode:
    return cast(TlsInterceptMode, data)
