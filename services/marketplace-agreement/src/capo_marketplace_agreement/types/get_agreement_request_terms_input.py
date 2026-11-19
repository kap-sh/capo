"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementRequestTermsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_request_id
    import capo_marketplace_agreement.types.agreement_request_terms_max_results
    import capo_marketplace_agreement.types.next_token


class GetAgreementRequestTermsInput(TypedDict, closed=True):
    agreement_request_id: (
        "capo_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    )
    """<p>The unique identifier of the agreement request.</p>"""
    max_results: NotRequired[
        "capo_marketplace_agreement.types.agreement_request_terms_max_results.AgreementRequestTermsMaxResults"
    ]
    """<p>The maximum number of terms to return in the response.</p>"""
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>A token to specify where to start pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementRequestTermsInput) -> dict:
    out: dict = {}
    out["agreementRequestId"] = value["agreement_request_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementRequestTermsInput:
    out: GetAgreementRequestTermsInput = {}  # type: ignore[typeddict-item]
    if data.get("agreementRequestId") is not None:
        out["agreement_request_id"] = data["agreementRequestId"]
    else:
        out["agreement_request_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
