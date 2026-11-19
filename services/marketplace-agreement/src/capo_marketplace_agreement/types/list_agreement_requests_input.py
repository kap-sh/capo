"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_status
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.resource_id


class ListAgreementRequestsInput(TypedDict, closed=True):
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional parameter to list agreement requests by catalog (for example, <code>AWSMarketplace</code>).</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_status.AgreementRequestStatus"
    ]
    """<p>An optional parameter to list agreement requests by status. Valid values include <code>DRAFT</code>, <code>PENDING_APPROVAL</code>, <code>APPROVED</code>, <code>ACCEPTED</code>, <code>REJECTED</code>, and <code>CANCELLED</code>. If you don't specify a status, agreement requests of all statuses are returned.</p>"""
    resource_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>An optional parameter to list agreement requests for a specific resource, such as a product.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of agreement requests to return in a single response (1-50). Default is 20.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementRequestsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementRequestsInput:
    out: ListAgreementRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgreementRequestsInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "status" in value:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.serialize_cbor(
                value["status"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgreementRequestsInput:
    out: ListAgreementRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.agreement_request_status

        out["status"] = (
            capo_marketplace_agreement.types.agreement_request_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
