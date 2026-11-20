"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ListCampaignsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier_list
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_sort
    import capo_partnercentral_marketing.types.campaign_state_list
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.max_results
    import capo_partnercentral_marketing.types.next_token


class ListCampaignsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifiers: NotRequired[
        "capo_partnercentral_marketing.types.campaign_identifier_list.CampaignIdentifierList"
    ]
    """Only these campaigns, each named by its id or its campaign ARN. A campaign that does not exist, was deleted, or whose ARN names another account or catalog is left out rather than refused."""
    name: NotRequired["capo_partnercentral_marketing.types.campaign_name.CampaignName"]
    """Only campaigns whose name contains this, compared case-insensitively."""
    states: NotRequired[
        "capo_partnercentral_marketing.types.campaign_state_list.CampaignStateList"
    ]
    """Only campaigns in one of these states."""
    sort: NotRequired["capo_partnercentral_marketing.types.campaign_sort.CampaignSort"]
    """The order of the results. Default: `CREATED_AT`, `DESCENDING`."""
    max_results: NotRequired[
        "capo_partnercentral_marketing.types.max_results.MaxResults"
    ]
    """Maximum results per page."""
    next_token: NotRequired["capo_partnercentral_marketing.types.next_token.NextToken"]
    """Pagination token. Bound to the filters and sort it was issued for: a request that changes `CampaignIdentifiers`, `Name`, `States` or `Sort` between pages is refused with `ValidationException`. `MaxResults` may change."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListCampaignsRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    if "campaign_identifiers" in value:
        import capo_partnercentral_marketing.types.campaign_identifier_list

        out["CampaignIdentifiers"] = (
            capo_partnercentral_marketing.types.campaign_identifier_list.serialize_cbor(
                value["campaign_identifiers"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "states" in value:
        import capo_partnercentral_marketing.types.campaign_state_list

        out["States"] = (
            capo_partnercentral_marketing.types.campaign_state_list.serialize_cbor(
                value["states"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_marketing.types.campaign_sort

        out["Sort"] = capo_partnercentral_marketing.types.campaign_sort.serialize_cbor(
            value["sort"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListCampaignsRequest:
    out: ListCampaignsRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("CampaignIdentifiers") is not None:
        import capo_partnercentral_marketing.types.campaign_identifier_list

        out["campaign_identifiers"] = (
            capo_partnercentral_marketing.types.campaign_identifier_list.deserialize_cbor(
                data["CampaignIdentifiers"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("States") is not None:
        import capo_partnercentral_marketing.types.campaign_state_list

        out["states"] = (
            capo_partnercentral_marketing.types.campaign_state_list.deserialize_cbor(
                data["States"]
            )
        )
    if data.get("Sort") is not None:
        import capo_partnercentral_marketing.types.campaign_sort

        out["sort"] = (
            capo_partnercentral_marketing.types.campaign_sort.deserialize_cbor(
                data["Sort"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
