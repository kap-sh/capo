"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteQueryDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.query_id


class DeleteQueryDefinitionRequest(TypedDict, closed=True):
    query_definition_id: "capo_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID of the query definition that you want to delete. You can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html">DescribeQueryDefinitions</a> to retrieve the IDs of your saved query definitions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteQueryDefinitionRequest) -> dict:
    out: dict = {}
    out["queryDefinitionId"] = value["query_definition_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteQueryDefinitionRequest:
    out: DeleteQueryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryDefinitionId") is not None:
        out["query_definition_id"] = data["queryDefinitionId"]
    else:
        out["query_definition_id"] = ""
    return out
