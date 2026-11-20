"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSocialConnectionIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.social_connection_id

CampaignSocialConnectionIds: TypeAlias = list[
    "capo_partnercentral_marketing.types.social_connection_id.SocialConnectionId"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSocialConnectionIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> CampaignSocialConnectionIds:
    return [item for item in data if item is not None]
