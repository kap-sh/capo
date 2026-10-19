"""Generated from Smithy shape ``com.amazonaws.qbusiness#OAuth2ClientCredentialConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.secret_arn
    import capo_qbusiness.types.url


class OAuth2ClientCredentialConfiguration(TypedDict, closed=True):
    secret_arn: "capo_qbusiness.types.secret_arn.SecretArn"
    """<p>The ARN of the Secrets Manager secret that stores the OAuth 2.0 credentials/token used for plugin configuration.</p>"""
    role_arn: "capo_qbusiness.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role used by Amazon Q Business to access the OAuth 2.0 authentication credentials stored in a Secrets Manager secret.</p>"""
    authorization_url: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The redirect URL required by the OAuth 2.0 protocol for Amazon Q Business to authenticate a plugin user through a third party authentication server.</p>"""
    token_url: NotRequired["capo_qbusiness.types.url.Url"]
    """<p>The URL required by the OAuth 2.0 protocol to exchange an end user authorization code for an access token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2ClientCredentialConfiguration) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["roleArn"] = value["role_arn"]
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    if "token_url" in value:
        out["tokenUrl"] = value["token_url"]
    return out


def deserialize_json(data: dict) -> OAuth2ClientCredentialConfiguration:
    out: OAuth2ClientCredentialConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("secretArn") is not None:
        out["secret_arn"] = data["secretArn"]
    else:
        out["secret_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    if data.get("tokenUrl") is not None:
        out["token_url"] = data["tokenUrl"]
    return out
