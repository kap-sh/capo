"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#PartnerSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.partner_summary

PartnerSummaryList: TypeAlias = list[
    "capo_partnercentral_account.types.partner_summary.PartnerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PartnerSummaryList) -> list:
    import capo_partnercentral_account.types.partner_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.partner_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PartnerSummaryList:
    import capo_partnercentral_account.types.partner_summary

    out: PartnerSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_partnercentral_account.types.partner_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: PartnerSummaryList) -> list[Any]:
    import capo_partnercentral_account.types.partner_summary

    return [
        capo_partnercentral_account.types.partner_summary.redact_sensitive(item)
        for item in value
    ]
