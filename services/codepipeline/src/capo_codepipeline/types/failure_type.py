"""Generated from Smithy shape ``com.amazonaws.codepipeline#FailureType``."""

from typing import Literal, TypeAlias, cast

FailureType: TypeAlias = Literal[
    "JobFailed",
    "ConfigurationError",
    "PermissionError",
    "RevisionOutOfSync",
    "RevisionUnavailable",
    "SystemUnavailable",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailureType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FailureType:
    return cast(FailureType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailureType) -> str:
    return value


def deserialize_cbor(data: str) -> FailureType:
    return cast(FailureType, data)
