"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_result

BatchCreateCampaignAssetResults: TypeAlias = list[
    "capo_partnercentral_marketing.types.batch_create_campaign_asset_result.BatchCreateCampaignAssetResult"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetResults) -> list:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_result

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_result.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> BatchCreateCampaignAssetResults:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_result

    out: BatchCreateCampaignAssetResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_result.deserialize_cbor(
                item
            )
        )
    return out
