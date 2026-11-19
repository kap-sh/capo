"""Generated from Smithy shape ``com.amazonaws.kinesis#ReceiveDeadLetterQueueRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_record_list


class ReceiveDeadLetterQueueRecordsOutput(TypedDict, closed=True):
    queue_records: "capo_kinesis.types.queue_record_list.QueueRecordList"
    """<p>The dead-letter records received from the queue. This list is empty when no dead-letter records are visible.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceiveDeadLetterQueueRecordsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.queue_record_list

    out["QueueRecords"] = capo_kinesis.types.queue_record_list.serialize_aws_json_1_1(
        value["queue_records"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReceiveDeadLetterQueueRecordsOutput:
    out: ReceiveDeadLetterQueueRecordsOutput = {}  # type: ignore[typeddict-item]
    if data.get("QueueRecords") is not None:
        import capo_kinesis.types.queue_record_list

        out["queue_records"] = (
            capo_kinesis.types.queue_record_list.deserialize_aws_json_1_1(
                data["QueueRecords"]
            )
        )
    else:
        out["queue_records"] = []
    return out
