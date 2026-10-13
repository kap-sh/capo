"""Generated from Smithy shape ``com.amazonaws.amplifybackend#SocialProviderSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.backend_auth_apple_provider_config
    import capo_amplifybackend.types.backend_auth_social_provider_config


class SocialProviderSettings(TypedDict, closed=True):
    facebook: NotRequired[
        "capo_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    google: NotRequired[
        "capo_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    login_with_amazon: NotRequired[
        "capo_amplifybackend.types.backend_auth_social_provider_config.BackendAuthSocialProviderConfig"
    ]
    sign_in_with_apple: NotRequired[
        "capo_amplifybackend.types.backend_auth_apple_provider_config.BackendAuthAppleProviderConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SocialProviderSettings) -> dict:
    out: dict = {}
    if "facebook" in value:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["Facebook"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["facebook"]
            )
        )
    if "google" in value:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["Google"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["google"]
            )
        )
    if "login_with_amazon" in value:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["LoginWithAmazon"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.serialize_json(
                value["login_with_amazon"]
            )
        )
    if "sign_in_with_apple" in value:
        import capo_amplifybackend.types.backend_auth_apple_provider_config

        out["SignInWithApple"] = (
            capo_amplifybackend.types.backend_auth_apple_provider_config.serialize_json(
                value["sign_in_with_apple"]
            )
        )
    return out


def deserialize_json(data: dict) -> SocialProviderSettings:
    out: SocialProviderSettings = {}  # type: ignore[typeddict-item]
    if data.get("Facebook") is not None:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["facebook"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["Facebook"]
            )
        )
    if data.get("Google") is not None:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["google"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["Google"]
            )
        )
    if data.get("LoginWithAmazon") is not None:
        import capo_amplifybackend.types.backend_auth_social_provider_config

        out["login_with_amazon"] = (
            capo_amplifybackend.types.backend_auth_social_provider_config.deserialize_json(
                data["LoginWithAmazon"]
            )
        )
    if data.get("SignInWithApple") is not None:
        import capo_amplifybackend.types.backend_auth_apple_provider_config

        out["sign_in_with_apple"] = (
            capo_amplifybackend.types.backend_auth_apple_provider_config.deserialize_json(
                data["SignInWithApple"]
            )
        )
    return out


def redact_sensitive(value: SocialProviderSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "facebook" in value:
        out["facebook"] = "*** Sensitive Data Redacted ***"
    if "google" in value:
        out["google"] = "*** Sensitive Data Redacted ***"
    if "login_with_amazon" in value:
        out["login_with_amazon"] = "*** Sensitive Data Redacted ***"
    if "sign_in_with_apple" in value:
        out["sign_in_with_apple"] = "*** Sensitive Data Redacted ***"
    return out
