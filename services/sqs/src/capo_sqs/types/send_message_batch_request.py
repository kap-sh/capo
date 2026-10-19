"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.send_message_batch_request_entry_list
    import capo_sqs.types.string


class SendMessageBatchRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue to which batched messages are sent.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    entries: "capo_sqs.types.send_message_batch_request_entry_list.SendMessageBatchRequestEntryList"
    """<p>A list of <code> <a>SendMessageBatchRequestEntry</a> </code> items.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageBatchRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    import capo_sqs.types.send_message_batch_request_entry_list

    out["Entries"] = (
        capo_sqs.types.send_message_batch_request_entry_list.serialize_aws_json_1_0(
            value["entries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> SendMessageBatchRequest:
    out: SendMessageBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        out["queue_url"] = ""
    if data.get("Entries") is not None:
        import capo_sqs.types.send_message_batch_request_entry_list

        out["entries"] = (
            capo_sqs.types.send_message_batch_request_entry_list.deserialize_aws_json_1_0(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    return out
