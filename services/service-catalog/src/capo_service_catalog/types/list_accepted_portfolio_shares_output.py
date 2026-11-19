"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListAcceptedPortfolioSharesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.portfolio_details


class ListAcceptedPortfolioSharesOutput(TypedDict, closed=True):
    portfolio_details: NotRequired[
        "capo_service_catalog.types.portfolio_details.PortfolioDetails"
    ]
    """<p>Information about the portfolios.</p>"""
    next_page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcceptedPortfolioSharesOutput) -> dict:
    out: dict = {}
    if "portfolio_details" in value:
        import capo_service_catalog.types.portfolio_details

        out["PortfolioDetails"] = (
            capo_service_catalog.types.portfolio_details.serialize_aws_json_1_1(
                value["portfolio_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcceptedPortfolioSharesOutput:
    out: ListAcceptedPortfolioSharesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioDetails") is not None:
        import capo_service_catalog.types.portfolio_details

        out["portfolio_details"] = (
            capo_service_catalog.types.portfolio_details.deserialize_aws_json_1_1(
                data["PortfolioDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListAcceptedPortfolioSharesOutput) -> dict:
    out: dict = {}
    if "portfolio_details" in value:
        import capo_service_catalog.types.portfolio_details

        out["PortfolioDetails"] = (
            capo_service_catalog.types.portfolio_details.serialize_cbor(
                value["portfolio_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_cbor(data: dict) -> ListAcceptedPortfolioSharesOutput:
    out: ListAcceptedPortfolioSharesOutput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioDetails") is not None:
        import capo_service_catalog.types.portfolio_details

        out["portfolio_details"] = (
            capo_service_catalog.types.portfolio_details.deserialize_cbor(
                data["PortfolioDetails"]
            )
        )
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
