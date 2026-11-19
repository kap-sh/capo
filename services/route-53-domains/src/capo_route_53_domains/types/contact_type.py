"""Generated from Smithy shape ``com.amazonaws.route53domains#ContactType``."""

from typing import Literal, TypeAlias, cast

ContactType: TypeAlias = Literal[
    "PERSON",
    "COMPANY",
    "ASSOCIATION",
    "PUBLIC_BODY",
    "RESELLER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactType:
    return cast(ContactType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContactType) -> str:
    return value


def deserialize_cbor(data: str) -> ContactType:
    return cast(ContactType, data)
