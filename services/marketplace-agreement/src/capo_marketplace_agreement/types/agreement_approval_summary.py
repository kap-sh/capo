"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_id
    import capo_marketplace_agreement.types.agreement_approval_name
    import capo_marketplace_agreement.types.agreement_approval_status
    import capo_marketplace_agreement.types.agreement_approval_type
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.timestamp


class AgreementApprovalSummary(TypedDict, closed=True):
    approval_type: (
        "capo_marketplace_agreement.types.agreement_approval_type.AgreementApprovalType"
    )
    """<p>The type of the agreement approval. The only value is <code>BUYER_AGREEMENT_APPROVAL</code>, an approval that the buyer's organization requires before the agreement request can be accepted.</p>"""
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request that the agreement approval is for.</p>"""
    agreement_approval_id: (
        "capo_marketplace_agreement.types.agreement_approval_id.AgreementApprovalId"
    )
    """<p>The unique identifier of the agreement approval.</p>"""
    name: (
        "capo_marketplace_agreement.types.agreement_approval_name.AgreementApprovalName"
    )
    """<p>The descriptive name of the agreement approval.</p>"""
    status: "capo_marketplace_agreement.types.agreement_approval_status.AgreementApprovalStatus"
    """<p>The current status of the agreement approval. Possible values include <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>EXPIRED</code>, and <code>CANCELLED</code>.</p>"""
    created_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the agreement approval was created.</p>"""
    updated_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the agreement approval was last updated.</p>"""
    started_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when approvers could start acting on the agreement approval.</p>"""
    expires_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement approval expires if it isn't approved or rejected.</p>"""
    approval_needed_by: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time by which the agreement approval must be completed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalSummary) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_type

    out["approvalType"] = (
        capo_marketplace_agreement.types.agreement_approval_type.serialize_aws_json_1_0(
            value["approval_type"]
        )
    )
    out["agreementRequestId"] = value["agreement_request_id"]
    out["agreementApprovalId"] = value["agreement_approval_id"]
    out["name"] = value["name"]
    import capo_marketplace_agreement.types.agreement_approval_status

    out["status"] = (
        capo_marketplace_agreement.types.agreement_approval_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
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
    if "started_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["startedAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["started_at"]
            )
        )
    if "expires_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["expiresAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    import capo_marketplace_agreement.types.timestamp

    out["approvalNeededBy"] = (
        capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["approval_needed_by"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalSummary:
    out: AgreementApprovalSummary = {}  # type: ignore[typeddict-item]
    if data.get("approvalType") is not None:
        import capo_marketplace_agreement.types.agreement_approval_type

        out["approval_type"] = (
            capo_marketplace_agreement.types.agreement_approval_type.deserialize_aws_json_1_0(
                data["approvalType"]
            )
        )
    else:
        import typing

        out["approval_type"] = typing.cast(
            "capo_marketplace_agreement.types.agreement_approval_type.AgreementApprovalType",
            "",
        )
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_approval_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_approval_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_marketplace_agreement.types.agreement_approval_status.AgreementApprovalStatus",
            "",
        )
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
    if data.get("startedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["started_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["startedAt"]
            )
        )
    if data.get("expiresAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["expires_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if data.get("approvalNeededBy") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["approval_needed_by"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["approvalNeededBy"]
            )
        )
    else:
        import datetime

        out["approval_needed_by"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
