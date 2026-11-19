"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RestoreStatusType``."""

from typing import Literal, TypeAlias, cast

RestoreStatusType: TypeAlias = Literal[
    "PREVIEW_GENERATING",
    "PREVIEW_GENERATED",
    "PREVIEW_CANCELLED",
    "PREVIEW_GENERATION_FAILED",
    "PREVIEW_EXPIRED",
    "RESTORING",
    "RESTORE_COMPLETED",
    "TEMPORARY_INTERNAL_ERROR_SEE_SUPPORT_CASE",
    "AWS_ABORTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RestoreStatusType:
    return cast(RestoreStatusType, data)
