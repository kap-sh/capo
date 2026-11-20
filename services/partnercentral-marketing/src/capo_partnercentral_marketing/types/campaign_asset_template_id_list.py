"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplateIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.id

CampaignAssetTemplateIdList: TypeAlias = list[
    "capo_partnercentral_marketing.types.id.Id"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplateIdList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CampaignAssetTemplateIdList:
    return [item for item in data if item is not None]
