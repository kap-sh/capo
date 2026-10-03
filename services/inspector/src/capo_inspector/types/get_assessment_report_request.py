"""Generated from Smithy shape ``com.amazonaws.inspector#GetAssessmentReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.report_file_format
    import capo_inspector.types.report_type


class GetAssessmentReportRequest(TypedDict, closed=True):
    assessment_run_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN that specifies the assessment run for which you want to generate a report.</p>"""
    report_file_format: "capo_inspector.types.report_file_format.ReportFileFormat"
    """<p>Specifies the file format (html or pdf) of the assessment report that you want to generate.</p>"""
    report_type: "capo_inspector.types.report_type.ReportType"
    """<p>Specifies the type of the assessment report that you want to generate. There are two types of assessment reports: a finding report and a full report. For more information, see <a href="https://docs.aws.amazon.com/inspector/latest/userguide/inspector_reports.html">Assessment Reports</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAssessmentReportRequest) -> dict:
    out: dict = {}
    out["assessmentRunArn"] = value["assessment_run_arn"]
    import capo_inspector.types.report_file_format

    out["reportFileFormat"] = (
        capo_inspector.types.report_file_format.serialize_aws_json_1_1(
            value["report_file_format"]
        )
    )
    import capo_inspector.types.report_type

    out["reportType"] = capo_inspector.types.report_type.serialize_aws_json_1_1(
        value["report_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAssessmentReportRequest:
    out: GetAssessmentReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunArn") is not None:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        raise DeserializationError(
            "GetAssessmentReportRequest.assessment_run_arn required"
        )
    if data.get("reportFileFormat") is not None:
        import capo_inspector.types.report_file_format

        out["report_file_format"] = (
            capo_inspector.types.report_file_format.deserialize_aws_json_1_1(
                data["reportFileFormat"]
            )
        )
    else:
        raise DeserializationError(
            "GetAssessmentReportRequest.report_file_format required"
        )
    if data.get("reportType") is not None:
        import capo_inspector.types.report_type

        out["report_type"] = capo_inspector.types.report_type.deserialize_aws_json_1_1(
            data["reportType"]
        )
    else:
        raise DeserializationError("GetAssessmentReportRequest.report_type required")
    return out
