"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id

CampaignAssetIdList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CampaignAssetIdList:
    return [item for item in data if item is not None]
