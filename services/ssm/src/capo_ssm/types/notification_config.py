"""Generated from Smithy shape ``com.amazonaws.ssm#NotificationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.notification_arn
    import capo_ssm.types.notification_event_list
    import capo_ssm.types.notification_type


class NotificationConfig(TypedDict, closed=True):
    notification_arn: NotRequired["capo_ssm.types.notification_arn.NotificationArn"]
    """<p>An Amazon Resource Name (ARN) for an Amazon Simple Notification Service (Amazon SNS) topic. Run Command pushes notifications about command status changes to this topic.</p>"""
    notification_events: NotRequired[
        "capo_ssm.types.notification_event_list.NotificationEventList"
    ]
    """<p>The different events for which you can receive notifications. To learn more about these events, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html">Monitoring Systems Manager status changes using Amazon SNS notifications</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>"""
    notification_type: NotRequired["capo_ssm.types.notification_type.NotificationType"]
    """<p>The type of notification.</p> <ul> <li> <p> <code>Command</code>: Receive notification when the status of a command changes.</p> </li> <li> <p> <code>Invocation</code>: For commands sent to multiple managed nodes, receive notification on a per-node basis when the status of a command changes. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationConfig) -> dict:
    out: dict = {}
    if "notification_arn" in value:
        out["NotificationArn"] = value["notification_arn"]
    if "notification_events" in value:
        import capo_ssm.types.notification_event_list

        out["NotificationEvents"] = (
            capo_ssm.types.notification_event_list.serialize_aws_json_1_1(
                value["notification_events"]
            )
        )
    if "notification_type" in value:
        import capo_ssm.types.notification_type

        out["NotificationType"] = (
            capo_ssm.types.notification_type.serialize_aws_json_1_1(
                value["notification_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationConfig:
    out: NotificationConfig = {}  # type: ignore[typeddict-item]
    if data.get("NotificationArn") is not None:
        out["notification_arn"] = data["NotificationArn"]
    if data.get("NotificationEvents") is not None:
        import capo_ssm.types.notification_event_list

        out["notification_events"] = (
            capo_ssm.types.notification_event_list.deserialize_aws_json_1_1(
                data["NotificationEvents"]
            )
        )
    if data.get("NotificationType") is not None:
        import capo_ssm.types.notification_type

        out["notification_type"] = (
            capo_ssm.types.notification_type.deserialize_aws_json_1_1(
                data["NotificationType"]
            )
        )
    return out
