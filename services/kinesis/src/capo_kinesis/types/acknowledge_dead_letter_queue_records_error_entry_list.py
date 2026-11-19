"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeDeadLetterQueueRecordsErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry

AcknowledgeDeadLetterQueueRecordsErrorEntryList: TypeAlias = list[
    "capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry.AcknowledgeDeadLetterQueueRecordsErrorEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcknowledgeDeadLetterQueueRecordsErrorEntryList,
) -> list:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AcknowledgeDeadLetterQueueRecordsErrorEntryList:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry

    out: AcknowledgeDeadLetterQueueRecordsErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
