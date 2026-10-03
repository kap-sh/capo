"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateCognitoUserPoolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.client_ids
    import capo_verifiedpermissions.types.update_cognito_group_configuration
    import capo_verifiedpermissions.types.user_pool_arn


class UpdateCognitoUserPoolConfiguration(TypedDict, closed=True):
    user_pool_arn: "capo_verifiedpermissions.types.user_pool_arn.UserPoolArn"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the Amazon Cognito user pool associated with this identity source.</p>"""
    client_ids: NotRequired["capo_verifiedpermissions.types.client_ids.ClientIds"]
    """<p>The client ID of an app client that is configured for the specified Amazon Cognito user pool.</p>"""
    group_configuration: NotRequired[
        "capo_verifiedpermissions.types.update_cognito_group_configuration.UpdateCognitoGroupConfiguration"
    ]
    """<p>The configuration of the user groups from an Amazon Cognito user pool identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCognitoUserPoolConfiguration) -> dict:
    out: dict = {}
    out["userPoolArn"] = value["user_pool_arn"]
    if "client_ids" in value:
        import capo_verifiedpermissions.types.client_ids

        out["clientIds"] = (
            capo_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
                value["client_ids"]
            )
        )
    if "group_configuration" in value:
        import capo_verifiedpermissions.types.update_cognito_group_configuration

        out["groupConfiguration"] = (
            capo_verifiedpermissions.types.update_cognito_group_configuration.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCognitoUserPoolConfiguration:
    out: UpdateCognitoUserPoolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("userPoolArn") is not None:
        out["user_pool_arn"] = data["userPoolArn"]
    else:
        raise DeserializationError(
            "UpdateCognitoUserPoolConfiguration.user_pool_arn required"
        )
    if data.get("clientIds") is not None:
        import capo_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            capo_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    if data.get("groupConfiguration") is not None:
        import capo_verifiedpermissions.types.update_cognito_group_configuration

        out["group_configuration"] = (
            capo_verifiedpermissions.types.update_cognito_group_configuration.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    return out
