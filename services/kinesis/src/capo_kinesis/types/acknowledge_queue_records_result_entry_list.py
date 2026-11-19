"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeQueueRecordsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_queue_records_result_entry

AcknowledgeQueueRecordsResultEntryList: TypeAlias = list[
    "capo_kinesis.types.acknowledge_queue_records_result_entry.AcknowledgeQueueRecordsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeQueueRecordsResultEntryList) -> list:
    import capo_kinesis.types.acknowledge_queue_records_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.acknowledge_queue_records_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AcknowledgeQueueRecordsResultEntryList:
    import capo_kinesis.types.acknowledge_queue_records_result_entry

    out: AcknowledgeQueueRecordsResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.acknowledge_queue_records_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
