"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsAttribute``."""

from typing import Literal, TypeAlias, cast

IngressTlsAttribute: TypeAlias = Literal["TLS_PROTOCOL",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressTlsAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsAttribute:
    return cast(IngressTlsAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressTlsAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> IngressTlsAttribute:
    return cast(IngressTlsAttribute, data)
