"""Generated from Smithy shape ``com.amazonaws.wickr#GetOidcInfoRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sensitive_string


class GetOidcInfoRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network whose OIDC configuration will be retrieved.</p>"""
    client_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The OAuth client ID for retrieving access tokens (optional).</p>"""
    code: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The authorization code for retrieving access tokens (optional).</p>"""
    grant_type: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The OAuth grant type for retrieving access tokens (optional).</p>"""
    redirect_uri: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The redirect URI for the OAuth flow (optional).</p>"""
    url: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The URL for the OIDC provider (optional).</p>"""
    client_secret: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The OAuth client secret for retrieving access tokens (optional).</p>"""
    code_verifier: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The PKCE code verifier for enhanced security in the OAuth flow (optional).</p>"""
    certificate: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The CA certificate for secure communication with the OIDC provider (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOidcInfoRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOidcInfoRequest:
    out: GetOidcInfoRequest = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: GetOidcInfoRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out
