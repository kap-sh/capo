"""Generated from Smithy shape ``com.amazonaws.ssooidc#CreateTokenWithIAMResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_oidc.types.access_token
    import capo_sso_oidc.types.aws_additional_details
    import capo_sso_oidc.types.expiration_in_seconds
    import capo_sso_oidc.types.id_token
    import capo_sso_oidc.types.refresh_token
    import capo_sso_oidc.types.scopes
    import capo_sso_oidc.types.token_type
    import capo_sso_oidc.types.token_type_uri


class CreateTokenWithIAMResponse(TypedDict, closed=True):
    access_token: NotRequired["capo_sso_oidc.types.access_token.AccessToken"]
    """<p>A bearer token to access Amazon Web Services accounts and applications assigned to a user.</p>"""
    token_type: NotRequired["capo_sso_oidc.types.token_type.TokenType"]
    """<p>Used to notify the requester that the returned token is an access token. The supported token type is <code>Bearer</code>.</p>"""
    expires_in: "capo_sso_oidc.types.expiration_in_seconds.ExpirationInSeconds"
    """<p>Indicates the time in seconds when an access token will expire.</p>"""
    refresh_token: NotRequired["capo_sso_oidc.types.refresh_token.RefreshToken"]
    """<p>A token that, if present, can be used to refresh a previously issued access token that might have expired.</p> <p>For more information about the features and limitations of the current IAM Identity Center OIDC implementation, see <i>Considerations for Using this Guide</i> in the <a href="https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html">IAM Identity Center OIDC API Reference</a>.</p>"""
    id_token: NotRequired["capo_sso_oidc.types.id_token.IdToken"]
    """<p>A JSON Web Token (JWT) that identifies the user associated with the issued access token. </p>"""
    issued_token_type: NotRequired["capo_sso_oidc.types.token_type_uri.TokenTypeURI"]
    """<p>Indicates the type of tokens that are issued by IAM Identity Center. The following values are supported: </p> <p>* Access Token - <code>urn:ietf:params:oauth:token-type:access_token</code> </p> <p>* Refresh Token - <code>urn:ietf:params:oauth:token-type:refresh_token</code> </p>"""
    scope: NotRequired["capo_sso_oidc.types.scopes.Scopes"]
    """<p>The list of scopes for which authorization is granted. The access token that is issued is limited to the scopes that are granted.</p>"""
    aws_additional_details: NotRequired[
        "capo_sso_oidc.types.aws_additional_details.AwsAdditionalDetails"
    ]
    """<p>A structure containing information from IAM Identity Center managed user and group information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTokenWithIAMResponse) -> dict:
    out: dict = {}
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "token_type" in value:
        out["tokenType"] = value["token_type"]
    out["expiresIn"] = value.get("expires_in", 0)
    if "refresh_token" in value:
        out["refreshToken"] = value["refresh_token"]
    if "id_token" in value:
        out["idToken"] = value["id_token"]
    if "issued_token_type" in value:
        out["issuedTokenType"] = value["issued_token_type"]
    if "scope" in value:
        import capo_sso_oidc.types.scopes

        out["scope"] = capo_sso_oidc.types.scopes.serialize_json(value["scope"])
    if "aws_additional_details" in value:
        import capo_sso_oidc.types.aws_additional_details

        out["awsAdditionalDetails"] = (
            capo_sso_oidc.types.aws_additional_details.serialize_json(
                value["aws_additional_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTokenWithIAMResponse:
    out: CreateTokenWithIAMResponse = {}  # type: ignore[typeddict-item]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("tokenType") is not None:
        out["token_type"] = data["tokenType"]
    if data.get("expiresIn") is not None:
        out["expires_in"] = data["expiresIn"]
    else:
        out["expires_in"] = 0
    if data.get("refreshToken") is not None:
        out["refresh_token"] = data["refreshToken"]
    if data.get("idToken") is not None:
        out["id_token"] = data["idToken"]
    if data.get("issuedTokenType") is not None:
        out["issued_token_type"] = data["issuedTokenType"]
    if data.get("scope") is not None:
        import capo_sso_oidc.types.scopes

        out["scope"] = capo_sso_oidc.types.scopes.deserialize_json(data["scope"])
    if data.get("awsAdditionalDetails") is not None:
        import capo_sso_oidc.types.aws_additional_details

        out["aws_additional_details"] = (
            capo_sso_oidc.types.aws_additional_details.deserialize_json(
                data["awsAdditionalDetails"]
            )
        )
    return out
