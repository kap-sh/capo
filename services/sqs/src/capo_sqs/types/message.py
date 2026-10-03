"""Generated from Smithy shape ``com.amazonaws.sqs#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.message_body_attribute_map
    import capo_sqs.types.message_system_attribute_map
    import capo_sqs.types.string


class Message(TypedDict, closed=True):
    message_id: NotRequired["capo_sqs.types.string.String"]
    """<p>A unique identifier for the message. A <code>MessageId</code>is considered unique across all Amazon Web Services accounts for an extended period of time.</p>"""
    receipt_handle: NotRequired["capo_sqs.types.string.String"]
    """<p>An identifier associated with the act of receiving the message. A new receipt handle is returned every time you receive a message. When deleting a message, you provide the last received receipt handle to delete the message.</p>"""
    md5_of_body: NotRequired["capo_sqs.types.string.String"]
    """<p>An MD5 digest of the non-URL-encoded message body string.</p>"""
    body: NotRequired["capo_sqs.types.string.String"]
    """<p>The message's contents (not URL-encoded).</p>"""
    attributes: NotRequired[
        "capo_sqs.types.message_system_attribute_map.MessageSystemAttributeMap"
    ]
    """<p>A map of the attributes requested in <code> <a>ReceiveMessage</a> </code> to their respective values. Supported attributes:</p> <ul> <li> <p> <code>ApproximateReceiveCount</code> </p> </li> <li> <p> <code>ApproximateFirstReceiveTimestamp</code> </p> </li> <li> <p> <code>MessageDeduplicationId</code> </p> </li> <li> <p> <code>MessageGroupId</code> </p> </li> <li> <p> <code>SenderId</code> </p> </li> <li> <p> <code>SentTimestamp</code> </p> </li> <li> <p> <code>SequenceNumber</code> </p> </li> </ul> <p> <code>ApproximateFirstReceiveTimestamp</code> and <code>SentTimestamp</code> are each returned as an integer representing the <a href="http://en.wikipedia.org/wiki/Unix_time">epoch time</a> in milliseconds.</p>"""
    md5_of_message_attributes: NotRequired["capo_sqs.types.string.String"]
    """<p>An MD5 digest of the non-URL-encoded message attribute string. You can use this attribute to verify that Amazon SQS received the message correctly. Amazon SQS URL-decodes the message before creating the MD5 digest. For information about MD5, see <a href="https://www.ietf.org/rfc/rfc1321.txt">RFC1321</a>.</p>"""
    message_attributes: NotRequired[
        "capo_sqs.types.message_body_attribute_map.MessageBodyAttributeMap"
    ]
    """<p>Each message attribute consists of a <code>Name</code>, <code>Type</code>, and <code>Value</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes">Amazon SQS message attributes</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Message) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "receipt_handle" in value:
        out["ReceiptHandle"] = value["receipt_handle"]
    if "md5_of_body" in value:
        out["MD5OfBody"] = value["md5_of_body"]
    if "body" in value:
        out["Body"] = value["body"]
    if "attributes" in value:
        import capo_sqs.types.message_system_attribute_map

        out["Attributes"] = (
            capo_sqs.types.message_system_attribute_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "md5_of_message_attributes" in value:
        out["MD5OfMessageAttributes"] = value["md5_of_message_attributes"]
    if "message_attributes" in value:
        import capo_sqs.types.message_body_attribute_map

        out["MessageAttributes"] = (
            capo_sqs.types.message_body_attribute_map.serialize_aws_json_1_0(
                value["message_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    if data.get("ReceiptHandle") is not None:
        out["receipt_handle"] = data["ReceiptHandle"]
    if data.get("MD5OfBody") is not None:
        out["md5_of_body"] = data["MD5OfBody"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("Attributes") is not None:
        import capo_sqs.types.message_system_attribute_map

        out["attributes"] = (
            capo_sqs.types.message_system_attribute_map.deserialize_aws_json_1_0(
                data["Attributes"]
            )
        )
    if data.get("MD5OfMessageAttributes") is not None:
        out["md5_of_message_attributes"] = data["MD5OfMessageAttributes"]
    if data.get("MessageAttributes") is not None:
        import capo_sqs.types.message_body_attribute_map

        out["message_attributes"] = (
            capo_sqs.types.message_body_attribute_map.deserialize_aws_json_1_0(
                data["MessageAttributes"]
            )
        )
    return out
