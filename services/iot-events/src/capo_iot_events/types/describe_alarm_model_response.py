"""Generated from Smithy shape ``com.amazonaws.iotevents#DescribeAlarmModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_capabilities
    import capo_iot_events.types.alarm_event_actions
    import capo_iot_events.types.alarm_model_arn
    import capo_iot_events.types.alarm_model_description
    import capo_iot_events.types.alarm_model_name
    import capo_iot_events.types.alarm_model_version
    import capo_iot_events.types.alarm_model_version_status
    import capo_iot_events.types.alarm_notification
    import capo_iot_events.types.alarm_rule
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.attribute_json_path
    import capo_iot_events.types.severity
    import capo_iot_events.types.status_message
    import capo_iot_events.types.timestamp


class DescribeAlarmModelResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The time the alarm model was created, in the Unix epoch format.</p>"""
    alarm_model_arn: NotRequired["capo_iot_events.types.alarm_model_arn.AlarmModelArn"]
    """<p>The ARN of the alarm model. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    alarm_model_version: NotRequired[
        "capo_iot_events.types.alarm_model_version.AlarmModelVersion"
    ]
    """<p>The version of the alarm model.</p>"""
    last_update_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The time the alarm model was last updated, in the Unix epoch format.</p>"""
    status: NotRequired[
        "capo_iot_events.types.alarm_model_version_status.AlarmModelVersionStatus"
    ]
    """<p>The status of the alarm model. The status can be one of the following values:</p> <ul> <li> <p> <code>ACTIVE</code> - The alarm model is active and it's ready to evaluate data.</p> </li> <li> <p> <code>ACTIVATING</code> - AWS IoT Events is activating your alarm model. Activating an alarm model can take up to a few minutes.</p> </li> <li> <p> <code>INACTIVE</code> - The alarm model is inactive, so it isn't ready to evaluate data. Check your alarm model information and update the alarm model.</p> </li> <li> <p> <code>FAILED</code> - You couldn't create or update the alarm model. Check your alarm model information and try again.</p> </li> </ul>"""
    status_message: NotRequired["capo_iot_events.types.status_message.StatusMessage"]
    """<p> Contains information about the status of the alarm model. </p>"""
    alarm_model_name: NotRequired[
        "capo_iot_events.types.alarm_model_name.AlarmModelName"
    ]
    """<p>The name of the alarm model.</p>"""
    alarm_model_description: NotRequired[
        "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
    ]
    """<p>The description of the alarm model.</p>"""
    role_arn: NotRequired[
        "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    key: NotRequired["capo_iot_events.types.attribute_json_path.AttributeJsonPath"]
    """<p>An input attribute used as a key to create an alarm. AWS IoT Events routes <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html">inputs</a> associated with this key to the alarm.</p>"""
    severity: NotRequired["capo_iot_events.types.severity.Severity"]
    """<p>A non-negative integer that reflects the severity level of the alarm.</p>"""
    alarm_rule: NotRequired["capo_iot_events.types.alarm_rule.AlarmRule"]
    """<p>Defines when your alarm is invoked.</p>"""
    alarm_notification: NotRequired[
        "capo_iot_events.types.alarm_notification.AlarmNotification"
    ]
    """<p>Contains information about one or more notification actions.</p>"""
    alarm_event_actions: NotRequired[
        "capo_iot_events.types.alarm_event_actions.AlarmEventActions"
    ]
    """<p>Contains information about one or more alarm actions.</p>"""
    alarm_capabilities: NotRequired[
        "capo_iot_events.types.alarm_capabilities.AlarmCapabilities"
    ]
    """<p>Contains the configuration information of alarm state changes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlarmModelResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_iot_events.types.timestamp

        out["creationTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "alarm_model_arn" in value:
        out["alarmModelArn"] = value["alarm_model_arn"]
    if "alarm_model_version" in value:
        out["alarmModelVersion"] = value["alarm_model_version"]
    if "last_update_time" in value:
        import capo_iot_events.types.timestamp

        out["lastUpdateTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    if "status" in value:
        import capo_iot_events.types.alarm_model_version_status

        out["status"] = capo_iot_events.types.alarm_model_version_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "alarm_model_name" in value:
        out["alarmModelName"] = value["alarm_model_name"]
    if "alarm_model_description" in value:
        out["alarmModelDescription"] = value["alarm_model_description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "key" in value:
        out["key"] = value["key"]
    if "severity" in value:
        out["severity"] = value["severity"]
    if "alarm_rule" in value:
        import capo_iot_events.types.alarm_rule

        out["alarmRule"] = capo_iot_events.types.alarm_rule.serialize_json(
            value["alarm_rule"]
        )
    if "alarm_notification" in value:
        import capo_iot_events.types.alarm_notification

        out["alarmNotification"] = (
            capo_iot_events.types.alarm_notification.serialize_json(
                value["alarm_notification"]
            )
        )
    if "alarm_event_actions" in value:
        import capo_iot_events.types.alarm_event_actions

        out["alarmEventActions"] = (
            capo_iot_events.types.alarm_event_actions.serialize_json(
                value["alarm_event_actions"]
            )
        )
    if "alarm_capabilities" in value:
        import capo_iot_events.types.alarm_capabilities

        out["alarmCapabilities"] = (
            capo_iot_events.types.alarm_capabilities.serialize_json(
                value["alarm_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAlarmModelResponse:
    out: DescribeAlarmModelResponse = {}  # type: ignore[typeddict-item]
    if data.get("creationTime") is not None:
        import capo_iot_events.types.timestamp

        out["creation_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("alarmModelArn") is not None:
        out["alarm_model_arn"] = data["alarmModelArn"]
    if data.get("alarmModelVersion") is not None:
        out["alarm_model_version"] = data["alarmModelVersion"]
    if data.get("lastUpdateTime") is not None:
        import capo_iot_events.types.timestamp

        out["last_update_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    if data.get("status") is not None:
        import capo_iot_events.types.alarm_model_version_status

        out["status"] = (
            capo_iot_events.types.alarm_model_version_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    if data.get("alarmModelDescription") is not None:
        out["alarm_model_description"] = data["alarmModelDescription"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("alarmRule") is not None:
        import capo_iot_events.types.alarm_rule

        out["alarm_rule"] = capo_iot_events.types.alarm_rule.deserialize_json(
            data["alarmRule"]
        )
    if data.get("alarmNotification") is not None:
        import capo_iot_events.types.alarm_notification

        out["alarm_notification"] = (
            capo_iot_events.types.alarm_notification.deserialize_json(
                data["alarmNotification"]
            )
        )
    if data.get("alarmEventActions") is not None:
        import capo_iot_events.types.alarm_event_actions

        out["alarm_event_actions"] = (
            capo_iot_events.types.alarm_event_actions.deserialize_json(
                data["alarmEventActions"]
            )
        )
    if data.get("alarmCapabilities") is not None:
        import capo_iot_events.types.alarm_capabilities

        out["alarm_capabilities"] = (
            capo_iot_events.types.alarm_capabilities.deserialize_json(
                data["alarmCapabilities"]
            )
        )
    return out
