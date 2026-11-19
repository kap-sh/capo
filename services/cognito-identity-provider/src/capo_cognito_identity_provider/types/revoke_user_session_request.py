"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeUserSessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.revoke_associated_sessions_type
    import capo_cognito_identity_provider.types.session_id_type
    import capo_cognito_identity_provider.types.token_model_type


class RevokeUserSessionRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the user. Amazon Cognito uses this token to authorize the request and to identify the user.</p>"""
    session_id: "capo_cognito_identity_provider.types.session_id_type.SessionIdType"
    """<p>The ID of the session to revoke. This is a 28-character string of lowercase letters and digits, prefixed with <code>tkn</code> for a token session or <code>sso</code> for an SSO session. This value can't identify the caller's own current session.</p>"""
    revoke_associated_sessions: NotRequired[
        "capo_cognito_identity_provider.types.revoke_associated_sessions_type.RevokeAssociatedSessionsType"
    ]
    """<p>Specifies whether to also revoke the sessions that are linked to the targeted session. <code>NONE</code>, the default, revokes only the targeted session. <code>LINKED</code> also revokes the directly linked session or sessions, interpreted relative to the type of the targeted session: revoking a token session also revokes the parent SSO session it came through, and revoking an SSO session also revokes the token sessions that came through it. The set of linked sessions is eventually consistent, so associated sessions are typically revoked within a few seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeUserSessionRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    out["SessionId"] = value["session_id"]
    if "revoke_associated_sessions" in value:
        import capo_cognito_identity_provider.types.revoke_associated_sessions_type

        out["RevokeAssociatedSessions"] = (
            capo_cognito_identity_provider.types.revoke_associated_sessions_type.serialize_aws_json_1_1(
                value["revoke_associated_sessions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeUserSessionRequest:
    out: RevokeUserSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        out["access_token"] = ""
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("RevokeAssociatedSessions") is not None:
        import capo_cognito_identity_provider.types.revoke_associated_sessions_type

        out["revoke_associated_sessions"] = (
            capo_cognito_identity_provider.types.revoke_associated_sessions_type.deserialize_aws_json_1_1(
                data["RevokeAssociatedSessions"]
            )
        )
    return out


def redact_sensitive(value: RevokeUserSessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
