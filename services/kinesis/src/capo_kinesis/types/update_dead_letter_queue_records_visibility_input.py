"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateDeadLetterQueueRecordsVisibilityInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.queue_arn
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list


class UpdateDeadLetterQueueRecordsVisibilityInput(TypedDict, closed=True):
    queue_arn: "capo_kinesis.types.queue_arn.QueueARN"
    """<p>The ARN of the queue whose dead-letter records are updated.</p>"""
    entries: "capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list.UpdateDeadLetterQueueRecordsVisibilityRequestEntryList"
    """<p>The dead-letter records whose visibility timeout is changed, identified by their receipt handles, and the new visibility timeout for each.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDeadLetterQueueRecordsVisibilityInput) -> dict:
    out: dict = {}
    out["QueueARN"] = value["queue_arn"]
    import capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list

    out["Entries"] = (
        capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list.serialize_aws_json_1_1(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDeadLetterQueueRecordsVisibilityInput:
    out: UpdateDeadLetterQueueRecordsVisibilityInput = {}  # type: ignore[typeddict-item]
    if data.get("QueueARN") is not None:
        out["queue_arn"] = data["QueueARN"]
    else:
        out["queue_arn"] = ""
    if data.get("Entries") is not None:
        import capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list

        out["entries"] = (
            capo_kinesis.types.update_dead_letter_queue_records_visibility_request_entry_list.deserialize_aws_json_1_1(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
