"""Generated from Smithy shape ``com.amazonaws.route53domains#ListDomainsAttributeName``."""

from typing import Literal, TypeAlias, cast

ListDomainsAttributeName: TypeAlias = Literal[
    "DomainName",
    "Expiry",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListDomainsAttributeName:
    return cast(ListDomainsAttributeName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDomainsAttributeName) -> str:
    return value


def deserialize_cbor(data: str) -> ListDomainsAttributeName:
    return cast(ListDomainsAttributeName, data)
