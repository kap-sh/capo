"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.account_id
    import capo_service_catalog.types.id
    import capo_service_catalog.types.nullable_boolean
    import capo_service_catalog.types.organization_node


class UpdatePortfolioShareInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The unique identifier of the portfolio for which the share will be updated.</p>"""
    account_id: NotRequired["capo_service_catalog.types.account_id.AccountId"]
    """<p>The Amazon Web Services account Id of the recipient account. This field is required when updating an external account to account type share.</p>"""
    organization_node: NotRequired[
        "capo_service_catalog.types.organization_node.OrganizationNode"
    ]
    share_tag_options: NotRequired[
        "capo_service_catalog.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Enables or disables <code>TagOptions</code> sharing for the portfolio share. If this field is not provided, the current state of TagOptions sharing on the portfolio share will not be modified.</p>"""
    share_principals: NotRequired[
        "capo_service_catalog.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A flag to enables or disables <code>Principals</code> sharing in the portfolio. If this field is not provided, the current state of the <code>Principals</code> sharing on the portfolio share will not be modified. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioShareInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "organization_node" in value:
        import capo_service_catalog.types.organization_node

        out["OrganizationNode"] = (
            capo_service_catalog.types.organization_node.serialize_aws_json_1_1(
                value["organization_node"]
            )
        )
    if "share_tag_options" in value:
        out["ShareTagOptions"] = value["share_tag_options"]
    if "share_principals" in value:
        out["SharePrincipals"] = value["share_principals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioShareInput:
    out: UpdatePortfolioShareInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        out["portfolio_id"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("OrganizationNode") is not None:
        import capo_service_catalog.types.organization_node

        out["organization_node"] = (
            capo_service_catalog.types.organization_node.deserialize_aws_json_1_1(
                data["OrganizationNode"]
            )
        )
    if data.get("ShareTagOptions") is not None:
        out["share_tag_options"] = data["ShareTagOptions"]
    if data.get("SharePrincipals") is not None:
        out["share_principals"] = data["SharePrincipals"]
    return out
