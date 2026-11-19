"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BuyerAgreementApproval``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_id
    import capo_marketplace_agreement.types.agreement_approval_name
    import capo_marketplace_agreement.types.agreement_approval_proposal_summary
    import capo_marketplace_agreement.types.agreement_approval_proposer
    import capo_marketplace_agreement.types.agreement_approval_requester
    import capo_marketplace_agreement.types.agreement_approval_status
    import capo_marketplace_agreement.types.agreement_approval_type
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.buyer_agreement_approval_levels
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input
    import capo_marketplace_agreement.types.timestamp


class BuyerAgreementApproval(TypedDict, closed=True):
    approval_type: (
        "capo_marketplace_agreement.types.agreement_approval_type.AgreementApprovalType"
    )
    """<p>The type of the agreement approval, which is <code>BUYER_AGREEMENT_APPROVAL</code>.</p>"""
    agreement_approval_id: (
        "capo_marketplace_agreement.types.agreement_approval_id.AgreementApprovalId"
    )
    """<p>The unique identifier of the agreement approval.</p>"""
    name: (
        "capo_marketplace_agreement.types.agreement_approval_name.AgreementApprovalName"
    )
    """<p>The descriptive name of the agreement approval.</p>"""
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request that the agreement approval is for. Use <code>GetAgreementRequest</code> to retrieve the agreement request details.</p>"""
    status: "capo_marketplace_agreement.types.agreement_approval_status.AgreementApprovalStatus"
    """<p>The current status of the agreement approval. Possible values include <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>EXPIRED</code>, and <code>CANCELLED</code>.</p>"""
    requester: "capo_marketplace_agreement.types.agreement_approval_requester.AgreementApprovalRequester"
    """<p>The account that started the agreement approval.</p>"""
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
    levels: "capo_marketplace_agreement.types.buyer_agreement_approval_levels.BuyerAgreementApprovalLevels"
    """<p>The approval levels, in the order they are evaluated. Approvers at a level can act only after the previous level is approved. Each level lists its approvers and the decision of each one.</p>"""
    plan_input: "capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.BuyerAgreementApprovalPlanInput"
    """<p>The approval plan and the note that the requester provided in <code>StartAgreementApprovals</code>.</p>"""
    proposer: "capo_marketplace_agreement.types.agreement_approval_proposer.AgreementApprovalProposer"
    """<p>The details of the party proposing the agreement terms. This is commonly the seller for <code>PurchaseAgreement</code>.</p>"""
    proposal_summary: "capo_marketplace_agreement.types.agreement_approval_proposal_summary.AgreementApprovalProposalSummary"
    """<p>A summary of the proposal received from the proposer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BuyerAgreementApproval) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_type

    out["approvalType"] = (
        capo_marketplace_agreement.types.agreement_approval_type.serialize_aws_json_1_0(
            value["approval_type"]
        )
    )
    out["agreementApprovalId"] = value["agreement_approval_id"]
    out["name"] = value["name"]
    out["agreementRequestId"] = value["agreement_request_id"]
    import capo_marketplace_agreement.types.agreement_approval_status

    out["status"] = (
        capo_marketplace_agreement.types.agreement_approval_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_requester

    out["requester"] = (
        capo_marketplace_agreement.types.agreement_approval_requester.serialize_aws_json_1_0(
            value["requester"]
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
    import capo_marketplace_agreement.types.buyer_agreement_approval_levels

    out["levels"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_levels.serialize_aws_json_1_0(
            value["levels"]
        )
    )
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

    out["planInput"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.serialize_aws_json_1_0(
            value["plan_input"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_proposer

    out["proposer"] = (
        capo_marketplace_agreement.types.agreement_approval_proposer.serialize_aws_json_1_0(
            value["proposer"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_proposal_summary

    out["proposalSummary"] = (
        capo_marketplace_agreement.types.agreement_approval_proposal_summary.serialize_aws_json_1_0(
            value["proposal_summary"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BuyerAgreementApproval:
    out: BuyerAgreementApproval = {}  # type: ignore[typeddict-item]
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
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
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
    if data.get("requester") is not None:
        import capo_marketplace_agreement.types.agreement_approval_requester

        out["requester"] = (
            capo_marketplace_agreement.types.agreement_approval_requester.deserialize_aws_json_1_0(
                data["requester"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.requester required")
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
    if data.get("levels") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_levels

        out["levels"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_levels.deserialize_aws_json_1_0(
                data["levels"]
            )
        )
    else:
        out["levels"] = []
    if data.get("planInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        out["plan_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.deserialize_aws_json_1_0(
                data["planInput"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.plan_input required")
    if data.get("proposer") is not None:
        import capo_marketplace_agreement.types.agreement_approval_proposer

        out["proposer"] = (
            capo_marketplace_agreement.types.agreement_approval_proposer.deserialize_aws_json_1_0(
                data["proposer"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.proposer required")
    if data.get("proposalSummary") is not None:
        import capo_marketplace_agreement.types.agreement_approval_proposal_summary

        out["proposal_summary"] = (
            capo_marketplace_agreement.types.agreement_approval_proposal_summary.deserialize_aws_json_1_0(
                data["proposalSummary"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.proposal_summary required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuyerAgreementApproval) -> dict:
    out: dict = {}
    import capo_marketplace_agreement.types.agreement_approval_type

    out["approvalType"] = (
        capo_marketplace_agreement.types.agreement_approval_type.serialize_cbor(
            value["approval_type"]
        )
    )
    out["agreementApprovalId"] = value["agreement_approval_id"]
    out["name"] = value["name"]
    out["agreementRequestId"] = value["agreement_request_id"]
    import capo_marketplace_agreement.types.agreement_approval_status

    out["status"] = (
        capo_marketplace_agreement.types.agreement_approval_status.serialize_cbor(
            value["status"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_requester

    out["requester"] = (
        capo_marketplace_agreement.types.agreement_approval_requester.serialize_cbor(
            value["requester"]
        )
    )
    import capo_marketplace_agreement.types.timestamp

    out["createdAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_marketplace_agreement.types.timestamp

    out["updatedAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
        value["updated_at"]
    )
    if "started_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["startedAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["started_at"]
        )
    if "expires_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["expiresAt"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["expires_at"]
        )
    import capo_marketplace_agreement.types.timestamp

    out["approvalNeededBy"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
        value["approval_needed_by"]
    )
    import capo_marketplace_agreement.types.buyer_agreement_approval_levels

    out["levels"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_levels.serialize_cbor(
            value["levels"]
        )
    )
    import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

    out["planInput"] = (
        capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.serialize_cbor(
            value["plan_input"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_proposer

    out["proposer"] = (
        capo_marketplace_agreement.types.agreement_approval_proposer.serialize_cbor(
            value["proposer"]
        )
    )
    import capo_marketplace_agreement.types.agreement_approval_proposal_summary

    out["proposalSummary"] = (
        capo_marketplace_agreement.types.agreement_approval_proposal_summary.serialize_cbor(
            value["proposal_summary"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> BuyerAgreementApproval:
    out: BuyerAgreementApproval = {}  # type: ignore[typeddict-item]
    if data.get("approvalType") is not None:
        import capo_marketplace_agreement.types.agreement_approval_type

        out["approval_type"] = (
            capo_marketplace_agreement.types.agreement_approval_type.deserialize_cbor(
                data["approvalType"]
            )
        )
    else:
        import typing

        out["approval_type"] = typing.cast(
            "capo_marketplace_agreement.types.agreement_approval_type.AgreementApprovalType",
            "",
        )
    if data.get("agreementApprovalId") is not None:
        out["agreement_approval_id"] = data["agreementApprovalId"]
    else:
        out["agreement_approval_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_approval_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_approval_status.deserialize_cbor(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_marketplace_agreement.types.agreement_approval_status.AgreementApprovalStatus",
            "",
        )
    if data.get("requester") is not None:
        import capo_marketplace_agreement.types.agreement_approval_requester

        out["requester"] = (
            capo_marketplace_agreement.types.agreement_approval_requester.deserialize_cbor(
                data["requester"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.requester required")
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["updated_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("startedAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["started_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["startedAt"]
        )
    if data.get("expiresAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["expires_at"] = capo_marketplace_agreement.types.timestamp.deserialize_cbor(
            data["expiresAt"]
        )
    if data.get("approvalNeededBy") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["approval_needed_by"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_cbor(
                data["approvalNeededBy"]
            )
        )
    else:
        import datetime

        out["approval_needed_by"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("levels") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_levels

        out["levels"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_levels.deserialize_cbor(
                data["levels"]
            )
        )
    else:
        out["levels"] = []
    if data.get("planInput") is not None:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        out["plan_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.deserialize_cbor(
                data["planInput"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.plan_input required")
    if data.get("proposer") is not None:
        import capo_marketplace_agreement.types.agreement_approval_proposer

        out["proposer"] = (
            capo_marketplace_agreement.types.agreement_approval_proposer.deserialize_cbor(
                data["proposer"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.proposer required")
    if data.get("proposalSummary") is not None:
        import capo_marketplace_agreement.types.agreement_approval_proposal_summary

        out["proposal_summary"] = (
            capo_marketplace_agreement.types.agreement_approval_proposal_summary.deserialize_cbor(
                data["proposalSummary"]
            )
        )
    else:
        raise DeserializationError("BuyerAgreementApproval.proposal_summary required")
    return out


def redact_sensitive(value: BuyerAgreementApproval) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "levels" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_levels

        out["levels"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_levels.redact_sensitive(
                value["levels"]
            )
        )
    if "plan_input" in value:
        import capo_marketplace_agreement.types.buyer_agreement_approval_plan_input

        out["plan_input"] = (
            capo_marketplace_agreement.types.buyer_agreement_approval_plan_input.redact_sensitive(
                value["plan_input"]
            )
        )
    return out
