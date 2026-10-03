"""Generated from Smithy shape ``com.amazonaws.sqs#SendMessageBatchResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sqs.types.string


class SendMessageBatchResultEntry(TypedDict, closed=True):
    id: "capo_sqs.types.string.String"
    """<p>An identifier for the message in this batch.</p>"""
    message_id: "capo_sqs.types.string.String"
    """<p>An identifier for the message.</p>"""
    md5_of_message_body: "capo_sqs.types.string.String"
    """<p>An MD5 digest of the non-URL-encoded message body string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href="https://www.ietf.org/rfc/rfc1321.txt">RFC1321</a>.</p>"""
    md5_of_message_attributes: NotRequired["capo_sqs.types.string.String"]
    """<p>An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href="https://www.ietf.org/rfc/rfc1321.txt">RFC1321</a>.</p>"""
    md5_of_message_system_attributes: NotRequired["capo_sqs.types.string.String"]
    """<p>An MD5 digest of the non-URL-encoded message system attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href="https://www.ietf.org/rfc/rfc1321.txt">RFC1321</a>.</p>"""
    sequence_number: NotRequired["capo_sqs.types.string.String"]
    """<p>This parameter applies only to FIFO (first-in-first-out) queues.</p> <p>The large, non-consecutive number that Amazon SQS assigns to each message.</p> <p>The length of <code>SequenceNumber</code> is 128 bits. As <code>SequenceNumber</code> continues to increase for a particular <code>MessageGroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendMessageBatchResultEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["MessageId"] = value["message_id"]
    out["MD5OfMessageBody"] = value["md5_of_message_body"]
    if "md5_of_message_attributes" in value:
        out["MD5OfMessageAttributes"] = value["md5_of_message_attributes"]
    if "md5_of_message_system_attributes" in value:
        out["MD5OfMessageSystemAttributes"] = value["md5_of_message_system_attributes"]
    if "sequence_number" in value:
        out["SequenceNumber"] = value["sequence_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendMessageBatchResultEntry:
    out: SendMessageBatchResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("SendMessageBatchResultEntry.id required")
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    else:
        raise DeserializationError("SendMessageBatchResultEntry.message_id required")
    if data.get("MD5OfMessageBody") is not None:
        out["md5_of_message_body"] = data["MD5OfMessageBody"]
    else:
        raise DeserializationError(
            "SendMessageBatchResultEntry.md5_of_message_body required"
        )
    if data.get("MD5OfMessageAttributes") is not None:
        out["md5_of_message_attributes"] = data["MD5OfMessageAttributes"]
    if data.get("MD5OfMessageSystemAttributes") is not None:
        out["md5_of_message_system_attributes"] = data["MD5OfMessageSystemAttributes"]
    if data.get("SequenceNumber") is not None:
        out["sequence_number"] = data["SequenceNumber"]
    return out
