"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2Credentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.access_token
    import capo_glue.types.jwt_token
    import capo_glue.types.refresh_token
    import capo_glue.types.user_managed_client_application_client_secret


class OAuth2Credentials(TypedDict, closed=True):
    user_managed_client_application_client_secret: NotRequired[
        "capo_glue.types.user_managed_client_application_client_secret.UserManagedClientApplicationClientSecret"
    ]
    """<p>The client application client secret if the client application is user managed.</p>"""
    access_token: NotRequired["capo_glue.types.access_token.AccessToken"]
    """<p>The access token used when the authentication type is OAuth2.</p>"""
    refresh_token: NotRequired["capo_glue.types.refresh_token.RefreshToken"]
    """<p>The refresh token used when the authentication type is OAuth2.</p>"""
    jwt_token: NotRequired["capo_glue.types.jwt_token.JwtToken"]
    """<p>The JSON Web Token (JWT) used when the authentication type is OAuth2.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuth2Credentials) -> dict:
    out: dict = {}
    if "user_managed_client_application_client_secret" in value:
        out["UserManagedClientApplicationClientSecret"] = value[
            "user_managed_client_application_client_secret"
        ]
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    if "refresh_token" in value:
        out["RefreshToken"] = value["refresh_token"]
    if "jwt_token" in value:
        out["JwtToken"] = value["jwt_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OAuth2Credentials:
    out: OAuth2Credentials = {}  # type: ignore[typeddict-item]
    if data.get("UserManagedClientApplicationClientSecret") is not None:
        out["user_managed_client_application_client_secret"] = data[
            "UserManagedClientApplicationClientSecret"
        ]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    if data.get("RefreshToken") is not None:
        out["refresh_token"] = data["RefreshToken"]
    if data.get("JwtToken") is not None:
        out["jwt_token"] = data["JwtToken"]
    return out


def redact_sensitive(value: OAuth2Credentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_managed_client_application_client_secret" in value:
        out["user_managed_client_application_client_secret"] = (
            "*** Sensitive Data Redacted ***"
        )
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    if "refresh_token" in value:
        out["refresh_token"] = "*** Sensitive Data Redacted ***"
    if "jwt_token" in value:
        out["jwt_token"] = "*** Sensitive Data Redacted ***"
    return out
