"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RiskConfigurationType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_takeover_risk_configuration_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.risk_exception_configuration_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class RiskConfigurationType(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that has the risk configuration applied.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The app client where this configuration is applied. When this parameter isn't present, the risk configuration applies to all user pool app clients that don't have client-level settings.</p>"""
    compromised_credentials_risk_configuration: NotRequired[
        "capo_cognito_identity_provider.types.compromised_credentials_risk_configuration_type.CompromisedCredentialsRiskConfigurationType"
    ]
    """<p>Settings for compromised-credentials actions and authentication types with threat protection in full-function <code>ENFORCED</code> mode.</p>"""
    account_takeover_risk_configuration: NotRequired[
        "capo_cognito_identity_provider.types.account_takeover_risk_configuration_type.AccountTakeoverRiskConfigurationType"
    ]
    """<p>The settings for automated responses and notification templates for adaptive authentication with threat protection.</p>"""
    risk_exception_configuration: NotRequired[
        "capo_cognito_identity_provider.types.risk_exception_configuration_type.RiskExceptionConfigurationType"
    ]
    """<p>Exceptions to the risk evaluation configuration, including always-allow and always-block IP address ranges. </p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RiskConfigurationType) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
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
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RiskConfigurationType:
    out: RiskConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
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
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    return out


def redact_sensitive(value: RiskConfigurationType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
