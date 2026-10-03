"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateAlarmModelRequest``."""

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
    import capo_iot_events.types.attribute_json_path
    import capo_iot_events.types.severity
    import capo_iot_events.types.tags


class CreateAlarmModelRequest(TypedDict, closed=True):
    alarm_model_name: "capo_iot_events.types.alarm_model_name.AlarmModelName"
    """<p>A unique name that helps you identify the alarm model. You can't change this name after you create the alarm model.</p>"""
    alarm_model_description: NotRequired[
        "capo_iot_events.types.alarm_model_description.AlarmModelDescription"
    ]
    """<p>A description that tells you what the alarm model detects.</p>"""
    role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    tags: NotRequired["capo_iot_events.types.tags.Tags"]
    """<p>A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html">Tagging your AWS IoT Events resources</a> in the <i>AWS IoT Events Developer Guide</i>.</p> <p>You can create up to 50 tags for one alarm model.</p>"""
    key: NotRequired["capo_iot_events.types.attribute_json_path.AttributeJsonPath"]
    """<p>An input attribute used as a key to create an alarm. AWS IoT Events routes <a href="https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html">inputs</a> associated with this key to the alarm.</p>"""
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
def serialize_json(value: CreateAlarmModelRequest) -> dict:
    out: dict = {}
    out["alarmModelName"] = value["alarm_model_name"]
    if "alarm_model_description" in value:
        out["alarmModelDescription"] = value["alarm_model_description"]
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_iot_events.types.tags

        out["tags"] = capo_iot_events.types.tags.serialize_json(value["tags"])
    if "key" in value:
        out["key"] = value["key"]
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


def deserialize_json(data: dict) -> CreateAlarmModelRequest:
    out: CreateAlarmModelRequest = {}  # type: ignore[typeddict-item]
    if data.get("alarmModelName") is not None:
        out["alarm_model_name"] = data["alarmModelName"]
    else:
        raise DeserializationError("CreateAlarmModelRequest.alarm_model_name required")
    if data.get("alarmModelDescription") is not None:
        out["alarm_model_description"] = data["alarmModelDescription"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateAlarmModelRequest.role_arn required")
    if data.get("tags") is not None:
        import capo_iot_events.types.tags

        out["tags"] = capo_iot_events.types.tags.deserialize_json(data["tags"])
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("severity") is not None:
        out["severity"] = data["severity"]
    if data.get("alarmRule") is not None:
        import capo_iot_events.types.alarm_rule

        out["alarm_rule"] = capo_iot_events.types.alarm_rule.deserialize_json(
            data["alarmRule"]
        )
    else:
        raise DeserializationError("CreateAlarmModelRequest.alarm_rule required")
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
