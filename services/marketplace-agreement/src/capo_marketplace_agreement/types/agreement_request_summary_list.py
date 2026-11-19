"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementRequestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_summary

AgreementRequestSummaryList: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_request_summary.AgreementRequestSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementRequestSummaryList) -> list:
    import capo_marketplace_agreement.types.agreement_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_request_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementRequestSummaryList:
    import capo_marketplace_agreement.types.agreement_request_summary

    out: AgreementRequestSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_request_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
