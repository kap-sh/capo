"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Contact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact_alias
    import capo_ssm_contacts.types.contact_name
    import capo_ssm_contacts.types.contact_type
    import capo_ssm_contacts.types.ssm_contacts_arn


class Contact(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""
    alias: "capo_ssm_contacts.types.contact_alias.ContactAlias"
    """<p>The unique and identifiable alias of the contact or escalation plan.</p>"""
    display_name: NotRequired["capo_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    type: "capo_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact.</p> <ul> <li> <p> <code>PERSONAL</code>: A single, individual contact.</p> </li> <li> <p> <code>ESCALATION</code>: An escalation plan.</p> </li> <li> <p> <code>ONCALL_SCHEDULE</code>: An on-call schedule.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Contact) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["Alias"] = value["alias"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import capo_ssm_contacts.types.contact_type

    out["Type"] = capo_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Contact:
    out: Contact = {}  # type: ignore[typeddict-item]
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Type") is not None:
        import capo_ssm_contacts.types.contact_type

        out["type"] = capo_ssm_contacts.types.contact_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_ssm_contacts.types.contact_type.ContactType", ""
        )
    return out
