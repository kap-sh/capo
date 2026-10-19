"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementInvoiceLineItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.invoice_billing_period
    import capo_marketplace_agreement.types.invoice_type
    import capo_marketplace_agreement.types.line_item_group_by
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.timestamp


class ListAgreementInvoiceLineItemsInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""
    group_by: "capo_marketplace_agreement.types.line_item_group_by.LineItemGroupBy"
    """<p>Specifies a grouping strategy for line items. Currently supports <code>INVOICE_ID</code>.</p>"""
    invoice_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>An optional filter to retrieve invoice information for a specific invoice.</p>"""
    invoice_type: NotRequired[
        "capo_marketplace_agreement.types.invoice_type.InvoiceType"
    ]
    """<p>An optional filter for the type of invoice. Valid values are <code>INVOICE</code> and <code>CREDIT_MEMO</code>.</p>"""
    invoice_billing_period: NotRequired[
        "capo_marketplace_agreement.types.invoice_billing_period.InvoiceBillingPeriod"
    ]
    """<p>An optional filter for the billing period associated with the invoice.</p>"""
    before_issued_time: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter for invoices issued before the specified timestamp.</p>"""
    after_issued_time: NotRequired[
        "capo_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>An optional filter for invoices issued after the specified timestamp.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementInvoiceLineItemsInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    import capo_marketplace_agreement.types.line_item_group_by

    out["groupBy"] = (
        capo_marketplace_agreement.types.line_item_group_by.serialize_aws_json_1_0(
            value["group_by"]
        )
    )
    if "invoice_id" in value:
        out["invoiceId"] = value["invoice_id"]
    if "invoice_type" in value:
        import capo_marketplace_agreement.types.invoice_type

        out["invoiceType"] = (
            capo_marketplace_agreement.types.invoice_type.serialize_aws_json_1_0(
                value["invoice_type"]
            )
        )
    if "invoice_billing_period" in value:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoiceBillingPeriod"] = (
            capo_marketplace_agreement.types.invoice_billing_period.serialize_aws_json_1_0(
                value["invoice_billing_period"]
            )
        )
    if "before_issued_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["beforeIssuedTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["before_issued_time"]
            )
        )
    if "after_issued_time" in value:
        import capo_marketplace_agreement.types.timestamp

        out["afterIssuedTime"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["after_issued_time"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementInvoiceLineItemsInput:
    out: ListAgreementInvoiceLineItemsInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("groupBy") is not None:
        import capo_marketplace_agreement.types.line_item_group_by

        out["group_by"] = (
            capo_marketplace_agreement.types.line_item_group_by.deserialize_aws_json_1_0(
                data["groupBy"]
            )
        )
    else:
        import typing

        out["group_by"] = typing.cast(
            "capo_marketplace_agreement.types.line_item_group_by.LineItemGroupBy", ""
        )
    if data.get("invoiceId") is not None:
        out["invoice_id"] = data["invoiceId"]
    if data.get("invoiceType") is not None:
        import capo_marketplace_agreement.types.invoice_type

        out["invoice_type"] = (
            capo_marketplace_agreement.types.invoice_type.deserialize_aws_json_1_0(
                data["invoiceType"]
            )
        )
    if data.get("invoiceBillingPeriod") is not None:
        import capo_marketplace_agreement.types.invoice_billing_period

        out["invoice_billing_period"] = (
            capo_marketplace_agreement.types.invoice_billing_period.deserialize_aws_json_1_0(
                data["invoiceBillingPeriod"]
            )
        )
    if data.get("beforeIssuedTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["before_issued_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["beforeIssuedTime"]
            )
        )
    if data.get("afterIssuedTime") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["after_issued_time"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["afterIssuedTime"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
