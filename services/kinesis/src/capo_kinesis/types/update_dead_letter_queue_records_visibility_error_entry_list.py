"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateDeadLetterQueueRecordsVisibilityErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry

UpdateDeadLetterQueueRecordsVisibilityErrorEntryList: TypeAlias = list[
    "capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry.UpdateDeadLetterQueueRecordsVisibilityErrorEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateDeadLetterQueueRecordsVisibilityErrorEntryList,
) -> list:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> UpdateDeadLetterQueueRecordsVisibilityErrorEntryList:
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry

    out: UpdateDeadLetterQueueRecordsVisibilityErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.update_dead_letter_queue_records_visibility_error_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
