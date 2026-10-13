"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInvitationPayload``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_invitation_customer
    import capo_partnercentral_selling.types.lead_invitation_interaction


class LeadInvitationPayload(TypedDict, closed=True):
    customer: "capo_partnercentral_selling.types.lead_invitation_customer.LeadInvitationCustomer"
    """<p>Contains information about the customer associated with the lead invitation. This data helps partners understand the customer's profile, industry, and business context to assess the lead opportunity.</p>"""
    interaction: "capo_partnercentral_selling.types.lead_invitation_interaction.LeadInvitationInteraction"
    """<p>Describes the interaction details associated with the lead, including the source of the lead generation and customer engagement information. This context helps partners evaluate the lead quality and engagement approach.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInvitationPayload) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.lead_invitation_customer

    out["Customer"] = (
        capo_partnercentral_selling.types.lead_invitation_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    import capo_partnercentral_selling.types.lead_invitation_interaction

    out["Interaction"] = (
        capo_partnercentral_selling.types.lead_invitation_interaction.serialize_aws_json_1_0(
            value["interaction"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInvitationPayload:
    out: LeadInvitationPayload = {}  # type: ignore[typeddict-item]
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.lead_invitation_customer

        out["customer"] = (
            capo_partnercentral_selling.types.lead_invitation_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("LeadInvitationPayload.customer required")
    if data.get("Interaction") is not None:
        import capo_partnercentral_selling.types.lead_invitation_interaction

        out["interaction"] = (
            capo_partnercentral_selling.types.lead_invitation_interaction.deserialize_aws_json_1_0(
                data["Interaction"]
            )
        )
    else:
        raise DeserializationError("LeadInvitationPayload.interaction required")
    return out


def redact_sensitive(value: LeadInvitationPayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer" in value:
        import capo_partnercentral_selling.types.lead_invitation_customer

        out["customer"] = (
            capo_partnercentral_selling.types.lead_invitation_customer.redact_sensitive(
                value["customer"]
            )
        )
    if "interaction" in value:
        import capo_partnercentral_selling.types.lead_invitation_interaction

        out["interaction"] = (
            capo_partnercentral_selling.types.lead_invitation_interaction.redact_sensitive(
                value["interaction"]
            )
        )
    return out
