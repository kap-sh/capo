"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookBuildType``."""

from typing import Literal, TypeAlias, cast

WebhookBuildType: TypeAlias = Literal[
    "BUILD",
    "BUILD_BATCH",
    "RUNNER_BUILDKITE_BUILD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookBuildType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebhookBuildType:
    return cast(WebhookBuildType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebhookBuildType) -> str:
    return value


def deserialize_cbor(data: str) -> WebhookBuildType:
    return cast(WebhookBuildType, data)
