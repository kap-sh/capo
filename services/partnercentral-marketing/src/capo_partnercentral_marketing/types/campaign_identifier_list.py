"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier

CampaignIdentifierList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignIdentifierList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CampaignIdentifierList:
    return [item for item in data if item is not None]
