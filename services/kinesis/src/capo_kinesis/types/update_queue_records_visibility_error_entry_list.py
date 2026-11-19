"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateQueueRecordsVisibilityErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.update_queue_records_visibility_error_entry

UpdateQueueRecordsVisibilityErrorEntryList: TypeAlias = list[
    "capo_kinesis.types.update_queue_records_visibility_error_entry.UpdateQueueRecordsVisibilityErrorEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQueueRecordsVisibilityErrorEntryList) -> list:
    import capo_kinesis.types.update_queue_records_visibility_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.update_queue_records_visibility_error_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateQueueRecordsVisibilityErrorEntryList:
    import capo_kinesis.types.update_queue_records_visibility_error_entry

    out: UpdateQueueRecordsVisibilityErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.update_queue_records_visibility_error_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
