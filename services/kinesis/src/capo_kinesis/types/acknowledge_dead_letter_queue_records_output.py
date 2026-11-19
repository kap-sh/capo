"""Generated from Smithy shape ``com.amazonaws.kinesis#AcknowledgeDeadLetterQueueRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list


class AcknowledgeDeadLetterQueueRecordsOutput(TypedDict, closed=True):
    successful: "capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list.AcknowledgeDeadLetterQueueRecordsResultEntryList"
    """<p>The records that were acknowledged.</p>"""
    failed: "capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list.AcknowledgeDeadLetterQueueRecordsErrorEntryList"
    """<p>The records that were not acknowledged, each with the reason the entry failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcknowledgeDeadLetterQueueRecordsOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list

    out["Successful"] = (
        capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list.serialize_aws_json_1_1(
            value["successful"]
        )
    )
    import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list

    out["Failed"] = (
        capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list.serialize_aws_json_1_1(
            value["failed"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AcknowledgeDeadLetterQueueRecordsOutput:
    out: AcknowledgeDeadLetterQueueRecordsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list

        out["successful"] = (
            capo_kinesis.types.acknowledge_dead_letter_queue_records_result_entry_list.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list

        out["failed"] = (
            capo_kinesis.types.acknowledge_dead_letter_queue_records_error_entry_list.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
