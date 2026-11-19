"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeDeadLetterQueueRecordsRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry

AcknowledgeDeadLetterQueueRecordsRequestEntryList: TypeAlias = list[
    "capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry.AcknowledgeDeadLetterQueueRecordsRequestEntry"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AcknowledgeDeadLetterQueueRecordsRequestEntryList,
) -> list:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry

    out: list = []
    for item in value:
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> AcknowledgeDeadLetterQueueRecordsRequestEntryList:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry

    out: AcknowledgeDeadLetterQueueRecordsRequestEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kinesis.types.acknowledge_dead_letter_queue_records_request_entry.deserialize_aws_json_1_1(
                item
            )
        )
    return out
