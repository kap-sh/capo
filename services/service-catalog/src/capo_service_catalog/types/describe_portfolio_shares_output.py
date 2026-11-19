"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.portfolio_share_details


class DescribePortfolioSharesOutput(TypedDict, closed=True):
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""
    portfolio_share_details: NotRequired[
        "capo_service_catalog.types.portfolio_share_details.PortfolioShareDetails"
    ]
    """<p>Summaries about each of the portfolio shares.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioSharesOutput) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "portfolio_share_details" in value:
        import capo_service_catalog.types.portfolio_share_details

        out["PortfolioShareDetails"] = (
            capo_service_catalog.types.portfolio_share_details.serialize_aws_json_1_1(
                value["portfolio_share_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioSharesOutput:
    out: DescribePortfolioSharesOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("PortfolioShareDetails") is not None:
        import capo_service_catalog.types.portfolio_share_details

        out["portfolio_share_details"] = (
            capo_service_catalog.types.portfolio_share_details.deserialize_aws_json_1_1(
                data["PortfolioShareDetails"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribePortfolioSharesOutput) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "portfolio_share_details" in value:
        import capo_service_catalog.types.portfolio_share_details

        out["PortfolioShareDetails"] = (
            capo_service_catalog.types.portfolio_share_details.serialize_cbor(
                value["portfolio_share_details"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribePortfolioSharesOutput:
    out: DescribePortfolioSharesOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("PortfolioShareDetails") is not None:
        import capo_service_catalog.types.portfolio_share_details

        out["portfolio_share_details"] = (
            capo_service_catalog.types.portfolio_share_details.deserialize_cbor(
                data["PortfolioShareDetails"]
            )
        )
    return out
