"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListCampaignsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_summary_list
    import capo_partnercentral_marketing.types.next_token


class ListCampaignsResponse(TypedDict, closed=True):
    items: (
        "capo_partnercentral_marketing.types.campaign_summary_list.CampaignSummaryList"
    )
    """The list of results."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCampaignsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_summary_list

    out["Items"] = (
        capo_partnercentral_marketing.types.campaign_summary_list.serialize_cbor(
            value["items"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListCampaignsResponse:
    out: ListCampaignsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_partnercentral_marketing.types.campaign_summary_list

        out["items"] = (
            capo_partnercentral_marketing.types.campaign_summary_list.deserialize_cbor(
                data["Items"]
            )
        )
    else:
        out["items"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
