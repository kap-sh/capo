"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateDeadLetterQueueRecordsVisibilityResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry

UpdateDeadLetterQueueRecordsVisibilityResultEntryList: TypeAlias = list[
    "capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry.UpdateDeadLetterQueueRecordsVisibilityResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateDeadLetterQueueRecordsVisibilityResultEntryList,
) -> list:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> UpdateDeadLetterQueueRecordsVisibilityResultEntryList:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry

    out: UpdateDeadLetterQueueRecordsVisibilityResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.update_dead_letter_queue_records_visibility_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
