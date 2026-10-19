"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ReportGenerationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.report_generation_status
    import capo_resiliencehubv2.types.report_output
    import capo_resiliencehubv2.types.report_type
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.uuid


class ReportGenerationResult(TypedDict, closed=True):
    report_type: "capo_resiliencehubv2.types.report_type.ReportType"
    """<p>The type of the generated report.</p>"""
    status: "capo_resiliencehubv2.types.report_generation_status.ReportGenerationStatus"
    """<p>The status of the report generation.</p>"""
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>The service this report was generated for.</p>"""
    assessment_id: NotRequired["capo_resiliencehubv2.types.uuid.Uuid"]
    """<p>Present for FAILURE_MODE reports.</p>"""
    test_run_id: NotRequired["capo_resiliencehubv2.types.test_run_id.TestRunId"]
    test_template_arn: NotRequired[
        "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    ]
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the report was created.</p>"""
    report_output: NotRequired["capo_resiliencehubv2.types.report_output.ReportOutput"]
    """<p>Present when status is SUCCEEDED or FAILED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportGenerationResult) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.report_type

    out["reportType"] = capo_resiliencehubv2.types.report_type.serialize_json(
        value["report_type"]
    )
    import capo_resiliencehubv2.types.report_generation_status

    out["status"] = capo_resiliencehubv2.types.report_generation_status.serialize_json(
        value["status"]
    )
    if "service_arn" in value:
        out["serviceArn"] = value["service_arn"]
    if "assessment_id" in value:
        out["assessmentId"] = value["assessment_id"]
    if "test_run_id" in value:
        out["testRunId"] = value["test_run_id"]
    if "test_template_arn" in value:
        out["testTemplateArn"] = value["test_template_arn"]
    if "created_at" in value:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["createdAt"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "report_output" in value:
        import capo_resiliencehubv2.types.report_output

        out["reportOutput"] = capo_resiliencehubv2.types.report_output.serialize_json(
            value["report_output"]
        )
    return out


def deserialize_json(data: dict) -> ReportGenerationResult:
    out: ReportGenerationResult = {}  # type: ignore[typeddict-item]
    if data.get("reportType") is not None:
        import capo_resiliencehubv2.types.report_type

        out["report_type"] = capo_resiliencehubv2.types.report_type.deserialize_json(
            data["reportType"]
        )
    else:
        import typing

        out["report_type"] = typing.cast(
            "capo_resiliencehubv2.types.report_type.ReportType", ""
        )
    if data.get("status") is not None:
        import capo_resiliencehubv2.types.report_generation_status

        out["status"] = (
            capo_resiliencehubv2.types.report_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_resiliencehubv2.types.report_generation_status.ReportGenerationStatus",
            "",
        )
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    if data.get("assessmentId") is not None:
        out["assessment_id"] = data["assessmentId"]
    if data.get("testRunId") is not None:
        out["test_run_id"] = data["testRunId"]
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    if data.get("createdAt") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["created_at"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("reportOutput") is not None:
        import capo_resiliencehubv2.types.report_output

        out["report_output"] = (
            capo_resiliencehubv2.types.report_output.deserialize_json(
                data["reportOutput"]
            )
        )
    return out
