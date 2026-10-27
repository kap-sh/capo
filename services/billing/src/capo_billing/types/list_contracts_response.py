"""Generated from Smithy shape ``com.amazonaws.billing#ListContractsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.contract_summaries
    import capo_billing.types.page_token


class ListContractsResponse(TypedDict, closed=True):
    items: "capo_billing.types.contract_summaries.ContractSummaries"
    """<p>The list of contracts that your Amazon Web Services account is an eligible payer account of.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token to use on subsequent calls to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContractsResponse) -> dict:
    out: dict = {}
    import capo_billing.types.contract_summaries

    out["items"] = capo_billing.types.contract_summaries.serialize_aws_json_1_0(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContractsResponse:
    out: ListContractsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_billing.types.contract_summaries

        out["items"] = capo_billing.types.contract_summaries.deserialize_aws_json_1_0(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
