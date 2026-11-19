"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareStatus``."""

from typing import Literal, TypeAlias, cast

ShareStatus: TypeAlias = Literal[
    "Shared",
    "PendingAcceptance",
    "Rejected",
    "Rejecting",
    "RejectFailed",
    "Sharing",
    "ShareFailed",
    "Deleted",
    "Deleting",
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
