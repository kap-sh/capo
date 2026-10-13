"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SendAgreementPaymentRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.client_token
    import capo_marketplace_agreement.types.payment_request_description
    import capo_marketplace_agreement.types.payment_request_name
    import capo_marketplace_agreement.types.positive_amount_upto8_decimals
    import capo_marketplace_agreement.types.term_id


class SendAgreementPaymentRequestInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_marketplace_agreement.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement for which the payment request is being submitted. Use <code>GetAgreementTerms</code> to retrieve agreement term details.</p>"""
    term_id: "capo_marketplace_agreement.types.term_id.TermId"
    """<p>The unique identifier of the <code>VariablePaymentTerm</code> for the agreement that the payment request is being sent for.</p>"""
    name: "capo_marketplace_agreement.types.payment_request_name.PaymentRequestName"
    """<p>A descriptive name for the payment request (5-64 characters).</p>"""
    charge_amount: "capo_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    """<p>The amount requested to be charged to the buyer, positive decimal value in the currency of the accepted term.</p> <note> <p>A <code>ValidationException</code> is returned if the <code>chargeAmount</code> exceeds the available balance, if the agreement doesn't have an active <code>VariablePaymentTerm</code>, or if the <code>termId</code> is invalid.</p> </note>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.payment_request_description.PaymentRequestDescription"
    ]
    """<p>An optional detailed description of the payment request (1-2000 characters).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendAgreementPaymentRequestInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["agreementId"] = value["agreement_id"]
    out["termId"] = value["term_id"]
    out["name"] = value["name"]
    out["chargeAmount"] = value["charge_amount"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendAgreementPaymentRequestInput:
    out: SendAgreementPaymentRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "SendAgreementPaymentRequestInput.agreement_id required"
        )
    if data.get("termId") is not None:
        out["term_id"] = data["termId"]
    else:
        raise DeserializationError("SendAgreementPaymentRequestInput.term_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SendAgreementPaymentRequestInput.name required")
    if data.get("chargeAmount") is not None:
        out["charge_amount"] = data["chargeAmount"]
    else:
        raise DeserializationError(
            "SendAgreementPaymentRequestInput.charge_amount required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: SendAgreementPaymentRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
