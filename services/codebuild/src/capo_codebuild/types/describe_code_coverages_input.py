"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeCodeCoveragesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.page_size
    import capo_codebuild.types.percentage
    import capo_codebuild.types.report_code_coverage_sort_by_type
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class DescribeCodeCoveragesInput(TypedDict, closed=True):
    report_arn: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p> The ARN of the report for which test cases are returned. </p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous call to <code>DescribeCodeCoverages</code>. This specifies the next item to return. To return the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of results to return.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>Specifies if the results are sorted in ascending or descending order.</p>"""
    sort_by: NotRequired[
        "capo_codebuild.types.report_code_coverage_sort_by_type.ReportCodeCoverageSortByType"
    ]
    """<p>Specifies how the results are sorted. Possible values are:</p> <dl> <dt>FILE_PATH</dt> <dd> <p>The results are sorted by file path.</p> </dd> <dt>LINE_COVERAGE_PERCENTAGE</dt> <dd> <p>The results are sorted by the percentage of lines that are covered.</p> </dd> </dl>"""
    min_line_coverage_percentage: NotRequired[
        "capo_codebuild.types.percentage.Percentage"
    ]
    """<p>The minimum line coverage percentage to report.</p>"""
    max_line_coverage_percentage: NotRequired[
        "capo_codebuild.types.percentage.Percentage"
    ]
    """<p>The maximum line coverage percentage to report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCodeCoveragesInput) -> dict:
    out: dict = {}
    out["reportArn"] = value["report_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "sort_by" in value:
        import capo_codebuild.types.report_code_coverage_sort_by_type

        out["sortBy"] = (
            capo_codebuild.types.report_code_coverage_sort_by_type.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "min_line_coverage_percentage" in value:
        out["minLineCoveragePercentage"] = (
            "NaN"
            if value["min_line_coverage_percentage"]
            != value["min_line_coverage_percentage"]
            else "Infinity"
            if value["min_line_coverage_percentage"] == float("inf")
            else "-Infinity"
            if value["min_line_coverage_percentage"] == float("-inf")
            else value["min_line_coverage_percentage"]
        )
    if "max_line_coverage_percentage" in value:
        out["maxLineCoveragePercentage"] = (
            "NaN"
            if value["max_line_coverage_percentage"]
            != value["max_line_coverage_percentage"]
            else "Infinity"
            if value["max_line_coverage_percentage"] == float("inf")
            else "-Infinity"
            if value["max_line_coverage_percentage"] == float("-inf")
            else value["max_line_coverage_percentage"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCodeCoveragesInput:
    out: DescribeCodeCoveragesInput = {}  # type: ignore[typeddict-item]
    if data.get("reportArn") is not None:
        out["report_arn"] = data["reportArn"]
    else:
        out["report_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("sortOrder") is not None:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if data.get("sortBy") is not None:
        import capo_codebuild.types.report_code_coverage_sort_by_type

        out["sort_by"] = (
            capo_codebuild.types.report_code_coverage_sort_by_type.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if data.get("minLineCoveragePercentage") is not None:
        out["min_line_coverage_percentage"] = float(data["minLineCoveragePercentage"])
    if data.get("maxLineCoveragePercentage") is not None:
        out["max_line_coverage_percentage"] = float(data["maxLineCoveragePercentage"])
    return out
