"""Generated from Smithy shape ``com.amazonaws.appintegrations#AuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.arn
    import capo_appintegrations.types.auth_type
    import capo_appintegrations.types.identifier


class AuthConfig(TypedDict, closed=True):
    auth_type: NotRequired["capo_appintegrations.types.auth_type.AuthType"]
    """<p>The type of authentication that Connect Customer uses to call the external application endpoint. You must specify an authentication type for <code>A2A_SERVER</code> applications. Valid values:</p> <ul> <li> <p> <code>API_KEY</code>: Connect Customer sends an API key that is stored in the Secrets Manager secret that you specify in <code>CredentialProviderIdentifier</code>.</p> </li> <li> <p> <code>CONNECT_JWT</code>: Connect Customer issues a short-lived, signed JSON Web Token (JWT). This authentication type doesn't require a stored credential.</p> </li> </ul>"""
    credential_provider_identifier: NotRequired["capo_appintegrations.types.arn.Arn"]
    """<p>The ARN of the Secrets Manager secret that stores the credentials. The secret must be accessible to Connect Customer.</p> <p>You must specify this ARN when <code>AuthType</code> is <code>API_KEY</code>. Don't specify it when <code>AuthType</code> is <code>CONNECT_JWT</code>.</p>"""
    audience_override: NotRequired["capo_appintegrations.types.identifier.Identifier"]
    """<p>The value that Connect Customer uses as the audience (<code>aud</code>) claim of the JSON Web Token (JWT) that it issues. You can specify this parameter only when <code>AuthType</code> is <code>CONNECT_JWT</code>. If you don't specify it, the audience is the <code>AccessUrl</code> of the application. The value can't contain <code>connect.amazonaws.com</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthConfig) -> dict:
    out: dict = {}
    if "auth_type" in value:
        import capo_appintegrations.types.auth_type

        out["AuthType"] = capo_appintegrations.types.auth_type.serialize_json(
            value["auth_type"]
        )
    if "credential_provider_identifier" in value:
        out["CredentialProviderIdentifier"] = value["credential_provider_identifier"]
    if "audience_override" in value:
        out["AudienceOverride"] = value["audience_override"]
    return out


def deserialize_json(data: dict) -> AuthConfig:
    out: AuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("AuthType") is not None:
        import capo_appintegrations.types.auth_type

        out["auth_type"] = capo_appintegrations.types.auth_type.deserialize_json(
            data["AuthType"]
        )
    if data.get("CredentialProviderIdentifier") is not None:
        out["credential_provider_identifier"] = data["CredentialProviderIdentifier"]
    if data.get("AudienceOverride") is not None:
        out["audience_override"] = data["AudienceOverride"]
    return out
