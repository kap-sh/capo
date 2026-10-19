"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetBillingAdjustmentRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.billing_adjustment_reason_code
    import capo_marketplace_agreement.types.billing_adjustment_request_id
    import capo_marketplace_agreement.types.billing_adjustment_status
    import capo_marketplace_agreement.types.billing_adjustment_status_message
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.invoice_id
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals
    import capo_marketplace_agreement.types.timestamp


class GetBillingAdjustmentRequestOutput(TypedDict, closed=True):
    billing_adjustment_request_id: "capo_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the billing adjustment request.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement associated with this billing adjustment request.</p>"""
    adjustment_reason_code: "capo_marketplace_agreement.types.billing_adjustment_reason_code.BillingAdjustmentReasonCode"
    """<p>The reason code for the billing adjustment.</p>"""
    description: NotRequired["str"]
    """<p>The detailed description of the billing adjustment reason, if provided.</p>"""
    original_invoice_id: "capo_marketplace_agreement.types.invoice_id.InvoiceId"
    """<p>The identifier of the original invoice being adjusted.</p>"""
    adjustment_amount: "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The adjustment amount as a string representation of a decimal number.</p>"""
    currency_code: "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    """<p>The currency code for the adjustment amount (e.g., <code>USD</code>).</p>"""
    status: "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    """<p>The current status of the billing adjustment request.</p>"""
    status_message: NotRequired[
        "capo_marketplace_agreement.types.billing_adjustment_status_message.BillingAdjustmentStatusMessage"
    ]
    """<p>A message providing additional context about the billing adjustment request status. This field is populated only when the status is <code>VALIDATION_FAILED</code>.</p>"""
    created_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was created.</p>"""
    updated_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the billing adjustment request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingAdjustmentRequestOutput) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["agreementId"] = value["agreement_id"]
    import capo_marketplace_agreement.types.billing_adjustment_reason_code

    out["adjustmentReasonCode"] = (
        capo_marketplace_agreement.types.billing_adjustment_reason_code.serialize_aws_json_1_0(
            value["adjustment_reason_code"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    out["originalInvoiceId"] = value["original_invoice_id"]
    out["adjustmentAmount"] = value["adjustment_amount"]
    out["currencyCode"] = value["currency_code"]
    import capo_marketplace_agreement.types.billing_adjustment_status

    out["status"] = (
        capo_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingAdjustmentRequestOutput:
    out: GetBillingAdjustmentRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("billingAdjustmentRequestId") is not None:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        out["billing_adjustment_request_id"] = ""
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        out["agreement_id"] = ""
    if data.get("adjustmentReasonCode") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_reason_code

        out["adjustment_reason_code"] = (
            capo_marketplace_agreement.types.billing_adjustment_reason_code.deserialize_aws_json_1_0(
                data["adjustmentReasonCode"]
            )
        )
    else:
        import typing

        out["adjustment_reason_code"] = typing.cast(
            "capo_marketplace_agreement.types.billing_adjustment_reason_code.BillingAdjustmentReasonCode",
            "",
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
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
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
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
    return out
