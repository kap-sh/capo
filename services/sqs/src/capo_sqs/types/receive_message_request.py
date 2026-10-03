"""Generated from Smithy shape ``com.amazonaws.sqs#ReceiveMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sqs.types.attribute_name_list
    import capo_sqs.types.message_attribute_name_list
    import capo_sqs.types.message_system_attribute_list
    import capo_sqs.types.nullable_integer
    import capo_sqs.types.string


class ReceiveMessageRequest(TypedDict, closed=True):
    queue_url: "capo_sqs.types.string.String"
    """<p>The URL of the Amazon SQS queue from which messages are received.</p> <p>Queue URLs and names are case-sensitive.</p>"""
    attribute_names: NotRequired["capo_sqs.types.attribute_name_list.AttributeNameList"]
    """<important> <p>This parameter has been discontinued but will be supported for backward compatibility. To provide attribute names, you are encouraged to use <code>MessageSystemAttributeNames</code>. </p> </important> <p>A list of attributes that need to be returned along with each message. These attributes include:</p> <ul> <li> <p> <code>All</code> – Returns all values.</p> </li> <li> <p> <code>ApproximateFirstReceiveTimestamp</code> – Returns the time the message was first received from the queue (<a href="http://en.wikipedia.org/wiki/Unix_time">epoch time</a> in milliseconds).</p> </li> <li> <p> <code>ApproximateReceiveCount</code> – Returns the number of times a message has been received across all queues but not deleted.</p> </li> <li> <p> <code>AWSTraceHeader</code> – Returns the X-Ray trace header string. </p> </li> <li> <p> <code>SenderId</code> </p> <ul> <li> <p>For a user, returns the user ID, for example <code>ABCDEFGHI1JKLMNOPQ23R</code>.</p> </li> <li> <p>For an IAM role, returns the IAM role ID, for example <code>ABCDE1F2GH3I4JK5LMNOP:i-a123b456</code>.</p> </li> </ul> </li> <li> <p> <code>SentTimestamp</code> – Returns the time the message was sent to the queue (<a href="http://en.wikipedia.org/wiki/Unix_time">epoch time</a> in milliseconds).</p> </li> <li> <p> <code>SqsManagedSseEnabled</code> – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html">SSE-KMS</a> or <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html">SSE-SQS</a>).</p> </li> <li> <p> <code>MessageDeduplicationId</code> – Returns the value provided by the producer that calls the <code> <a>SendMessage</a> </code> action.</p> </li> <li> <p> <code>MessageGroupId</code> – Returns the value provided by the producer that calls the <code> <a>SendMessage</a> </code> action. </p> </li> <li> <p> <code>SequenceNumber</code> – Returns the value provided by Amazon SQS.</p> </li> </ul>"""
    message_system_attribute_names: NotRequired[
        "capo_sqs.types.message_system_attribute_list.MessageSystemAttributeList"
    ]
    """<p>A list of attributes that need to be returned along with each message. These attributes include:</p> <ul> <li> <p> <code>All</code> – Returns all values.</p> </li> <li> <p> <code>ApproximateFirstReceiveTimestamp</code> – Returns the time the message was first received from the queue (<a href="http://en.wikipedia.org/wiki/Unix_time">epoch time</a> in milliseconds).</p> </li> <li> <p> <code>ApproximateReceiveCount</code> – Returns the number of times a message has been received across all queues but not deleted.</p> </li> <li> <p> <code>AWSTraceHeader</code> – Returns the X-Ray trace header string. </p> </li> <li> <p> <code>SenderId</code> </p> <ul> <li> <p>For a user, returns the user ID, for example <code>ABCDEFGHI1JKLMNOPQ23R</code>.</p> </li> <li> <p>For an IAM role, returns the IAM role ID, for example <code>ABCDE1F2GH3I4JK5LMNOP:i-a123b456</code>.</p> </li> </ul> </li> <li> <p> <code>SentTimestamp</code> – Returns the time the message was sent to the queue (<a href="http://en.wikipedia.org/wiki/Unix_time">epoch time</a> in milliseconds).</p> </li> <li> <p> <code>SqsManagedSseEnabled</code> – Enables server-side queue encryption using SQS owned encryption keys. Only one server-side encryption option is supported per queue (for example, <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sse-existing-queue.html">SSE-KMS</a> or <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-sqs-sse-queue.html">SSE-SQS</a>).</p> </li> <li> <p> <code>MessageDeduplicationId</code> – Returns the value provided by the producer that calls the <code> <a>SendMessage</a> </code> action.</p> </li> <li> <p> <code>MessageGroupId</code> – Returns the value provided by the producer that calls the <code> <a>SendMessage</a> </code> action.</p> </li> <li> <p> <code>SequenceNumber</code> – Returns the value provided by Amazon SQS.</p> </li> </ul>"""
    message_attribute_names: NotRequired[
        "capo_sqs.types.message_attribute_name_list.MessageAttributeNameList"
    ]
    """<p>The name of the message attribute, where <i>N</i> is the index.</p> <ul> <li> <p>The name can contain alphanumeric characters and the underscore (<code>_</code>), hyphen (<code>-</code>), and period (<code>.</code>).</p> </li> <li> <p>The name is case-sensitive and must be unique among all attribute names for the message.</p> </li> <li> <p>The name must not start with AWS-reserved prefixes such as <code>AWS.</code> or <code>Amazon.</code> (or any casing variants).</p> </li> <li> <p>The name must not start or end with a period (<code>.</code>), and it should not have periods in succession (<code>..</code>).</p> </li> <li> <p>The name can be up to 256 characters long.</p> </li> </ul> <p>When using <code>ReceiveMessage</code>, you can send a list of attribute names to receive, or you can return all of the attributes by specifying <code>All</code> or <code>.*</code> in your request. You can also use all message attributes starting with a prefix, for example <code>bar.*</code>.</p>"""
    max_number_of_messages: NotRequired[
        "capo_sqs.types.nullable_integer.NullableInteger"
    ]
    """<p>The maximum number of messages to return. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10. Default: 1.</p>"""
    visibility_timeout: NotRequired["capo_sqs.types.nullable_integer.NullableInteger"]
    """<p>The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a <code>ReceiveMessage</code> request. If not specified, the default visibility timeout for the queue is used, which is 30 seconds.</p> <p>Understanding <code>VisibilityTimeout</code>:</p> <ul> <li> <p>When a message is received from a queue, it becomes temporarily invisible to other consumers for the duration of the visibility timeout. This prevents multiple consumers from processing the same message simultaneously. If the message is not deleted or its visibility timeout is not extended before the timeout expires, it becomes visible again and can be retrieved by other consumers.</p> </li> <li> <p>Setting an appropriate visibility timeout is crucial. If it's too short, the message might become visible again before processing is complete, leading to duplicate processing. If it's too long, it delays the reprocessing of messages if the initial processing fails.</p> </li> <li> <p>You can adjust the visibility timeout using the <code>--visibility-timeout</code> parameter in the <code>receive-message</code> command to match the processing time required by your application.</p> </li> <li> <p>A message that isn't deleted or a message whose visibility isn't extended before the visibility timeout expires counts as a failed receive. Depending on the configuration of the queue, the message might be sent to the dead-letter queue.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html">Visibility Timeout</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""
    wait_time_seconds: NotRequired["capo_sqs.types.nullable_integer.NullableInteger"]
    """<p>The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call does not return a message list. If you are using the Java SDK, it returns a <code>ReceiveMessageResponse</code> object, which has a empty list instead of a Null object.</p> <important> <p>To avoid HTTP errors, ensure that the HTTP response timeout for <code>ReceiveMessage</code> requests is longer than the <code>WaitTimeSeconds</code> parameter. For example, with the Java SDK, you can set HTTP transport settings using the <a href="https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/nio/netty/NettyNioAsyncHttpClient.html"> NettyNioAsyncHttpClient</a> for asynchronous clients, or the <a href="https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/http/apache/ApacheHttpClient.html"> ApacheHttpClient</a> for synchronous clients. </p> </important>"""
    receive_request_attempt_id: NotRequired["capo_sqs.types.string.String"]
    r"""<p>This parameter applies only to FIFO (first-in-first-out) queues.</p> <p>The token used for deduplication of <code>ReceiveMessage</code> calls. If a networking issue occurs after a <code>ReceiveMessage</code> action, and instead of a response you receive a generic error, it is possible to retry the same action with an identical <code>ReceiveRequestAttemptId</code> to retrieve the same set of messages, even if their visibility timeout has not yet expired.</p> <ul> <li> <p>You can use <code>ReceiveRequestAttemptId</code> only for 5 minutes after a <code>ReceiveMessage</code> action.</p> </li> <li> <p>When you set <code>FifoQueue</code>, a caller of the <code>ReceiveMessage</code> action can provide a <code>ReceiveRequestAttemptId</code> explicitly.</p> </li> <li> <p>It is possible to retry the <code>ReceiveMessage</code> action with the same <code>ReceiveRequestAttemptId</code> if none of the messages have been modified (deleted or had their visibility changes).</p> </li> <li> <p>During a visibility timeout, subsequent calls with the same <code>ReceiveRequestAttemptId</code> return the same messages and receipt handles. If a retry occurs within the deduplication interval, it resets the visibility timeout. For more information, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html">Visibility Timeout</a> in the <i>Amazon SQS Developer Guide</i>.</p> <important> <p>If a caller of the <code>ReceiveMessage</code> action still processes messages when the visibility timeout expires and messages become visible, another worker consuming from the same queue can receive the same messages and therefore process duplicates. Also, if a consumer whose message processing time is longer than the visibility timeout tries to delete the processed messages, the action fails with an error.</p> <p>To mitigate this effect, ensure that your application observes a safe threshold before the visibility timeout expires and extend the visibility timeout as necessary.</p> </important> </li> <li> <p>While messages with a particular <code>MessageGroupId</code> are invisible, no more messages belonging to the same <code>MessageGroupId</code> are returned until the visibility timeout expires. You can still receive messages with another <code>MessageGroupId</code> from your FIFO queue as long as they are visible.</p> </li> <li> <p>If a caller of <code>ReceiveMessage</code> can't track the <code>ReceiveRequestAttemptId</code>, no retries work until the original visibility timeout expires. As a result, delays might occur but the messages in the queue remain in a strict order.</p> </li> </ul> <p>The maximum length of <code>ReceiveRequestAttemptId</code> is 128 characters. <code>ReceiveRequestAttemptId</code> can contain alphanumeric characters (<code>a-z</code>, <code>A-Z</code>, <code>0-9</code>) and punctuation (<code>!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~</code>).</p> <p>For best practices of using <code>ReceiveRequestAttemptId</code>, see <a href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/using-receiverequestattemptid-request-parameter.html">Using the ReceiveRequestAttemptId Request Parameter</a> in the <i>Amazon SQS Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiveMessageRequest) -> dict:
    out: dict = {}
    out["QueueUrl"] = value["queue_url"]
    if "attribute_names" in value:
        import capo_sqs.types.attribute_name_list

        out["AttributeNames"] = (
            capo_sqs.types.attribute_name_list.serialize_aws_json_1_0(
                value["attribute_names"]
            )
        )
    if "message_system_attribute_names" in value:
        import capo_sqs.types.message_system_attribute_list

        out["MessageSystemAttributeNames"] = (
            capo_sqs.types.message_system_attribute_list.serialize_aws_json_1_0(
                value["message_system_attribute_names"]
            )
        )
    if "message_attribute_names" in value:
        import capo_sqs.types.message_attribute_name_list

        out["MessageAttributeNames"] = (
            capo_sqs.types.message_attribute_name_list.serialize_aws_json_1_0(
                value["message_attribute_names"]
            )
        )
    if "max_number_of_messages" in value:
        out["MaxNumberOfMessages"] = value["max_number_of_messages"]
    if "visibility_timeout" in value:
        out["VisibilityTimeout"] = value["visibility_timeout"]
    if "wait_time_seconds" in value:
        out["WaitTimeSeconds"] = value["wait_time_seconds"]
    if "receive_request_attempt_id" in value:
        out["ReceiveRequestAttemptId"] = value["receive_request_attempt_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ReceiveMessageRequest:
    out: ReceiveMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueueUrl") is not None:
        out["queue_url"] = data["QueueUrl"]
    else:
        raise DeserializationError("ReceiveMessageRequest.queue_url required")
    if data.get("AttributeNames") is not None:
        import capo_sqs.types.attribute_name_list

        out["attribute_names"] = (
            capo_sqs.types.attribute_name_list.deserialize_aws_json_1_0(
                data["AttributeNames"]
            )
        )
    if data.get("MessageSystemAttributeNames") is not None:
        import capo_sqs.types.message_system_attribute_list

        out["message_system_attribute_names"] = (
            capo_sqs.types.message_system_attribute_list.deserialize_aws_json_1_0(
                data["MessageSystemAttributeNames"]
            )
        )
    if data.get("MessageAttributeNames") is not None:
        import capo_sqs.types.message_attribute_name_list

        out["message_attribute_names"] = (
            capo_sqs.types.message_attribute_name_list.deserialize_aws_json_1_0(
                data["MessageAttributeNames"]
            )
        )
    if data.get("MaxNumberOfMessages") is not None:
        out["max_number_of_messages"] = data["MaxNumberOfMessages"]
    if data.get("VisibilityTimeout") is not None:
        out["visibility_timeout"] = data["VisibilityTimeout"]
    if data.get("WaitTimeSeconds") is not None:
        out["wait_time_seconds"] = data["WaitTimeSeconds"]
    if data.get("ReceiveRequestAttemptId") is not None:
        out["receive_request_attempt_id"] = data["ReceiveRequestAttemptId"]
    return out
