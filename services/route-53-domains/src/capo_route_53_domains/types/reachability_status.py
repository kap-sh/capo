"""Generated from Smithy shape ``com.amazonaws.route53domains#ReachabilityStatus``."""

from typing import Literal, TypeAlias, cast

ReachabilityStatus: TypeAlias = Literal[
    "PENDING",
    "DONE",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReachabilityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReachabilityStatus:
    return cast(ReachabilityStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReachabilityStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ReachabilityStatus:
    return cast(ReachabilityStatus, data)
