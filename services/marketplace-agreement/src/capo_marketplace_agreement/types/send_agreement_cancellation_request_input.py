"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SendAgreementCancellationRequestInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_description
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.client_token


class SendAgreementCancellationRequestInput(TypedDict, closed=True):
    agreement_id: "capo_marketplace_agreement.types.agreement_id.AgreementId"
    """<p>The unique identifier of the agreement for which the cancellation request is being submitted.</p>"""
    reason_code: "capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    """<p>The reason code for the cancellation request.</p>"""
    client_token: NotRequired[
        "capo_marketplace_agreement.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_description.AgreementCancellationRequestDescription"
    ]
    """<p>An optional detailed description of the cancellation reason (1-2000 characters).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendAgreementCancellationRequestInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

    out["reasonCode"] = (
        capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.serialize_aws_json_1_0(
            value["reason_code"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SendAgreementCancellationRequestInput:
    out: SendAgreementCancellationRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError(
            "SendAgreementCancellationRequestInput.agreement_id required"
        )
    if data.get("reasonCode") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reason_code"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.deserialize_aws_json_1_0(
                data["reasonCode"]
            )
        )
    else:
        raise DeserializationError(
            "SendAgreementCancellationRequestInput.reason_code required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: SendAgreementCancellationRequestInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
