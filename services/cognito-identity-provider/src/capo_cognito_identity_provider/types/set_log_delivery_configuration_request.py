"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetLogDeliveryConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.log_configuration_list_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class SetLogDeliveryConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to configure logging.</p>"""
    log_configurations: "capo_cognito_identity_provider.types.log_configuration_list_type.LogConfigurationListType"
    """<p>A collection of the logging configurations for a user pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetLogDeliveryConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import capo_cognito_identity_provider.types.log_configuration_list_type

    out["LogConfigurations"] = (
        capo_cognito_identity_provider.types.log_configuration_list_type.serialize_aws_json_1_1(
            value["log_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetLogDeliveryConfigurationRequest:
    out: SetLogDeliveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("LogConfigurations") is not None:
        import capo_cognito_identity_provider.types.log_configuration_list_type

        out["log_configurations"] = (
            capo_cognito_identity_provider.types.log_configuration_list_type.deserialize_aws_json_1_1(
                data["LogConfigurations"]
            )
        )
    else:
        out["log_configurations"] = []
    return out
