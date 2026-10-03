"""Generated from Smithy shape ``com.amazonaws.iotevents#UpdateAlarmModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_capabilities
    import capo_iot_events.types.alarm_event_actions
    import capo_iot_events.types.alarm_model_description
    import capo_iot_events.types.alarm_model_name
    import capo_iot_events.types.alarm_notification
    import capo_iot_events.types.alarm_rule
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.severity


class UpdateAlarmModelRequest(TypedDict, closed=True):
    alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>The name of the alarm model.</p>"""
    alarm_model_description: NotRequired[
        "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
    ]
    """<p>The description of the alarm model.</p>"""
    role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    severity: NotRequired["capo_iot_events.types.severity.Severity"]
    """<p>A non-negative integer that reflects the severity level of the alarm.</p>"""
    alarm_rule: "capo_iot_events.types.alarm_rule.AlarmRule"
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
def serialize_json(value: UpdateAlarmModelRequest) -> dict:
    out: dict = {}
    if "alarm_model_description" in value:
        out["alarmModelDescription"] = value["alarm_model_description"]
    out["roleArn"] = value["role_arn"]
    if "severity" in value:
        out["severity"] = value["severity"]
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


def deserialize_json(data: dict) -> UpdateAlarmModelRequest:
    out: UpdateAlarmModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("alarmModelDescription") is not None:
        out["alarm_model_description"] = data["alarmModelDescription"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("UpdateAlarmModelRequest.role_arn required")
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("alarmRule") is not None:
        import capo_iot_events.types.alarm_rule

        out["alarm_rule"] = capo_iot_events.types.alarm_rule.deserialize_json(
            data["alarmRule"]
        )
    else:
        raise DeserializationError("UpdateAlarmModelRequest.alarm_rule required")
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
