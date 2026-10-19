"""Generated from Smithy shape ``com.amazonaws.sqs#ListDeadLetterSourceQueuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.boxed_integer
    import capo_sqs.types.string
    import capo_sqs.types.token


class ListDeadLetterSourceQueuesRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of a dead-letter queue.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    next_token: NotRequired["capo_sqs.types.token.Token"]
    """<p>Pagination token to request the next set of results.</p>"""
    max_results: NotRequired["capo_sqs.types.boxed_integer.BoxedInteger"]
    """<p>Maximum number of results to include in the response. Value range is 1 to 1000. You must set <code>MaxResults</code> to receive a value for <code>NextToken</code> in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDeadLetterSourceQueuesRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDeadLetterSourceQueuesRequest:
    out: ListDeadLetterSourceQueuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
