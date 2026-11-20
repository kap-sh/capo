"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_error

BatchCreateCampaignAssetErrors: TypeAlias = list[
    "capo_partnercentral_marketing.types.batch_create_campaign_asset_error.BatchCreateCampaignAssetError"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetErrors) -> list:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_error

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_error.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> BatchCreateCampaignAssetErrors:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_error

    out: BatchCreateCampaignAssetErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.batch_create_campaign_asset_error.deserialize_cbor(
                item
            )
        )
    return out
