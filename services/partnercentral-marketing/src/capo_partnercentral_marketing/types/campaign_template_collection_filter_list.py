"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplateCollectionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_template_collection

CampaignTemplateCollectionFilterList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_template_collection.CampaignTemplateCollection"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignTemplateCollectionFilterList) -> list:
    import capo_partnercentral_marketing.types.campaign_template_collection

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_template_collection.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignTemplateCollectionFilterList:
    import capo_partnercentral_marketing.types.campaign_template_collection

    out: CampaignTemplateCollectionFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_template_collection.deserialize_cbor(
                item
            )
        )
    return out
