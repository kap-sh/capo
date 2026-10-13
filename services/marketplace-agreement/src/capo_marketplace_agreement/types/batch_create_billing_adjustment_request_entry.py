"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.billing_adjustment_description
    import capo_marketplace_agreement.types.billing_adjustment_reason_code
    import capo_marketplace_agreement.types.client_token
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.invoice_id
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals


class BatchCreateBillingAdjustmentRequestEntry(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with the invoice.</p>"""
    original_invoice_id: "capo_marketplace_agreement.types.invoice_id.InvoiceId"
    """<p>The identifier of the original invoice to adjust.</p>"""
    adjustment_amount: "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The adjustment amount as a string representation of a decimal number in the currency of the invoice.</p>"""
    currency_code: "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    """<p>The 3-letter ISO 4217 currency code for the adjustment amount. Must match the currency code of the offer associated with the agreement (e.g., <code>USD</code>).</p>"""
    adjustment_reason_code: "capo_marketplace_agreement.types.billing_adjustment_reason_code.BillingAdjustmentReasonCode"
    """<p>The reason code for the billing adjustment.</p>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.billing_adjustment_description.BillingAdjustmentDescription"
    ]
    """<p>An optional detailed description of the adjustment reason.</p>"""
    client_token: "capo_marketplace_agreement.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestEntry) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    out["originalInvoiceId"] = value["original_invoice_id"]
    out["adjustmentAmount"] = value["adjustment_amount"]
    out["currencyCode"] = value["currency_code"]
    import capo_marketplace_agreement.types.billing_adjustment_reason_code

    out["adjustmentReasonCode"] = (
        capo_marketplace_agreement.types.billing_adjustment_reason_code.serialize_aws_json_1_0(
            value["adjustment_reason_code"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentRequestEntry:
    out: BatchCreateBillingAdjustmentRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.agreement_id required"
        )
    if data.get("originalInvoiceId") is not None:
        out["original_invoice_id"] = data["originalInvoiceId"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.original_invoice_id required"
        )
    if data.get("adjustmentAmount") is not None:
        out["adjustment_amount"] = data["adjustmentAmount"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.adjustment_amount required"
        )
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.currency_code required"
        )
    if data.get("adjustmentReasonCode") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_reason_code

        out["adjustment_reason_code"] = (
            capo_marketplace_agreement.types.billing_adjustment_reason_code.deserialize_aws_json_1_0(
                data["adjustmentReasonCode"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.adjustment_reason_code required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestEntry.client_token required"
        )
    return out


def redact_sensitive(value: BatchCreateBillingAdjustmentRequestEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
