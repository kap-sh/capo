"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#InvitationProspectingResultAws``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.prospecting_insights
    import capo_partnercentral_selling.types.prospecting_result_customer


class InvitationProspectingResultAws(TypedDict, closed=True):
    customer: NotRequired[
        "capo_partnercentral_selling.types.prospecting_result_customer.ProspectingResultCustomer"
    ]
    """<p>The prospected customer account details, including geographic classification, industry segmentation, company size, and program eligibility.</p>"""
    insights: NotRequired[
        "capo_partnercentral_selling.types.prospecting_insights.ProspectingInsights"
    ]
    """<p>The AI-generated insights from the prospecting analysis, including marketplace engagement scoring, solution fit assessments, and solution categorization.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvitationProspectingResultAws) -> dict:
    out: dict = {}
    if "customer" in value:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["Customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "insights" in value:
        import capo_partnercentral_selling.types.prospecting_insights

        out["Insights"] = (
            capo_partnercentral_selling.types.prospecting_insights.serialize_aws_json_1_0(
                value["insights"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvitationProspectingResultAws:
    out: InvitationProspectingResultAws = {}  # type: ignore[typeddict-item]
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Insights") is not None:
        import capo_partnercentral_selling.types.prospecting_insights

        out["insights"] = (
            capo_partnercentral_selling.types.prospecting_insights.deserialize_aws_json_1_0(
                data["Insights"]
            )
        )
    return out


def redact_sensitive(value: InvitationProspectingResultAws) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customer" in value:
        import capo_partnercentral_selling.types.prospecting_result_customer

        out["customer"] = (
            capo_partnercentral_selling.types.prospecting_result_customer.redact_sensitive(
                value["customer"]
            )
        )
    return out
