"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeQueueRecordsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_queue_records_request_entry

AcknowledgeQueueRecordsRequestEntryList: TypeAlias = list[
    "capo_kinesis.types.acknowledge_queue_records_request_entry.AcknowledgeQueueRecordsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeQueueRecordsRequestEntryList) -> list:
    import capo_kinesis.types.acknowledge_queue_records_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.acknowledge_queue_records_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcknowledgeQueueRecordsRequestEntryList:
    import capo_kinesis.types.acknowledge_queue_records_request_entry

    out: AcknowledgeQueueRecordsRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.acknowledge_queue_records_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
