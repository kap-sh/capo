"""Generated from Smithy shape ``com.amazonaws.autoscaling#PutNotificationConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.auto_scaling_notification_types
    import capo_auto_scaling.types.xml_string_max_len255


class PutNotificationConfigurationType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    topic_arn: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic.</p>"""
    notification_types: NotRequired[
        "capo_auto_scaling.types.auto_scaling_notification_types.AutoScalingNotificationTypes"
    ]
    """<p>The type of event that causes the notification to be sent. To query the notification types supported by Amazon EC2 Auto Scaling, call the <a href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingNotificationTypes.html">DescribeAutoScalingNotificationTypes</a> API.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PutNotificationConfigurationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{key_prefix}AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "topic_arn" in value:
        pairs.append((f"{key_prefix}TopicARN", str(value["topic_arn"])))
    if "notification_types" in value:
        import capo_auto_scaling.types.auto_scaling_notification_types

        capo_auto_scaling.types.auto_scaling_notification_types.serialize_query(
            value["notification_types"], pairs, f"{key_prefix}NotificationTypes"
        )


def deserialize_query(el: Element) -> PutNotificationConfigurationType:
    out: PutNotificationConfigurationType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_topic_arn = el.find("TopicARN")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    child_notification_types = el.find("NotificationTypes")
    if child_notification_types is not None:
        import capo_auto_scaling.types.auto_scaling_notification_types

        out["notification_types"] = (
            capo_auto_scaling.types.auto_scaling_notification_types.deserialize_query(
                child_notification_types
            )
        )
    return out
