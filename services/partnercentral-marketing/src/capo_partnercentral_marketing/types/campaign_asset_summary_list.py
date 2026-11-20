"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_summary

CampaignAssetSummaryList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_summary.CampaignAssetSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetSummaryList) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetSummaryList:
    import capo_partnercentral_marketing.types.campaign_asset_summary

    out: CampaignAssetSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_summary.deserialize_cbor(
                item
            )
        )
    return out
