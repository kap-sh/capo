"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#StopQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.query_id


class StopQueryRequest(TypedDict, closed=True):
    query_id: "capo_cloudwatch_logs.types.query_id.QueryId"
    """<p>The ID number of the query to stop. To find this ID number, use <code>DescribeQueries</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopQueryRequest) -> dict:
    out: dict = {}
    out["queryId"] = value["query_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopQueryRequest:
    out: StopQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    else:
        out["query_id"] = ""
    return out
