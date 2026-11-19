"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookStatus``."""

from typing import Literal, TypeAlias, cast

WebhookStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookStatus:
    return cast(WebhookStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookStatus) -> str:
    return value


def deserialize_cbor(data: str) -> WebhookStatus:
    return cast(WebhookStatus, data)
