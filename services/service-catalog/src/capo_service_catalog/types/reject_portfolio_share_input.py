"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RejectPortfolioShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.portfolio_share_type


class RejectPortfolioShareInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    portfolio_share_type: NotRequired[
        "capo_service_catalog.types.portfolio_share_type.PortfolioShareType"
    ]
    """<p>The type of shared portfolios to reject. The default is to reject imported portfolios.</p> <ul> <li> <p> <code>AWS_ORGANIZATIONS</code> - Reject portfolios shared by the management account of your organization.</p> </li> <li> <p> <code>IMPORTED</code> - Reject imported portfolios.</p> </li> <li> <p> <code>AWS_SERVICECATALOG</code> - Not supported. (Throws ResourceNotFoundException.)</p> </li> </ul> <p>For example, <code>aws servicecatalog reject-portfolio-share --portfolio-id "port-2qwzkwxt3y5fk" --portfolio-share-type AWS_ORGANIZATIONS</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RejectPortfolioShareInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    if "portfolio_share_type" in value:
        import capo_service_catalog.types.portfolio_share_type

        out["PortfolioShareType"] = (
            capo_service_catalog.types.portfolio_share_type.serialize_aws_json_1_1(
                value["portfolio_share_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RejectPortfolioShareInput:
    out: RejectPortfolioShareInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError("RejectPortfolioShareInput.portfolio_id required")
    if data.get("PortfolioShareType") is not None:
        import capo_service_catalog.types.portfolio_share_type

        out["portfolio_share_type"] = (
            capo_service_catalog.types.portfolio_share_type.deserialize_aws_json_1_1(
                data["PortfolioShareType"]
            )
        )
    return out
