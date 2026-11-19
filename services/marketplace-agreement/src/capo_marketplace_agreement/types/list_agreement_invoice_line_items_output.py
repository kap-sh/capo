"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementInvoiceLineItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries
    import capo_marketplace_agreement.types.next_token


class ListAgreementInvoiceLineItemsOutput(TypedDict, closed=True):
    agreement_invoice_line_item_group_summaries: NotRequired[
        "capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.AgreementInvoiceLineItemGroupSummaries"
    ]
    """<p>A list of grouped billing data objects.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementInvoiceLineItemsOutput) -> dict:
    out: dict = {}
    if "agreement_invoice_line_item_group_summaries" in value:
        import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreementInvoiceLineItemGroupSummaries"] = (
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.serialize_aws_json_1_0(
                value["agreement_invoice_line_item_group_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementInvoiceLineItemsOutput:
    out: ListAgreementInvoiceLineItemsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementInvoiceLineItemGroupSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreement_invoice_line_item_group_summaries"] = (
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.deserialize_aws_json_1_0(
                data["agreementInvoiceLineItemGroupSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgreementInvoiceLineItemsOutput) -> dict:
    out: dict = {}
    if "agreement_invoice_line_item_group_summaries" in value:
        import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreementInvoiceLineItemGroupSummaries"] = (
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.serialize_cbor(
                value["agreement_invoice_line_item_group_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgreementInvoiceLineItemsOutput:
    out: ListAgreementInvoiceLineItemsOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementInvoiceLineItemGroupSummaries") is not None:
        import capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries

        out["agreement_invoice_line_item_group_summaries"] = (
            capo_marketplace_agreement.types.agreement_invoice_line_item_group_summaries.deserialize_cbor(
                data["agreementInvoiceLineItemGroupSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
