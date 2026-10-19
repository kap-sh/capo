"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Engagement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.date_time
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.sender
    import capo_ssm_contacts.types.ssm_contacts_arn


class Engagement(TypedDict, closed=True):
    engagement_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the engagement.</p>"""
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the escalation plan or contact that Incident Manager is engaging.</p>"""
    sender: "capo_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    incident_id: NotRequired["capo_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that's engaging the contact.</p>"""
    start_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement began.</p>"""
    stop_time: NotRequired["capo_ssm_contacts.types.date_time.DateTime"]
    """<p>The time that the engagement ended.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Engagement) -> dict:
    out: dict = {}
    out["EngagementArn"] = value["engagement_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Sender"] = value["sender"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "start_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StartTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "stop_time" in value:
        import capo_ssm_contacts.types.date_time

        out["StopTime"] = capo_ssm_contacts.types.date_time.serialize_aws_json_1_1(
            value["stop_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Engagement:
    out: Engagement = {}  # type: ignore[typeddict-item]
    if data.get("EngagementArn") is not None:
        out["engagement_arn"] = data["EngagementArn"]
    else:
        out["engagement_arn"] = ""
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("Sender") is not None:
        out["sender"] = data["Sender"]
    else:
        out["sender"] = ""
    if data.get("IncidentId") is not None:
        out["incident_id"] = data["IncidentId"]
    if data.get("StartTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["start_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if data.get("StopTime") is not None:
        import capo_ssm_contacts.types.date_time

        out["stop_time"] = capo_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
            data["StopTime"]
        )
    return out
