"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.dedupe_string
    import capo_ssm_incidents.types.impact
    import capo_ssm_incidents.types.incident_summary
    import capo_ssm_incidents.types.incident_title
    import capo_ssm_incidents.types.notification_target_set
    import capo_ssm_incidents.types.tag_map


class IncidentTemplate(TypedDict, closed=True):
    title: "capo_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident. </p>"""
    impact: "capo_ssm_incidents.types.impact.Impact"
    """<p>The impact of the incident on your customers and applications.</p> <p class="title"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    summary: NotRequired["capo_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context.</p>"""
    dedupe_string: NotRequired["capo_ssm_incidents.types.dedupe_string.DedupeString"]
    """<p>The string Incident Manager uses to prevent the same root cause from creating multiple incidents in the same account.</p> <p>A deduplication string is a term or phrase the system uses to check for duplicate incidents. If you specify a deduplication string, Incident Manager searches for open incidents that contain the same string in the <code>dedupeString</code> field when it creates the incident. If a duplicate is detected, Incident Manager deduplicates the newer incident into the existing incident.</p> <note> <p>By default, Incident Manager automatically deduplicates multiple incidents created by the same Amazon CloudWatch alarm or Amazon EventBridge event. You don't have to enter your own deduplication string to prevent duplication for these resource types.</p> </note>"""
    notification_targets: NotRequired[
        "capo_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""
    incident_tags: NotRequired["capo_ssm_incidents.types.tag_map.TagMap"]
    """<p>Tags to assign to the template. When the <code>StartIncident</code> API action is called, Incident Manager assigns the tags specified in the template to the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentTemplate) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["impact"] = value["impact"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "dedupe_string" in value:
        out["dedupeString"] = value["dedupe_string"]
    if "notification_targets" in value:
        import capo_ssm_incidents.types.notification_target_set

        out["notificationTargets"] = (
            capo_ssm_incidents.types.notification_target_set.serialize_json(
                value["notification_targets"]
            )
        )
    if "incident_tags" in value:
        import capo_ssm_incidents.types.tag_map

        out["incidentTags"] = capo_ssm_incidents.types.tag_map.serialize_json(
            value["incident_tags"]
        )
    return out


def deserialize_json(data: dict) -> IncidentTemplate:
    out: IncidentTemplate = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("IncidentTemplate.title required")
    if data.get("impact") is not None:
        out["impact"] = data["impact"]
    else:
        raise DeserializationError("IncidentTemplate.impact required")
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    if data.get("dedupeString") is not None:
        out["dedupe_string"] = data["dedupeString"]
    if data.get("notificationTargets") is not None:
        import capo_ssm_incidents.types.notification_target_set

        out["notification_targets"] = (
            capo_ssm_incidents.types.notification_target_set.deserialize_json(
                data["notificationTargets"]
            )
        )
    if data.get("incidentTags") is not None:
        import capo_ssm_incidents.types.tag_map

        out["incident_tags"] = capo_ssm_incidents.types.tag_map.deserialize_json(
            data["incidentTags"]
        )
    return out
