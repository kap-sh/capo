"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AwsOrganizationApproverOutcome``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_note
    import capo_marketplace_agreement.types.agreement_approval_purchase_orders
    import capo_marketplace_agreement.types.approver_outcome_id
    import capo_marketplace_agreement.types.approver_outcome_status
    import capo_marketplace_agreement.types.timestamp


class AwsOrganizationApproverOutcome(TypedDict, closed=True):
    note: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_note.AgreementApprovalNote"
    ]
    """<p>The note that the approver provided with the decision.</p>"""
    status: (
        "capo_marketplace_agreement.types.approver_outcome_status.ApproverOutcomeStatus"
    )
    """<p>The decision status of the approver. Possible values include <code>QUEUED</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>EXPIRED</code>, and <code>SKIPPED</code>.</p>"""
    updated_at: "capo_marketplace_agreement.types.timestamp.Timestamp"
    """<p>The date and time when the decision was last updated.</p>"""
    approver_outcome_id: NotRequired[
        "capo_marketplace_agreement.types.approver_outcome_id.ApproverOutcomeId"
    ]
    """<p>The unique identifier of this approver in the agreement approval.</p>"""
    purchase_orders: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_purchase_orders.AgreementApprovalPurchaseOrders"
    ]
    """<p>The purchase order references that the approver provided with the decision.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOrganizationApproverOutcome) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    import capo_marketplace_agreement.types.approver_outcome_status

    out["status"] = (
        capo_marketplace_agreement.types.approver_outcome_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_marketplace_agreement.types.timestamp

    out["updatedAt"] = (
        capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    if "approver_outcome_id" in value:
        out["approverOutcomeId"] = value["approver_outcome_id"]
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.serialize_aws_json_1_0(
                value["purchase_orders"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOrganizationApproverOutcome:
    out: AwsOrganizationApproverOutcome = {}  # type: ignore[typeddict-item]
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.approver_outcome_status

        out["status"] = (
            capo_marketplace_agreement.types.approver_outcome_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_marketplace_agreement.types.approver_outcome_status.ApproverOutcomeStatus",
            "",
        )
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
    if data.get("approverOutcomeId") is not None:
        out["approver_outcome_id"] = data["approverOutcomeId"]
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    return out


def redact_sensitive(value: AwsOrganizationApproverOutcome) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "note" in value:
        out["note"] = "*** Sensitive Data Redacted ***"
    return out
