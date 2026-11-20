"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetFieldValueList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_field_value

CampaignAssetFieldValueList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_asset_field_value.CampaignAssetFieldValue"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetFieldValueList) -> list:
    import capo_partnercentral_marketing.types.campaign_asset_field_value

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_field_value.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignAssetFieldValueList:
    import capo_partnercentral_marketing.types.campaign_asset_field_value

    out: CampaignAssetFieldValueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_asset_field_value.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: CampaignAssetFieldValueList) -> list[Any]:
    import capo_partnercentral_marketing.types.campaign_asset_field_value

    return [
        capo_partnercentral_marketing.types.campaign_asset_field_value.redact_sensitive(
            item
        )
        for item in value
    ]
