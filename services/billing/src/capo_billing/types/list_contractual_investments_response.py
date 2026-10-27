"""Generated from Smithy shape ``com.amazonaws.billing#ListContractualInvestmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.investments
    import capo_billing.types.page_token


class ListContractualInvestmentsResponse(TypedDict, closed=True):
    items: "capo_billing.types.investments.Investments"
    """<p>The list of investments for the investment summary.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token to use on subsequent calls to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListContractualInvestmentsResponse) -> dict:
    out: dict = {}
    import capo_billing.types.investments

    out["items"] = capo_billing.types.investments.serialize_aws_json_1_0(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListContractualInvestmentsResponse:
    out: ListContractualInvestmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_billing.types.investments

        out["items"] = capo_billing.types.investments.deserialize_aws_json_1_0(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
