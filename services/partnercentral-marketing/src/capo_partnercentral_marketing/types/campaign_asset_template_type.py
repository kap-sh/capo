"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetTemplateType``."""

from typing import Literal, TypeAlias, cast

"""The kind of asset an asset template instantiates as."""
CampaignAssetTemplateType: TypeAlias = Literal[
    "EMAIL",
    "SOCIAL_POST",
    "LANDING_PAGE",
    "BANNER_AD",
    "DOCUMENT",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetTemplateType) -> str:
    return value


def deserialize_cbor(data: str) -> CampaignAssetTemplateType:
    return cast(CampaignAssetTemplateType, data)
