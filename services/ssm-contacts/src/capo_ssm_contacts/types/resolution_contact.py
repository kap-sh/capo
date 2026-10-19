"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ResolutionContact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contact_type
    import capo_ssm_contacts.types.ssm_contacts_arn
    import capo_ssm_contacts.types.stage_index


class ResolutionContact(TypedDict, closed=True):
    contact_arn: "capo_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of a contact in the engagement resolution process. </p>"""
    type: "capo_ssm_contacts.types.contact_type.ContactType"
    """<p>The type of contact for a resolution step.</p>"""
    stage_index: NotRequired["capo_ssm_contacts.types.stage_index.StageIndex"]
    """<p>The stage in the escalation plan that resolves to this contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResolutionContact) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    import capo_ssm_contacts.types.contact_type

    out["Type"] = capo_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "stage_index" in value:
        out["StageIndex"] = value["stage_index"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResolutionContact:
    out: ResolutionContact = {}  # type: ignore[typeddict-item]
    if data.get("ContactArn") is not None:
        out["contact_arn"] = data["ContactArn"]
    else:
        out["contact_arn"] = ""
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
    if data.get("StageIndex") is not None:
        out["stage_index"] = data["StageIndex"]
    return out
