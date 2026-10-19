"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifyUserAttributeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_name_type
    import capo_cognito_identity_provider.types.confirmation_code_type
    import capo_cognito_identity_provider.types.token_model_type


class VerifyUserAttributeRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    attribute_name: (
        "capo_cognito_identity_provider.types.attribute_name_type.AttributeNameType"
    )
    """<p>The name of the attribute that you want to verify.</p>"""
    code: "capo_cognito_identity_provider.types.confirmation_code_type.ConfirmationCodeType"
    """<p>The verification code that your user pool sent to the added or changed attribute, for example the user's email address.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyUserAttributeRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["AttributeName"] = value["attribute_name"]
    out["Code"] = value["code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyUserAttributeRequest:
    out: VerifyUserAttributeRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        out["access_token"] = ""
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    return out


def redact_sensitive(value: VerifyUserAttributeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
