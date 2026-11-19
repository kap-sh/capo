"""Generated from Smithy shape ``com.amazonaws.kinesis#RestoreDeadLetterQueueRecordsErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.restore_dead_letter_queue_records_error_entry

RestoreDeadLetterQueueRecordsErrorEntryList: TypeAlias = list[
    "capo_kinesis.types.restore_dead_letter_queue_records_error_entry.RestoreDeadLetterQueueRecordsErrorEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreDeadLetterQueueRecordsErrorEntryList) -> list:
    import capo_kinesis.types.restore_dead_letter_queue_records_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.restore_dead_letter_queue_records_error_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RestoreDeadLetterQueueRecordsErrorEntryList:
    import capo_kinesis.types.restore_dead_letter_queue_records_error_entry

    out: RestoreDeadLetterQueueRecordsErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.restore_dead_letter_queue_records_error_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
