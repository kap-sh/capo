"""Generated from Smithy shape ``com.amazonaws.kinesis#ReceiveDeadLetterQueueRecordsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn
    import capo_kinesis.types.receive_queue_records_input_limit
    import capo_kinesis.types.receive_queue_records_wait_time_seconds
    import capo_kinesis.types.visibility_timeout_seconds


class ReceiveDeadLetterQueueRecordsInput(TypedDict, closed=True):
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue whose dead-letter records are received.</p>"""
    limit: NotRequired[
        "capo_kinesis.types.receive_queue_records_input_limit.ReceiveQueueRecordsInputLimit"
    ]
    """<p>The maximum number of records to return. The queue never returns more dead-letter records than this value, and might return fewer. The default is 10.</p>"""
    wait_time_seconds: NotRequired[
        "capo_kinesis.types.receive_queue_records_wait_time_seconds.ReceiveQueueRecordsWaitTimeSeconds"
    ]
    """<p>The duration, in seconds, that the call waits for a record to become visible before returning. The default is 9.</p>"""
    visibility_timeout_seconds: NotRequired[
        "capo_kinesis.types.visibility_timeout_seconds.VisibilityTimeoutSeconds"
    ]
    """<p>The duration, in seconds, that the records returned by this request are in flight and not visible to any consumer instance. If you do not specify this value, the queue's visibility timeout is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceiveDeadLetterQueueRecordsInput) -> dict:
    out: dict = {}
    out["QueueARN"] = value["queue_arn"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "wait_time_seconds" in value:
        out["WaitTimeSeconds"] = value["wait_time_seconds"]
    if "visibility_timeout_seconds" in value:
        out["VisibilityTimeoutSeconds"] = value["visibility_timeout_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReceiveDeadLetterQueueRecordsInput:
    out: ReceiveDeadLetterQueueRecordsInput = {}  # type: ignore[typeddict-item]
    if data.get("QueueARN") is not None:
        out["queue_arn"] = data["QueueARN"]
    else:
        out["queue_arn"] = ""
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("WaitTimeSeconds") is not None:
        out["wait_time_seconds"] = data["WaitTimeSeconds"]
    if data.get("VisibilityTimeoutSeconds") is not None:
        out["visibility_timeout_seconds"] = data["VisibilityTimeoutSeconds"]
    return out
