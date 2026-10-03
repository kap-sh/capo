"""Generated from Smithy shape ``com.amazonaws.sns#CreateTopicInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.attribute_value
    import capo_sns.types.tag_list
    import capo_sns.types.topic_attributes_map
    import capo_sns.types.topic_name


class CreateTopicInput(TypedDict, closed=True):
    name: "capo_sns.types.topic_name.topicName"
    """<p>The name of the topic you want to create.</p> <p>Constraints: Topic names must be made up of only uppercase and lowercase ASCII letters, numbers, underscores, and hyphens, and must be between 1 and 256 characters long.</p> <p>For a FIFO (first-in-first-out) topic, the name must end with the <code>.fifo</code> suffix. </p>"""
    attributes: NotRequired["capo_sns.types.topic_attributes_map.TopicAttributesMap"]
    """<p>A map of attributes with their corresponding values.</p> <p>The following lists names, descriptions, and values of the special request parameters that the <code>CreateTopic</code> action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>DisplayName</code> – The display name to use for a topic with SMS, <code>email</code>, and <code>email-json</code> subscriptions. For <code>email</code> and <code>email-json</code> subscriptions, the display name is used as the sender name for regular notification messages. Subscription confirmation and unsubscribe confirmation emails always use "Amazon Web Services Notifications" as the sender name.</p> </li> <li> <p> <code>MaximumMessageSize</code> – The maximum size, in bytes, of a message that can be published to the topic. Valid values are <code>1024</code> to <code>1048576</code> (1 MiB). The default is <code>262144</code> (256 KiB).</p> <p>A topic with a <code>MaximumMessageSize</code> above 256 KiB must have 100 or fewer subscriptions, and each subscription must be an Amazon SQS, Amazon Data Firehose, or Lambda subscription.</p> </li> <li> <p> <code>Policy</code> – The policy that defines who can access your topic. By default, only the topic owner can publish or subscribe to the topic.</p> </li> <li> <p> <code>TracingConfig</code> – Tracing mode of an Amazon SNS topic. By default <code>TracingConfig</code> is set to <code>PassThrough</code>, and the topic passes through the tracing header it receives from an Amazon SNS publisher to its subscriptions. If set to <code>Active</code>, Amazon SNS will vend X-Ray segment data to topic owner account if the sampled flag in the tracing header is true. This is only supported on standard topics.</p> </li> <li> <p>HTTP</p> <ul> <li> <p> <code>HTTPSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint. </p> </li> <li> <p> <code>HTTPSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> <li> <p> <code>HTTPFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an HTTP endpoint.</p> </li> </ul> </li> <li> <p>Amazon Data Firehose</p> <ul> <li> <p> <code>FirehoseSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint.</p> </li> <li> <p> <code>FirehoseFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon Data Firehose endpoint. </p> </li> </ul> </li> <li> <p>Lambda</p> <ul> <li> <p> <code>LambdaSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Lambda endpoint.</p> </li> <li> <p> <code>LambdaFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Lambda endpoint. </p> </li> </ul> </li> <li> <p>Platform application endpoint</p> <ul> <li> <p> <code>ApplicationSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to a platform application endpoint.</p> </li> <li> <p> <code>ApplicationSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> <li> <p> <code>ApplicationFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an platform application endpoint.</p> </li> </ul> <note> <p>In addition to being able to configure topic attributes for message delivery status of notification messages sent to Amazon SNS application endpoints, you can also configure application attributes for the delivery status of push notification messages sent to push notification services.</p> <p>For example, For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-msg-status.html">Using Amazon SNS Application Attributes for Message Delivery Status</a>. </p> </note> </li> <li> <p>Amazon SQS</p> <ul> <li> <p> <code>SQSSuccessFeedbackRoleArn</code> – Indicates successful message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSSuccessFeedbackSampleRate</code> – Indicates percentage of successful messages to sample for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> <li> <p> <code>SQSFailureFeedbackRoleArn</code> – Indicates failed message delivery status for an Amazon SNS topic that is subscribed to an Amazon SQS endpoint. </p> </li> </ul> </li> </ul> <note> <p>The <ENDPOINT>SuccessFeedbackRoleArn and <ENDPOINT>FailureFeedbackRoleArn attributes are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <ENDPOINT>SuccessFeedbackSampleRate attribute is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the <ENDPOINT>FailureFeedbackRoleArn attribute, then all failed message deliveries generate CloudWatch Logs. </p> </note> <p>The following attribute applies only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html">server-side encryption</a>:</p> <ul> <li> <p> <code>KmsMasterKeyId</code> – The ID of an Amazon Web Services managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a>. For more examples, see <a href="https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html#API_DescribeKey_RequestParameters">KeyId</a> in the <i>Key Management Service API Reference</i>. </p> </li> </ul> <p>The following attributes apply only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html">FIFO topics</a>:</p> <ul> <li> <p> <code>ArchivePolicy</code> – The policy that sets the retention period for messages stored in the message archive of an Amazon SNS FIFO topic.</p> </li> <li> <p> <code>ContentBasedDeduplication</code> – Enables content-based deduplication for FIFO topics.</p> <ul> <li> <p>By default, <code>ContentBasedDeduplication</code> is set to <code>false</code>. If you create a FIFO topic and this attribute is <code>false</code>, you must specify a value for the <code>MessageDeduplicationId</code> parameter for the <a href="https://docs.aws.amazon.com/sns/latest/api/API_Publish.html">Publish</a> action. </p> </li> <li> <p>When you set <code>ContentBasedDeduplication</code> to <code>true</code>, Amazon SNS uses a SHA-256 hash to generate the <code>MessageDeduplicationId</code> using the body of the message (but not the attributes of the message).</p> <p>(Optional) To override the generated value, you can specify a value for the <code>MessageDeduplicationId</code> parameter for the <code>Publish</code> action.</p> </li> </ul> </li> </ul> <ul> <li> <p> <code>FifoThroughputScope</code> – Enables higher throughput for your FIFO topic by adjusting the scope of deduplication. This attribute has two possible values:</p> <ul> <li> <p> <code>Topic</code> – The scope of message deduplication is across the entire topic. This is the default value and maintains existing behavior, with a maximum throughput of 3000 messages per second or 20MB per second, whichever comes first.</p> </li> <li> <p> <code>MessageGroup</code> – The scope of deduplication is within each individual message group, which enables higher throughput per topic subject to regional quotas. For more information on quotas or to request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/sns.html">Amazon SNS service quotas</a> in the Amazon Web Services General Reference.</p> </li> </ul> </li> </ul>"""
    tags: NotRequired["capo_sns.types.tag_list.TagList"]
    """<p>The list of tags to add to a new topic.</p> <note> <p>To be able to tag a topic on creation, you must have the <code>sns:CreateTopic</code> and <code>sns:TagResource</code> permissions.</p> </note>"""
    data_protection_policy: NotRequired["capo_sns.types.attribute_value.attributeValue"]
    """<important> <p>Amazon SNS message data protection is no longer available to new customers. For more information and guidance on alternatives, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-message-data-protection-availability-change.html">Amazon SNS message data protection availability change</a>.</p> </important> <p>The body of the policy document you want to use for this topic.</p> <p>You can only add one policy per topic.</p> <p>The policy must be in JSON string format.</p> <p>Length Constraints: Maximum length of 30,720.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateTopicInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "attributes" in value:
        import capo_sns.types.topic_attributes_map

        capo_sns.types.topic_attributes_map.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )
    if "tags" in value:
        import capo_sns.types.tag_list

        capo_sns.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "data_protection_policy" in value:
        pairs.append(
            (f"{key_prefix}DataProtectionPolicy", str(value["data_protection_policy"]))
        )


def deserialize_query(el: Element) -> CreateTopicInput:
    out: CreateTopicInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateTopicInput.name required")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.topic_attributes_map

        out["attributes"] = capo_sns.types.topic_attributes_map.deserialize_query(
            child_attributes
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_sns.types.tag_list

        out["tags"] = capo_sns.types.tag_list.deserialize_query(child_tags)
    child_data_protection_policy = el.find("DataProtectionPolicy")
    if child_data_protection_policy is not None:
        out["data_protection_policy"] = str(child_data_protection_policy.text or "")
    return out
