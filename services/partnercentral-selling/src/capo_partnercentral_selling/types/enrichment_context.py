"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EnrichmentContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.invitation_prospecting_result_aws
    import capo_partnercentral_selling.types.lead_insights


class EnrichmentContext(TypedDict, closed=True):
    prospecting_result_aws: NotRequired[
        "capo_partnercentral_selling.types.invitation_prospecting_result_aws.InvitationProspectingResultAws"
    ]
    """<p>The customer account data and propensity insights for the prospected account. It includes geographic, industry, and segment classifications, along with engagement and solution scoring.</p>"""
    lead_insights: NotRequired[
        "capo_partnercentral_selling.types.lead_insights.LeadInsights"
    ]
    """<p>The AI-generated lead readiness score for this lead. Use this score to assess lead quality and prioritize engagement efforts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnrichmentContext) -> dict:
    out: dict = {}
    if "prospecting_result_aws" in value:
        import capo_partnercentral_selling.types.invitation_prospecting_result_aws

        out["ProspectingResultAws"] = (
            capo_partnercentral_selling.types.invitation_prospecting_result_aws.serialize_aws_json_1_0(
                value["prospecting_result_aws"]
            )
        )
    if "lead_insights" in value:
        import capo_partnercentral_selling.types.lead_insights

        out["LeadInsights"] = (
            capo_partnercentral_selling.types.lead_insights.serialize_aws_json_1_0(
                value["lead_insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnrichmentContext:
    out: EnrichmentContext = {}  # type: ignore[typeddict-item]
    if data.get("ProspectingResultAws") is not None:
        import capo_partnercentral_selling.types.invitation_prospecting_result_aws

        out["prospecting_result_aws"] = (
            capo_partnercentral_selling.types.invitation_prospecting_result_aws.deserialize_aws_json_1_0(
                data["ProspectingResultAws"]
            )
        )
    if data.get("LeadInsights") is not None:
        import capo_partnercentral_selling.types.lead_insights

        out["lead_insights"] = (
            capo_partnercentral_selling.types.lead_insights.deserialize_aws_json_1_0(
                data["LeadInsights"]
            )
        )
    return out


def redact_sensitive(value: EnrichmentContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "prospecting_result_aws" in value:
        import capo_partnercentral_selling.types.invitation_prospecting_result_aws

        out["prospecting_result_aws"] = (
            capo_partnercentral_selling.types.invitation_prospecting_result_aws.redact_sensitive(
                value["prospecting_result_aws"]
            )
        )
    return out
