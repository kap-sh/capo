"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv4Attribute``."""

from typing import Literal, TypeAlias, cast

IngressIpv4Attribute: TypeAlias = Literal["SENDER_IP",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv4Attribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpv4Attribute:
    return cast(IngressIpv4Attribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressIpv4Attribute) -> str:
    return value


def deserialize_cbor(data: str) -> IngressIpv4Attribute:
    return cast(IngressIpv4Attribute, data)
