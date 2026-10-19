"""Generated from Smithy shape ``com.amazonaws.sfn#GetExecutionHistoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.include_execution_data_get_execution_history
    import capo_sfn.types.page_size
    import capo_sfn.types.page_token
    import capo_sfn.types.reverse_order


class GetExecutionHistoryInput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution.</p>"""
    max_results: NotRequired["capo_sfn.types.page_size.PageSize"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>"""
    reverse_order: NotRequired["capo_sfn.types.reverse_order.ReverseOrder"]
    """<p>Lists events in descending order of their <code>timeStamp</code>.</p>"""
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""
    include_execution_data: NotRequired[
        "capo_sfn.types.include_execution_data_get_execution_history.IncludeExecutionDataGetExecutionHistory"
    ]
    """<p>You can select whether execution data (input or output of a history event) is returned. The default is <code>true</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetExecutionHistoryInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "reverse_order" in value:
        out["reverseOrder"] = value["reverse_order"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "include_execution_data" in value:
        out["includeExecutionData"] = value["include_execution_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetExecutionHistoryInput:
    out: GetExecutionHistoryInput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        out["execution_arn"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("reverseOrder") is not None:
        out["reverse_order"] = data["reverseOrder"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("includeExecutionData") is not None:
        out["include_execution_data"] = data["includeExecutionData"]
    return out
