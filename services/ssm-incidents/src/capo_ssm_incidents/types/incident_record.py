"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.automation_execution_set
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.dedupe_string
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_record_source
    import capo_ssm_incidents.types.incident_record_status
    import capo_ssm_incidents.types.incident_summary
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.notification_target_set


class IncidentRecord(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record.</p>"""
    title: "capo_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident.</p>"""
    summary: NotRequired["capo_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context of the incident.</p>"""
    status: "capo_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    """<p>The current status of the incident.</p>"""
    impact: "capo_ssm_incidents.types.impact.Impact"
    """<p>The impact of the incident on customers and applications.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when Incident Manager created the incident record.</p>"""
    resolved_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the incident was resolved. This appears as a timeline event.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp for when the incident was most recently modified.</p>"""
    last_modified_by: "capo_ssm_incidents.types.arn.Arn"
    """<p>Who modified the incident most recently.</p>"""
    automation_executions: NotRequired[
        "capo_ssm_incidents.types.automation_execution_set.AutomationExecutionSet"
    ]
    """<p>The runbook, or automation document, that's run at the beginning of the incident.</p>"""
    incident_record_source: (
        "capo_ssm_incidents.types.incident_record_source.IncidentRecordSource"
    )
    """<p>Details about the action that started the incident.</p>"""
    dedupe_string: "capo_ssm_incidents.types.dedupe_string.DedupeString"
    """<p>The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.</p>"""
    chat_channel: NotRequired["capo_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The chat channel used for collaboration during an incident.</p>"""
    notification_targets: NotRequired[
        "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecord) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    if "summary" in value:
        out["summary"] = value["summary"]
    out["status"] = value["status"]
    out["impact"] = value["impact"]
    import capo_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = capo_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "resolved_time" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        out["resolvedTime"] = (
            capo_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["resolved_time"]
            )
        )
    import capo_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        capo_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    if "automation_executions" in value:
        import capo_ssm_incidents.types.automation_execution_set

        out["automationExecutions"] = (
            capo_ssm_incidents.types.automation_execution_set.serialize_json(
                value["automation_executions"]
            )
        )
    import capo_ssm_incidents.types.incident_record_source

    out["incidentRecordSource"] = (
        capo_ssm_incidents.types.incident_record_source.serialize_json(
            value["incident_record_source"]
        )
    )
    out["dedupeString"] = value["dedupe_string"]
    if "chat_channel" in value:
        import capo_ssm_incidents.types.chat_channel

        out["chatChannel"] = capo_ssm_incidents.types.chat_channel.serialize_json(
            value["chat_channel"]
        )
    if "notification_targets" in value:
        import capo_ssm_incidents.types.notification_target_set

        out["notificationTargets"] = (
            capo_ssm_incidents.types.notification_target_set.serialize_json(
                value["notification_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> IncidentRecord:
    out: IncidentRecord = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IncidentRecord.arn required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("IncidentRecord.title required")
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        raise DeserializationError("IncidentRecord.status required")
    if data.get("impact") is not None:
        out["impact"] = data["impact"]
    else:
        raise DeserializationError("IncidentRecord.impact required")
    if data.get("creationTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.creation_time required")
    if data.get("resolvedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["resolved_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["resolvedTime"]
            )
        )
    if data.get("lastModifiedTime") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.last_modified_time required")
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("IncidentRecord.last_modified_by required")
    if data.get("automationExecutions") is not None:
        import capo_ssm_incidents.types.automation_execution_set

        out["automation_executions"] = (
            capo_ssm_incidents.types.automation_execution_set.deserialize_json(
                data["automationExecutions"]
            )
        )
    if data.get("incidentRecordSource") is not None:
        import capo_ssm_incidents.types.incident_record_source

        out["incident_record_source"] = (
            capo_ssm_incidents.types.incident_record_source.deserialize_json(
                data["incidentRecordSource"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.incident_record_source required")
    if data.get("dedupeString") is not None:
        out["dedupe_string"] = data["dedupeString"]
    else:
        raise DeserializationError("IncidentRecord.dedupe_string required")
    if data.get("chatChannel") is not None:
        import capo_ssm_incidents.types.chat_channel

        out["chat_channel"] = capo_ssm_incidents.types.chat_channel.deserialize_json(
            data["chatChannel"]
        )
    if data.get("notificationTargets") is not None:
        import capo_ssm_incidents.types.notification_target_set

        out["notification_targets"] = (
            capo_ssm_incidents.types.notification_target_set.deserialize_json(
                data["notificationTargets"]
            )
        )
    return out
