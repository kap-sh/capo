"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociatePrincipalFromPortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.principal_arn
    import capo_service_catalog.types.principal_type


class DisassociatePrincipalFromPortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    principal_arn: "capo_service_catalog.types.principal_arn.PrincipalARN"
    """<p>The ARN of the principal (user, role, or group). This field allows an ARN with no <code>accountID</code> with or without wildcard characters if <code>PrincipalType</code> is <code>IAM_PATTERN</code>.</p>"""
    principal_type: NotRequired[
        "capo_service_catalog.types.principal_type.PrincipalType"
    ]
    """<p>The supported value is <code>IAM</code> if you use a fully defined ARN, or <code>IAM_PATTERN</code> if you specify an <code>IAM</code> ARN with no AccountId, with or without wildcard characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociatePrincipalFromPortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    out["PrincipalARN"] = value["principal_arn"]
    if "principal_type" in value:
        import capo_service_catalog.types.principal_type

        out["PrincipalType"] = (
            capo_service_catalog.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociatePrincipalFromPortfolioInput:
    out: DisassociatePrincipalFromPortfolioInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        out["portfolio_id"] = ""
    if data.get("PrincipalARN") is not None:
        out["principal_arn"] = data["PrincipalARN"]
    else:
        out["principal_arn"] = ""
    if data.get("PrincipalType") is not None:
        import capo_service_catalog.types.principal_type

        out["principal_type"] = (
            capo_service_catalog.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    return out
