"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#SocialConnectionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.social_connection_summary

SocialConnectionSummaryList: TypeAlias = list[
    "capo_partnercentral_marketing.types.social_connection_summary.SocialConnectionSummary"
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SocialConnectionSummaryList) -> list:
    import capo_partnercentral_marketing.types.social_connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_marketing.types.social_connection_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> SocialConnectionSummaryList:
    import capo_partnercentral_marketing.types.social_connection_summary

    out: SocialConnectionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_marketing.types.social_connection_summary.deserialize_cbor(
                item
            )
        )
    return out


def redact_sensitive(value: SocialConnectionSummaryList) -> list[Any]:
    import capo_partnercentral_marketing.types.social_connection_summary

    return [
        capo_partnercentral_marketing.types.social_connection_summary.redact_sensitive(
            item
        )
        for item in value
    ]
