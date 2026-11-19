"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildPhaseType``."""

from typing import Literal, TypeAlias, cast

BuildPhaseType: TypeAlias = Literal[
    "SUBMITTED",
    "QUEUED",
    "PROVISIONING",
    "DOWNLOAD_SOURCE",
    "INSTALL",
    "PRE_BUILD",
    "BUILD",
    "POST_BUILD",
    "UPLOAD_ARTIFACTS",
    "FINALIZING",
    "COMPLETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildPhaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BuildPhaseType:
    return cast(BuildPhaseType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildPhaseType) -> str:
    return value


def deserialize_cbor(data: str) -> BuildPhaseType:
    return cast(BuildPhaseType, data)
