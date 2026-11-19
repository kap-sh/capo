"""Generated from Smithy shape ``com.amazonaws.codepipeline#ApprovalStatus``."""

from typing import Literal, TypeAlias, cast

ApprovalStatus: TypeAlias = Literal[
    "Approved",
    "Rejected",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApprovalStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ApprovalStatus:
    return cast(ApprovalStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApprovalStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ApprovalStatus:
    return cast(ApprovalStatus, data)
