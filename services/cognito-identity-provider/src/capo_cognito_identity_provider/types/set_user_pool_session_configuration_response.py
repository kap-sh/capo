"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserPoolSessionConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.user_pool_token_session_config_type
    import capo_cognito_identity_provider.types.user_session_tracking_type


class SetUserPoolSessionConfigurationResponse(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that the session configuration was applied to.</p>"""
    user_session_tracking: NotRequired[
        "capo_cognito_identity_provider.types.user_session_tracking_type.UserSessionTrackingType"
    ]
    """<p>The session tracking setting that was applied to the user pool.</p>"""
    token_session: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_token_session_config_type.UserPoolTokenSessionConfigType"
    ]
    """<p>The pool-wide token session settings that were applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserPoolSessionConfigurationResponse) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "user_session_tracking" in value:
        import capo_cognito_identity_provider.types.user_session_tracking_type

        out["UserSessionTracking"] = (
            capo_cognito_identity_provider.types.user_session_tracking_type.serialize_aws_json_1_1(
                value["user_session_tracking"]
            )
        )
    if "token_session" in value:
        import capo_cognito_identity_provider.types.user_pool_token_session_config_type

        out["TokenSession"] = (
            capo_cognito_identity_provider.types.user_pool_token_session_config_type.serialize_aws_json_1_1(
                value["token_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUserPoolSessionConfigurationResponse:
    out: SetUserPoolSessionConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("UserSessionTracking") is not None:
        import capo_cognito_identity_provider.types.user_session_tracking_type

        out["user_session_tracking"] = (
            capo_cognito_identity_provider.types.user_session_tracking_type.deserialize_aws_json_1_1(
                data["UserSessionTracking"]
            )
        )
    if data.get("TokenSession") is not None:
        import capo_cognito_identity_provider.types.user_pool_token_session_config_type

        out["token_session"] = (
            capo_cognito_identity_provider.types.user_pool_token_session_config_type.deserialize_aws_json_1_1(
                data["TokenSession"]
            )
        )
    return out
