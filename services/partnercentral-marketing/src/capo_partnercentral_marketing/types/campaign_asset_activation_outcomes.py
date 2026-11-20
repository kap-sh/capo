"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetActivationOutcomes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_activation_outcome

CampaignAssetActivationOutcomes: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_activation_outcome.CampaignAssetActivationOutcome"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetActivationOutcomes) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_activation_outcome

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_activation_outcome.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetActivationOutcomes:
    import capo_partnercentral_marketing.types.campaign_asset_activation_outcome

    out: CampaignAssetActivationOutcomes = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_activation_outcome.deserialize_cbor(
                item
            )
        )
    return out
