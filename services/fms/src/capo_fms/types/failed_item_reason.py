"""Generated from Smithy shape ``com.amazonaws.fms#FailedItemReason``."""

from typing import Literal, TypeAlias, cast

FailedItemReason: TypeAlias = Literal[
    "NOT_VALID_ARN",
    "NOT_VALID_PARTITION",
    "NOT_VALID_REGION",
    "NOT_VALID_SERVICE",
    "NOT_VALID_RESOURCE_TYPE",
    "NOT_VALID_ACCOUNT_ID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItemReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailedItemReason:
    return cast(FailedItemReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedItemReason) -> str:
    return value


def deserialize_cbor(data: str) -> FailedItemReason:
    return cast(FailedItemReason, data)
