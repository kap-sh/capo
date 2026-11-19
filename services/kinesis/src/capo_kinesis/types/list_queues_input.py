"""Generated from Smithy shape ``com.amazonaws.kinesis#ListQueuesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.list_queues_input_limit
    import capo_kinesis.types.next_token
    import capo_kinesis.types.queue_stream_filter_list


class ListQueuesInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_kinesis.types.list_queues_input_limit.ListQueuesInputLimit"
    ]
    """<p>The maximum number of queue summaries to return in one response. The response might contain fewer summaries than this value, and might contain a <code>NextToken</code> even when it contains fewer.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>The <code>NextToken</code> returned by a previous <code>ListQueues</code> request. Use it to retrieve the next page of queue summaries.</p>"""
    stream_filter: NotRequired[
        "capo_kinesis.types.queue_stream_filter_list.QueueStreamFilterList"
    ]
    """<p>Lists only the queues created on the specified data stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQueuesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "stream_filter" in value:
        import capo_kinesis.types.queue_stream_filter_list

        out["StreamFilter"] = (
            capo_kinesis.types.queue_stream_filter_list.serialize_aws_json_1_1(
                value["stream_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQueuesInput:
    out: ListQueuesInput = {}  # type: ignore[typeddict-item]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("StreamFilter") is not None:
        import capo_kinesis.types.queue_stream_filter_list

        out["stream_filter"] = (
            capo_kinesis.types.queue_stream_filter_list.deserialize_aws_json_1_1(
                data["StreamFilter"]
            )
        )
    return out
