"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListOrganizationPortfolioAccessInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.organization_node_type
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token


class ListOrganizationPortfolioAccessInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier. For example, <code>port-2abcdext3y5fk</code>.</p>"""
    organization_node_type: (
        "capo_service_catalog.types.organization_node_type.OrganizationNodeType"
    )
    """<p>The organization node type that will be returned in the output.</p> <ul> <li> <p> <code>ORGANIZATION</code> - Organization that has access to the portfolio. </p> </li> <li> <p> <code>ORGANIZATIONAL_UNIT</code> - Organizational unit that has access to the portfolio within your organization.</p> </li> <li> <p> <code>ACCOUNT</code> - Account that has access to the portfolio within your organization.</p> </li> </ul>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOrganizationPortfolioAccessInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    import capo_service_catalog.types.organization_node_type

    out["OrganizationNodeType"] = (
        capo_service_catalog.types.organization_node_type.serialize_aws_json_1_1(
            value["organization_node_type"]
        )
    )
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOrganizationPortfolioAccessInput:
    out: ListOrganizationPortfolioAccessInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError(
            "ListOrganizationPortfolioAccessInput.portfolio_id required"
        )
    if data.get("OrganizationNodeType") is not None:
        import capo_service_catalog.types.organization_node_type

        out["organization_node_type"] = (
            capo_service_catalog.types.organization_node_type.deserialize_aws_json_1_1(
                data["OrganizationNodeType"]
            )
        )
    else:
        raise DeserializationError(
            "ListOrganizationPortfolioAccessInput.organization_node_type required"
        )
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
