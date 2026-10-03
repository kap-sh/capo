"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompleteWebAuthnRegistrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.document
    import capo_cognito_identity_provider.types.token_model_type


class CompleteWebAuthnRegistrationRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""
    credential: "capo_cognito_identity_provider.types.document.Document"
    """<p>A <a href="https://www.w3.org/TR/WebAuthn-3/#dictdef-registrationresponsejson">RegistrationResponseJSON</a> public-key credential response from the user's passkey provider.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteWebAuthnRegistrationRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["Credential"] = value["credential"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteWebAuthnRegistrationRequest:
    out: CompleteWebAuthnRegistrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError(
            "CompleteWebAuthnRegistrationRequest.access_token required"
        )
    if data.get("Credential") is not None:
        out["credential"] = data["Credential"]
    else:
        raise DeserializationError(
            "CompleteWebAuthnRegistrationRequest.credential required"
        )
    return out
