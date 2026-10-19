"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OAuthConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_url
    import capo_iot_managed_integrations.types.proactive_refresh_token_renewal
    import capo_iot_managed_integrations.types.token_endpoint_authentication_scheme
    import capo_iot_managed_integrations.types.token_url


class OAuthConfig(TypedDict, closed=True):
    auth_url: "capo_iot_managed_integrations.types.auth_url.AuthUrl"
    """<p>The authorization URL for the OAuth service, where users are directed to authenticate and authorize access.</p>"""
    token_url: "capo_iot_managed_integrations.types.token_url.TokenUrl"
    """<p>The token URL for the OAuth service, where authorization codes are exchanged for access tokens.</p>"""
    scope: NotRequired["str"]
    """<p>The OAuth scopes requested during authorization, which define the permissions granted to the application.</p>"""
    token_endpoint_authentication_scheme: "capo_iot_managed_integrations.types.token_endpoint_authentication_scheme.TokenEndpointAuthenticationScheme"
    """<p>The authentication scheme used when requesting tokens from the token endpoint.</p>"""
    o_auth_complete_redirect_url: NotRequired["str"]
    """<p>The URL where users are redirected after completing the OAuth authorization process.</p>"""
    proactive_refresh_token_renewal: NotRequired[
        "capo_iot_managed_integrations.types.proactive_refresh_token_renewal.ProactiveRefreshTokenRenewal"
    ]
    """<p>Configuration for proactively refreshing OAuth tokens before they expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuthConfig) -> dict:
    out: dict = {}
    out["authUrl"] = value["auth_url"]
    out["tokenUrl"] = value["token_url"]
    if "scope" in value:
        out["scope"] = value["scope"]
    import capo_iot_managed_integrations.types.token_endpoint_authentication_scheme

    out["tokenEndpointAuthenticationScheme"] = (
        capo_iot_managed_integrations.types.token_endpoint_authentication_scheme.serialize_json(
            value["token_endpoint_authentication_scheme"]
        )
    )
    if "o_auth_complete_redirect_url" in value:
        out["oAuthCompleteRedirectUrl"] = value["o_auth_complete_redirect_url"]
    if "proactive_refresh_token_renewal" in value:
        import capo_iot_managed_integrations.types.proactive_refresh_token_renewal

        out["proactiveRefreshTokenRenewal"] = (
            capo_iot_managed_integrations.types.proactive_refresh_token_renewal.serialize_json(
                value["proactive_refresh_token_renewal"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuthConfig:
    out: OAuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("authUrl") is not None:
        out["auth_url"] = data["authUrl"]
    else:
        out["auth_url"] = ""
    if data.get("tokenUrl") is not None:
        out["token_url"] = data["tokenUrl"]
    else:
        out["token_url"] = ""
    if data.get("scope") is not None:
        out["scope"] = data["scope"]
    if data.get("tokenEndpointAuthenticationScheme") is not None:
        import capo_iot_managed_integrations.types.token_endpoint_authentication_scheme

        out["token_endpoint_authentication_scheme"] = (
            capo_iot_managed_integrations.types.token_endpoint_authentication_scheme.deserialize_json(
                data["tokenEndpointAuthenticationScheme"]
            )
        )
    else:
        import typing

        out["token_endpoint_authentication_scheme"] = typing.cast(
            "capo_iot_managed_integrations.types.token_endpoint_authentication_scheme.TokenEndpointAuthenticationScheme",
            "",
        )
    if data.get("oAuthCompleteRedirectUrl") is not None:
        out["o_auth_complete_redirect_url"] = data["oAuthCompleteRedirectUrl"]
    if data.get("proactiveRefreshTokenRenewal") is not None:
        import capo_iot_managed_integrations.types.proactive_refresh_token_renewal

        out["proactive_refresh_token_renewal"] = (
            capo_iot_managed_integrations.types.proactive_refresh_token_renewal.deserialize_json(
                data["proactiveRefreshTokenRenewal"]
            )
        )
    return out
