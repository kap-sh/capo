"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BillingAdjustmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.billing_adjustment_request_id
    import capo_marketplace_agreement.types.billing_adjustment_status
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.invoice_id
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals
    import capo_marketplace_agreement.types.timestamp


class BillingAdjustmentSummary(TypedDict, closed=True):
    billing_adjustment_request_id: "capo_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""
    original_invoice_id: "capo_marketplace_agreement.types.invoice_id.InvoiceId"
    """<p>The identifier of the original invoice being adjusted.</p>"""
    adjustment_amount: "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The adjustment amount as a string representation of a decimal number.</p>"""
    currency_code: "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    """<p>The currency code for the adjustment amount.</p>"""
    status: "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    """<p>The current status of the billing adjustment request.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with this billing adjustment request.</p>"""
    created_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was created.</p>"""
    updated_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was last updated.</p>"""
    agreement_type: "capo_marketplace_agreement.types.agreement_type.AgreementType"
    """<p>The type of agreement.</p>"""
    catalog: "capo_marketplace_agreement.types.catalog.Catalog"
    """<p>The catalog in which the agreement was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingAdjustmentSummary) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["originalInvoiceId"] = value["original_invoice_id"]
    out["adjustmentAmount"] = value["adjustment_amount"]
    out["currencyCode"] = value["currency_code"]
    import capo_marketplace_agreement.types.billing_adjustment_status

    out["status"] = (
        capo_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["agreementId"] = value["agreement_id"]
    import capo_marketplace_agreement.types.timestamp

    out["createdAt"] = (
        capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import capo_marketplace_agreement.types.timestamp

    out["updatedAt"] = (
        capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    out["agreementType"] = value["agreement_type"]
    out["catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingAdjustmentSummary:
    out: BillingAdjustmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("billingAdjustmentRequestId") is not None:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        out["billing_adjustment_request_id"] = ""
    if data.get("originalInvoiceId") is not None:
        out["original_invoice_id"] = data["originalInvoiceId"]
    else:
        out["original_invoice_id"] = ""
    if data.get("adjustmentAmount") is not None:
        out["adjustment_amount"] = data["adjustmentAmount"]
    else:
        out["adjustment_amount"] = ""
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    else:
        out["currency_code"] = ""
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            capo_marketplace_agreement.types.billing_adjustment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus",
            "",
        )
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    else:
        out["agreement_type"] = ""
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    return out
