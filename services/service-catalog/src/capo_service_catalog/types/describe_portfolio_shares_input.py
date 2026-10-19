"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribePortfolioSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.describe_portfolio_share_type
    import capo_service_catalog.types.id
    import capo_service_catalog.types.page_size_max100
    import capo_service_catalog.types.page_token


class DescribePortfolioSharesInput(TypedDict, closed=True):
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The unique identifier of the portfolio for which shares will be retrieved.</p>"""
    type: "capo_service_catalog.types.describe_portfolio_share_type.DescribePortfolioShareType"
    """<p>The type of portfolio share to summarize. This field acts as a filter on the type of portfolio share, which can be one of the following:</p> <p>1. <code>ACCOUNT</code> - Represents an external account to account share.</p> <p>2. <code>ORGANIZATION</code> - Represents a share to an organization. This share is available to every account in the organization.</p> <p>3. <code>ORGANIZATIONAL_UNIT</code> - Represents a share to an organizational unit.</p> <p>4. <code>ORGANIZATION_MEMBER_ACCOUNT</code> - Represents a share to an account in the organization.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size_max100.PageSizeMax100"]
    """<p>The maximum number of items to return with this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePortfolioSharesInput) -> dict:
    out: dict = {}
    out["PortfolioId"] = value["portfolio_id"]
    import capo_service_catalog.types.describe_portfolio_share_type

    out["Type"] = (
        capo_service_catalog.types.describe_portfolio_share_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePortfolioSharesInput:
    out: DescribePortfolioSharesInput = {}  # type: ignore[typeddict-item]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("DescribePortfolioSharesInput.portfolio_id required")
    if data.get("Type") is not None:
        import capo_service_catalog.types.describe_portfolio_share_type

        out["type"] = (
            capo_service_catalog.types.describe_portfolio_share_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("DescribePortfolioSharesInput.type required")
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
