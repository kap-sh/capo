"""Generated from Smithy shape ``com.amazonaws.codedeploy#RevisionLocationType``."""

from typing import Literal, TypeAlias, cast

RevisionLocationType: TypeAlias = Literal[
    "S3",
    "GitHub",
    "String",
    "AppSpecContent",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevisionLocationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RevisionLocationType:
    return cast(RevisionLocationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevisionLocationType) -> str:
    return value


def deserialize_cbor(data: str) -> RevisionLocationType:
    return cast(RevisionLocationType, data)
