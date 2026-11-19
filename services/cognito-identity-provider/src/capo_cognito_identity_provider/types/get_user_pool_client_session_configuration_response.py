"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserPoolClientSessionConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_sso_session_config_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetUserPoolClientSessionConfigurationResponse(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client that the session configuration applies to.</p>"""
    sso_session: NotRequired[
        "capo_cognito_identity_provider.types.client_sso_session_config_type.ClientSSOSessionConfigType"
    ]
    """<p>The SSO session settings for the app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: GetUserPoolClientSessionConfigurationResponse,
) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "sso_session" in value:
        import capo_cognito_identity_provider.types.client_sso_session_config_type

        out["SSOSession"] = (
            capo_cognito_identity_provider.types.client_sso_session_config_type.serialize_aws_json_1_1(
                value["sso_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetUserPoolClientSessionConfigurationResponse:
    out: GetUserPoolClientSessionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("SSOSession") is not None:
        import capo_cognito_identity_provider.types.client_sso_session_config_type

        out["sso_session"] = (
            capo_cognito_identity_provider.types.client_sso_session_config_type.deserialize_aws_json_1_1(
                data["SSOSession"]
            )
        )
    return out


def redact_sensitive(
    value: GetUserPoolClientSessionConfigurationResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
