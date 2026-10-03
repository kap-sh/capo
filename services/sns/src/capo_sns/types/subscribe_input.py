"""Generated from Smithy shape ``com.amazonaws.sns#SubscribeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.boolean
    import capo_sns.types.endpoint2
    import capo_sns.types.protocol
    import capo_sns.types.subscription_attributes_map
    import capo_sns.types.topic_arn


class SubscribeInput(TypedDict, closed=True):
    topic_arn: "capo_sns.types.topic_arn.topicARN"
    """<p>The ARN of the topic you want to subscribe to.</p>"""
    protocol: "capo_sns.types.protocol.protocol"
    """<p>The protocol that you want to use. Supported protocols include:</p> <ul> <li> <p> <code>http</code> – delivery of JSON-encoded message via HTTP POST</p> </li> <li> <p> <code>https</code> – delivery of JSON-encoded message via HTTPS POST</p> </li> <li> <p> <code>email</code> – delivery of message via SMTP</p> </li> <li> <p> <code>email-json</code> – delivery of JSON-encoded message via SMTP</p> </li> <li> <p> <code>sms</code> – delivery of message via SMS</p> </li> <li> <p> <code>sqs</code> – delivery of JSON-encoded message to an Amazon SQS queue</p> </li> <li> <p> <code>application</code> – delivery of JSON-encoded message to an EndpointArn for a mobile app and device</p> </li> <li> <p> <code>lambda</code> – delivery of JSON-encoded message to an Lambda function</p> </li> <li> <p> <code>firehose</code> – delivery of JSON-encoded message to an Amazon Data Firehose delivery stream.</p> </li> </ul>"""
    endpoint: NotRequired["capo_sns.types.endpoint2.Endpoint2"]
    """<p>The endpoint that you want to receive notifications. Endpoints vary by protocol:</p> <ul> <li> <p>For the <code>http</code> protocol, the (public) endpoint is a URL beginning with <code>http://</code>.</p> </li> <li> <p>For the <code>https</code> protocol, the (public) endpoint is a URL beginning with <code>https://</code>.</p> </li> <li> <p>For the <code>email</code> protocol, the endpoint is an email address.</p> </li> <li> <p>For the <code>email-json</code> protocol, the endpoint is an email address.</p> </li> <li> <p>For the <code>sms</code> protocol, the endpoint is a phone number of an SMS-enabled device.</p> </li> <li> <p>For the <code>sqs</code> protocol, the endpoint is the ARN of an Amazon SQS queue.</p> </li> <li> <p>For the <code>application</code> protocol, the endpoint is the EndpointArn of a mobile app and device.</p> </li> <li> <p>For the <code>lambda</code> protocol, the endpoint is the ARN of an Lambda function.</p> </li> <li> <p>For the <code>firehose</code> protocol, the endpoint is the ARN of an Amazon Data Firehose delivery stream.</p> </li> </ul>"""
    attributes: NotRequired[
        "capo_sns.types.subscription_attributes_map.SubscriptionAttributesMap"
    ]
    """<p>A map of attributes with their corresponding values.</p> <p>The following lists the names, descriptions, and values of the special request parameters that the <code>Subscribe</code> action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>FilterPolicy</code> – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.</p> </li> <li> <p> <code>FilterPolicyScope</code> – This attribute lets you choose the filtering scope by using one of the following string value types:</p> <ul> <li> <p> <code>MessageAttributes</code> (default) – The filter is applied on the message attributes.</p> </li> <li> <p> <code>MessageBody</code> – The filter is applied on the message body.</p> </li> </ul> </li> <li> <p> <code>RawMessageDelivery</code> – When set to <code>true</code>, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.</p> </li> <li> <p> <code>RedrivePolicy</code> – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.</p> </li> </ul> <p>The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:</p> <ul> <li> <p> <code>SubscriptionRoleArn</code> – The ARN of the IAM role that has the following:</p> <ul> <li> <p>Permission to write to the Firehose delivery stream</p> </li> <li> <p>Amazon SNS listed as a trusted entity</p> </li> </ul> <p>Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html">Fanout to Firehose delivery streams</a> in the <i>Amazon SNS Developer Guide</i>.</p> </li> </ul> <p>The following attributes apply only to <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html">FIFO topics</a>:</p> <ul> <li> <p> <code>ReplayPolicy</code> – Adds or updates an inline policy document for a subscription to replay messages stored in the specified Amazon SNS topic.</p> </li> <li> <p> <code>ReplayStatus</code> – Retrieves the status of the subscription message replay, which can be one of the following:</p> <ul> <li> <p> <code>Completed</code> – The replay has successfully redelivered all messages, and is now delivering newly published messages. If an ending point was specified in the <code>ReplayPolicy</code> then the subscription will no longer receive newly published messages.</p> </li> <li> <p> <code>In progress</code> – The replay is currently replaying the selected messages.</p> </li> <li> <p> <code>Failed</code> – The replay was unable to complete.</p> </li> <li> <p> <code>Pending</code> – The default state while the replay initiates.</p> </li> </ul> </li> </ul>"""
    return_subscription_arn: "capo_sns.types.boolean.boolean"
    """<p>Sets whether the response from the <code>Subscribe</code> request includes the subscription ARN, even if the subscription is not yet confirmed.</p> <p>If you set this parameter to <code>true</code>, the response includes the ARN in all cases, even if the subscription is not yet confirmed. In addition to the ARN for confirmed subscriptions, the response also includes the <code>pending subscription</code> ARN value for subscriptions that aren't yet confirmed. A subscription becomes confirmed when the subscriber calls the <code>ConfirmSubscription</code> action with a confirmation token.</p> <p></p> <p>The default value is <code>false</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SubscribeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}TopicArn", str(value["topic_arn"])))
    pairs.append((f"{key_prefix}Protocol", str(value["protocol"])))
    if "endpoint" in value:
        pairs.append((f"{key_prefix}Endpoint", str(value["endpoint"])))
    if "attributes" in value:
        import capo_sns.types.subscription_attributes_map

        capo_sns.types.subscription_attributes_map.serialize_query(
            value["attributes"], pairs, f"{key_prefix}Attributes"
        )
    pairs.append(
        (
            f"{key_prefix}ReturnSubscriptionArn",
            "true" if value.get("return_subscription_arn", False) else "false",
        )
    )


def deserialize_query(el: Element) -> SubscribeInput:
    out: SubscribeInput = {}  # type: ignore[typeddict-item]
    child_topic_arn = el.find("TopicArn")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    else:
        raise DeserializationError("SubscribeInput.topic_arn required")
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        out["protocol"] = str(child_protocol.text or "")
    else:
        raise DeserializationError("SubscribeInput.protocol required")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        out["endpoint"] = str(child_endpoint.text or "")
    child_attributes = el.find("Attributes")
    if child_attributes is not None:
        import capo_sns.types.subscription_attributes_map

        out["attributes"] = (
            capo_sns.types.subscription_attributes_map.deserialize_query(
                child_attributes
            )
        )
    child_return_subscription_arn = el.find("ReturnSubscriptionArn")
    if child_return_subscription_arn is not None:
        out["return_subscription_arn"] = (
            child_return_subscription_arn.text or ""
        ).lower() == "true"
    else:
        out["return_subscription_arn"] = False
    return out
