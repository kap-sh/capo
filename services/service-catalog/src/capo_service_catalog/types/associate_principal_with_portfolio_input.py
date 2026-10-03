"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociatePrincipalWithPortfolioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.principal_arn
    import capo_service_catalog.types.principal_type


class AssociatePrincipalWithPortfolioInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    portfolio_id: "capo_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    principal_arn: "capo_service_catalog.types.principal_arn.PrincipalARN"
    """<p>The ARN of the principal (user, role, or group). If the <code>PrincipalType</code> is <code>IAM</code>, the supported value is a fully defined <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns">IAM Amazon Resource Name (ARN)</a>. If the <code>PrincipalType</code> is <code>IAM_PATTERN</code>, the supported value is an <code>IAM</code> ARN <i>without an AccountID</i> in the following format:</p> <p> <i>arn:partition:iam:::resource-type/resource-id</i> </p> <p>The ARN resource-id can be either:</p> <ul> <li> <p>A fully formed resource-id. For example, <i>arn:aws:iam:::role/resource-name</i> or <i>arn:aws:iam:::role/resource-path/resource-name</i> </p> </li> <li> <p>A wildcard ARN. The wildcard ARN accepts <code>IAM_PATTERN</code> values with a "*" or "?" in the resource-id segment of the ARN. For example <i>arn:partition:service:::resource-type/resource-path/resource-name</i>. The new symbols are exclusive to the <b>resource-path</b> and <b>resource-name</b> and cannot replace the <b>resource-type</b> or other ARN values. </p> <p>The ARN path and principal name allow unlimited wildcard characters.</p> </li> </ul> <p>Examples of an <b>acceptable</b> wildcard ARN:</p> <ul> <li> <p>arn:aws:iam:::role/ResourceName_*</p> </li> <li> <p>arn:aws:iam:::role/*/ResourceName_?</p> </li> </ul> <p>Examples of an <b>unacceptable</b> wildcard ARN:</p> <ul> <li> <p>arn:aws:iam:::*/ResourceName</p> </li> </ul> <p>You can associate multiple <code>IAM_PATTERN</code>s even if the account has no principal with that name. </p> <p>The "?" wildcard character matches zero or one of any character. This is similar to ".?" in regular regex context. The "*" wildcard character matches any number of any characters. This is similar to ".*" in regular regex context.</p> <p>In the IAM Principal ARN format (<i>arn:partition:iam:::resource-type/resource-path/resource-name</i>), valid resource-type values include <b>user/</b>, <b>group/</b>, or <b>role/</b>. The "?" and "*" characters are allowed only after the resource-type in the resource-id segment. You can use special characters anywhere within the resource-id. </p> <p>The "*" character also matches the "/" character, allowing paths to be formed <i>within</i> the resource-id. For example, <i>arn:aws:iam:::role/<b>*</b>/ResourceName_?</i> matches both <i>arn:aws:iam:::role/pathA/pathB/ResourceName_1</i> and <i>arn:aws:iam:::role/pathA/ResourceName_1</i>. </p>"""
    principal_type: "capo_service_catalog.types.principal_type.PrincipalType"
    """<p>The principal type. The supported value is <code>IAM</code> if you use a fully defined Amazon Resource Name (ARN), or <code>IAM_PATTERN</code> if you use an ARN with no <code>accountID</code>, with or without wildcard characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociatePrincipalWithPortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PortfolioId"] = value["portfolio_id"]
    out["PrincipalARN"] = value["principal_arn"]
    import capo_service_catalog.types.principal_type

    out["PrincipalType"] = (
        capo_service_catalog.types.principal_type.serialize_aws_json_1_1(
            value["principal_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociatePrincipalWithPortfolioInput:
    out: AssociatePrincipalWithPortfolioInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PortfolioId") is not None:
        out["portfolio_id"] = data["PortfolioId"]
    else:
        raise DeserializationError(
            "AssociatePrincipalWithPortfolioInput.portfolio_id required"
        )
    if data.get("PrincipalARN") is not None:
        out["principal_arn"] = data["PrincipalARN"]
    else:
        raise DeserializationError(
            "AssociatePrincipalWithPortfolioInput.principal_arn required"
        )
    if data.get("PrincipalType") is not None:
        import capo_service_catalog.types.principal_type

        out["principal_type"] = (
            capo_service_catalog.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        raise DeserializationError(
            "AssociatePrincipalWithPortfolioInput.principal_type required"
        )
    return out
