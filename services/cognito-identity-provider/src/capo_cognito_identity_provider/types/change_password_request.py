"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChangePasswordRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.password_type
    import capo_cognito_identity_provider.types.token_model_type


class ChangePasswordRequest(TypedDict, closed=True):
    previous_password: NotRequired[
        "capo_cognito_identity_provider.types.password_type.PasswordType"
    ]
    """<p>The user's previous password. Required if the user has a password. If the user has no password and only signs in with passwordless authentication options, you can omit this parameter.</p>"""
    proposed_password: "capo_cognito_identity_provider.types.password_type.PasswordType"
    """<p>A new password that you prompted the user to enter in your application.</p>"""
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the user whose password you want to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangePasswordRequest) -> dict:
    out: dict = {}
    if "previous_password" in value:
        out["PreviousPassword"] = value["previous_password"]
    out["ProposedPassword"] = value["proposed_password"]
    out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChangePasswordRequest:
    out: ChangePasswordRequest = {}  # type: ignore[typeddict-item]
    if data.get("PreviousPassword") is not None:
        out["previous_password"] = data["PreviousPassword"]
    if data.get("ProposedPassword") is not None:
        out["proposed_password"] = data["ProposedPassword"]
    else:
        raise DeserializationError("ChangePasswordRequest.proposed_password required")
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("ChangePasswordRequest.access_token required")
    return out


def redact_sensitive(value: ChangePasswordRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "previous_password" in value:
        out["previous_password"] = "*** Sensitive Data Redacted ***"
    if "proposed_password" in value:
        out["proposed_password"] = "*** Sensitive Data Redacted ***"
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
