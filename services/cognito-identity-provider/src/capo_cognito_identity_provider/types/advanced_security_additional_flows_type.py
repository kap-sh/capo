"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdvancedSecurityAdditionalFlowsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.advanced_security_enabled_mode_type


class AdvancedSecurityAdditionalFlowsType(TypedDict, closed=True):
    custom_auth_mode: NotRequired[
        "capo_cognito_identity_provider.types.advanced_security_enabled_mode_type.AdvancedSecurityEnabledModeType"
    ]
    """<p>The operating mode of threat protection in custom authentication with <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html"> Custom authentication challenge Lambda triggers</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdvancedSecurityAdditionalFlowsType) -> dict:
    out: dict = {}
    if "custom_auth_mode" in value:
        import capo_cognito_identity_provider.types.advanced_security_enabled_mode_type

        out["CustomAuthMode"] = (
            capo_cognito_identity_provider.types.advanced_security_enabled_mode_type.serialize_aws_json_1_1(
                value["custom_auth_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdvancedSecurityAdditionalFlowsType:
    out: AdvancedSecurityAdditionalFlowsType = {}  # type: ignore[typeddict-item]
    if data.get("CustomAuthMode") is not None:
        import capo_cognito_identity_provider.types.advanced_security_enabled_mode_type

        out["custom_auth_mode"] = (
            capo_cognito_identity_provider.types.advanced_security_enabled_mode_type.deserialize_aws_json_1_1(
                data["CustomAuthMode"]
            )
        )
    return out
