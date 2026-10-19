"""Generated from Smithy shape ``com.amazonaws.sqs#ListDeadLetterSourceQueuesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.queue_url_list
    import capo_sqs.types.token


class ListDeadLetterSourceQueuesResult(TypedDict, closed=True):
    queue_urls: "capo_sqs.types.queue_url_list.QueueUrlList"
    """<p>A list of source queue URLs that have the <code>RedrivePolicy</code> queue attribute configured with a dead-letter queue.</p>"""
    next_token: NotRequired["capo_sqs.types.token.Token"]
    """<p>Pagination token to include in the next request. Token value is <code>null</code> if there are no additional results to request, or if you did not set <code>MaxResults</code> in the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDeadLetterSourceQueuesResult) -> dict:
    out: dict = {}
    import capo_sqs.types.queue_url_list

    out["queueUrls"] = capo_sqs.types.queue_url_list.serialize_aws_json_1_0(
        value["queue_urls"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDeadLetterSourceQueuesResult:
    out: ListDeadLetterSourceQueuesResult = {}  # type: ignore[typeddict-item]
    if data.get("queueUrls") is not None:
        import capo_sqs.types.queue_url_list

        out["queue_urls"] = capo_sqs.types.queue_url_list.deserialize_aws_json_1_0(
            data["queueUrls"]
        )
    else:
        out["queue_urls"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
