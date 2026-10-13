"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SendAgreementCancellationRequestOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_description
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import capo_marketplace_agreement.types.agreement_cancellation_request_status
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.timestamp


class SendAgreementCancellationRequestOutput(TypedDict, closed=True):
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement.</p>"""
    agreement_cancellation_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    ]
    """<p>The unique identifier for the created cancellation request.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>The current status of the cancellation request. The initial status is <code>PENDING_APPROVAL</code>.</p>"""
    reason_code: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    ]
    """<p>The reason code provided for the cancellation.</p>"""
    description: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_description.AgreementCancellationRequestDescription"
    ]
    """<p>The detailed description of the cancellation reason, if provided.</p>"""
    created_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The time when the cancellation request was created.</p>"""
    updated_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The time when the cancellation request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendAgreementCancellationRequestOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "reason_code" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reasonCode"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.serialize_aws_json_1_0(
                value["reason_code"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
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


def deserialize_aws_json_1_0(data: dict) -> SendAgreementCancellationRequestOutput:
    out: SendAgreementCancellationRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("agreementCancellationRequestId") is not None:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("reasonCode") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reason_code"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.deserialize_aws_json_1_0(
                data["reasonCode"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
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


def redact_sensitive(value: SendAgreementCancellationRequestOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
