"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetOpenIdTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.oidc_token


class GetOpenIdTokenResponse(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID. Note that the IdentityId returned may not match the one passed on input.</p>"""
    token: NotRequired["capo_cognito_identity.types.oidc_token.OIDCToken"]
    """<p>An OpenID token, valid for 10 minutes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpenIdTokenResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "token" in value:
        out["Token"] = value["token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpenIdTokenResponse:
    out: GetOpenIdTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    if data.get("Token") is not None:
        out["token"] = data["Token"]
    return out


def redact_sensitive(value: GetOpenIdTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
