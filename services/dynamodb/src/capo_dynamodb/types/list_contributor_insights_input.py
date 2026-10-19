"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListContributorInsightsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.list_contributor_insights_limit
    import capo_dynamodb.types.next_token_string
    import capo_dynamodb.types.table_arn


class ListContributorInsightsInput(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    next_token: NotRequired["capo_dynamodb.types.next_token_string.NextTokenString"]
    """<p>A token to for the desired page, if there is one.</p>"""
    max_results: NotRequired[
        "capo_dynamodb.types.list_contributor_insights_limit.ListContributorInsightsLimit"
    ]
    """<p>Maximum number of results to return per page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContributorInsightsInput) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContributorInsightsInput:
    out: ListContributorInsightsInput = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
