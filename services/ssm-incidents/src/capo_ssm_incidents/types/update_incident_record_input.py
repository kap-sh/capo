"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateIncidentRecordInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.chat_channel
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_record_status
    import capo_ssm_incidents.types.incident_summary
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.notification_target_set


class UpdateIncidentRecordInput(TypedDict, closed=True):
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the operation only once with the specified details.</p>"""
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record you are updating.</p>"""
    title: NotRequired["capo_ssm_incidents.types.incident_title.IncidentTitle"]
    """<p>A brief description of the incident.</p>"""
    summary: NotRequired["capo_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>A longer description of what occurred during the incident.</p>"""
    impact: NotRequired["capo_ssm_incidents.types.impact.Impact"]
    """<p>Defines the impact of the incident to customers and applications. If you provide an impact for an incident, it overwrites the impact provided by the response plan.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    status: NotRequired[
        "capo_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    ]
    """<p>The status of the incident. Possible statuses are <code>Open</code> or <code>Resolved</code>.</p>"""
    chat_channel: NotRequired["capo_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel where responders can collaborate.</p>"""
    notification_targets: NotRequired[
        "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that Incident Manager notifies when a client updates an incident.</p> <p>Using multiple SNS topics creates redundancy in the event that a Region is down during the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIncidentRecordInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["arn"] = value["arn"]
    if "title" in value:
        out["title"] = value["title"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "impact" in value:
        out["impact"] = value["impact"]
    if "status" in value:
        out["status"] = value["status"]
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


def deserialize_json(data: dict) -> UpdateIncidentRecordInput:
    out: UpdateIncidentRecordInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateIncidentRecordInput.arn required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("impact") is not None:
        out["impact"] = data["impact"]
    if data.get("status") is not None:
        out["status"] = data["status"]
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
