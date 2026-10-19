"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteWebAuthnCredentialRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.token_model_type


class DeleteWebAuthnCredentialRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    credential_id: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The unique identifier of the passkey that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteWebAuthnCredentialRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["CredentialId"] = value["credential_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteWebAuthnCredentialRequest:
    out: DeleteWebAuthnCredentialRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        out["access_token"] = ""
    if data.get("CredentialId") is not None:
        out["credential_id"] = data["CredentialId"]
    else:
        out["credential_id"] = ""
    return out


def redact_sensitive(value: DeleteWebAuthnCredentialRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
