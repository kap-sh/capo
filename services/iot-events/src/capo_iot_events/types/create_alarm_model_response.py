"""Generated from Smithy shape ``com.amazonaws.iotevents#CreateAlarmModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.alarm_model_arn
    import capo_iot_events.types.alarm_model_version
    import capo_iot_events.types.alarm_model_version_status
    import capo_iot_events.types.timestamp


class CreateAlarmModelResponse(TypedDict, closed=True):
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


# --- restJson1 ser/de ---
def serialize_json(value: CreateAlarmModelResponse) -> dict:
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
    return out


def deserialize_json(data: dict) -> CreateAlarmModelResponse:
    out: CreateAlarmModelResponse = {}  # type: ignore[typeddict-item]
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
    return out
