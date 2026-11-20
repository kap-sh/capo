"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id

CampaignAssetIdentifiers: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetIdentifiers) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CampaignAssetIdentifiers:
    return [item for item in data if item is not None]
