"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeDeadLetterQueueRecordsResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry

AcknowledgeDeadLetterQueueRecordsResultEntryList: TypeAlias = list[
    "capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry.AcknowledgeDeadLetterQueueRecordsResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcknowledgeDeadLetterQueueRecordsResultEntryList,
) -> list:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AcknowledgeDeadLetterQueueRecordsResultEntryList:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry

    out: AcknowledgeDeadLetterQueueRecordsResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
