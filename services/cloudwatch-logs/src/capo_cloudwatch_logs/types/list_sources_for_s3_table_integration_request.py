"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListSourcesForS3TableIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_max_results
    import capo_cloudwatch_logs.types.next_token


class ListSourcesForS3TableIntegrationRequest(TypedDict, closed=True):
    integration_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the S3 Table Integration to list associations for.</p>"""
    max_results: NotRequired[
        "capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_max_results.ListSourcesForS3TableIntegrationMaxResults"
    ]
    """<p>The maximum number of associations to return in a single call. Valid range is 1 to 100.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSourcesForS3TableIntegrationRequest) -> dict:
    out: dict = {}
    out["integrationArn"] = value["integration_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSourcesForS3TableIntegrationRequest:
    out: ListSourcesForS3TableIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("integrationArn") is not None:
        out["integration_arn"] = data["integrationArn"]
    else:
        out["integration_arn"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
