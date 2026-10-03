"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteReportGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.boolean
    import capo_codebuild.types.non_empty_string


class DeleteReportGroupInput(TypedDict, closed=True):
    arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the report group to delete. </p>"""
    delete_reports: "capo_codebuild.types.boolean.Boolean"
    """<p>If <code>true</code>, deletes any reports that belong to a report group before deleting the report group. </p> <p>If <code>false</code>, you must delete any reports in the report group. Use <a href="https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html">ListReportsForReportGroup</a> to get the reports in a report group. Use <a href="https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DeleteReport.html">DeleteReport</a> to delete the reports. If you call <code>DeleteReportGroup</code> for a report group that contains one or more reports, an exception is thrown. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteReportGroupInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["deleteReports"] = value.get("delete_reports", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteReportGroupInput:
    out: DeleteReportGroupInput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteReportGroupInput.arn required")
    if data.get("deleteReports") is not None:
        out["delete_reports"] = data["deleteReports"]
    else:
        out["delete_reports"] = False
    return out
