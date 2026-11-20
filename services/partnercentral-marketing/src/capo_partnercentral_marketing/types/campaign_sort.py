"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_sort_name
    import capo_partnercentral_marketing.types.sort_order


class CampaignSort(TypedDict, closed=True):
    sort_by: "capo_partnercentral_marketing.types.campaign_sort_name.CampaignSortName"
    """The attribute to sort by."""
    sort_order: "capo_partnercentral_marketing.types.sort_order.SortOrder"
    """The direction."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSort) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_sort_name

    out["SortBy"] = (
        capo_partnercentral_marketing.types.campaign_sort_name.serialize_cbor(
            value["sort_by"]
        )
    )
    import capo_partnercentral_marketing.types.sort_order

    out["SortOrder"] = capo_partnercentral_marketing.types.sort_order.serialize_cbor(
        value["sort_order"]
    )
    return out


def deserialize_cbor(data: dict) -> CampaignSort:
    out: CampaignSort = {}  # type: ignore[typeddict-item]
    if data.get("SortBy") is not None:
        import capo_partnercentral_marketing.types.campaign_sort_name

        out["sort_by"] = (
            capo_partnercentral_marketing.types.campaign_sort_name.deserialize_cbor(
                data["SortBy"]
            )
        )
    else:
        import typing

        out["sort_by"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_sort_name.CampaignSortName",
            "",
        )
    if data.get("SortOrder") is not None:
        import capo_partnercentral_marketing.types.sort_order

        out["sort_order"] = (
            capo_partnercentral_marketing.types.sort_order.deserialize_cbor(
                data["SortOrder"]
            )
        )
    else:
        import typing

        out["sort_order"] = typing.cast(
            "capo_partnercentral_marketing.types.sort_order.SortOrder", ""
        )
    return out
