"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListAcceptedPortfolioSharesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.page_size_max100
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.portfolio_share_type


class ListAcceptedPortfolioSharesInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size_max100.PageSizeMax100"]
    """<p>The maximum number of items to return with this call.</p>"""
    portfolio_share_type: NotRequired[
        "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
    ]
    """<p>The type of shared portfolios to list. The default is to list imported portfolios.</p> <ul> <li> <p> <code>AWS_ORGANIZATIONS</code> - List portfolios accepted and shared via organizational sharing by the management account or delegated administrator of your organization.</p> </li> <li> <p> <code>AWS_SERVICECATALOG</code> - Deprecated type.</p> </li> <li> <p> <code>IMPORTED</code> - List imported portfolios that have been accepted and shared through account-to-account sharing.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAcceptedPortfolioSharesInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "portfolio_share_type" in value:
        import capo_service_catalog.types.portfolio_share_type

        out["PortfolioShareType"] = (
            capo_service_catalog.types.portfolio_share_type.serialize_aws_json_1_1(
                value["portfolio_share_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAcceptedPortfolioSharesInput:
    out: ListAcceptedPortfolioSharesInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PortfolioShareType") is not None:
        import capo_service_catalog.types.portfolio_share_type

        out["portfolio_share_type"] = (
            capo_service_catalog.types.portfolio_share_type.deserialize_aws_json_1_1(
                data["PortfolioShareType"]
            )
        )
    return out
