"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_secret_type
    import capo_cognito_identity_provider.types.revoke_associated_sessions_type
    import capo_cognito_identity_provider.types.token_model_type


class RevokeTokenRequest(TypedDict, closed=True):
    token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>The refresh token that you want to revoke.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client where the token that you want to revoke was issued.</p>"""
    client_secret: NotRequired[
        "capo_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The client secret of the requested app client, if the client has a secret.</p>"""
    revoke_associated_sessions: NotRequired[
        "capo_cognito_identity_provider.types.revoke_associated_sessions_type.RevokeAssociatedSessionsType"
    ]
    """<p>Specifies whether to also revoke the SSO session that is linked to the token session being revoked. <code>NONE</code>, the default, revokes only the token session that is associated with the refresh token. <code>LINKED</code> also revokes the parent SSO session that the token session came through; the other token sessions that came through that SSO session aren't revoked. <code>LINKED</code> has no effect when session tracking is disabled or when the token session has no parent SSO session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeTokenRequest) -> dict:
    out: dict = {}
    out["Token"] = value["token"]
    out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "revoke_associated_sessions" in value:
        import capo_cognito_identity_provider.types.revoke_associated_sessions_type

        out["RevokeAssociatedSessions"] = (
            capo_cognito_identity_provider.types.revoke_associated_sessions_type.serialize_aws_json_1_1(
                value["revoke_associated_sessions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeTokenRequest:
    out: RevokeTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("Token") is not None:
        out["token"] = data["Token"]
    else:
        out["token"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("RevokeAssociatedSessions") is not None:
        import capo_cognito_identity_provider.types.revoke_associated_sessions_type

        out["revoke_associated_sessions"] = (
            capo_cognito_identity_provider.types.revoke_associated_sessions_type.deserialize_aws_json_1_1(
                data["RevokeAssociatedSessions"]
            )
        )
    return out


def redact_sensitive(value: RevokeTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
