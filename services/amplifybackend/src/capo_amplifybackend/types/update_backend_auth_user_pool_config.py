"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthUserPoolConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.update_backend_auth_forgot_password_config
    import capo_amplifybackend.types.update_backend_auth_mfa_config
    import capo_amplifybackend.types.update_backend_auth_o_auth_config
    import capo_amplifybackend.types.update_backend_auth_password_policy_config
    import capo_amplifybackend.types.update_backend_auth_verification_message_config


class UpdateBackendAuthUserPoolConfig(TypedDict, closed=True):
    forgot_password: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_forgot_password_config.UpdateBackendAuthForgotPasswordConfig"
    ]
    """<p><b>(DEPRECATED)</b> Describes the forgot password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    mfa: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_mfa_config.UpdateBackendAuthMFAConfig"
    ]
    """<p>Describes whether to apply multi-factor authentication policies for your Amazon Cognito user pool configured as a part of your Amplify project.</p>"""
    o_auth: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_o_auth_config.UpdateBackendAuthOAuthConfig"
    ]
    """<p>Describes the OAuth policy and rules for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    password_policy: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_password_policy_config.UpdateBackendAuthPasswordPolicyConfig"
    ]
    """<p>Describes the password policy for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""
    verification_message: NotRequired[
        "capo_amplifybackend.types.update_backend_auth_verification_message_config.UpdateBackendAuthVerificationMessageConfig"
    ]
    """<p>Describes the email or SMS verification message for your Amazon Cognito user pool, configured as a part of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthUserPoolConfig) -> dict:
    out: dict = {}
    if "forgot_password" in value:
        import capo_amplifybackend.types.update_backend_auth_forgot_password_config

        out["forgotPassword"] = (
            capo_amplifybackend.types.update_backend_auth_forgot_password_config.serialize_json(
                value["forgot_password"]
            )
        )
    if "mfa" in value:
        import capo_amplifybackend.types.update_backend_auth_mfa_config

        out["mfa"] = (
            capo_amplifybackend.types.update_backend_auth_mfa_config.serialize_json(
                value["mfa"]
            )
        )
    if "o_auth" in value:
        import capo_amplifybackend.types.update_backend_auth_o_auth_config

        out["oAuth"] = (
            capo_amplifybackend.types.update_backend_auth_o_auth_config.serialize_json(
                value["o_auth"]
            )
        )
    if "password_policy" in value:
        import capo_amplifybackend.types.update_backend_auth_password_policy_config

        out["passwordPolicy"] = (
            capo_amplifybackend.types.update_backend_auth_password_policy_config.serialize_json(
                value["password_policy"]
            )
        )
    if "verification_message" in value:
        import capo_amplifybackend.types.update_backend_auth_verification_message_config

        out["verificationMessage"] = (
            capo_amplifybackend.types.update_backend_auth_verification_message_config.serialize_json(
                value["verification_message"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthUserPoolConfig:
    out: UpdateBackendAuthUserPoolConfig = {}  # type: ignore[typeddict-item]
    if data.get("forgotPassword") is not None:
        import capo_amplifybackend.types.update_backend_auth_forgot_password_config

        out["forgot_password"] = (
            capo_amplifybackend.types.update_backend_auth_forgot_password_config.deserialize_json(
                data["forgotPassword"]
            )
        )
    if data.get("mfa") is not None:
        import capo_amplifybackend.types.update_backend_auth_mfa_config

        out["mfa"] = (
            capo_amplifybackend.types.update_backend_auth_mfa_config.deserialize_json(
                data["mfa"]
            )
        )
    if data.get("oAuth") is not None:
        import capo_amplifybackend.types.update_backend_auth_o_auth_config

        out["o_auth"] = (
            capo_amplifybackend.types.update_backend_auth_o_auth_config.deserialize_json(
                data["oAuth"]
            )
        )
    if data.get("passwordPolicy") is not None:
        import capo_amplifybackend.types.update_backend_auth_password_policy_config

        out["password_policy"] = (
            capo_amplifybackend.types.update_backend_auth_password_policy_config.deserialize_json(
                data["passwordPolicy"]
            )
        )
    if data.get("verificationMessage") is not None:
        import capo_amplifybackend.types.update_backend_auth_verification_message_config

        out["verification_message"] = (
            capo_amplifybackend.types.update_backend_auth_verification_message_config.deserialize_json(
                data["verificationMessage"]
            )
        )
    return out


def redact_sensitive(value: UpdateBackendAuthUserPoolConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "forgot_password" in value:
        import capo_amplifybackend.types.update_backend_auth_forgot_password_config

        out["forgot_password"] = (
            capo_amplifybackend.types.update_backend_auth_forgot_password_config.redact_sensitive(
                value["forgot_password"]
            )
        )
    if "o_auth" in value:
        import capo_amplifybackend.types.update_backend_auth_o_auth_config

        out["o_auth"] = (
            capo_amplifybackend.types.update_backend_auth_o_auth_config.redact_sensitive(
                value["o_auth"]
            )
        )
    if "verification_message" in value:
        import capo_amplifybackend.types.update_backend_auth_verification_message_config

        out["verification_message"] = (
            capo_amplifybackend.types.update_backend_auth_verification_message_config.redact_sensitive(
                value["verification_message"]
            )
        )
    return out
