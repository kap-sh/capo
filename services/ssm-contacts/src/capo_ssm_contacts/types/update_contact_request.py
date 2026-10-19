"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#UpdateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact_name
    import capo_ssm_contacts.types.plan
    import capo_ssm_contacts.types.ssm_contacts_arn


class UpdateContactRequest(TypedDict, closed=True):
    contact_id: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan you're updating.</p>"""
    display_name: NotRequired["capo_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    plan: NotRequired["capo_ssm_contacts.types.plan.Plan"]
    """<p>A list of stages. A contact has an engagement plan with stages for specified contact channels. An escalation plan uses these stages to contact specified contacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "plan" in value:
        import capo_ssm_contacts.types.plan

        out["Plan"] = capo_ssm_contacts.types.plan.serialize_aws_json_1_1(value["plan"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContactRequest:
    out: UpdateContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Plan") is not None:
        import capo_ssm_contacts.types.plan

        out["plan"] = capo_ssm_contacts.types.plan.deserialize_aws_json_1_1(
            data["Plan"]
        )
    return out
