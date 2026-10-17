"""Generated from Smithy shape ``com.amazonaws.sagemaker#CleanupFailureErrorCode``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of error that prevented the Cleanup step from deleting output resources. Valid values are:</p> <ul> <li> <p> <code>ClientError</code> indicates that the failure was caused by the request.</p> </li> <li> <p> <code>InternalFailure</code> indicates that the failure was caused by an internal error.</p> </li> </ul>"""
CleanupFailureErrorCode: TypeAlias = Literal[
    "ClientError",
    "InternalFailure",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CleanupFailureErrorCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CleanupFailureErrorCode:
    return cast(CleanupFailureErrorCode, data)
