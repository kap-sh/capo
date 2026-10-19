"""Generated from Smithy shape ``com.amazonaws.sqs#ChangeMessageVisibilityBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.change_message_visibility_batch_request_entry_list
    import capo_sqs.types.string


class ChangeMessageVisibilityBatchRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue whose messages' visibility is changed.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    entries: "capo_sqs.types.change_message_visibility_batch_request_entry_list.ChangeMessageVisibilityBatchRequestEntryList"
    """<p>Lists the receipt handles of the messages for which the visibility timeout must be changed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChangeMessageVisibilityBatchRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import capo_sqs.types.change_message_visibility_batch_request_entry_list

    out["Entries"] = (
        capo_sqs.types.change_message_visibility_batch_request_entry_list.serialize_aws_json_1_0(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ChangeMessageVisibilityBatchRequest:
    out: ChangeMessageVisibilityBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("Entries") is not None:
        import capo_sqs.types.change_message_visibility_batch_request_entry_list

        out["entries"] = (
            capo_sqs.types.change_message_visibility_batch_request_entry_list.deserialize_aws_json_1_0(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
