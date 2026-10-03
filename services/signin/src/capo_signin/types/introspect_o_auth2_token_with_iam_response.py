"""Generated from Smithy shape ``com.amazonaws.signin#IntrospectOAuth2TokenWithIAMResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.account_id
    import capo_signin.types.introspected_token_type


class IntrospectOAuth2TokenWithIAMResponse(TypedDict, closed=True):
    active: "bool"
    """Indicates whether the token is currently active. `true` only when the token is valid, has not expired, has not been revoked, and belongs to the caller's account."""
    client_id: NotRequired["str"]
    """Client identifier for the OAuth 2.0 client that requested the token."""
    user_id: NotRequired["str"]
    """User identifier matching sts:GetCallerIdentity's `UserId` field for the token's subject principal (e.g. "AIDAEXAMPLE" for an IAM user, or "AROAEXAMPLE:session-name" for an assumed role)."""
    token_type: NotRequired[
        "capo_signin.types.introspected_token_type.IntrospectedTokenType"
    ]
    """Indicates which kind of token was introspected. One of "access_token" or "refresh_token"."""
    exp: NotRequired["int"]
    """Token expiration time as a NumericDate (Unix epoch seconds)."""
    iat: NotRequired["int"]
    """Token issuance time as a NumericDate (Unix epoch seconds)."""
    nbf: NotRequired["int"]
    """Token "not before" time as a NumericDate (Unix epoch seconds)."""
    sub: NotRequired["str"]
    """Subject of the token: the IAM principal ARN. For assumed-role sessions, this is the session ARN (matches sts:GetCallerIdentity's `Arn` field), e.g. arn:aws:sts::123456789012:assumed-role/MyRole/session-name."""
    aud: NotRequired["str"]
    """Audience of the token: the OAuth resource the token is scoped to (for example, "aws-mcp.amazonaws.com"). Omitted for refresh tokens."""
    iss: NotRequired["str"]
    """Issuer of the token. Always "signin.amazonaws.com" for AWS Sign-In."""
    jti: NotRequired["str"]
    """Unique identifier for the token."""
    account_id: NotRequired["capo_signin.types.account_id.AccountId"]
    """12-digit AWS account ID of the token's subject principal."""
    signin_session: NotRequired["str"]
    """AWS Sign-In session ARN bound to the token, of the form arn:aws:signin:{region}:{account}:session/{uuid}."""
    resource: NotRequired["str"]
    """The OAuth resource the token is scoped to during Human OAuth flow. Only present for refresh token introspection."""


# --- restJson1 ser/de ---
def serialize_json(value: IntrospectOAuth2TokenWithIAMResponse) -> dict:
    out: dict = {}
    out["active"] = value["active"]
    if "client_id" in value:
        out["client_id"] = value["client_id"]
    if "user_id" in value:
        out["user_id"] = value["user_id"]
    if "token_type" in value:
        out["token_type"] = value["token_type"]
    if "exp" in value:
        out["exp"] = value["exp"]
    if "iat" in value:
        out["iat"] = value["iat"]
    if "nbf" in value:
        out["nbf"] = value["nbf"]
    if "sub" in value:
        out["sub"] = value["sub"]
    if "aud" in value:
        out["aud"] = value["aud"]
    if "iss" in value:
        out["iss"] = value["iss"]
    if "jti" in value:
        out["jti"] = value["jti"]
    if "account_id" in value:
        out["account_id"] = value["account_id"]
    if "signin_session" in value:
        out["signin_session"] = value["signin_session"]
    if "resource" in value:
        out["resource"] = value["resource"]
    return out


def deserialize_json(data: dict) -> IntrospectOAuth2TokenWithIAMResponse:
    out: IntrospectOAuth2TokenWithIAMResponse = {}  # type: ignore[typeddict-item]
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        raise DeserializationError(
            "IntrospectOAuth2TokenWithIAMResponse.active required"
        )
    if data.get("client_id") is not None:
        out["client_id"] = data["client_id"]
    if data.get("user_id") is not None:
        out["user_id"] = data["user_id"]
    if data.get("token_type") is not None:
        out["token_type"] = data["token_type"]
    if data.get("exp") is not None:
        out["exp"] = data["exp"]
    if data.get("iat") is not None:
        out["iat"] = data["iat"]
    if data.get("nbf") is not None:
        out["nbf"] = data["nbf"]
    if data.get("sub") is not None:
        out["sub"] = data["sub"]
    if data.get("aud") is not None:
        out["aud"] = data["aud"]
    if data.get("iss") is not None:
        out["iss"] = data["iss"]
    if data.get("jti") is not None:
        out["jti"] = data["jti"]
    if data.get("account_id") is not None:
        out["account_id"] = data["account_id"]
    if data.get("signin_session") is not None:
        out["signin_session"] = data["signin_session"]
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    return out
