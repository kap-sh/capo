"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetCategory``."""

from typing import Literal, TypeAlias, cast

"""The kind of a campaign asset. Shares its vocabulary with CampaignAssetTemplateType, deliberately: an asset is instantiated from a blueprint and carries the blueprint's kind forward, so two spellings of one concept only ever diverge. LANDING_PAGE, SOCIAL_POST and BANNER_AD were previously WEBPAGE, SOCIAL and VISUAL_AD here while the template side already used these names, and nothing mapped between them. DG-038 removed VIDEO. Its own comment here recorded why it was the odd one -- "video assets are uploaded rather than instantiated from a blueprint" -- and once BatchCreateCampaignAsset became the only create path, nothing uploads an asset into existence, so the value was unreachable rather than merely unused. The five remaining values correspond one-to-one with CampaignAssetTemplateType, which is what lets the blueprint-to-category mapping be a total switch with no default arm."""
CampaignAssetCategory: TypeAlias = Literal[
    "EMAIL",
    "LANDING_PAGE",
    "SOCIAL_POST",
    "BANNER_AD",
    "DOCUMENT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetCategory) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetCategory:
    return cast(CampaignAssetCategory, data)
