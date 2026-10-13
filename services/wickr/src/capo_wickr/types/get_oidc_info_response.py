"""Generated from Smithy shape ``com.amazonaws.wickr#GetOidcInfoResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.oidc_config_info
    import capo_wickr.types.oidc_token_info


class GetOidcInfoResponse(TypedDict, closed=True):
    openid_connect_info: NotRequired["capo_wickr.types.oidc_config_info.OidcConfigInfo"]
    """<p>The OpenID Connect configuration information for the network, including issuer, client ID, scopes, and other SSO settings.</p>"""
    token_info: NotRequired["capo_wickr.types.oidc_token_info.OidcTokenInfo"]
    """<p>OAuth token information including access token, refresh token, and expiration details (only present if token parameters were provided in the request).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOidcInfoResponse) -> dict:
    out: dict = {}
    if "openid_connect_info" in value:
        import capo_wickr.types.oidc_config_info

        out["openidConnectInfo"] = capo_wickr.types.oidc_config_info.serialize_json(
            value["openid_connect_info"]
        )
    if "token_info" in value:
        import capo_wickr.types.oidc_token_info

        out["tokenInfo"] = capo_wickr.types.oidc_token_info.serialize_json(
            value["token_info"]
        )
    return out


def deserialize_json(data: dict) -> GetOidcInfoResponse:
    out: GetOidcInfoResponse = {}  # type: ignore[typeddict-item]
    if data.get("openidConnectInfo") is not None:
        import capo_wickr.types.oidc_config_info

        out["openid_connect_info"] = capo_wickr.types.oidc_config_info.deserialize_json(
            data["openidConnectInfo"]
        )
    if data.get("tokenInfo") is not None:
        import capo_wickr.types.oidc_token_info

        out["token_info"] = capo_wickr.types.oidc_token_info.deserialize_json(
            data["tokenInfo"]
        )
    return out


def redact_sensitive(value: GetOidcInfoResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "openid_connect_info" in value:
        import capo_wickr.types.oidc_config_info

        out["openid_connect_info"] = capo_wickr.types.oidc_config_info.redact_sensitive(
            value["openid_connect_info"]
        )
    return out
