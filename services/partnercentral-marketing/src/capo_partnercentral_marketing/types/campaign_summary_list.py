"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_summary

CampaignSummaryList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_summary.CampaignSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSummaryList) -> list:
    import capo_partnercentral_marketing.types.campaign_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> CampaignSummaryList:
    import capo_partnercentral_marketing.types.campaign_summary

    out: CampaignSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_summary.deserialize_cbor(item)
        )
    return out
