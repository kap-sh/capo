"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookFilterType``."""

from typing import Literal, TypeAlias, cast

WebhookFilterType: TypeAlias = Literal[
    "EVENT",
    "BASE_REF",
    "HEAD_REF",
    "ACTOR_ACCOUNT_ID",
    "FILE_PATH",
    "COMMIT_MESSAGE",
    "WORKFLOW_NAME",
    "TAG_NAME",
    "RELEASE_NAME",
    "REPOSITORY_NAME",
    "ORGANIZATION_NAME",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookFilterType:
    return cast(WebhookFilterType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookFilterType) -> str:
    return value


def deserialize_cbor(data: str) -> WebhookFilterType:
    return cast(WebhookFilterType, data)
