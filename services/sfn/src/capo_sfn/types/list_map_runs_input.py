"""Generated from Smithy shape ``com.amazonaws.sfn#ListMapRunsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.page_size
    import capo_sfn.types.page_token


class ListMapRunsInput(TypedDict, closed=True):
    execution_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the execution for which the Map Runs must be listed.</p>"""
    max_results: NotRequired["capo_sfn.types.page_size.PageSize"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>"""
    next_token: NotRequired["capo_sfn.types.page_token.PageToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken</i> error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListMapRunsInput) -> dict:
    out: dict = {}
    out["executionArn"] = value["execution_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListMapRunsInput:
    out: ListMapRunsInput = {}  # type: ignore[typeddict-item]
    if data.get("executionArn") is not None:
        out["execution_arn"] = data["executionArn"]
    else:
        raise DeserializationError("ListMapRunsInput.execution_arn required")
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
