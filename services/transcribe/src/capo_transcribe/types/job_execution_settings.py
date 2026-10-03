"""Generated from Smithy shape ``com.amazonaws.transcribe#JobExecutionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.boolean
    import capo_transcribe.types.data_access_role_arn


class JobExecutionSettings(TypedDict, closed=True):
    allow_deferred_execution: NotRequired["capo_transcribe.types.boolean.Boolean"]
    """<p>Makes it possible to enable job queuing when your concurrent request limit is exceeded. When <code>AllowDeferredExecution</code> is set to <code>true</code>, transcription job requests are placed in a queue until the number of jobs falls below the concurrent request limit. If <code>AllowDeferredExecution</code> is set to <code>false</code> and the number of transcription job requests exceed the concurrent request limit, you get a <code>LimitExceededException</code> error.</p> <p>If you include <code>AllowDeferredExecution</code> in your request, you must also include <code>DataAccessRoleArn</code>.</p>"""
    data_access_role_arn: NotRequired[
        "capo_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files. If the role that you specify doesn’t have the appropriate permissions to access the specified Amazon S3 location, your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM ARNs</a>.</p> <p>Note that if you include <code>DataAccessRoleArn</code> in your request, you must also include <code>AllowDeferredExecution</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobExecutionSettings) -> dict:
    out: dict = {}
    if "allow_deferred_execution" in value:
        out["AllowDeferredExecution"] = value["allow_deferred_execution"]
    if "data_access_role_arn" in value:
        out["DataAccessRoleArn"] = value["data_access_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobExecutionSettings:
    out: JobExecutionSettings = {}  # type: ignore[typeddict-item]
    if data.get("AllowDeferredExecution") is not None:
        out["allow_deferred_execution"] = data["AllowDeferredExecution"]
    if data.get("DataAccessRoleArn") is not None:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    return out
