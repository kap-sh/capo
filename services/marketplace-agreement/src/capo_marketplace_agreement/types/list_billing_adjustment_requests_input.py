"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListBillingAdjustmentRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_id
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.billing_adjustment_status
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.timestamp


class ListBillingAdjustmentRequestsInput(TypedDict, closed=True):
    agreement_id: NotRequired[
        "capo_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement to list billing adjustment requests for.</p>"""
    status: NotRequired[
        "capo_marketplace_agreement.types.billing_adjustment_status.BillingAdjustmentStatus"
    ]
    """<p>An optional filter to return billing adjustment requests with the specified status.</p>"""
    created_after: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>An optional filter to return billing adjustment requests created after the specified timestamp.</p>"""
    created_before: NotRequired["capo_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>An optional filter to return billing adjustment requests created before the specified timestamp.</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of billing adjustment requests to return in the response.</p>"""
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>An optional filter to return billing adjustment requests by catalog (e.g., <code>AWSMarketplace</code>).</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>An optional filter to return billing adjustment requests by agreement type (e.g., <code>PurchaseAgreement</code>).</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingAdjustmentRequestsInput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            capo_marketplace_agreement.types.billing_adjustment_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_after" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAfter"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_after"]
            )
        )
    if "created_before" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdBefore"] = (
            capo_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["created_before"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingAdjustmentRequestsInput:
    out: ListBillingAdjustmentRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            capo_marketplace_agreement.types.billing_adjustment_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("createdAfter") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_after"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdAfter"]
            )
        )
    if data.get("createdBefore") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_before"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["createdBefore"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListBillingAdjustmentRequestsInput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import capo_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            capo_marketplace_agreement.types.billing_adjustment_status.serialize_cbor(
                value["status"]
            )
        )
    if "created_after" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdAfter"] = capo_marketplace_agreement.types.timestamp.serialize_cbor(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_marketplace_agreement.types.timestamp

        out["createdBefore"] = (
            capo_marketplace_agreement.types.timestamp.serialize_cbor(
                value["created_before"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListBillingAdjustmentRequestsInput:
    out: ListBillingAdjustmentRequestsInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("status") is not None:
        import capo_marketplace_agreement.types.billing_adjustment_status

        out["status"] = (
            capo_marketplace_agreement.types.billing_adjustment_status.deserialize_cbor(
                data["status"]
            )
        )
    if data.get("createdAfter") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_after"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_cbor(
                data["createdAfter"]
            )
        )
    if data.get("createdBefore") is not None:
        import capo_marketplace_agreement.types.timestamp

        out["created_before"] = (
            capo_marketplace_agreement.types.timestamp.deserialize_cbor(
                data["createdBefore"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
