"""Generated from Smithy shape ``com.amazonaws.sns#PublishInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.message
    import capo_sns.types.message_attribute_map
    import capo_sns.types.message_structure
    import capo_sns.types.phone_number
    import capo_sns.types.string
    import capo_sns.types.subject
    import capo_sns.types.topic_arn


class PublishInput(TypedDict, closed=True):
    topic_arn: NotRequired["capo_sns.types.topic_arn.topicARN"]
    """<p>The topic you want to publish to.</p> <p>If you don't specify a value for the <code>TopicArn</code> parameter, you must specify a value for the <code>PhoneNumber</code> or <code>TargetArn</code> parameters.</p>"""
    target_arn: NotRequired["capo_sns.types.string.String"]
    """<p>If you don't specify a value for the <code>TargetArn</code> parameter, you must specify a value for the <code>PhoneNumber</code> or <code>TopicArn</code> parameters.</p>"""
    phone_number: NotRequired["capo_sns.types.phone_number.PhoneNumber"]
    """<p>The phone number to which you want to deliver an SMS message. Use E.164 format.</p> <p>If you don't specify a value for the <code>PhoneNumber</code> parameter, you must specify a value for the <code>TargetArn</code> or <code>TopicArn</code> parameters.</p>"""
    message: "capo_sns.types.message.message"
    """<p>The message you want to send.</p> <p>If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the <code>MessageStructure</code> parameter to <code>json</code> and use a JSON object for the <code>Message</code> parameter. </p> <p></p> <p>Constraints:</p> <ul> <li> <p>With the exception of SMS, messages must be UTF-8 encoded strings. By default, a message can be at most 256 KiB in size (262,144 bytes, not 262,144 characters).</p> <p>When you publish to a topic, the maximum size is determined by the topic's <code>MaximumMessageSize</code> attribute, which supports values up to 1 MiB (1,048,576 bytes). Amazon SNS validates the combined size of the message body and message attributes against this value and returns an <code>InvalidParameter</code> error if the limit is exceeded.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html">Large message payloads</a> in the <i>Amazon SNS Developer Guide.</i> </p> </li> <li> <p>For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters.</p> <p>If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages aren't truncated mid-word but are cut off at whole-word boundaries.</p> <p>The total size limit for a single SMS <code>Publish</code> action is 1,600 characters.</p> </li> </ul> <p>JSON-specific constraints:</p> <ul> <li> <p>Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.</p> </li> <li> <p>The values will be parsed (unescaped) before they are used in outgoing messages.</p> </li> <li> <p>Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).</p> </li> <li> <p>Values have a minimum length of 0 (the empty string, "", is allowed).</p> </li> <li> <p>Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).</p> </li> <li> <p>Non-string values will cause the key to be ignored.</p> </li> <li> <p>Keys that do not correspond to supported transport protocols are ignored.</p> </li> <li> <p>Duplicate keys are not allowed.</p> </li> <li> <p>Failure to parse or validate any key or value in the message will cause the <code>Publish</code> call to return an error (no partial delivery).</p> </li> </ul>"""
    subject: NotRequired["capo_sns.types.subject.subject"]
    """<p>Optional parameter to be used as the "Subject" line when the message is delivered to email endpoints. This field will also be included, if present, in the standard JSON messages delivered to other endpoints.</p> <p>Constraints: Subjects must be UTF-8 text with no line breaks or control characters, and less than 100 characters long.</p>"""
    message_structure: NotRequired["capo_sns.types.message_structure.messageStructure"]
    """<p>Set <code>MessageStructure</code> to <code>json</code> if you want to send a different message for each protocol. For example, using one publish action, you can send a short message to your SMS subscribers and a longer message to your email subscribers. If you set <code>MessageStructure</code> to <code>json</code>, the value of the <code>Message</code> parameter must: </p> <ul> <li> <p>be a syntactically valid JSON object; and</p> </li> <li> <p>contain at least a top-level JSON key of "default" with a value that is a string.</p> </li> </ul> <p>You can define other top-level keys that define the message you want to send to a specific transport protocol (e.g., "http").</p> <p>Valid value: <code>json</code> </p>"""
    message_attributes: NotRequired[
        "capo_sns.types.message_attribute_map.MessageAttributeMap"
    ]
    """<p>Message attributes for Publish action.</p>"""
    message_deduplication_id: NotRequired["capo_sns.types.string.String"]
    r"""<ul> <li> <p>This parameter applies only to FIFO (first-in-first-out) topics. The <code>MessageDeduplicationId</code> can contain up to 128 alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>, which is a token used for deduplication of sent messages within the 5 minute minimum deduplication interval.</p> </li> <li> <p>The scope of deduplication depends on the <code>FifoThroughputScope</code> attribute, when set to <code>Topic</code> the message deduplication scope is across the entire topic, when set to <code>MessageGroup</code> the message deduplication scope is within each individual message group.</p> </li> <li> <p>If a message with a particular <code>MessageDeduplicationId</code> is sent successfully, subsequent messages within the deduplication scope and interval, with the same <code>MessageDeduplicationId</code>, are accepted successfully but aren't delivered.</p> </li> <li> <p>Every message must have a unique <code>MessageDeduplicationId</code>:</p> <ul> <li> <p>You may provide a <code>MessageDeduplicationId</code> explicitly.</p> </li> <li> <p>If you aren't able to provide a <code>MessageDeduplicationId</code> and you enable <code>ContentBasedDeduplication</code> for your topic, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> </li> <li> <p>If you don't provide a <code>MessageDeduplicationId</code> and the topic doesn't have <code>ContentBasedDeduplication</code> set, the action fails with an error.</p> </li> <li> <p>If the topic has a <code>ContentBasedDeduplication</code> set, your <code>MessageDeduplicationId</code> overrides the generated one. </p> </li> </ul> </li> <li> <p>When <code>ContentBasedDeduplication</code> is in effect, messages with identical content sent within the deduplication scope and interval are treated as duplicates and only one copy of the message is delivered.</p> </li> <li> <p>If you send one message with <code>ContentBasedDeduplication</code> enabled, and then another message with a <code>MessageDeduplicationId</code> that is the same as the one generated for the first <code>MessageDeduplicationId</code>, the two messages are treated as duplicates, within the deduplication scope and interval, and only one copy of the message is delivered.</p> </li> </ul>"""
    message_group_id: NotRequired["capo_sns.types.string.String"]
    r"""<p>The <code>MessageGroupId</code> can contain up to 128 alphanumeric characters <code>(a-z, A-Z, 0-9)</code> and punctuation <code>(!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)</code>.</p> <p> For FIFO topics: The <code>MessageGroupId</code> is a tag that specifies that a message belongs to a specific message group. Messages that belong to the same message group are processed in a FIFO manner (however, messages in different message groups might be processed out of order). Every message must include a <code>MessageGroupId</code>. </p> <p> For standard topics: The <code>MessageGroupId</code> is optional and is forwarded only to Amazon SQS standard subscriptions to activate <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-fair-queues.html">fair queues</a>. The <code>MessageGroupId</code> is not used for, or sent to, any other endpoint types. When provided, the same validation rules apply as for FIFO topics. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PublishInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    if "target_arn" in value:
        pairs.append((f"{key_prefix}TargetArn", str(value["target_arn"])))
    if "phone_number" in value:
        pairs.append((f"{key_prefix}PhoneNumber", str(value["phone_number"])))
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


def deserialize_query(el: Element) -> PublishInput:
    out: PublishInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_target_arn = el.find("TargetArn")
    if child_target_arn is not None:
        out["target_arn"] = str(child_target_arn.text or "")
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("PublishInput.message required")
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
