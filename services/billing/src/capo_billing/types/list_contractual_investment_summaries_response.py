"""Generated from Smithy shape ``com.amazonaws.billing#ListContractualInvestmentSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.investment_summaries
    import capo_billing.types.page_token


class ListContractualInvestmentSummariesResponse(TypedDict, closed=True):
    items: "capo_billing.types.investment_summaries.InvestmentSummaries"
    """<p>The list of investment summaries under the contract. It includes the investment name, maximum investment amount, and investment type. It does not provide investment details. Use this to know if the contract has investment terms and what type.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token to use on subsequent calls to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContractualInvestmentSummariesResponse) -> dict:
    out: dict = {}
    import capo_billing.types.investment_summaries

    out["items"] = capo_billing.types.investment_summaries.serialize_aws_json_1_0(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContractualInvestmentSummariesResponse:
    out: ListContractualInvestmentSummariesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_billing.types.investment_summaries

        out["items"] = capo_billing.types.investment_summaries.deserialize_aws_json_1_0(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
