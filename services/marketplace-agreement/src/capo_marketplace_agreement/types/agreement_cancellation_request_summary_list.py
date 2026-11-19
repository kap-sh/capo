"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary

AgreementCancellationRequestSummaryList: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_cancellation_request_summary.AgreementCancellationRequestSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementCancellationRequestSummaryList) -> list:
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_cancellation_request_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementCancellationRequestSummaryList:
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary

    out: AgreementCancellationRequestSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_cancellation_request_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementCancellationRequestSummaryList) -> list:
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_cancellation_request_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementCancellationRequestSummaryList:
    import capo_marketplace_agreement.types.agreement_cancellation_request_summary

    out: AgreementCancellationRequestSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_cancellation_request_summary.deserialize_cbor(
                item
            )
        )
    return out
