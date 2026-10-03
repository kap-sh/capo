"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInvitationInteraction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_use_case
    import capo_partnercentral_selling.types.job_title
    import capo_partnercentral_selling.types.lead_source_id
    import capo_partnercentral_selling.types.lead_source_name
    import capo_partnercentral_selling.types.lead_source_type


class LeadInvitationInteraction(TypedDict, closed=True):
    source_type: "capo_partnercentral_selling.types.lead_source_type.LeadSourceType"
    """<p>Specifies the type of source that generated the lead interaction, such as "Event", "Website", or "Campaign". This helps partners understand the lead generation channel and assess lead quality based on the source type.</p>"""
    source_id: "capo_partnercentral_selling.types.lead_source_id.LeadSourceId"
    """<p>The unique identifier of the specific source that generated the lead interaction. This provides traceability to the original lead generation activity for reference and follow-up purposes.</p>"""
    source_name: "capo_partnercentral_selling.types.lead_source_name.LeadSourceName"
    """<p>The descriptive name of the source that generated the lead interaction. This human-readable identifier helps partners understand the specific lead generation channel or campaign that created the opportunity.</p>"""
    usecase: NotRequired[
        "capo_partnercentral_selling.types.engagement_use_case.EngagementUseCase"
    ]
    """<p>Describes the specific use case or business scenario associated with the lead interaction. This information helps partners understand the customer's interests and potential solution requirements.</p>"""
    contact_business_title: "capo_partnercentral_selling.types.job_title.JobTitle"
    """<p>The business title or job role of the customer contact involved in the lead interaction. This helps partners identify the decision-making level and engagement approach for the lead.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInvitationInteraction) -> dict:
    out: dict = {}
    out["SourceType"] = value.get("source_type", "")
    out["SourceId"] = value.get("source_id", "")
    out["SourceName"] = value.get("source_name", "")
    if "usecase" in value:
        out["Usecase"] = value["usecase"]
    out["ContactBusinessTitle"] = value["contact_business_title"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInvitationInteraction:
    out: LeadInvitationInteraction = {}  # type: ignore[typeddict-item]
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
    if data.get("ContactBusinessTitle") is not None:
        out["contact_business_title"] = data["ContactBusinessTitle"]
    else:
        raise DeserializationError(
            "LeadInvitationInteraction.contact_business_title required"
        )
    return out
