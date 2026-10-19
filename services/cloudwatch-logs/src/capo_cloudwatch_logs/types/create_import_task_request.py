"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.import_filter
    import capo_cloudwatch_logs.types.role_arn


class CreateImportTaskRequest(TypedDict, closed=True):
    import_source_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the source to import from.</p>"""
    import_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that grants CloudWatch Logs permission to import from the CloudTrail Lake Event Data Store.</p>"""
    import_filter: NotRequired["capo_cloudwatch_logs.types.import_filter.ImportFilter"]
    """<p>Optional filters to constrain the import by CloudTrail event time. Times are specified in Unix timestamp milliseconds. The range of data being imported must be within the specified source's retention period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateImportTaskRequest) -> dict:
    out: dict = {}
    out["importSourceArn"] = value["import_source_arn"]
    out["importRoleArn"] = value["import_role_arn"]
    if "import_filter" in value:
        import capo_cloudwatch_logs.types.import_filter

        out["importFilter"] = (
            capo_cloudwatch_logs.types.import_filter.serialize_aws_json_1_1(
                value["import_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateImportTaskRequest:
    out: CreateImportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("importSourceArn") is not None:
        out["import_source_arn"] = data["importSourceArn"]
    else:
        out["import_source_arn"] = ""
    if data.get("importRoleArn") is not None:
        out["import_role_arn"] = data["importRoleArn"]
    else:
        out["import_role_arn"] = ""
    if data.get("importFilter") is not None:
        import capo_cloudwatch_logs.types.import_filter

        out["import_filter"] = (
            capo_cloudwatch_logs.types.import_filter.deserialize_aws_json_1_1(
                data["importFilter"]
            )
        )
    return out
