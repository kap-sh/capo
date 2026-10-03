"""Generated from Smithy shape ``com.amazonaws.sns#SetSubscriptionAttributesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.attribute_name
    import capo_sns.types.attribute_value
    import capo_sns.types.subscription_arn


class SetSubscriptionAttributesInput(TypedDict, closed=True):
    subscription_arn: "capo_sns.types.subscription_arn.subscriptionARN"
    """<p>The ARN of the subscription to modify.</p>"""
    attribute_name: "capo_sns.types.attribute_name.attributeName"
    """<p>A map of attributes with their corresponding values.</p> <p>The following lists the names, descriptions, and values of the special request parameters that this action uses:</p> <ul> <li> <p> <code>DeliveryPolicy</code> – The policy that defines how Amazon SNS retries failed deliveries to HTTP/S endpoints.</p> </li> <li> <p> <code>FilterPolicy</code> – The simple JSON object that lets your subscriber receive only a subset of messages, rather than receiving every message published to the topic.</p> </li> <li> <p> <code>FilterPolicyScope</code> – This attribute lets you choose the filtering scope by using one of the following string value types:</p> <ul> <li> <p> <code>MessageAttributes</code> (default) – The filter is applied on the message attributes.</p> </li> <li> <p> <code>MessageBody</code> – The filter is applied on the message body.</p> </li> </ul> </li> <li> <p> <code>RawMessageDelivery</code> – When set to <code>true</code>, enables raw message delivery to Amazon SQS or HTTP/S endpoints. This eliminates the need for the endpoints to process JSON formatting, which is otherwise created for Amazon SNS metadata.</p> </li> <li> <p> <code>RedrivePolicy</code> – When specified, sends undeliverable messages to the specified Amazon SQS dead-letter queue. Messages that can't be delivered due to client errors (for example, when the subscribed endpoint is unreachable) or server errors (for example, when the service that powers the subscribed endpoint becomes unavailable) are held in the dead-letter queue for further analysis or reprocessing.</p> </li> </ul> <p>The following attribute applies only to Amazon Data Firehose delivery stream subscriptions:</p> <ul> <li> <p> <code>SubscriptionRoleArn</code> – The ARN of the IAM role that has the following:</p> <ul> <li> <p>Permission to write to the Firehose delivery stream</p> </li> <li> <p>Amazon SNS listed as a trusted entity</p> </li> </ul> <p>Specifying a valid ARN for this attribute is required for Firehose delivery stream subscriptions. For more information, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-firehose-as-subscriber.html">Fanout to Firehose delivery streams</a> in the <i>Amazon SNS Developer Guide</i>.</p> </li> </ul>"""
    attribute_value: NotRequired["capo_sns.types.attribute_value.attributeValue"]
    """<p>The new value for the attribute in JSON format.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetSubscriptionAttributesInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}SubscriptionArn", str(value["subscription_arn"])))
    pairs.append((f"{key_prefix}AttributeName", str(value["attribute_name"])))
    if "attribute_value" in value:
        pairs.append((f"{key_prefix}AttributeValue", str(value["attribute_value"])))


def deserialize_query(el: Element) -> SetSubscriptionAttributesInput:
    out: SetSubscriptionAttributesInput = {}  # type: ignore[typeddict-item]
    child_subscription_arn = el.find("SubscriptionArn")
    if child_subscription_arn is not None:
        out["subscription_arn"] = str(child_subscription_arn.text or "")
    else:
        raise DeserializationError(
            "SetSubscriptionAttributesInput.subscription_arn required"
        )
    child_attribute_name = el.find("AttributeName")
    if child_attribute_name is not None:
        out["attribute_name"] = str(child_attribute_name.text or "")
    else:
        raise DeserializationError(
            "SetSubscriptionAttributesInput.attribute_name required"
        )
    child_attribute_value = el.find("AttributeValue")
    if child_attribute_value is not None:
        out["attribute_value"] = str(child_attribute_value.text or "")
    return out
