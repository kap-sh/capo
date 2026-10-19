"""Generated from Smithy shape ``com.amazonaws.inspector#Subscription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.event_subscription_list


class Subscription(TypedDict, closed=True):
    resource_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the assessment template that is used during the event for which the SNS notification is sent.</p>"""
    topic_arn: "capo_inspector.types.arn.Arn"
    """<p>The ARN of the Amazon Simple Notification Service (SNS) topic to which the SNS notifications are sent.</p>"""
    event_subscriptions: (
        "capo_inspector.types.event_subscription_list.EventSubscriptionList"
    )
    """<p>The list of existing event subscriptions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscription) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["topicArn"] = value["topic_arn"]
    import capo_inspector.types.event_subscription_list

    out["eventSubscriptions"] = (
        capo_inspector.types.event_subscription_list.serialize_aws_json_1_1(
            value["event_subscriptions"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscription:
    out: Subscription = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("topicArn") is not None:
        out["topic_arn"] = data["topicArn"]
    else:
        out["topic_arn"] = ""
    if data.get("eventSubscriptions") is not None:
        import capo_inspector.types.event_subscription_list

        out["event_subscriptions"] = (
            capo_inspector.types.event_subscription_list.deserialize_aws_json_1_1(
                data["eventSubscriptions"]
            )
        )
    else:
        out["event_subscriptions"] = []
    return out
