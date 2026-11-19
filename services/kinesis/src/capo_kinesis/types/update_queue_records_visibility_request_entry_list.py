"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateQueueRecordsVisibilityRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.update_queue_records_visibility_request_entry

UpdateQueueRecordsVisibilityRequestEntryList: TypeAlias = list[
    "capo_kinesis.types.update_queue_records_visibility_request_entry.UpdateQueueRecordsVisibilityRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQueueRecordsVisibilityRequestEntryList) -> list:
    import capo_kinesis.types.update_queue_records_visibility_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.update_queue_records_visibility_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> UpdateQueueRecordsVisibilityRequestEntryList:
    import capo_kinesis.types.update_queue_records_visibility_request_entry

    out: UpdateQueueRecordsVisibilityRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.update_queue_records_visibility_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
