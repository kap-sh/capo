"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CreateAgreementRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.agreement_request_status
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.approval_requirement
    import capo_marketplace_agreement.types.charge_summary
    import capo_marketplace_agreement.types.timestamp


class CreateAgreementRequestOutput(TypedDict, closed=True):
    agreement_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    ]
    """<p>The unique identifier of the agreement request created. Use this identifier with <code>AcceptAgreementRequest</code> to accept the agreement.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement (for example, <code>PurchaseAgreement</code>).</p>"""
    charge_summary: NotRequired[
        "capo_marketplace_agreement.types.charge_summary.ChargeSummary"
    ]
    """<p>Provides details of the charges associated with the agreement request. This is only applicable when a request is created for <code>PurchaseAgreement</code>.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_status.AgreementRequestStatus"
    ]
    """<p>The current status of the agreement request. Possible values include:</p> <ul> <li> <p> <code>DRAFT</code> – The agreement request has been created but not yet submitted for approval.</p> </li> <li> <p> <code>PENDING_APPROVAL</code> – The agreement request is waiting for one or more approvers to decide.</p> </li> <li> <p> <code>APPROVED</code> – All required approvals have been granted, but the agreement request wasn't accepted automatically. Call <code>AcceptAgreementRequest</code> to accept it. If the call fails, its error explains why.</p> </li> <li> <p> <code>ACCEPTED</code> – The agreement request has been accepted and the resulting agreement has been created.</p> </li> <li> <p> <code>REJECTED</code> – At least one approver rejected the agreement request. It won't proceed.</p> </li> <li> <p> <code>CANCELLED</code> – The agreement request was cancelled before completion, by the acceptor or because the acceptor's account left its AWS organization.</p> </li> </ul>"""
    approval_requirement: NotRequired[
        "capo_marketplace_agreement.types.approval_requirement.ApprovalRequirement"
    ]
    """<p>Indicates whether the agreement request requires approval before it can be accepted. Values are <code>REQUIRED</code> and <code>NOT_REQUIRED</code>.</p>"""
    created_at: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement request was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAgreementRequestOutput) -> dict:
    out: dict = {}
    if "agreement_request_id" in value:
        out["agreementRequestId"] = value["agreement_request_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "charge_summary" in value:
        import capo_marketplace_agreement.types.charge_summary

        out["chargeSummary"] = (
            capo_marketplace_agreement.types.charge_summary.serialize_aws_json_1_0(
                value["charge_summary"]
            )
        )
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "approval_requirement" in value:
        import capo_marketplace_agreement.types.approval_requirement

        out["approvalRequirement"] = (
            capo_marketplace_agreement.types.approval_requirement.serialize_aws_json_1_0(
                value["approval_requirement"]
            )
        )
    if "created_at" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAt"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAgreementRequestOutput:
    out: CreateAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("chargeSummary") is not None:
        import capo_marketplace_agreement.types.charge_summary

        out["charge_summary"] = (
            capo_marketplace_agreement.types.charge_summary.deserialize_aws_json_1_0(
                data["chargeSummary"]
            )
        )
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("approvalRequirement") is not None:
        import capo_marketplace_agreement.types.approval_requirement

        out["approval_requirement"] = (
            capo_marketplace_agreement.types.approval_requirement.deserialize_aws_json_1_0(
                data["approvalRequirement"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_at"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    return out
