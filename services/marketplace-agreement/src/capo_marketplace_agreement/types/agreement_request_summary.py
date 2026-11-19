"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementRequestSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.agreement_request_status
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.proposal_summary
    import capo_marketplace_agreement.types.resource_id


class AgreementRequestSummary(TypedDict, closed=True):
    agreement_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    ]
    """<p>The unique identifier of the agreement request.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement (for example, <code>PurchaseAgreement</code>).</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_status.AgreementRequestStatus"
    ]
    """<p>The current status of the agreement request. Possible values include <code>DRAFT</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>ACCEPTED</code>, <code>REJECTED</code>, and <code>CANCELLED</code>.</p>"""
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement that the agreement request is for.</p>"""
    proposal_summary: NotRequired[
        "capo_marketplace_agreement.types.proposal_summary.ProposalSummary"
    ]
    """<p>A summary of the proposal received from the proposer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementRequestSummary) -> dict:
    out: dict = {}
    if "agreement_request_id" in value:
        out["agreementRequestId"] = value["agreement_request_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "proposal_summary" in value:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposalSummary"] = (
            capo_marketplace_agreement.types.proposal_summary.serialize_aws_json_1_0(
                value["proposal_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementRequestSummary:
    out: AgreementRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("proposalSummary") is not None:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposal_summary"] = (
            capo_marketplace_agreement.types.proposal_summary.deserialize_aws_json_1_0(
                data["proposalSummary"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementRequestSummary) -> dict:
    out: dict = {}
    if "agreement_request_id" in value:
        out["agreementRequestId"] = value["agreement_request_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.serialize_cbor(
                value["status"]
            )
        )
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "proposal_summary" in value:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposalSummary"] = (
            capo_marketplace_agreement.types.proposal_summary.serialize_cbor(
                value["proposal_summary"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AgreementRequestSummary:
    out: AgreementRequestSummary = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("proposalSummary") is not None:
        import capo_marketplace_agreement.types.proposal_summary

        out["proposal_summary"] = (
            capo_marketplace_agreement.types.proposal_summary.deserialize_cbor(
                data["proposalSummary"]
            )
        )
    return out
