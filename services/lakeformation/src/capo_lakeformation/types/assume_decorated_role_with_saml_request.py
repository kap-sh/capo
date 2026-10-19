"""Generated from Smithy shape ``com.amazonaws.lakeformation#AssumeDecoratedRoleWithSAMLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.credential_timeout_duration_second_integer
    import capo_lakeformation.types.iam_role_arn
    import capo_lakeformation.types.iamsaml_provider_arn
    import capo_lakeformation.types.saml_assertion_string


class AssumeDecoratedRoleWithSAMLRequest(TypedDict, closed=True):
    saml_assertion: "capo_lakeformation.types.saml_assertion_string.SAMLAssertionString"
    """<p>A SAML assertion consisting of an assertion statement for the user who needs temporary credentials. This must match the SAML assertion that was issued to IAM. This must be Base64 encoded.</p>"""
    role_arn: "capo_lakeformation.types.iam_role_arn.IAMRoleArn"
    """<p>The role that represents an IAM principal whose scope down policy allows it to call credential vending APIs such as <code>GetTemporaryTableCredentials</code>. The caller must also have iam:PassRole permission on this role. </p>"""
    principal_arn: "capo_lakeformation.types.iamsaml_provider_arn.IAMSAMLProviderArn"
    """<p>The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.</p>"""
    duration_seconds: NotRequired[
        "capo_lakeformation.types.credential_timeout_duration_second_integer.CredentialTimeoutDurationSecondInteger"
    ]
    """<p>The time period, between 900 and 43,200 seconds, for the timeout of the temporary credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssumeDecoratedRoleWithSAMLRequest) -> dict:
    out: dict = {}
    out["SAMLAssertion"] = value["saml_assertion"]
    out["RoleArn"] = value["role_arn"]
    out["PrincipalArn"] = value["principal_arn"]
    if "duration_seconds" in value:
        out["DurationSeconds"] = value["duration_seconds"]
    return out


def deserialize_json(data: dict) -> AssumeDecoratedRoleWithSAMLRequest:
    out: AssumeDecoratedRoleWithSAMLRequest = {}  # type: ignore[typeddict-item]
    if data.get("SAMLAssertion") is not None:
        out["saml_assertion"] = data["SAMLAssertion"]
    else:
        out["saml_assertion"] = ""
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("PrincipalArn") is not None:
        out["principal_arn"] = data["PrincipalArn"]
    else:
        out["principal_arn"] = ""
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = data["DurationSeconds"]
    return out
