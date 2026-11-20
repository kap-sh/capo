"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListCampaignAssetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.next_token


class ListCampaignAssetsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign identifier."""
    max_results: NotRequired[
        "capo_partnercentral_marketing.types.max_results.MaxResults"
    ]
    """Maximum results per page."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCampaignAssetsRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListCampaignAssetsRequest:
    out: ListCampaignAssetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
