"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeADAssessmentResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.assessment
    import capo_directory_service.types.assessment_reports


class DescribeADAssessmentResult(TypedDict, closed=True):
    assessment: NotRequired["capo_directory_service.types.assessment.Assessment"]
    """<p>Detailed information about the self-managed instance settings (IDs and DNS IPs).</p>"""
    assessment_reports: NotRequired[
        "capo_directory_service.types.assessment_reports.AssessmentReports"
    ]
    """<p>A list of assessment reports containing validation results for each domain controller and test category. Each report includes specific validation details and outcomes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeADAssessmentResult) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_directory_service.types.assessment

        out["Assessment"] = (
            capo_directory_service.types.assessment.serialize_aws_json_1_1(
                value["assessment"]
            )
        )
    if "assessment_reports" in value:
        import capo_directory_service.types.assessment_reports

        out["AssessmentReports"] = (
            capo_directory_service.types.assessment_reports.serialize_aws_json_1_1(
                value["assessment_reports"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeADAssessmentResult:
    out: DescribeADAssessmentResult = {}  # type: ignore[typeddict-item]
    if data.get("Assessment") is not None:
        import capo_directory_service.types.assessment

        out["assessment"] = (
            capo_directory_service.types.assessment.deserialize_aws_json_1_1(
                data["Assessment"]
            )
        )
    if data.get("AssessmentReports") is not None:
        import capo_directory_service.types.assessment_reports

        out["assessment_reports"] = (
            capo_directory_service.types.assessment_reports.deserialize_aws_json_1_1(
                data["AssessmentReports"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeADAssessmentResult) -> dict:
    out: dict = {}
    if "assessment" in value:
        import capo_directory_service.types.assessment

        out["Assessment"] = capo_directory_service.types.assessment.serialize_cbor(
            value["assessment"]
        )
    if "assessment_reports" in value:
        import capo_directory_service.types.assessment_reports

        out["AssessmentReports"] = (
            capo_directory_service.types.assessment_reports.serialize_cbor(
                value["assessment_reports"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeADAssessmentResult:
    out: DescribeADAssessmentResult = {}  # type: ignore[typeddict-item]
    if data.get("Assessment") is not None:
        import capo_directory_service.types.assessment

        out["assessment"] = capo_directory_service.types.assessment.deserialize_cbor(
            data["Assessment"]
        )
    if data.get("AssessmentReports") is not None:
        import capo_directory_service.types.assessment_reports

        out["assessment_reports"] = (
            capo_directory_service.types.assessment_reports.deserialize_cbor(
                data["AssessmentReports"]
            )
        )
    return out
