"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementPaymentRequestOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.payment_request_description
    import capo_marketplace_agreement.types.payment_request_id
    import capo_marketplace_agreement.types.payment_request_name
    import capo_marketplace_agreement.types.payment_request_status
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals
    import capo_marketplace_agreement.types.timestamp


class CancelAgreementPaymentRequestOutput(TypedDict, closed=True):
    payment_request_id: NotRequired[
        "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    ]
    """<p>The unique identifier of the cancelled payment request.</p>"""
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this payment request.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
    ]
    """<p>The updated status of the payment request, which is <code>CANCELLED</code>.</p>"""
    name: NotRequired[
        "capo_marketplace_agreement.types.payment_request_name.PaymentRequestName"
    ]
    """<p>The descriptive name of the payment request.</p>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.payment_request_description.PaymentRequestDescription"
    ]
    """<p>The detailed description of the payment request, if provided.</p>"""
    charge_amount: NotRequired[
        "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    ]
    """<p>The amount that was requested to be charged.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the charge amount.</p>"""
    created_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the payment request was originally created.</p>"""
    updated_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the payment request was cancelled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementPaymentRequestOutput) -> dict:
    out: dict = {}
    if "payment_request_id" in value:
        out["paymentRequestId"] = value["payment_request_id"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.payment_request_status

        out["status"] = (
            capo_marketplace_agreement.types.payment_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "charge_amount" in value:
        out["chargeAmount"] = value["charge_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "created_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["updatedAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementPaymentRequestOutput:
    out: CancelAgreementPaymentRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("paymentRequestId") is not None:
        out["payment_request_id"] = data["paymentRequestId"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.payment_request_status

        out["status"] = (
            capo_marketplace_agreement.types.payment_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["updated_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out


def redact_sensitive(value: CancelAgreementPaymentRequestOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
