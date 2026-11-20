"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#BatchGetEventErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Why an event was not returned, named for the exception <code>GetEvent</code> would return for it.</p>"""
BatchGetEventErrorCode: TypeAlias = Literal[
    "RESOURCE_NOT_FOUND",
    "THROTTLING",
    "ACCESS_DENIED",
    "INTERNAL_SERVER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetEventErrorCode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchGetEventErrorCode:
    return cast(BatchGetEventErrorCode, data)
