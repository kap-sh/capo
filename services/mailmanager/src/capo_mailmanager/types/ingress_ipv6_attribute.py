"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6Attribute``."""

from typing import Literal, TypeAlias, cast

IngressIpv6Attribute: TypeAlias = Literal["SENDER_IPV6",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressIpv6Attribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpv6Attribute:
    return cast(IngressIpv6Attribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressIpv6Attribute) -> str:
    return value


def deserialize_cbor(data: str) -> IngressIpv6Attribute:
    return cast(IngressIpv6Attribute, data)
