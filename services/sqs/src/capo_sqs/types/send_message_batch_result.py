"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageBatchResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.batch_result_error_entry_list
    import capo_sqs.types.send_message_batch_result_entry_list


class SendMessageBatchResult(TypedDict, closed=True):
    successful: "capo_sqs.types.send_message_batch_result_entry_list.SendMessageBatchResultEntryList"
    """<p>A list of <code> <a>SendMessageBatchResultEntry</a> </code> items.</p>"""
    failed: "capo_sqs.types.batch_result_error_entry_list.BatchResultErrorEntryList"
    """<p>A list of <code> <a>BatchResultErrorEntry</a> </code> items with error details about each message that can't be enqueued.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageBatchResult) -> dict:
    out: dict = {}
    import capo_sqs.types.send_message_batch_result_entry_list

    out["Successful"] = (
        capo_sqs.types.send_message_batch_result_entry_list.serialize_aws_json_1_0(
            value["successful"]
        )
    )
    import capo_sqs.types.batch_result_error_entry_list

    out["Failed"] = capo_sqs.types.batch_result_error_entry_list.serialize_aws_json_1_0(
        value["failed"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SendMessageBatchResult:
    out: SendMessageBatchResult = {}  # type: ignore[typeddict-item]
    if data.get("Successful") is not None:
        import capo_sqs.types.send_message_batch_result_entry_list

        out["successful"] = (
            capo_sqs.types.send_message_batch_result_entry_list.deserialize_aws_json_1_0(
                data["Successful"]
            )
        )
    else:
        out["successful"] = []
    if data.get("Failed") is not None:
        import capo_sqs.types.batch_result_error_entry_list

        out["failed"] = (
            capo_sqs.types.batch_result_error_entry_list.deserialize_aws_json_1_0(
                data["Failed"]
            )
        )
    else:
        out["failed"] = []
    return out
