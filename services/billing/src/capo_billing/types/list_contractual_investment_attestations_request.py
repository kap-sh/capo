"""Generated from Smithy shape ``com.amazonaws.billing#ListContractualInvestmentAttestationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.arn_string
    import capo_billing.types.identifier_string
    import capo_billing.types.page_token


class ListContractualInvestmentAttestationsRequest(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract whose attestations you want to list.</p>"""
    investment_summary_id: NotRequired[
        "capo_billing.types.identifier_string.IdentifierString"
    ]
    """<p>The identifier of a specific investment summary to filter the attestations by. If omitted, attestations for all investment summaries in the contract are returned.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token that indicates the next set of results to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of attestations to return in a single call. Minimum value of 1, maximum value of 100.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContractualInvestmentAttestationsRequest) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    if "investment_summary_id" in value:
        out["investmentSummaryId"] = value["investment_summary_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListContractualInvestmentAttestationsRequest:
    out: ListContractualInvestmentAttestationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    if data.get("investmentSummaryId") is not None:
        out["investment_summary_id"] = data["investmentSummaryId"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
