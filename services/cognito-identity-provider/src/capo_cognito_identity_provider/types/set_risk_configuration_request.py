"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetRiskConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_takeover_risk_configuration_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type
    import capo_cognito_identity_provider.types.risk_exception_configuration_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class SetRiskConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to set a risk configuration. If you include <code>UserPoolId</code> in your request, don't include <code>ClientId</code>. When the client ID is null, the same risk configuration is applied to all the clients in the userPool. When you include both <code>ClientId</code> and <code>UserPoolId</code>, Amazon Cognito maps the configuration to the app client only.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client where you want to set a risk configuration. If <code>ClientId</code> is null, then the risk configuration is mapped to <code>UserPoolId</code>. When the client ID is null, the same risk configuration is applied to all the clients in the userPool.</p> <p>When you include a <code>ClientId</code> parameter, Amazon Cognito maps the configuration to the app client. When you include both <code>ClientId</code> and <code>UserPoolId</code>, Amazon Cognito maps the configuration to the app client only.</p>"""
    compromised_credentials_risk_configuration: NotRequired[
        "capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.CompromisedCredentialsRiskConfigurationType"
    ]
    """<p>The configuration of automated reactions to detected compromised credentials. Includes settings for blocking future sign-in requests and for the types of password-submission events you want to monitor.</p>"""
    account_takeover_risk_configuration: NotRequired[
        "capo_cognito_identity_provider.types.account_takeover_risk_configuration_type.AccountTakeoverRiskConfigurationType"
    ]
    """<p>The settings for automated responses and notification templates for adaptive authentication with threat protection.</p>"""
    risk_exception_configuration: NotRequired[
        "capo_cognito_identity_provider.types.risk_exception_configuration_type.RiskExceptionConfigurationType"
    ]
    """<p>A set of IP-address overrides to threat protection. You can set up IP-address always-block and always-allow lists.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetRiskConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "compromised_credentials_risk_configuration" in value:
        import capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type

        out["CompromisedCredentialsRiskConfiguration"] = (
            capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.serialize_aws_json_1_1(
                value["compromised_credentials_risk_configuration"]
            )
        )
    if "account_takeover_risk_configuration" in value:
        import capo_cognito_identity_provider.types.account_takeover_risk_configuration_type

        out["AccountTakeoverRiskConfiguration"] = (
            capo_cognito_identity_provider.types.account_takeover_risk_configuration_type.serialize_aws_json_1_1(
                value["account_takeover_risk_configuration"]
            )
        )
    if "risk_exception_configuration" in value:
        import capo_cognito_identity_provider.types.risk_exception_configuration_type

        out["RiskExceptionConfiguration"] = (
            capo_cognito_identity_provider.types.risk_exception_configuration_type.serialize_aws_json_1_1(
                value["risk_exception_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetRiskConfigurationRequest:
    out: SetRiskConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("CompromisedCredentialsRiskConfiguration") is not None:
        import capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type

        out["compromised_credentials_risk_configuration"] = (
            capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.deserialize_aws_json_1_1(
                data["CompromisedCredentialsRiskConfiguration"]
            )
        )
    if data.get("AccountTakeoverRiskConfiguration") is not None:
        import capo_cognito_identity_provider.types.account_takeover_risk_configuration_type

        out["account_takeover_risk_configuration"] = (
            capo_cognito_identity_provider.types.account_takeover_risk_configuration_type.deserialize_aws_json_1_1(
                data["AccountTakeoverRiskConfiguration"]
            )
        )
    if data.get("RiskExceptionConfiguration") is not None:
        import capo_cognito_identity_provider.types.risk_exception_configuration_type

        out["risk_exception_configuration"] = (
            capo_cognito_identity_provider.types.risk_exception_configuration_type.deserialize_aws_json_1_1(
                data["RiskExceptionConfiguration"]
            )
        )
    return out


def redact_sensitive(value: SetRiskConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
