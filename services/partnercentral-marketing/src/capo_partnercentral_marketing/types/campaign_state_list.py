"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_state

CampaignStateList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_state.CampaignState"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignStateList) -> list:
    import capo_partnercentral_marketing.types.campaign_state

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_state.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CampaignStateList:
    import capo_partnercentral_marketing.types.campaign_state

    out: CampaignStateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_state.deserialize_cbor(item)
        )
    return out
