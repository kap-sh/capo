"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolAttribute``."""

from typing import Literal, TypeAlias, cast

IngressTlsProtocolAttribute: TypeAlias = Literal[
    "TLS1_2",
    "TLS1_3",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsProtocolAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsProtocolAttribute:
    return cast(IngressTlsProtocolAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressTlsProtocolAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> IngressTlsProtocolAttribute:
    return cast(IngressTlsProtocolAttribute, data)
