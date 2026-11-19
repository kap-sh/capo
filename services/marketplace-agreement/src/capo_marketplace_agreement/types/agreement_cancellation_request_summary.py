"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementCancellationRequestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_id
    import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code
    import capo_marketplace_agreement.types.agreement_cancellation_request_status
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.timestamp


class AgreementCancellationRequestSummary(TypedDict, closed=True):
    agreement_cancellation_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_id.AgreementCancellationRequestId"
    ]
    """<p>The unique identifier of the cancellation request.</p>"""
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this cancellation request.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>The current status of the cancellation request. Possible values include <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>CANCELLED</code>, and <code>VALIDATION_FAILED</code>.</p>"""
    reason_code: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.AgreementCancellationRequestReasonCode"
    ]
    """<p>The reason code provided for the cancellation.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement.</p>"""
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>The catalog in which the agreement was created.</p>"""
    created_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was created.</p>"""
    updated_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the cancellation request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementCancellationRequestSummary) -> dict:
    out: dict = {}
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
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
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
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


def deserialize_aws_json_1_0(data: dict) -> AgreementCancellationRequestSummary:
    out: AgreementCancellationRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementCancellationRequestId") is not None:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
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
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
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


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementCancellationRequestSummary) -> dict:
    out: dict = {}
    if "agreement_cancellation_request_id" in value:
        out["agreementCancellationRequestId"] = value[
            "agreement_cancellation_request_id"
        ]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.serialize_cbor(
                value["status"]
            )
        )
    if "reason_code" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reasonCode"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.serialize_cbor(
                value["reason_code"]
            )
        )
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "created_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["updatedAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    return out


def deserialize_cbor(data: dict) -> AgreementCancellationRequestSummary:
    out: AgreementCancellationRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementCancellationRequestId") is not None:
        out["agreement_cancellation_request_id"] = data[
            "agreementCancellationRequestId"
        ]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("reasonCode") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_reason_code

        out["reason_code"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_reason_code.deserialize_cbor(
                data["reasonCode"]
            )
        )
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["updated_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["updatedAt"]
        )
    return out
