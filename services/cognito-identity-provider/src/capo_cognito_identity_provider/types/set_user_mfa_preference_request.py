"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserMFAPreferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.email_mfa_settings_type
    import capo_cognito_identity_provider.types.sms_mfa_settings_type
    import capo_cognito_identity_provider.types.software_token_mfa_settings_type
    import capo_cognito_identity_provider.types.token_model_type
    import capo_cognito_identity_provider.types.web_authn_mfa_settings_type


class SetUserMFAPreferenceRequest(TypedDict, closed=True):
    sms_mfa_settings: NotRequired[
        "capo_cognito_identity_provider.types.sms_mfa_settings_type.SMSMfaSettingsType"
    ]
    """<p>User preferences for SMS message MFA. Activates or deactivates SMS MFA and sets it as the preferred MFA method when multiple methods are available.</p>"""
    software_token_mfa_settings: NotRequired[
        "capo_cognito_identity_provider.types.software_token_mfa_settings_type.SoftwareTokenMfaSettingsType"
    ]
    """<p>User preferences for time-based one-time password (TOTP) MFA. Activates or deactivates TOTP MFA and sets it as the preferred MFA method when multiple methods are available. Users must register a TOTP authenticator before they set this as their preferred MFA method.</p>"""
    email_mfa_settings: NotRequired[
        "capo_cognito_identity_provider.types.email_mfa_settings_type.EmailMfaSettingsType"
    ]
    """<p>User preferences for email message MFA. Activates or deactivates email MFA and sets it as the preferred MFA method when multiple methods are available. To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p>"""
    web_authn_mfa_settings: NotRequired[
        "capo_cognito_identity_provider.types.web_authn_mfa_settings_type.WebAuthnMfaSettingsType"
    ]
    """<p>User preferences for passkey MFA. Activates or deactivates passkey MFA for the user. When activated, passkey authentication requires user verification, and passkey sign-in is available when MFA is required. To activate this setting, the <code>FactorConfiguration</code> of your user pool <code>WebAuthnConfiguration</code> must be <code>MULTI_FACTOR_WITH_USER_VERIFICATION</code>. To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p>"""
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserMFAPreferenceRequest) -> dict:
    out: dict = {}
    if "sms_mfa_settings" in value:
        import capo_cognito_identity_provider.types.sms_mfa_settings_type

        out["SMSMfaSettings"] = (
            capo_cognito_identity_provider.types.sms_mfa_settings_type.serialize_aws_json_1_1(
                value["sms_mfa_settings"]
            )
        )
    if "software_token_mfa_settings" in value:
        import capo_cognito_identity_provider.types.software_token_mfa_settings_type

        out["SoftwareTokenMfaSettings"] = (
            capo_cognito_identity_provider.types.software_token_mfa_settings_type.serialize_aws_json_1_1(
                value["software_token_mfa_settings"]
            )
        )
    if "email_mfa_settings" in value:
        import capo_cognito_identity_provider.types.email_mfa_settings_type

        out["EmailMfaSettings"] = (
            capo_cognito_identity_provider.types.email_mfa_settings_type.serialize_aws_json_1_1(
                value["email_mfa_settings"]
            )
        )
    if "web_authn_mfa_settings" in value:
        import capo_cognito_identity_provider.types.web_authn_mfa_settings_type

        out["WebAuthnMfaSettings"] = (
            capo_cognito_identity_provider.types.web_authn_mfa_settings_type.serialize_aws_json_1_1(
                value["web_authn_mfa_settings"]
            )
        )
    out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUserMFAPreferenceRequest:
    out: SetUserMFAPreferenceRequest = {}  # type: ignore[typeddict-item]
    if data.get("SMSMfaSettings") is not None:
        import capo_cognito_identity_provider.types.sms_mfa_settings_type

        out["sms_mfa_settings"] = (
            capo_cognito_identity_provider.types.sms_mfa_settings_type.deserialize_aws_json_1_1(
                data["SMSMfaSettings"]
            )
        )
    if data.get("SoftwareTokenMfaSettings") is not None:
        import capo_cognito_identity_provider.types.software_token_mfa_settings_type

        out["software_token_mfa_settings"] = (
            capo_cognito_identity_provider.types.software_token_mfa_settings_type.deserialize_aws_json_1_1(
                data["SoftwareTokenMfaSettings"]
            )
        )
    if data.get("EmailMfaSettings") is not None:
        import capo_cognito_identity_provider.types.email_mfa_settings_type

        out["email_mfa_settings"] = (
            capo_cognito_identity_provider.types.email_mfa_settings_type.deserialize_aws_json_1_1(
                data["EmailMfaSettings"]
            )
        )
    if data.get("WebAuthnMfaSettings") is not None:
        import capo_cognito_identity_provider.types.web_authn_mfa_settings_type

        out["web_authn_mfa_settings"] = (
            capo_cognito_identity_provider.types.web_authn_mfa_settings_type.deserialize_aws_json_1_1(
                data["WebAuthnMfaSettings"]
            )
        )
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("SetUserMFAPreferenceRequest.access_token required")
    return out
