"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserPoolSessionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.user_pool_token_session_config_type
    import capo_cognito_identity_provider.types.user_session_tracking_type


class SetUserPoolSessionConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to configure session tracking.</p>"""
    user_session_tracking: "capo_cognito_identity_provider.types.user_session_tracking_type.UserSessionTrackingType"
    """<p>Specifies whether Amazon Cognito tracks sessions for users in the user pool. Set this value to <code>ENABLED</code> to turn on server-side session tracking, or <code>DISABLED</code> to turn it off. When you set this value to <code>DISABLED</code> while the user pool remains active, existing client-level session configurations are retained but dormant, and are reactivated when you enable tracking again.</p>"""
    token_session: "capo_cognito_identity_provider.types.user_pool_token_session_config_type.UserPoolTokenSessionConfigType"
    """<p>The pool-wide token session settings to apply.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserPoolSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import capo_cognito_identity_provider.types.user_session_tracking_type

    out["UserSessionTracking"] = (
        capo_cognito_identity_provider.types.user_session_tracking_type.serialize_aws_json_1_1(
            value["user_session_tracking"]
        )
    )
    import capo_cognito_identity_provider.types.user_pool_token_session_config_type

    out["TokenSession"] = (
        capo_cognito_identity_provider.types.user_pool_token_session_config_type.serialize_aws_json_1_1(
            value["token_session"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUserPoolSessionConfigurationRequest:
    out: SetUserPoolSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("UserSessionTracking") is not None:
        import capo_cognito_identity_provider.types.user_session_tracking_type

        out["user_session_tracking"] = (
            capo_cognito_identity_provider.types.user_session_tracking_type.deserialize_aws_json_1_1(
                data["UserSessionTracking"]
            )
        )
    else:
        import typing

        out["user_session_tracking"] = typing.cast(
            "capo_cognito_identity_provider.types.user_session_tracking_type.UserSessionTrackingType",
            "",
        )
    if data.get("TokenSession") is not None:
        import capo_cognito_identity_provider.types.user_pool_token_session_config_type

        out["token_session"] = (
            capo_cognito_identity_provider.types.user_pool_token_session_config_type.deserialize_aws_json_1_1(
                data["TokenSession"]
            )
        )
    else:
        raise DeserializationError(
            "SetUserPoolSessionConfigurationRequest.token_session required"
        )
    return out
