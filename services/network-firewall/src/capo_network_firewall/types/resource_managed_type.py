"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ResourceManagedType``."""

from typing import Literal, TypeAlias, cast

ResourceManagedType: TypeAlias = Literal[
    "AWS_MANAGED_THREAT_SIGNATURES",
    "AWS_MANAGED_DOMAIN_LISTS",
    "ACTIVE_THREAT_DEFENSE",
    "PARTNER_MANAGED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceManagedType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceManagedType:
    return cast(ResourceManagedType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceManagedType) -> str:
    return value


def deserialize_cbor(data: str) -> ResourceManagedType:
    return cast(ResourceManagedType, data)
