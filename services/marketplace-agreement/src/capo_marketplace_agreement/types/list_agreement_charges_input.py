"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementChargesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_type
    import capo_marketplace_agreement.types.catalog
    import capo_marketplace_agreement.types.max_results
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.resource_id


class ListAgreementChargesInput(TypedDict, closed=True):
    catalog: NotRequired["capo_marketplace_agreement.types.catalog.Catalog"]
    """<p>The catalog in which the charges were created.</p>"""
    agreement_id: NotRequired["capo_marketplace_agreement.types.resource_id.ResourceId"]
    """<p>The unique identifier of the agreement.</p>"""
    agreement_type: NotRequired[
        "capo_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>Filter to retrieve charges of a specific agreement type (for example, <code>PurchaseAgreement</code>).</p>"""
    max_results: NotRequired["capo_marketplace_agreement.types.max_results.MaxResults"]
    """<p>The maximum number of charges to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementChargesInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementChargesInput:
    out: ListAgreementChargesInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAgreementChargesInput) -> dict:
    out: dict = {}
    if "catalog" in value:
        out["catalog"] = value["catalog"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListAgreementChargesInput:
    out: ListAgreementChargesInput = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    if data.get("agreementId") is not None:
        out["agreement_id"] = data["agreementId"]
    if data.get("agreementType") is not None:
        out["agreement_type"] = data["agreementType"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
