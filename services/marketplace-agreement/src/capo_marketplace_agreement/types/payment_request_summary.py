"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.charge_id
    import capo_marketplace_agreement.types.currency_code
    import capo_marketplace_agreement.types.payment_request_id
    import capo_marketplace_agreement.types.payment_request_name
    import capo_marketplace_agreement.types.payment_request_status
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals


class PaymentRequestSummary(TypedDict, closed=True):
    payment_request_id: NotRequired[
        "capo_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    ]
    """<p>The unique identifier of the payment request.</p>"""
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this payment request.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
    ]
    """<p>The current status of the payment request. Possible values include <code>VALIDATING</code>, <code>VALIDATION_FAILED</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, and <code>CANCELLED</code>.</p>"""
    name: NotRequired[
        "capo_marketplace_agreement.types.payment_request_name.PaymentRequestName"
    ]
    """<p>The descriptive name of the payment request.</p>"""
    charge_id: NotRequired["capo_marketplace_agreement.types.charge_id.ChargeId"]
    """<p>The unique identifier of the charge created after the payment request is approved. This field is only present for approved payment requests.</p>"""
    charge_amount: NotRequired[
        "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    ]
    """<p>The amount charged or to be charged to the buyer.</p>"""
    currency_code: NotRequired[
        "capo_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the charge amount.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the payment request was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the payment request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentRequestSummary) -> dict:
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
    if "charge_id" in value:
        out["chargeId"] = value["charge_id"]
    if "charge_amount" in value:
        out["chargeAmount"] = value["charge_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "created_at" in value:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["createdAt"] = (
            capo_marketplace_agreement.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["updatedAt"] = (
            capo_marketplace_agreement.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PaymentRequestSummary:
    out: PaymentRequestSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("chargeId") is not None:
        out["charge_id"] = data["chargeId"]
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["updated_at"] = (
            capo_marketplace_agreement.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PaymentRequestSummary) -> dict:
    out: dict = {}
    if "payment_request_id" in value:
        out["paymentRequestId"] = value["payment_request_id"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.payment_request_status

        out["status"] = (
            capo_marketplace_agreement.types.payment_request_status.serialize_cbor(
                value["status"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "charge_id" in value:
        out["chargeId"] = value["charge_id"]
    if "charge_amount" in value:
        out["chargeAmount"] = value["charge_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "created_at" in value:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["createdAt"] = (
            capo_marketplace_agreement.types._prelude.timestamp.serialize_cbor(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["updatedAt"] = (
            capo_marketplace_agreement.types._prelude.timestamp.serialize_cbor(
                value["updated_at"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PaymentRequestSummary:
    out: PaymentRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("paymentRequestId") is not None:
        out["payment_request_id"] = data["paymentRequestId"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.payment_request_status

        out["status"] = (
            capo_marketplace_agreement.types.payment_request_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("chargeId") is not None:
        out["charge_id"] = data["chargeId"]
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    if data.get("currencyCode") is not None:
        out["currency_code"] = data["currencyCode"]
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types._prelude.timestamp

        out["updated_at"] = (
            capo_marketplace_agreement.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    return out
