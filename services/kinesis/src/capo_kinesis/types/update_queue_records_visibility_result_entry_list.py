"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateQueueRecordsVisibilityResultEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.update_queue_records_visibility_result_entry

UpdateQueueRecordsVisibilityResultEntryList: TypeAlias = list[
    "capo_kinesis.types.update_queue_records_visibility_result_entry.UpdateQueueRecordsVisibilityResultEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQueueRecordsVisibilityResultEntryList) -> list:
    import capo_kinesis.types.update_queue_records_visibility_result_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.update_queue_records_visibility_result_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateQueueRecordsVisibilityResultEntryList:
    import capo_kinesis.types.update_queue_records_visibility_result_entry

    out: UpdateQueueRecordsVisibilityResultEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.update_queue_records_visibility_result_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
