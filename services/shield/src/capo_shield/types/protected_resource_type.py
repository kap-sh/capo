"""Generated from Smithy shape ``com.amazonaws.shield#ProtectedResourceType``."""

from typing import Literal, TypeAlias, cast

ProtectedResourceType: TypeAlias = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "ROUTE_53_HOSTED_ZONE",
    "ELASTIC_IP_ALLOCATION",
    "CLASSIC_LOAD_BALANCER",
    "APPLICATION_LOAD_BALANCER",
    "GLOBAL_ACCELERATOR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectedResourceType:
    return cast(ProtectedResourceType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtectedResourceType) -> str:
    return value


def deserialize_cbor(data: str) -> ProtectedResourceType:
    return cast(ProtectedResourceType, data)
