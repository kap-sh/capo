"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.relying_party_id_type
    import capo_cognito_identity_provider.types.user_verification_type
    import capo_cognito_identity_provider.types.web_authn_factor_configuration_type


class WebAuthnConfigurationType(TypedDict, closed=True):
    relying_party_id: NotRequired[
        "capo_cognito_identity_provider.types.relying_party_id_type.RelyingPartyIdType"
    ]
    """<p>Sets or displays the authentication domain, typically your user pool domain, that passkey providers must use as a relying party (RP) in their configuration.</p> <p>Under the following conditions, the passkey relying party ID must be the fully-qualified domain name of your custom domain:</p> <ul> <li> <p>The user pool is configured for passkey authentication.</p> </li> <li> <p>The user pool has a custom domain, whether or not it also has a prefix domain.</p> </li> <li> <p>Your application performs authentication with managed login or the classic hosted UI.</p> </li> </ul>"""
    user_verification: NotRequired[
        "capo_cognito_identity_provider.types.user_verification_type.UserVerificationType"
    ]
    """<p>When <code>required</code>, users can only register and sign in users with passkeys that are capable of <a href="https://www.w3.org/TR/webauthn-2/#enum-userVerificationRequirement">user verification</a>. When <code>preferred</code>, your user pool doesn't require the use of authenticators with user verification but encourages it.</p>"""
    factor_configuration: NotRequired[
        "capo_cognito_identity_provider.types.web_authn_factor_configuration_type.WebAuthnFactorConfigurationType"
    ]
    """<p>Sets whether passkeys can be used as multi-factor authentication (MFA). When set to <code>MULTI_FACTOR_WITH_USER_VERIFICATION</code>, passkey authentication with user verification satisfies MFA requirements. When set to <code>SINGLE_FACTOR</code> or not set, passkeys are a single authentication factor. To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnConfigurationType) -> dict:
    out: dict = {}
    if "relying_party_id" in value:
        out["RelyingPartyId"] = value["relying_party_id"]
    if "user_verification" in value:
        import capo_cognito_identity_provider.types.user_verification_type

        out["UserVerification"] = (
            capo_cognito_identity_provider.types.user_verification_type.serialize_aws_json_1_1(
                value["user_verification"]
            )
        )
    if "factor_configuration" in value:
        import capo_cognito_identity_provider.types.web_authn_factor_configuration_type

        out["FactorConfiguration"] = (
            capo_cognito_identity_provider.types.web_authn_factor_configuration_type.serialize_aws_json_1_1(
                value["factor_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAuthnConfigurationType:
    out: WebAuthnConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("RelyingPartyId") is not None:
        out["relying_party_id"] = data["RelyingPartyId"]
    if data.get("UserVerification") is not None:
        import capo_cognito_identity_provider.types.user_verification_type

        out["user_verification"] = (
            capo_cognito_identity_provider.types.user_verification_type.deserialize_aws_json_1_1(
                data["UserVerification"]
            )
        )
    if data.get("FactorConfiguration") is not None:
        import capo_cognito_identity_provider.types.web_authn_factor_configuration_type

        out["factor_configuration"] = (
            capo_cognito_identity_provider.types.web_authn_factor_configuration_type.deserialize_aws_json_1_1(
                data["FactorConfiguration"]
            )
        )
    return out
