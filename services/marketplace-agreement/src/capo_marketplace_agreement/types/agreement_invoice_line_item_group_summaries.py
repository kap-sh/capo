"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementInvoiceLineItemGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary

AgreementInvoiceLineItemGroupSummaries: TypeAlias = list[
    "capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.AgreementInvoiceLineItemGroupSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementInvoiceLineItemGroupSummaries) -> list:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementInvoiceLineItemGroupSummaries:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary

    out: AgreementInvoiceLineItemGroupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementInvoiceLineItemGroupSummaries) -> list:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> AgreementInvoiceLineItemGroupSummaries:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary

    out: AgreementInvoiceLineItemGroupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summary.deserialize_cbor(
                item
            )
        )
    return out
