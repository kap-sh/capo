"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchGetReportsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_arns
    import capo_codebuild.types.reports


class BatchGetReportsOutput(TypedDict, closed=True):
    reports: NotRequired["capo_codebuild.types.reports.Reports"]
    """<p> The array of <code>Report</code> objects returned by <code>BatchGetReports</code>. </p>"""
    reports_not_found: NotRequired["capo_codebuild.types.report_arns.ReportArns"]
    """<p> An array of ARNs passed to <code>BatchGetReportGroups</code> that are not associated with a <code>Report</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetReportsOutput) -> dict:
    out: dict = {}
    if "reports" in value:
        import capo_codebuild.types.reports

        out["reports"] = capo_codebuild.types.reports.serialize_aws_json_1_1(
            value["reports"]
        )
    if "reports_not_found" in value:
        import capo_codebuild.types.report_arns

        out["reportsNotFound"] = (
            capo_codebuild.types.report_arns.serialize_aws_json_1_1(
                value["reports_not_found"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetReportsOutput:
    out: BatchGetReportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("reports") is not None:
        import capo_codebuild.types.reports

        out["reports"] = capo_codebuild.types.reports.deserialize_aws_json_1_1(
            data["reports"]
        )
    if data.get("reportsNotFound") is not None:
        import capo_codebuild.types.report_arns

        out["reports_not_found"] = (
            capo_codebuild.types.report_arns.deserialize_aws_json_1_1(
                data["reportsNotFound"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchGetReportsOutput) -> dict:
    out: dict = {}
    if "reports" in value:
        import capo_codebuild.types.reports

        out["reports"] = capo_codebuild.types.reports.serialize_cbor(value["reports"])
    if "reports_not_found" in value:
        import capo_codebuild.types.report_arns

        out["reportsNotFound"] = capo_codebuild.types.report_arns.serialize_cbor(
            value["reports_not_found"]
        )
    return out


def deserialize_cbor(data: dict) -> BatchGetReportsOutput:
    out: BatchGetReportsOutput = {}  # type: ignore[typeddict-item]
    if data.get("reports") is not None:
        import capo_codebuild.types.reports

        out["reports"] = capo_codebuild.types.reports.deserialize_cbor(data["reports"])
    if data.get("reportsNotFound") is not None:
        import capo_codebuild.types.report_arns

        out["reports_not_found"] = capo_codebuild.types.report_arns.deserialize_cbor(
            data["reportsNotFound"]
        )
    return out
