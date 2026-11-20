"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entry

BatchCreateCampaignAssetEntries: TypeAlias = list[
    "capo_partnercentral_marketing.types.batch_create_campaign_asset_entry.BatchCreateCampaignAssetEntry"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetEntries) -> list:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entry

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_entry.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> BatchCreateCampaignAssetEntries:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_entry

    out: BatchCreateCampaignAssetEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_entry.deserialize_cbor(
                item
            )
        )
    return out
