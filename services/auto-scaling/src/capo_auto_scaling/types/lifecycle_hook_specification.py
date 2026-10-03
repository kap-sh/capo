"""Generated from Smithy shape ``com.amazonaws.autoscaling#LifecycleHookSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.any_printable_ascii_string_max_len4000
    import capo_auto_scaling.types.ascii_string_max_len255
    import capo_auto_scaling.types.heartbeat_timeout
    import capo_auto_scaling.types.lifecycle_action_result
    import capo_auto_scaling.types.lifecycle_transition
    import capo_auto_scaling.types.notification_target_resource_name
    import capo_auto_scaling.types.xml_string_max_len255


class LifecycleHookSpecification(TypedDict, closed=True):
    lifecycle_hook_name: NotRequired[
        "capo_auto_scaling.types.ascii_string_max_len255.AsciiStringMaxLen255"
    ]
    """<p>The name of the lifecycle hook.</p>"""
    lifecycle_transition: NotRequired[
        "capo_auto_scaling.types.lifecycle_transition.LifecycleTransition"
    ]
    """<p>The lifecycle transition. For Auto Scaling groups, there are two major lifecycle transitions.</p> <ul> <li> <p>To create a lifecycle hook for scale-out events, specify <code>autoscaling:EC2_INSTANCE_LAUNCHING</code>.</p> </li> <li> <p>To create a lifecycle hook for scale-in events, specify <code>autoscaling:EC2_INSTANCE_TERMINATING</code>.</p> </li> </ul>"""
    notification_metadata: NotRequired[
        "capo_auto_scaling.types.any_printable_ascii_string_max_len4000.AnyPrintableAsciiStringMaxLen4000"
    ]
    """<p>Additional information that you want to include any time Amazon EC2 Auto Scaling sends a message to the notification target.</p>"""
    heartbeat_timeout: NotRequired[
        "capo_auto_scaling.types.heartbeat_timeout.HeartbeatTimeout"
    ]
    """<p>The maximum time, in seconds, that can elapse before the lifecycle hook times out. The range is from <code>30</code> to <code>7200</code> seconds. The default value is <code>3600</code> seconds (1 hour).</p>"""
    default_result: NotRequired[
        "capo_auto_scaling.types.lifecycle_action_result.LifecycleActionResult"
    ]
    """<p>The action the Auto Scaling group takes when the lifecycle hook timeout elapses or if an unexpected failure occurs. The default value is <code>ABANDON</code>.</p> <p>Valid values: <code>CONTINUE</code> | <code>ABANDON</code> </p>"""
    notification_target_arn: NotRequired[
        "capo_auto_scaling.types.notification_target_resource_name.NotificationTargetResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the notification target that Amazon EC2 Auto Scaling sends notifications to when an instance is in a wait state for the lifecycle hook. You can specify an Amazon SNS topic or an Amazon SQS queue.</p>"""
    role_arn: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The ARN of the IAM role that allows the Auto Scaling group to publish to the specified notification target. For information about creating this role, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/prepare-for-lifecycle-notifications.html">Prepare to add a lifecycle hook to your Auto Scaling group</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> <p>Valid only if the notification target is an Amazon SNS topic or an Amazon SQS queue.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LifecycleHookSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "lifecycle_hook_name" in value:
        pairs.append(
            (f"{key_prefix}LifecycleHookName", str(value["lifecycle_hook_name"]))
        )
    if "lifecycle_transition" in value:
        pairs.append(
            (f"{key_prefix}LifecycleTransition", str(value["lifecycle_transition"]))
        )
    if "notification_metadata" in value:
        pairs.append(
            (f"{key_prefix}NotificationMetadata", str(value["notification_metadata"]))
        )
    if "heartbeat_timeout" in value:
        pairs.append((f"{key_prefix}HeartbeatTimeout", str(value["heartbeat_timeout"])))
    if "default_result" in value:
        pairs.append((f"{key_prefix}DefaultResult", str(value["default_result"])))
    if "notification_target_arn" in value:
        pairs.append(
            (
                f"{key_prefix}NotificationTargetARN",
                str(value["notification_target_arn"]),
            )
        )
    if "role_arn" in value:
        pairs.append((f"{key_prefix}RoleARN", str(value["role_arn"])))


def deserialize_query(el: Element) -> LifecycleHookSpecification:
    out: LifecycleHookSpecification = {}  # type: ignore[typeddict-item]
    child_lifecycle_hook_name = el.find("LifecycleHookName")
    if child_lifecycle_hook_name is not None:
        out["lifecycle_hook_name"] = str(child_lifecycle_hook_name.text or "")
    child_lifecycle_transition = el.find("LifecycleTransition")
    if child_lifecycle_transition is not None:
        out["lifecycle_transition"] = str(child_lifecycle_transition.text or "")
    child_notification_metadata = el.find("NotificationMetadata")
    if child_notification_metadata is not None:
        out["notification_metadata"] = str(child_notification_metadata.text or "")
    child_heartbeat_timeout = el.find("HeartbeatTimeout")
    if child_heartbeat_timeout is not None:
        out["heartbeat_timeout"] = int(child_heartbeat_timeout.text or "")
    child_default_result = el.find("DefaultResult")
    if child_default_result is not None:
        out["default_result"] = str(child_default_result.text or "")
    child_notification_target_arn = el.find("NotificationTargetARN")
    if child_notification_target_arn is not None:
        out["notification_target_arn"] = str(child_notification_target_arn.text or "")
    child_role_arn = el.find("RoleARN")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    return out
