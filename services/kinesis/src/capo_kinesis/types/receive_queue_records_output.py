"""Generated from Smithy shape ``com.amazonaws.kinesis#ReceiveQueueRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_record_list


class ReceiveQueueRecordsOutput(TypedDict, closed=True):
    queue_records: "capo_kinesis.types.queue_record_list.QueueRecordList"
    """<p>The records received from the queue. This list is empty when no records are visible.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceiveQueueRecordsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.queue_record_list

    out["QueueRecords"] = capo_kinesis.types.queue_record_list.serialize_aws_json_1_1(
        value["queue_records"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReceiveQueueRecordsOutput:
    out: ReceiveQueueRecordsOutput = {}  # type: ignore[typeddict-item]
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
