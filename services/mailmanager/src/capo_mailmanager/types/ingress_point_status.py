"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressPointStatus``."""

from typing import Literal, TypeAlias, cast

IngressPointStatus: TypeAlias = Literal[
    "PROVISIONING",
    "DEPROVISIONING",
    "UPDATING",
    "ACTIVE",
    "CLOSED",
    "FAILED",
    "ASSOCIATED_VPC_ENDPOINT_DOES_NOT_EXIST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressPointStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressPointStatus:
    return cast(IngressPointStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressPointStatus) -> str:
    return value


def deserialize_cbor(data: str) -> IngressPointStatus:
    return cast(IngressPointStatus, data)
