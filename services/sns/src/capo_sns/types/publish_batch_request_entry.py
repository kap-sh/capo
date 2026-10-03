"""Generated from Smithy shape ``com.amazonaws.sns#PublishBatchRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.message
    import capo_sns.types.message_attribute_map
    import capo_sns.types.message_structure
    import capo_sns.types.string
    import capo_sns.types.subject


class PublishBatchRequestEntry(TypedDict, closed=True):
    id: "capo_sns.types.string.String"
    """<p>An identifier for the message in this batch.</p> <note> <p>The <code>Ids</code> of a batch request must be unique within a request. </p> <p>This identifier can have up to 80 characters. The following characters are accepted: alphanumeric characters, hyphens(-), and underscores (_). </p> </note>"""
    message: "capo_sns.types.message.message"
    """<p>The body of the message.</p>"""
    subject: NotRequired["capo_sns.types.subject.subject"]
    """<p>The subject of the batch message.</p>"""
    message_structure: NotRequired["capo_sns.types.message_structure.messageStructure"]
    """<p>Set <code>MessageStructure</code> to <code>json</code> if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set <code>MessageStructure</code> to <code>json</code>, the value of the <code>Message</code> parameter must: </p> <ul> <li> <p>be a syntactically valid JSON object; and</p> </li> <li> <p>contain at least a top-level JSON key of "default" with a value that is a string.</p> </li> </ul> <p>You can define other top-level keys that define the message you want to send to a specific transport protocol (for example, http). </p>"""
    message_attributes: NotRequired[
        "capo_sns.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>Each message attribute consists of a <code>Name</code>, <code>Type</code>, and <code>Value</code>. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-message-attributes.html">Amazon SNS message attributes</a> in the Amazon SNS Developer Guide.</p>"""
    message_deduplication_id: NotRequired["capo_sns.types.string.String"]
    r"""<p>This parameter applies only to FIFO (first-in-first-out) topics.</p> <ul> <li> <p>This parameter applies only to FIFO (first-in-first-out) topics. The <code>MessageDeduplicationId</code> can contain up to 128 alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>, which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.</p> </li> <li> <p>The scope of deduplication depends on the <code>FifoThroughputScope</code> attribute, when set to <code>Topic</code> the message deduplication scope is across the entire topic, when set to <code>MessageGroup</code> the message deduplication scope is within each individual message group. </p> </li> <li> <p>If a message with a particular <code>MessageDeduplicationId</code> is sent successfully, subsequent messages within the deduplication scope and interval, with the same <code>MessageDeduplicationId</code>, are accepted successfully but aren't delivered.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>.</p> <ul> <li> <p>You may provide a <code>MessageDeduplicationId</code> explicitly.</p> </li> <li> <p>If you aren't able to provide a <code>MessageDeduplicationId</code> and you enable <code>ContentBasedDeduplication</code> for your topic, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> </li> <li> <p>If you don't provide a <code>MessageDeduplicationId</code> and the topic doesn't have <code>ContentBasedDeduplication</code> set, the action fails with an error.</p> </li> <li> <p>If the topic has a <code>ContentBasedDeduplication</code> set, your <code>MessageDeduplicationId</code> overrides the generated one. </p> </li> </ul> </li> <li> <p>When <code>ContentBasedDeduplication</code> is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.</p> </li> <li> <p>If you send one message with <code>ContentBasedDeduplication</code> enabled, and then another message with a <code>MessageDeduplicationId</code> that is the same as the one generated for the first <code>MessageDeduplicationId</code>, the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered. </p> </li> </ul> <note> <p>The <code>MessageDeduplicationId</code> is available to the consumer of the message (this can be useful for troubleshooting delivery issues).</p> <p>If a message is sent successfully but the acknowledgement is lost and the message is resent with the same <code>MessageDeduplicationId</code> after the deduplication interval, Amazon SNS can't detect duplicate messages. </p> <p>Amazon SNS continues to keep track of the message deduplication ID even after the message is received and deleted. </p> </note>"""
    message_group_id: NotRequired["capo_sns.types.string.String"]
    r"""<p>FIFO topics: The tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). To interleave multiple ordered streams within a single topic, use <code>MessageGroupId</code> values (for example, session data for multiple users). In this scenario, multiple consumers can process the topic, but the session data of each user is processed in a FIFO fashion. You must associate a non-empty <code>MessageGroupId</code> with a message. If you do not provide a <code>MessageGroupId</code>, the action fails. </p> <p>Standard topics: The <code>MessageGroupId</code> is optional and is forwarded only to Amazon SQS standard subscriptions to activate <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html">fair queues</a>. The <code>MessageGroupId</code> is not used for, or sent to, any other endpoint types.</p> <p>The length of <code>MessageGroupId</code> is 128 characters.</p> <p> <code>MessageGroupId</code> can contain alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishBatchRequestEntry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Id", str(value["id"])))
    pairs.append((f"{key_prefix}Message", str(value["message"])))
    if "subject" in value:
        pairs.append((f"{key_prefix}Subject", str(value["subject"])))
    if "message_structure" in value:
        pairs.append((f"{key_prefix}MessageStructure", str(value["message_structure"])))
    if "message_attributes" in value:
        import capo_sns.types.message_attribute_map

        capo_sns.types.message_attribute_map.serialize_query(
            value["message_attributes"], pairs, f"{key_prefix}MessageAttributes"
        )
    if "message_deduplication_id" in value:
        pairs.append(
            (
                f"{key_prefix}MessageDeduplicationId",
                str(value["message_deduplication_id"]),
            )
        )
    if "message_group_id" in value:
        pairs.append((f"{key_prefix}MessageGroupId", str(value["message_group_id"])))


def deserialize_query(el: Element) -> PublishBatchRequestEntry:
    out: PublishBatchRequestEntry = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("PublishBatchRequestEntry.id required")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("PublishBatchRequestEntry.message required")
    child_subject = el.find("Subject")
    if child_subject is not None:
        out["subject"] = str(child_subject.text or "")
    child_message_structure = el.find("MessageStructure")
    if child_message_structure is not None:
        out["message_structure"] = str(child_message_structure.text or "")
    child_message_attributes = el.find("MessageAttributes")
    if child_message_attributes is not None:
        import capo_sns.types.message_attribute_map

        out["message_attributes"] = (
            capo_sns.types.message_attribute_map.deserialize_query(
                child_message_attributes
            )
        )
    child_message_deduplication_id = el.find("MessageDeduplicationId")
    if child_message_deduplication_id is not None:
        out["message_deduplication_id"] = str(child_message_deduplication_id.text or "")
    child_message_group_id = el.find("MessageGroupId")
    if child_message_group_id is not None:
        out["message_group_id"] = str(child_message_group_id.text or "")
    return out
