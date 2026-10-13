"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifySoftwareTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_type
    import capo_cognito_identity_provider.types.verify_software_token_response_type


class VerifySoftwareTokenResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_cognito_identity_provider.types.verify_software_token_response_type.VerifySoftwareTokenResponseType"
    ]
    """<p>Amazon Cognito can accept or reject the code that you provide. This response parameter indicates the success of TOTP verification. Some reasons that this operation might return an error are clock skew on the user's device and excessive retries.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>This session ID satisfies an <code>MFA_SETUP</code> challenge. Supply the session ID in your challenge response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifySoftwareTokenResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_cognito_identity_provider.types.verify_software_token_response_type

        out["Status"] = (
            capo_cognito_identity_provider.types.verify_software_token_response_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifySoftwareTokenResponse:
    out: VerifySoftwareTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_cognito_identity_provider.types.verify_software_token_response_type

        out["status"] = (
            capo_cognito_identity_provider.types.verify_software_token_response_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    return out


def redact_sensitive(value: VerifySoftwareTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session" in value:
        out["session"] = "*** Sensitive Data Redacted ***"
    return out
