"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#StartEngagementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.content
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.public_content
    import capo_ssm_contacts.types.public_subject
    import capo_ssm_contacts.types.sender
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.subject


class StartEngagementRequest(TypedDict, closed=True):
    contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact being engaged.</p>"""
    sender: "capo_ssm_contacts.types.sender.Sender"
    """<p>The user that started the engagement.</p>"""
    subject: "capo_ssm_contacts.types.subject.Subject"
    """<p>The secure subject of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>"""
    content: "capo_ssm_contacts.types.content.Content"
    """<p>The secure content of the message that was sent to the contact. Use this field for engagements to <code>VOICE</code> or <code>EMAIL</code>.</p>"""
    public_subject: NotRequired["capo_ssm_contacts.types.public_subject.PublicSubject"]
    """<p>The insecure subject of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    public_content: NotRequired["capo_ssm_contacts.types.public_content.PublicContent"]
    """<p>The insecure content of the message that was sent to the contact. Use this field for engagements to <code>SMS</code>.</p>"""
    incident_id: NotRequired["capo_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The ARN of the incident that the engagement is part of.</p>"""
    idempotency_token: NotRequired[
        "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartEngagementRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["Sender"] = value["sender"]
    out["Subject"] = value["subject"]
    out["Content"] = value["content"]
    if "public_subject" in value:
        out["PublicSubject"] = value["public_subject"]
    if "public_content" in value:
        out["PublicContent"] = value["public_content"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartEngagementRequest:
    out: StartEngagementRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("Sender") is not None:
        out["sender"] = data["Sender"]
    else:
        out["sender"] = ""
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    else:
        out["subject"] = ""
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        out["content"] = ""
    if data.get("PublicSubject") is not None:
        out["public_subject"] = data["PublicSubject"]
    if data.get("PublicContent") is not None:
        out["public_content"] = data["PublicContent"]
    if data.get("IncidentId") is not None:
        out["incident_id"] = data["IncidentId"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
