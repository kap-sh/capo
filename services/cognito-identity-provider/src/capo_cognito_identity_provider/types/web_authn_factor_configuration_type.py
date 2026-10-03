"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#WebAuthnFactorConfigurationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The configuration of passkey authentication as a single factor or a multi-factor authentication (MFA) method. When set to <code>MULTI_FACTOR_WITH_USER_VERIFICATION</code>, your user pool requires passkey authenticators to perform <a href="https://www.w3.org/TR/webauthn-2/#user-verification">user verification</a>, for example a biometric or PIN. User verification combined with the passkey constitutes multi-factor authentication. When set to <code>SINGLE_FACTOR</code>, passkeys are a single authentication factor.</p>"""
WebAuthnFactorConfigurationType: TypeAlias = Literal[
    "SINGLE_FACTOR",
    "MULTI_FACTOR_WITH_USER_VERIFICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAuthnFactorConfigurationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WebAuthnFactorConfigurationType:
    return cast(WebAuthnFactorConfigurationType, data)
