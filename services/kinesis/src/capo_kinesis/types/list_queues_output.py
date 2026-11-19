"""Generated from Smithy shape ``com.amazonaws.kinesis#ListQueuesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.next_token
    import capo_kinesis.types.queue_summary_list


class ListQueuesOutput(TypedDict, closed=True):
    queue_summaries: "capo_kinesis.types.queue_summary_list.QueueSummaryList"
    """<p>A summary of each queue that matched the request.</p>"""
    next_token: NotRequired["capo_kinesis.types.next_token.NextToken"]
    """<p>The token to pass to the next <code>ListQueues</code> request to retrieve the next page of queue summaries. This member is absent when no more queues are available.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQueuesOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.queue_summary_list

    out["QueueSummaries"] = (
        capo_kinesis.types.queue_summary_list.serialize_aws_json_1_1(
            value["queue_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQueuesOutput:
    out: ListQueuesOutput = {}  # type: ignore[typeddict-item]
    if data.get("QueueSummaries") is not None:
        import capo_kinesis.types.queue_summary_list

        out["queue_summaries"] = (
            capo_kinesis.types.queue_summary_list.deserialize_aws_json_1_1(
                data["QueueSummaries"]
            )
        )
    else:
        out["queue_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
