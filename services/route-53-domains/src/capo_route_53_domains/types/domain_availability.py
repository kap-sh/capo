"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainAvailability``."""

from typing import Literal, TypeAlias, cast

DomainAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "AVAILABLE_RESERVED",
    "AVAILABLE_PREORDER",
    "UNAVAILABLE",
    "UNAVAILABLE_PREMIUM",
    "UNAVAILABLE_RESTRICTED",
    "RESERVED",
    "DONT_KNOW",
    "INVALID_NAME_FOR_TLD",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainAvailability:
    return cast(DomainAvailability, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainAvailability) -> str:
    return value


def deserialize_cbor(data: str) -> DomainAvailability:
    return cast(DomainAvailability, data)
