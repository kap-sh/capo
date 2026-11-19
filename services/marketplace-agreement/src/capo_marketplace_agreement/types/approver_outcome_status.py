"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ApproverOutcomeStatus``."""

from typing import Literal, TypeAlias, cast

ApproverOutcomeStatus: TypeAlias = Literal[
    "QUEUED",
    "PENDING_APPROVAL",
    "APPROVED",
    "REJECTED",
    "EXPIRED",
    "SKIPPED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApproverOutcomeStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ApproverOutcomeStatus:
    return cast(ApproverOutcomeStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApproverOutcomeStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ApproverOutcomeStatus:
    return cast(ApproverOutcomeStatus, data)
