"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminRevokeUserSessionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.revoke_associated_sessions_type
    import capo_cognito_identity_provider.types.session_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminRevokeUserSessionRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the session.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The username of the user who owns the session. The username must match the user associated with the <code>SessionId</code>, to confirm they are the intended target user.</p>"""
    session_id: "capo_cognito_identity_provider.types.session_id_type.SessionIdType"
    """<p>The ID of the session to revoke. This is a 28-character string of lowercase letters and digits, prefixed with <code>tkn</code> for a token session or <code>sso</code> for an SSO session.</p>"""
    revoke_associated_sessions: NotRequired[
        "capo_cognito_identity_provider.types.revoke_associated_sessions_type.RevokeAssociatedSessionsType"
    ]
    """<p>Specifies whether to also revoke the sessions that are linked to the targeted session. <code>NONE</code>, the default, revokes only the targeted session. <code>LINKED</code> also revokes the directly linked session or sessions, interpreted relative to the type of the targeted session: revoking a token session also revokes the parent SSO session it came through, and revoking an SSO session also revokes the token sessions that came through it. The set of linked sessions is eventually consistent, so associated sessions are typically revoked within a few seconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminRevokeUserSessionRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["SessionId"] = value["session_id"]
    if "revoke_associated_sessions" in value:
        import capo_cognito_identity_provider.types.revoke_associated_sessions_type

        out["RevokeAssociatedSessions"] = (
            capo_cognito_identity_provider.types.revoke_associated_sessions_type.serialize_aws_json_1_1(
                value["revoke_associated_sessions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminRevokeUserSessionRequest:
    out: AdminRevokeUserSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
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


def redact_sensitive(value: AdminRevokeUserSessionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
