"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementApprovalsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_approval_party_type
    import capo_marketplace_agreement.types.agreement_approval_status
    import capo_marketplace_agreement.types.agreement_approval_type
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token


class ListAgreementApprovalsInput(TypedDict, closed=True):
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional parameter to filter agreement approvals by catalog (for example, <code>AWSMarketplace</code>).</p>"""
    party_type: "capo_marketplace_agreement.types.agreement_approval_party_type.AgreementApprovalPartyType"
    """<p>The party type for the agreement approvals. Required parameter. Use <code>REQUESTER</code> to list agreement approvals for agreement requests that you created, or <code>AWS_ORGANIZATION_ADMIN</code> to list agreement approvals as an AWS Organizations administrator.</p>"""
    agreement_request_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    ]
    """<p>An optional parameter to filter agreement approvals for a specific agreement request.</p>"""
    approval_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_type.AgreementApprovalType"
    ]
    """<p>An optional parameter to filter agreement approvals by type. The only valid value is <code>BUYER_AGREEMENT_APPROVAL</code>.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_approval_status.AgreementApprovalStatus"
    ]
    """<p>An optional parameter to filter agreement approvals by status. Valid values include <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>REJECTED</code>, <code>EXPIRED</code>, and <code>CANCELLED</code>. If you don't specify a status, agreement approvals of all statuses are returned.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of agreement approvals to return in a single response (1-50). Default is 20.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementApprovalsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    import capo_marketplace_agreement.types.agreement_approval_party_type

    out["partyType"] = (
        capo_marketplace_agreement.types.agreement_approval_party_type.serialize_aws_json_1_0(
            value["party_type"]
        )
    )
    if "agreement_request_id" in value:
        out["agreementRequestId"] = value["agreement_request_id"]
    if "approval_type" in value:
        import capo_marketplace_agreement.types.agreement_approval_type

        out["approvalType"] = (
            capo_marketplace_agreement.types.agreement_approval_type.serialize_aws_json_1_0(
                value["approval_type"]
            )
        )
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_approval_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_approval_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementApprovalsInput:
    out: ListAgreementApprovalsInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("partyType") is not None:
        import capo_marketplace_agreement.types.agreement_approval_party_type

        out["party_type"] = (
            capo_marketplace_agreement.types.agreement_approval_party_type.deserialize_aws_json_1_0(
                data["partyType"]
            )
        )
    else:
        import typing

        out["party_type"] = typing.cast(
            "capo_marketplace_agreement.types.agreement_approval_party_type.AgreementApprovalPartyType",
            "",
        )
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    if data.get("approvalType") is not None:
        import capo_marketplace_agreement.types.agreement_approval_type

        out["approval_type"] = (
            capo_marketplace_agreement.types.agreement_approval_type.deserialize_aws_json_1_0(
                data["approvalType"]
            )
        )
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_approval_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_approval_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
