"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetLayoutOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_layout_option

CampaignAssetLayoutOptionList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_layout_option.CampaignAssetLayoutOption"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetLayoutOptionList) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_layout_option

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_layout_option.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetLayoutOptionList:
    import capo_partnercentral_marketing.types.campaign_asset_layout_option

    out: CampaignAssetLayoutOptionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_layout_option.deserialize_cbor(
                item
            )
        )
    return out
