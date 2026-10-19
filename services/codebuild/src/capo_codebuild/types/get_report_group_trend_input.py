"""Generated from Smithy shape ``com.amazonaws.codebuild#GetReportGroupTrendInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.page_size
    import capo_codebuild.types.report_group_trend_field_type


class GetReportGroupTrendInput(TypedDict, closed=True):
    report_group_arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The ARN of the report group that contains the reports to analyze.</p>"""
    num_of_reports: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The number of reports to analyze. This operation always retrieves the most recent reports.</p> <p>If this parameter is omitted, the most recent 100 reports are analyzed.</p>"""
    trend_field: (
        "capo_codebuild.types.report_group_trend_field_type.ReportGroupTrendFieldType"
    )
    """<p>The test report value to accumulate. This must be one of the following values:</p> <dl> <dt>Test reports:</dt> <dd> <dl> <dt>DURATION</dt> <dd> <p>Accumulate the test run times for the specified reports.</p> </dd> <dt>PASS_RATE</dt> <dd> <p>Accumulate the percentage of tests that passed for the specified test reports.</p> </dd> <dt>TOTAL</dt> <dd> <p>Accumulate the total number of tests for the specified test reports.</p> </dd> </dl> </dd> </dl> <dl> <dt>Code coverage reports:</dt> <dd> <dl> <dt>BRANCH_COVERAGE</dt> <dd> <p>Accumulate the branch coverage percentages for the specified test reports.</p> </dd> <dt>BRANCHES_COVERED</dt> <dd> <p>Accumulate the branches covered values for the specified test reports.</p> </dd> <dt>BRANCHES_MISSED</dt> <dd> <p>Accumulate the branches missed values for the specified test reports.</p> </dd> <dt>LINE_COVERAGE</dt> <dd> <p>Accumulate the line coverage percentages for the specified test reports.</p> </dd> <dt>LINES_COVERED</dt> <dd> <p>Accumulate the lines covered values for the specified test reports.</p> </dd> <dt>LINES_MISSED</dt> <dd> <p>Accumulate the lines not covered values for the specified test reports.</p> </dd> </dl> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetReportGroupTrendInput) -> dict:
    out: dict = {}
    out["reportGroupArn"] = value["report_group_arn"]
    if "num_of_reports" in value:
        out["numOfReports"] = value["num_of_reports"]
    import capo_codebuild.types.report_group_trend_field_type

    out["trendField"] = (
        capo_codebuild.types.report_group_trend_field_type.serialize_aws_json_1_1(
            value["trend_field"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetReportGroupTrendInput:
    out: GetReportGroupTrendInput = {}  # type: ignore[typeddict-item]
    if data.get("reportGroupArn") is not None:
        out["report_group_arn"] = data["reportGroupArn"]
    else:
        out["report_group_arn"] = ""
    if data.get("numOfReports") is not None:
        out["num_of_reports"] = data["numOfReports"]
    if data.get("trendField") is not None:
        import capo_codebuild.types.report_group_trend_field_type

        out["trend_field"] = (
            capo_codebuild.types.report_group_trend_field_type.deserialize_aws_json_1_1(
                data["trendField"]
            )
        )
    else:
        import typing

        out["trend_field"] = typing.cast(
            "capo_codebuild.types.report_group_trend_field_type.ReportGroupTrendFieldType",
            "",
        )
    return out
