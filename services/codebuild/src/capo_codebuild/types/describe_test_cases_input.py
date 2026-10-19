"""Generated from Smithy shape ``com.amazonaws.codebuild#DescribeTestCasesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.page_size
    import capo_codebuild.types.string
    import capo_codebuild.types.test_case_filter


class DescribeTestCasesInput(TypedDict, closed=True):
    report_arn: "capo_codebuild.types.string.String"
    """<p> The ARN of the report for which test cases are returned. </p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p> During a previous call, the maximum number of items that can be returned is the value specified in <code>maxResults</code>. If there more items in the list, then a unique string called a <i>nextToken</i> is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned. </p>"""
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p> The maximum number of paginated test cases returned per response. Use <code>nextToken</code> to iterate pages in the list of returned <code>TestCase</code> objects. The default value is 100. </p>"""
    filter: NotRequired["capo_codebuild.types.test_case_filter.TestCaseFilter"]
    """<p> A <code>TestCaseFilter</code> object used to filter the returned reports. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTestCasesInput) -> dict:
    out: dict = {}
    out["reportArn"] = value["report_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_codebuild.types.test_case_filter

        out["filter"] = capo_codebuild.types.test_case_filter.serialize_aws_json_1_1(
            value["filter"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTestCasesInput:
    out: DescribeTestCasesInput = {}  # type: ignore[typeddict-item]
    if data.get("reportArn") is not None:
        out["report_arn"] = data["reportArn"]
    else:
        out["report_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_codebuild.types.test_case_filter

        out["filter"] = capo_codebuild.types.test_case_filter.deserialize_aws_json_1_1(
            data["filter"]
        )
    return out
