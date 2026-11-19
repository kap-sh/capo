"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EmailApproverOutcome``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_note
    import capo_marketplace_agreement.types.agreement_approval_purchase_orders
    import capo_marketplace_agreement.types.approver_name
    import capo_marketplace_agreement.types.approver_outcome_id
    import capo_marketplace_agreement.types.approver_outcome_status
    import capo_marketplace_agreement.types.caller_identity
    import capo_marketplace_agreement.types.email_address
    import capo_marketplace_agreement.types.timestamp


class EmailApproverOutcome(TypedDict, closed=True):
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
    """<p>The unique identifier of this approver in the agreement approval. An administrator of the buyer's AWS organization passes it as <code>approverOutcomeIdToOverride</code> to decide on the approver's behalf.</p>"""
    email_address: "capo_marketplace_agreement.types.email_address.EmailAddress"
    """<p>The email address of the approver.</p>"""
    name: NotRequired["capo_marketplace_agreement.types.approver_name.ApproverName"]
    """<p>The name of the approver.</p>"""
    purchase_orders: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_purchase_orders.AgreementApprovalPurchaseOrders"
    ]
    """<p>The purchase order references that the approver provided with the decision.</p>"""
    overridden_by: NotRequired[
        "capo_marketplace_agreement.types.caller_identity.CallerIdentity"
    ]
    """<p>The identity that decided on the approver's behalf. This field is empty unless an administrator of the buyer's AWS organization decided for the approver.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EmailApproverOutcome) -> dict:
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
    out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.serialize_aws_json_1_0(
                value["purchase_orders"]
            )
        )
    if "overridden_by" in value:
        import capo_marketplace_agreement.types.caller_identity

        out["overriddenBy"] = (
            capo_marketplace_agreement.types.caller_identity.serialize_aws_json_1_0(
                value["overridden_by"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EmailApproverOutcome:
    out: EmailApproverOutcome = {}  # type: ignore[typeddict-item]
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
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.deserialize_aws_json_1_0(
                data["purchaseOrders"]
            )
        )
    if data.get("overriddenBy") is not None:
        import capo_marketplace_agreement.types.caller_identity

        out["overridden_by"] = (
            capo_marketplace_agreement.types.caller_identity.deserialize_aws_json_1_0(
                data["overriddenBy"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EmailApproverOutcome) -> dict:
    out: dict = {}
    if "note" in value:
        out["note"] = value["note"]
    import capo_marketplace_agreement.types.approver_outcome_status

    out["status"] = (
        capo_marketplace_agreement.types.approver_outcome_status.serialize_cbor(
            value["status"]
        )
    )
    import capo_marketplace_agreement.types.timestamp

    out["updatedAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
        value["updated_at"]
    )
    if "approver_outcome_id" in value:
        out["approverOutcomeId"] = value["approver_outcome_id"]
    out["emailAddress"] = value["email_address"]
    if "name" in value:
        out["name"] = value["name"]
    if "purchase_orders" in value:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchaseOrders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.serialize_cbor(
                value["purchase_orders"]
            )
        )
    if "overridden_by" in value:
        import capo_marketplace_agreement.types.caller_identity

        out["overriddenBy"] = (
            capo_marketplace_agreement.types.caller_identity.serialize_cbor(
                value["overridden_by"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EmailApproverOutcome:
    out: EmailApproverOutcome = {}  # type: ignore[typeddict-item]
    if data.get("note") is not None:
        out["note"] = data["note"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.approver_outcome_status

        out["status"] = (
            capo_marketplace_agreement.types.approver_outcome_status.deserialize_cbor(
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

        out["updated_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("approverOutcomeId") is not None:
        out["approver_outcome_id"] = data["approverOutcomeId"]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    else:
        out["email_address"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("purchaseOrders") is not None:
        import capo_marketplace_agreement.types.agreement_approval_purchase_orders

        out["purchase_orders"] = (
            capo_marketplace_agreement.types.agreement_approval_purchase_orders.deserialize_cbor(
                data["purchaseOrders"]
            )
        )
    if data.get("overriddenBy") is not None:
        import capo_marketplace_agreement.types.caller_identity

        out["overridden_by"] = (
            capo_marketplace_agreement.types.caller_identity.deserialize_cbor(
                data["overriddenBy"]
            )
        )
    return out


def redact_sensitive(value: EmailApproverOutcome) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "note" in value:
        out["note"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
