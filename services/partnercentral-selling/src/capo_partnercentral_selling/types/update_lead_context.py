"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateLeadContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_customer
    import capo_partnercentral_selling.types.lead_insights
    import capo_partnercentral_selling.types.lead_interaction
    import capo_partnercentral_selling.types.lead_qualification_status


class UpdateLeadContext(TypedDict, closed=True):
    qualification_status: "capo_partnercentral_selling.types.lead_qualification_status.LeadQualificationStatus"
    """<p>The updated qualification status of the lead.</p>"""
    customer: "capo_partnercentral_selling.types.lead_customer.LeadCustomer"
    """<p>Updated customer information associated with the lead.</p>"""
    interaction: NotRequired[
        "capo_partnercentral_selling.types.lead_interaction.LeadInteraction"
    ]
    """<p>Updated interaction details for the lead context.</p>"""
    insights: NotRequired[
        "capo_partnercentral_selling.types.lead_insights.LeadInsights"
    ]
    """<p>Insights that AI generates and associates with the lead. These insights provide automated analysis to help partners assess the lead quality and readiness.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLeadContext) -> dict:
    out: dict = {}
    out["QualificationStatus"] = value.get("qualification_status", "Unqualified")
    import capo_partnercentral_selling.types.lead_customer

    out["Customer"] = (
        capo_partnercentral_selling.types.lead_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    if "interaction" in value:
        import capo_partnercentral_selling.types.lead_interaction

        out["Interaction"] = (
            capo_partnercentral_selling.types.lead_interaction.serialize_aws_json_1_0(
                value["interaction"]
            )
        )
    if "insights" in value:
        import capo_partnercentral_selling.types.lead_insights

        out["Insights"] = (
            capo_partnercentral_selling.types.lead_insights.serialize_aws_json_1_0(
                value["insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLeadContext:
    out: UpdateLeadContext = {}  # type: ignore[typeddict-item]
    if data.get("QualificationStatus") is not None:
        out["qualification_status"] = data["QualificationStatus"]
    else:
        out["qualification_status"] = "Unqualified"
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.lead_customer

        out["customer"] = (
            capo_partnercentral_selling.types.lead_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("UpdateLeadContext.customer required")
    if data.get("Interaction") is not None:
        import capo_partnercentral_selling.types.lead_interaction

        out["interaction"] = (
            capo_partnercentral_selling.types.lead_interaction.deserialize_aws_json_1_0(
                data["Interaction"]
            )
        )
    if data.get("Insights") is not None:
        import capo_partnercentral_selling.types.lead_insights

        out["insights"] = (
            capo_partnercentral_selling.types.lead_insights.deserialize_aws_json_1_0(
                data["Insights"]
            )
        )
    return out


def redact_sensitive(value: UpdateLeadContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer" in value:
        import capo_partnercentral_selling.types.lead_customer

        out["customer"] = (
            capo_partnercentral_selling.types.lead_customer.redact_sensitive(
                value["customer"]
            )
        )
    if "interaction" in value:
        import capo_partnercentral_selling.types.lead_interaction

        out["interaction"] = (
            capo_partnercentral_selling.types.lead_interaction.redact_sensitive(
                value["interaction"]
            )
        )
    return out
