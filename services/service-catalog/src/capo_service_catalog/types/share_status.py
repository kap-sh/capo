"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ShareStatus``."""

from typing import Literal, TypeAlias, cast

ShareStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ShareStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareStatus:
    return cast(ShareStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ShareStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ShareStatus:
    return cast(ShareStatus, data)
