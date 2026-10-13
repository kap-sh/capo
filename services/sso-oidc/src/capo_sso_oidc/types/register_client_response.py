"""Generated from Smithy shape ``com.amazonaws.ssooidc#RegisterClientResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_oidc.types.client_id
    import capo_sso_oidc.types.client_secret
    import capo_sso_oidc.types.long_time_stamp_type
    import capo_sso_oidc.types.uri


class RegisterClientResponse(TypedDict, closed=True):
    client_id: NotRequired["capo_sso_oidc.types.client_id.ClientId"]
    """<p>The unique identifier string for each client. This client uses this identifier to get authenticated by the service in subsequent calls.</p>"""
    client_secret: NotRequired["capo_sso_oidc.types.client_secret.ClientSecret"]
    """<p>A secret string generated for the client. The client will use this string to get authenticated by the service in subsequent calls.</p>"""
    client_id_issued_at: "capo_sso_oidc.types.long_time_stamp_type.LongTimeStampType"
    """<p>Indicates the time at which the <code>clientId</code> and <code>clientSecret</code> were issued.</p>"""
    client_secret_expires_at: (
        "capo_sso_oidc.types.long_time_stamp_type.LongTimeStampType"
    )
    """<p>Indicates the time at which the <code>clientId</code> and <code>clientSecret</code> will become invalid.</p>"""
    authorization_endpoint: NotRequired["capo_sso_oidc.types.uri.URI"]
    """<p>An endpoint that the client can use to request authorization.</p>"""
    token_endpoint: NotRequired["capo_sso_oidc.types.uri.URI"]
    """<p>An endpoint that the client can use to create tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterClientResponse) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    if "client_secret" in value:
        out["clientSecret"] = value["client_secret"]
    out["clientIdIssuedAt"] = value.get("client_id_issued_at", 0)
    out["clientSecretExpiresAt"] = value.get("client_secret_expires_at", 0)
    if "authorization_endpoint" in value:
        out["authorizationEndpoint"] = value["authorization_endpoint"]
    if "token_endpoint" in value:
        out["tokenEndpoint"] = value["token_endpoint"]
    return out


def deserialize_json(data: dict) -> RegisterClientResponse:
    out: RegisterClientResponse = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    if data.get("clientIdIssuedAt") is not None:
        out["client_id_issued_at"] = data["clientIdIssuedAt"]
    else:
        out["client_id_issued_at"] = 0
    if data.get("clientSecretExpiresAt") is not None:
        out["client_secret_expires_at"] = data["clientSecretExpiresAt"]
    else:
        out["client_secret_expires_at"] = 0
    if data.get("authorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["authorizationEndpoint"]
    if data.get("tokenEndpoint") is not None:
        out["token_endpoint"] = data["tokenEndpoint"]
    return out


def redact_sensitive(value: RegisterClientResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
