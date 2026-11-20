"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplateList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_template

CampaignAssetTemplateList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_template.CampaignAssetTemplate"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplateList) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_template

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_template.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetTemplateList:
    import capo_partnercentral_marketing.types.campaign_asset_template

    out: CampaignAssetTemplateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_template.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: CampaignAssetTemplateList) -> list[Any]:
    import capo_partnercentral_marketing.types.campaign_asset_template

    return [
        capo_partnercentral_marketing.types.campaign_asset_template.redact_sensitive(
            item
        )
        for item in value
    ]
