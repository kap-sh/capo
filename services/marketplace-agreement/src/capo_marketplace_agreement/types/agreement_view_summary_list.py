"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementViewSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_view_summary

AgreementViewSummaryList: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_view_summary.AgreementViewSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementViewSummaryList) -> list:
    import capo_marketplace_agreement.types.agreement_view_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_view_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementViewSummaryList:
    import capo_marketplace_agreement.types.agreement_view_summary

    out: AgreementViewSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_view_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementViewSummaryList) -> list:
    import capo_marketplace_agreement.types.agreement_view_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_view_summary.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AgreementViewSummaryList:
    import capo_marketplace_agreement.types.agreement_view_summary

    out: AgreementViewSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_view_summary.deserialize_cbor(
                item
            )
        )
    return out
