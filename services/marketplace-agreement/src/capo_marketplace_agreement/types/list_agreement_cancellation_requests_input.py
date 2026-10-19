"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementCancellationRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_cancellation_request_status
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.party_type


class ListAgreementCancellationRequestsInput(TypedDict, closed=True):
    party_type: "capo_marketplace_agreement.types.party_type.PartyType"
    """<p>The party type for the cancellation requests. Required parameter. Use <code>Proposer</code> to list cancellation requests where you are the seller, or <code>Acceptor</code> to list cancellation requests where you are the buyer.</p>"""
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>An optional parameter to filter cancellation requests for a specific agreement.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_cancellation_request_status.AgreementCancellationRequestStatus"
    ]
    """<p>An optional parameter to filter cancellation requests by status.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>An optional parameter to filter cancellation requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>"""
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional parameter to filter cancellation requests by catalog (e.g., <code>AWSMarketplace</code>).</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of cancellation requests to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementCancellationRequestsInput) -> dict:
    out: dict = {}
    out["partyType"] = value["party_type"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementCancellationRequestsInput:
    out: ListAgreementCancellationRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("partyType") is not None:
        out["party_type"] = data["partyType"]
    else:
        out["party_type"] = ""
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_cancellation_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_cancellation_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
