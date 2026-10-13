"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientAuthenticationResultType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.token_model_type


class ClientAuthenticationResultType(TypedDict, closed=True):
    access_token: NotRequired[
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    ]
    """<p>The access token for the requested app client. Present this token to a resource server to authorize a request, using the scopes granted in the token.</p>"""
    expires_in: "capo_cognito_identity_provider.types.integer_type.IntegerType"
    """<p>The number of seconds until the access token expires.</p>"""
    token_type: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The type of the token. For example, <code>Bearer</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientAuthenticationResultType) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["AccessToken"] = value["access_token"]
    out["ExpiresIn"] = value.get("expires_in", 0)
    if "token_type" in value:
        out["TokenType"] = value["token_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientAuthenticationResultType:
    out: ClientAuthenticationResultType = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    if data.get("ExpiresIn") is not None:
        out["expires_in"] = data["ExpiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("TokenType") is not None:
        out["token_type"] = data["TokenType"]
    return out


def redact_sensitive(value: ClientAuthenticationResultType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
