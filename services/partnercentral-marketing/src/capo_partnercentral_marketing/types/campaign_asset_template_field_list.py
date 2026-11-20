"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplateFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_template_field

CampaignAssetTemplateFieldList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_template_field.CampaignAssetTemplateField"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplateFieldList) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_template_field

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_template_field.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetTemplateFieldList:
    import capo_partnercentral_marketing.types.campaign_asset_template_field

    out: CampaignAssetTemplateFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_template_field.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: CampaignAssetTemplateFieldList) -> list[Any]:
    import capo_partnercentral_marketing.types.campaign_asset_template_field

    return [
        capo_partnercentral_marketing.types.campaign_asset_template_field.redact_sensitive(
            item
        )
        for item in value
    ]
