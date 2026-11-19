"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_summary

AgreementApprovalSummaries: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_approval_summary.AgreementApprovalSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalSummaries) -> list:
    import capo_marketplace_agreement.types.agreement_approval_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementApprovalSummaries:
    import capo_marketplace_agreement.types.agreement_approval_summary

    out: AgreementApprovalSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalSummaries) -> list:
    import capo_marketplace_agreement.types.agreement_approval_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_approval_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementApprovalSummaries:
    import capo_marketplace_agreement.types.agreement_approval_summary

    out: AgreementApprovalSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_approval_summary.deserialize_cbor(
                item
            )
        )
    return out
