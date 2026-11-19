"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolOperator``."""

from typing import Literal, TypeAlias, cast

IngressTlsProtocolOperator: TypeAlias = Literal[
    "MINIMUM_TLS_VERSION",
    "IS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsProtocolOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsProtocolOperator:
    return cast(IngressTlsProtocolOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressTlsProtocolOperator) -> str:
    return value


def deserialize_cbor(data: str) -> IngressTlsProtocolOperator:
    return cast(IngressTlsProtocolOperator, data)
