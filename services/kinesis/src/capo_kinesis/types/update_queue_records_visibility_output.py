"""Generated from Smithy shape ``com.amazonaws.kinesis#UpdateQueueRecordsVisibilityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.update_queue_records_visibility_error_entry_list
    import capo_kinesis.types.update_queue_records_visibility_result_entry_list


class UpdateQueueRecordsVisibilityOutput(TypedDict, closed=True):
    successful: "capo_kinesis.types.update_queue_records_visibility_result_entry_list.UpdateQueueRecordsVisibilityResultEntryList"
    """<p>The records whose visibility timeout was changed.</p>"""
    failed: "capo_kinesis.types.update_queue_records_visibility_error_entry_list.UpdateQueueRecordsVisibilityErrorEntryList"
    """<p>The records whose visibility timeout was not changed, each with the reason the entry failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQueueRecordsVisibilityOutput) -> dict:
    out: dict = {}
    import capo_kinesis.types.update_queue_records_visibility_result_entry_list

    out["Successful"] = (
        capo_kinesis.types.update_queue_records_visibility_result_entry_list.serialize_aws_json_1_1(
            value["successful"]
        )
    )
    import capo_kinesis.types.update_queue_records_visibility_error_entry_list

    out["Failed"] = (
        capo_kinesis.types.update_queue_records_visibility_error_entry_list.serialize_aws_json_1_1(
            value["failed"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQueueRecordsVisibilityOutput:
    out: UpdateQueueRecordsVisibilityOutput = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_kinesis.types.update_queue_records_visibility_result_entry_list

        out["successful"] = (
            capo_kinesis.types.update_queue_records_visibility_result_entry_list.deserialize_aws_json_1_1(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_kinesis.types.update_queue_records_visibility_error_entry_list

        out["failed"] = (
            capo_kinesis.types.update_queue_records_visibility_error_entry_list.deserialize_aws_json_1_1(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
