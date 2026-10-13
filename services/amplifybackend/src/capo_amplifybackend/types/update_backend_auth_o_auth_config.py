"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthOAuthConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.list_of__string
    import capo_amplifybackend.types.list_of_o_auth_scopes_element
    import capo_amplifybackend.types.o_auth_grant_type
    import capo_amplifybackend.types.social_provider_settings


class UpdateBackendAuthOAuthConfig(TypedDict, closed=True):
    domain_prefix: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The Amazon Cognito domain prefix used to create a hosted UI for authentication.</p>"""
    o_auth_grant_type: NotRequired[
        "capo_amplifybackend.types.o_auth_grant_type.OAuthGrantType"
    ]
    """<p>The OAuth grant type to allow app users to authenticate from your Amplify app.</p>"""
    o_auth_scopes: NotRequired[
        "capo_amplifybackend.types.list_of_o_auth_scopes_element.ListOfOAuthScopesElement"
    ]
    """<p>The list of OAuth-related flows that can allow users to authenticate from your Amplify app.</p>"""
    redirect_sign_in_ur_is: NotRequired[
        "capo_amplifybackend.types.list_of__string.ListOf__string"
    ]
    """<p>Redirect URLs that OAuth uses when a user signs in to an Amplify app.</p>"""
    redirect_sign_out_ur_is: NotRequired[
        "capo_amplifybackend.types.list_of__string.ListOf__string"
    ]
    """<p>Redirect URLs that OAuth uses when a user signs out of an Amplify app.</p>"""
    social_provider_settings: NotRequired[
        "capo_amplifybackend.types.social_provider_settings.SocialProviderSettings"
    ]
    """<p>Describes third-party social federation configurations for allowing your users to sign in with OAuth.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthOAuthConfig) -> dict:
    out: dict = {}
    if "domain_prefix" in value:
        out["domainPrefix"] = value["domain_prefix"]
    if "o_auth_grant_type" in value:
        import capo_amplifybackend.types.o_auth_grant_type

        out["oAuthGrantType"] = (
            capo_amplifybackend.types.o_auth_grant_type.serialize_json(
                value["o_auth_grant_type"]
            )
        )
    if "o_auth_scopes" in value:
        import capo_amplifybackend.types.list_of_o_auth_scopes_element

        out["oAuthScopes"] = (
            capo_amplifybackend.types.list_of_o_auth_scopes_element.serialize_json(
                value["o_auth_scopes"]
            )
        )
    if "redirect_sign_in_ur_is" in value:
        import capo_amplifybackend.types.list_of__string

        out["redirectSignInURIs"] = (
            capo_amplifybackend.types.list_of__string.serialize_json(
                value["redirect_sign_in_ur_is"]
            )
        )
    if "redirect_sign_out_ur_is" in value:
        import capo_amplifybackend.types.list_of__string

        out["redirectSignOutURIs"] = (
            capo_amplifybackend.types.list_of__string.serialize_json(
                value["redirect_sign_out_ur_is"]
            )
        )
    if "social_provider_settings" in value:
        import capo_amplifybackend.types.social_provider_settings

        out["socialProviderSettings"] = (
            capo_amplifybackend.types.social_provider_settings.serialize_json(
                value["social_provider_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthOAuthConfig:
    out: UpdateBackendAuthOAuthConfig = {}  # type: ignore[typeddict-item]
    if data.get("domainPrefix") is not None:
        out["domain_prefix"] = data["domainPrefix"]
    if data.get("oAuthGrantType") is not None:
        import capo_amplifybackend.types.o_auth_grant_type

        out["o_auth_grant_type"] = (
            capo_amplifybackend.types.o_auth_grant_type.deserialize_json(
                data["oAuthGrantType"]
            )
        )
    if data.get("oAuthScopes") is not None:
        import capo_amplifybackend.types.list_of_o_auth_scopes_element

        out["o_auth_scopes"] = (
            capo_amplifybackend.types.list_of_o_auth_scopes_element.deserialize_json(
                data["oAuthScopes"]
            )
        )
    if data.get("redirectSignInURIs") is not None:
        import capo_amplifybackend.types.list_of__string

        out["redirect_sign_in_ur_is"] = (
            capo_amplifybackend.types.list_of__string.deserialize_json(
                data["redirectSignInURIs"]
            )
        )
    if data.get("redirectSignOutURIs") is not None:
        import capo_amplifybackend.types.list_of__string

        out["redirect_sign_out_ur_is"] = (
            capo_amplifybackend.types.list_of__string.deserialize_json(
                data["redirectSignOutURIs"]
            )
        )
    if data.get("socialProviderSettings") is not None:
        import capo_amplifybackend.types.social_provider_settings

        out["social_provider_settings"] = (
            capo_amplifybackend.types.social_provider_settings.deserialize_json(
                data["socialProviderSettings"]
            )
        )
    return out


def redact_sensitive(value: UpdateBackendAuthOAuthConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "social_provider_settings" in value:
        import capo_amplifybackend.types.social_provider_settings

        out["social_provider_settings"] = (
            capo_amplifybackend.types.social_provider_settings.redact_sensitive(
                value["social_provider_settings"]
            )
        )
    return out
