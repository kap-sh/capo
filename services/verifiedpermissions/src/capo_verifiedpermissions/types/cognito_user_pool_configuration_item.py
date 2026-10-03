"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#CognitoUserPoolConfigurationItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.client_ids
    import capo_verifiedpermissions.types.cognito_group_configuration_item
    import capo_verifiedpermissions.types.issuer
    import capo_verifiedpermissions.types.user_pool_arn


class CognitoUserPoolConfigurationItem(TypedDict, closed=True):
    user_pool_arn: "capo_verifiedpermissions.types.user_pool_arn.UserPoolArn"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the Amazon Cognito user pool that contains the identities to be authorized.</p> <p>Example: <code>"userPoolArn": "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_1a2b3c4d5"</code> </p>"""
    client_ids: "capo_verifiedpermissions.types.client_ids.ClientIds"
    """<p>The unique application client IDs that are associated with the specified Amazon Cognito user pool.</p> <p>Example: <code>"clientIds": ["&amp;ExampleCogClientId;"]</code> </p>"""
    issuer: "capo_verifiedpermissions.types.issuer.Issuer"
    """<p>The OpenID Connect (OIDC) <code>issuer</code> ID of the Amazon Cognito user pool that contains the identities to be authorized.</p> <p>Example: <code>"issuer": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_1a2b3c4d5"</code> </p>"""
    group_configuration: NotRequired[
        "capo_verifiedpermissions.types.cognito_group_configuration_item.CognitoGroupConfigurationItem"
    ]
    """<p>The type of entity that a policy store maps to groups from an Amazon Cognito user pool identity source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CognitoUserPoolConfigurationItem) -> dict:
    out: dict = {}
    out["userPoolArn"] = value["user_pool_arn"]
    import capo_verifiedpermissions.types.client_ids

    out["clientIds"] = capo_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
        value["client_ids"]
    )
    out["issuer"] = value["issuer"]
    if "group_configuration" in value:
        import capo_verifiedpermissions.types.cognito_group_configuration_item

        out["groupConfiguration"] = (
            capo_verifiedpermissions.types.cognito_group_configuration_item.serialize_aws_json_1_0(
                value["group_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CognitoUserPoolConfigurationItem:
    out: CognitoUserPoolConfigurationItem = {}  # type: ignore[typeddict-item]
    if data.get("userPoolArn") is not None:
        out["user_pool_arn"] = data["userPoolArn"]
    else:
        raise DeserializationError(
            "CognitoUserPoolConfigurationItem.user_pool_arn required"
        )
    if data.get("clientIds") is not None:
        import capo_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            capo_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    else:
        raise DeserializationError(
            "CognitoUserPoolConfigurationItem.client_ids required"
        )
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("CognitoUserPoolConfigurationItem.issuer required")
    if data.get("groupConfiguration") is not None:
        import capo_verifiedpermissions.types.cognito_group_configuration_item

        out["group_configuration"] = (
            capo_verifiedpermissions.types.cognito_group_configuration_item.deserialize_aws_json_1_0(
                data["groupConfiguration"]
            )
        )
    return out
