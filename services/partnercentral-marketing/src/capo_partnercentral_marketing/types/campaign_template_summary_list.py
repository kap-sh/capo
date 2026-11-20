"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignTemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_template_summary

CampaignTemplateSummaryList: TypeAlias = list[
    "capo_partnercentral_marketing.types.campaign_template_summary.CampaignTemplateSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignTemplateSummaryList) -> list:
    import capo_partnercentral_marketing.types.campaign_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.campaign_template_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> CampaignTemplateSummaryList:
    import capo_partnercentral_marketing.types.campaign_template_summary

    out: CampaignTemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.campaign_template_summary.deserialize_cbor(
                item
            )
        )
    return out
