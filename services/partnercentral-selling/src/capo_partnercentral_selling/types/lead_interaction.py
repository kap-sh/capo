"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInteraction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.customer_action
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_use_case
    import capo_partnercentral_selling.types.lead_business_problem
    import capo_partnercentral_selling.types.lead_contact
    import capo_partnercentral_selling.types.lead_source_id
    import capo_partnercentral_selling.types.lead_source_name
    import capo_partnercentral_selling.types.lead_source_type


class LeadInteraction(TypedDict, closed=True):
    source_type: "capo_partnercentral_selling.types.lead_source_type.LeadSourceType"
    """<p>Specifies the type of source that generated the lead interaction, such as "Event", "Website", "Referral", or "Campaign". This categorization helps track lead generation effectiveness across different channels.</p>"""
    source_id: "capo_partnercentral_selling.types.lead_source_id.LeadSourceId"
    """<p>The unique identifier of the specific source that generated the lead interaction. This ID provides traceability back to the original lead generation activity.</p>"""
    source_name: "capo_partnercentral_selling.types.lead_source_name.LeadSourceName"
    """<p>The descriptive name of the source that generated the lead interaction, providing a human-readable identifier for the lead generation channel or activity.</p>"""
    usecase: NotRequired[
        "capo_partnercentral_selling.types.engagement_use_case.EngagementUseCase"
    ]
    """<p>Describes the specific use case or business scenario discussed during the lead interaction. This helps categorize the customer's interests and potential solutions.</p>"""
    interaction_date: NotRequired[
        "capo_partnercentral_selling.types.date_time.DateTime"
    ]
    """<p>The date and time when the lead interaction occurred, in ISO 8601 format (UTC). This timestamp helps track the chronology of lead engagement activities.</p>"""
    customer_action: "capo_partnercentral_selling.types.customer_action.CustomerAction"
    """<p>Describes the action taken by the customer during or as a result of the interaction, such as requesting information, scheduling a meeting, or expressing interest in a solution.</p>"""
    business_problem: NotRequired[
        "capo_partnercentral_selling.types.lead_business_problem.LeadBusinessProblem"
    ]
    """<p>Describes the business problem or challenge that the customer discussed during the interaction. This information helps qualify the lead and identify appropriate solutions.</p>"""
    contact: "capo_partnercentral_selling.types.lead_contact.LeadContact"
    """<p>Contains contact information for the customer representative involved in the lead interaction, including their name, title, and contact details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInteraction) -> dict:
    out: dict = {}
    out["SourceType"] = value.get("source_type", "")
    out["SourceId"] = value.get("source_id", "")
    out["SourceName"] = value.get("source_name", "")
    if "usecase" in value:
        out["Usecase"] = value["usecase"]
    if "interaction_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["InteractionDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["interaction_date"]
            )
        )
    out["CustomerAction"] = value.get("customer_action", "")
    if "business_problem" in value:
        out["BusinessProblem"] = value["business_problem"]
    import capo_partnercentral_selling.types.lead_contact

    out["Contact"] = (
        capo_partnercentral_selling.types.lead_contact.serialize_aws_json_1_0(
            value["contact"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInteraction:
    out: LeadInteraction = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        out["source_type"] = data["SourceType"]
    else:
        out["source_type"] = ""
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    else:
        out["source_id"] = ""
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    else:
        out["source_name"] = ""
    if data.get("Usecase") is not None:
        out["usecase"] = data["Usecase"]
    if data.get("InteractionDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["interaction_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["InteractionDate"]
            )
        )
    if data.get("CustomerAction") is not None:
        out["customer_action"] = data["CustomerAction"]
    else:
        out["customer_action"] = ""
    if data.get("BusinessProblem") is not None:
        out["business_problem"] = data["BusinessProblem"]
    if data.get("Contact") is not None:
        import capo_partnercentral_selling.types.lead_contact

        out["contact"] = (
            capo_partnercentral_selling.types.lead_contact.deserialize_aws_json_1_0(
                data["Contact"]
            )
        )
    else:
        raise DeserializationError("LeadInteraction.contact required")
    return out
