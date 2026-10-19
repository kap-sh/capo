"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolAddOnsType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.advanced_security_additional_flows_type
    import capo_cognito_identity_provider.types.advanced_security_mode_type


class UserPoolAddOnsType(TypedDict, closed=True):
    advanced_security_mode: "capo_cognito_identity_provider.types.advanced_security_mode_type.AdvancedSecurityModeType"
    """<p>The operating mode of threat protection for standard authentication types in your user pool, including username-password and secure remote password (SRP) authentication. </p>"""
    advanced_security_additional_flows: NotRequired[
        "capo_cognito_identity_provider.types.advanced_security_additional_flows_type.AdvancedSecurityAdditionalFlowsType"
    ]
    """<p>Threat protection configuration options for additional authentication types in your user pool, including custom authentication. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolAddOnsType) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.advanced_security_mode_type

    out["AdvancedSecurityMode"] = (
        capo_cognito_identity_provider.types.advanced_security_mode_type.serialize_aws_json_1_1(
            value["advanced_security_mode"]
        )
    )
    if "advanced_security_additional_flows" in value:
        import capo_cognito_identity_provider.types.advanced_security_additional_flows_type

        out["AdvancedSecurityAdditionalFlows"] = (
            capo_cognito_identity_provider.types.advanced_security_additional_flows_type.serialize_aws_json_1_1(
                value["advanced_security_additional_flows"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolAddOnsType:
    out: UserPoolAddOnsType = {}  # type: ignore[typeddict-item]
    if data.get("AdvancedSecurityMode") is not None:
        import capo_cognito_identity_provider.types.advanced_security_mode_type

        out["advanced_security_mode"] = (
            capo_cognito_identity_provider.types.advanced_security_mode_type.deserialize_aws_json_1_1(
                data["AdvancedSecurityMode"]
            )
        )
    else:
        import typing

        out["advanced_security_mode"] = typing.cast(
            "capo_cognito_identity_provider.types.advanced_security_mode_type.AdvancedSecurityModeType",
            "",
        )
    if data.get("AdvancedSecurityAdditionalFlows") is not None:
        import capo_cognito_identity_provider.types.advanced_security_additional_flows_type

        out["advanced_security_additional_flows"] = (
            capo_cognito_identity_provider.types.advanced_security_additional_flows_type.deserialize_aws_json_1_1(
                data["AdvancedSecurityAdditionalFlows"]
            )
        )
    return out
