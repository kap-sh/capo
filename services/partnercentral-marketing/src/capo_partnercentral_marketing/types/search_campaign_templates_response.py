"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SearchCampaignTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_template_summary_list
    import capo_partnercentral_marketing.types.next_token


class SearchCampaignTemplatesResponse(TypedDict, closed=True):
    total_results: "int"
    """Total count over the whole matching set, not just this page — for "over N results" display."""
    campaign_templates: "capo_partnercentral_marketing.types.campaign_template_summary_list.CampaignTemplateSummaryList"
    """This page of template summaries."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SearchCampaignTemplatesResponse) -> dict:
    out: dict = {}
    out["TotalResults"] = value["total_results"]
    import capo_partnercentral_marketing.types.campaign_template_summary_list

    out["CampaignTemplates"] = (
        capo_partnercentral_marketing.types.campaign_template_summary_list.serialize_cbor(
            value["campaign_templates"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> SearchCampaignTemplatesResponse:
    out: SearchCampaignTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("TotalResults") is not None:
        out["total_results"] = data["TotalResults"]
    else:
        out["total_results"] = 0
    if data.get("CampaignTemplates") is not None:
        import capo_partnercentral_marketing.types.campaign_template_summary_list

        out["campaign_templates"] = (
            capo_partnercentral_marketing.types.campaign_template_summary_list.deserialize_cbor(
                data["CampaignTemplates"]
            )
        )
    else:
        out["campaign_templates"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
