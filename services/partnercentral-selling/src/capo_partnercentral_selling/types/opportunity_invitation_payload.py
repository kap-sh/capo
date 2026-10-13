"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityInvitationPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_customer
    import capo_partnercentral_selling.types.project_details
    import capo_partnercentral_selling.types.receiver_responsibility_list
    import capo_partnercentral_selling.types.sender_contact_list


class OpportunityInvitationPayload(TypedDict, closed=True):
    sender_contacts: NotRequired[
        "capo_partnercentral_selling.types.sender_contact_list.SenderContactList"
    ]
    """<p>Represents the contact details of the AWS representatives involved in sending the Engagement Invitation. These contacts are opportunity stakeholders.</p>"""
    receiver_responsibilities: "capo_partnercentral_selling.types.receiver_responsibility_list.ReceiverResponsibilityList"
    """<p>Outlines the responsibilities or expectations of the receiver in the context of the invitation.</p>"""
    customer: "capo_partnercentral_selling.types.engagement_customer.EngagementCustomer"
    """<p>Contains information about the customer related to the opportunity in the Engagement Invitation. This data helps partners understand the customer’s profile and requirements.</p>"""
    project: "capo_partnercentral_selling.types.project_details.ProjectDetails"
    """<p>Describes the project details associated with the opportunity, including the customer’s needs and the scope of work expected to be performed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityInvitationPayload) -> dict:
    out: dict = {}
    if "sender_contacts" in value:
        import capo_partnercentral_selling.types.sender_contact_list

        out["SenderContacts"] = (
            capo_partnercentral_selling.types.sender_contact_list.serialize_aws_json_1_0(
                value["sender_contacts"]
            )
        )
    import capo_partnercentral_selling.types.receiver_responsibility_list

    out["ReceiverResponsibilities"] = (
        capo_partnercentral_selling.types.receiver_responsibility_list.serialize_aws_json_1_0(
            value["receiver_responsibilities"]
        )
    )
    import capo_partnercentral_selling.types.engagement_customer

    out["Customer"] = (
        capo_partnercentral_selling.types.engagement_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    import capo_partnercentral_selling.types.project_details

    out["Project"] = (
        capo_partnercentral_selling.types.project_details.serialize_aws_json_1_0(
            value["project"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunityInvitationPayload:
    out: OpportunityInvitationPayload = {}  # type: ignore[typeddict-item]
    if data.get("SenderContacts") is not None:
        import capo_partnercentral_selling.types.sender_contact_list

        out["sender_contacts"] = (
            capo_partnercentral_selling.types.sender_contact_list.deserialize_aws_json_1_0(
                data["SenderContacts"]
            )
        )
    if data.get("ReceiverResponsibilities") is not None:
        import capo_partnercentral_selling.types.receiver_responsibility_list

        out["receiver_responsibilities"] = (
            capo_partnercentral_selling.types.receiver_responsibility_list.deserialize_aws_json_1_0(
                data["ReceiverResponsibilities"]
            )
        )
    else:
        raise DeserializationError(
            "OpportunityInvitationPayload.receiver_responsibilities required"
        )
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            capo_partnercentral_selling.types.engagement_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("OpportunityInvitationPayload.customer required")
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.project_details

        out["project"] = (
            capo_partnercentral_selling.types.project_details.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    else:
        raise DeserializationError("OpportunityInvitationPayload.project required")
    return out


def redact_sensitive(value: OpportunityInvitationPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_contacts" in value:
        import capo_partnercentral_selling.types.sender_contact_list

        out["sender_contacts"] = (
            capo_partnercentral_selling.types.sender_contact_list.redact_sensitive(
                value["sender_contacts"]
            )
        )
    if "customer" in value:
        import capo_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            capo_partnercentral_selling.types.engagement_customer.redact_sensitive(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project_details

        out["project"] = (
            capo_partnercentral_selling.types.project_details.redact_sensitive(
                value["project"]
            )
        )
    return out
