"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserPoolClientSessionConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_sso_session_config_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class SetUserPoolClientSessionConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that you want to configure.</p>"""
    sso_session: "capo_cognito_identity_provider.types.client_sso_session_config_type.ClientSSOSessionConfigType"
    """<p>The SSO session settings for the app client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserPoolClientSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    import capo_cognito_identity_provider.types.client_sso_session_config_type

    out["SSOSession"] = (
        capo_cognito_identity_provider.types.client_sso_session_config_type.serialize_aws_json_1_1(
            value["sso_session"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> SetUserPoolClientSessionConfigurationRequest:
    out: SetUserPoolClientSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("SSOSession") is not None:
        import capo_cognito_identity_provider.types.client_sso_session_config_type

        out["sso_session"] = (
            capo_cognito_identity_provider.types.client_sso_session_config_type.deserialize_aws_json_1_1(
                data["SSOSession"]
            )
        )
    else:
        raise DeserializationError(
            "SetUserPoolClientSessionConfigurationRequest.sso_session required"
        )
    return out


def redact_sensitive(
    value: SetUserPoolClientSessionConfigurationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
