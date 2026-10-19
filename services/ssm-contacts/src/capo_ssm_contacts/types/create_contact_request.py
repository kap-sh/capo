"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact_alias
    import capo_ssm_contacts.types.contact_name
    import capo_ssm_contacts.types.contact_type
    import capo_ssm_contacts.types.idempotency_token
    import capo_ssm_contacts.types.plan
    import capo_ssm_contacts.types.tags_list


class CreateContactRequest(TypedDict, closed=True):
    alias: "capo_ssm_contacts.types.contact_alias.ContactAlias"
    """<p>The short name to quickly identify a contact or escalation plan. The contact alias must be unique and identifiable.</p>"""
    display_name: NotRequired["capo_ssm_contacts.types.contact_name.ContactName"]
    """<p>The full name of the contact or escalation plan.</p>"""
    type: "capo_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact to create.</p> <ul> <li> <p> <code>PERSONAL</code>: A single, individual contact.</p> </li> <li> <p> <code>ESCALATION</code>: An escalation plan.</p> </li> <li> <p> <code>ONCALL_SCHEDULE</code>: An on-call schedule.</p> </li> </ul>"""
    plan: "capo_ssm_contacts.types.plan.Plan"
    """<p>A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.</p>"""
    tags: NotRequired["capo_ssm_contacts.types.tags_list.TagsList"]
    """<p>Adds a tag to the target. You can only tag resources created in the first Region of your replication set.</p>"""
    idempotency_token: NotRequired[
        "capo_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactRequest) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    import capo_ssm_contacts.types.contact_type

    out["Type"] = capo_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    import capo_ssm_contacts.types.plan

    out["Plan"] = capo_ssm_contacts.types.plan.serialize_aws_json_1_1(value["plan"])
    if "tags" in value:
        import capo_ssm_contacts.types.tags_list

        out["Tags"] = capo_ssm_contacts.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactRequest:
    out: CreateContactRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Plan") is not None:
        import capo_ssm_contacts.types.plan

        out["plan"] = capo_ssm_contacts.types.plan.deserialize_aws_json_1_1(
            data["Plan"]
        )
    else:
        raise DeserializationError("CreateContactRequest.plan required")
    if data.get("Tags") is not None:
        import capo_ssm_contacts.types.tags_list

        out["tags"] = capo_ssm_contacts.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
