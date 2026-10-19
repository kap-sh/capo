"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioShareStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id


class DescribePortfolioShareStatusInput(TypedDict, closed=True):
    portfolio_share_token: "capo_service_catalog.types.id.Id"
    """<p>The token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioShareStatusInput) -> dict:
    out: dict = {}
    out["PortfolioShareToken"] = value["portfolio_share_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioShareStatusInput:
    out: DescribePortfolioShareStatusInput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioShareToken") is not None:
        out["portfolio_share_token"] = data["PortfolioShareToken"]
    else:
        out["portfolio_share_token"] = ""
    return out
