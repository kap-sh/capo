"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminCreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_list_type
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.delivery_medium_list_type
    import capo_cognito_identity_provider.types.force_alias_creation
    import capo_cognito_identity_provider.types.message_action_type
    import capo_cognito_identity_provider.types.password_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminCreateUserRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to create a user.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The value that you want to set as the username sign-in attribute. The following conditions apply to the username parameter.</p> <ul> <li> <p>The username can't be a duplicate of another username in the same user pool.</p> </li> <li> <p>You can't change the value of a username after you create it.</p> </li> <li> <p>You can only provide a value if usernames are a valid sign-in attribute for your user pool. If your user pool only supports phone numbers or email addresses as sign-in attributes, Amazon Cognito automatically generates a username value. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases">Customizing sign-in attributes</a>.</p> </li> </ul>"""
    user_attributes: NotRequired[
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>An array of name-value pairs that contain user attributes and attribute values to be set for the user to be created. You can create a user without specifying any attributes other than <code>Username</code>. However, any attributes that you specify as required (when creating a user pool or in the <b>Attributes</b> tab of the console) either you should supply (in your call to <code>AdminCreateUser</code>) or the user should supply (when they sign up in response to your welcome message).</p> <p>For custom attributes, you must prepend the <code>custom:</code> prefix to the attribute name.</p> <p>To send a message inviting the user to sign up, you must specify the user's email address or phone number. You can do this in your call to AdminCreateUser or in the <b>Users</b> tab of the Amazon Cognito console for managing your user pools.</p> <p>You must also provide an email address or phone number when you expect the user to do passwordless sign-in with an email or SMS OTP. These attributes must be provided when passwordless options are the only available, or when you don't submit a <code>TemporaryPassword</code>.</p> <p>In your <code>AdminCreateUser</code> request, you can set the <code>email_verified</code> and <code>phone_number_verified</code> attributes to <code>true</code>. The following conditions apply:</p> <dl> <dt>email</dt> <dd> <p>The email address where you want the user to receive their confirmation code and username. You must provide a value for <code>email</code> when you want to set <code>email_verified</code> to <code>true</code>, or if you set <code>EMAIL</code> in the <code>DesiredDeliveryMediums</code> parameter.</p> </dd> <dt>phone_number</dt> <dd> <p>The phone number where you want the user to receive their confirmation code and username. You must provide a value for <code>phone_number</code> when you want to set <code>phone_number_verified</code> to <code>true</code>, or if you set <code>SMS</code> in the <code>DesiredDeliveryMediums</code> parameter.</p> </dd> </dl>"""
    validation_data: NotRequired[
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>Temporary user attributes that contribute to the outcomes of your pre sign-up Lambda trigger. This set of key-value pairs are for custom validation of information that you collect from your users but don't need to retain.</p> <p>Your Lambda function can analyze this additional data and act on it. Your function can automatically confirm and verify select users or perform external API operations like logging user attributes and validation data to Amazon CloudWatch Logs.</p> <p>For more information about the pre sign-up Lambda trigger, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html">Pre sign-up Lambda trigger</a>.</p>"""
    temporary_password: NotRequired[
        "capo_cognito_identity_provider.types.password_type.PasswordType"
    ]
    """<p>The user's temporary password. This password must conform to the password policy that you specified when you created the user pool.</p> <p>The exception to the requirement for a password is when your user pool supports passwordless sign-in with email or SMS OTPs. To create a user with no password, omit this parameter or submit a blank value. You can only create a passwordless user when passwordless sign-in is available.</p> <p>The temporary password is valid only once. To complete the Admin Create User flow, the user must enter the temporary password in the sign-in page, along with a new password to be used in all future sign-ins.</p> <p>If you don't specify a value, Amazon Cognito generates one for you unless you have passwordless options active for your user pool.</p> <p>The temporary password can only be used until the user account expiration limit that you set for your user pool. To reset the account after that time limit, you must call <code>AdminCreateUser</code> again and specify <code>RESEND</code> for the <code>MessageAction</code> parameter.</p>"""
    force_alias_creation: (
        "capo_cognito_identity_provider.types.force_alias_creation.ForceAliasCreation"
    )
    """<p>This parameter is used only if the <code>phone_number_verified</code> or <code>email_verified</code> attribute is set to <code>True</code>. Otherwise, it is ignored.</p> <p>If this parameter is set to <code>True</code> and the phone number or email address specified in the <code>UserAttributes</code> parameter already exists as an alias with a different user, this request migrates the alias from the previous user to the newly-created user. The previous user will no longer be able to log in using that alias.</p> <p>If this parameter is set to <code>False</code>, the API throws an <code>AliasExistsException</code> error if the alias already exists. The default value is <code>False</code>.</p>"""
    message_action: NotRequired[
        "capo_cognito_identity_provider.types.message_action_type.MessageActionType"
    ]
    """<p>Set to <code>RESEND</code> to resend the invitation message to a user that already exists, and to reset the temporary-password duration with a new temporary password. Set to <code>SUPPRESS</code> to suppress sending the message. You can specify only one value.</p>"""
    desired_delivery_mediums: NotRequired[
        "capo_cognito_identity_provider.types.delivery_medium_list_type.DeliveryMediumListType"
    ]
    """<p>Specify <code>EMAIL</code> if email will be used to send the welcome message. Specify <code>SMS</code> if the phone number will be used. The default value is <code>SMS</code>. You can specify more than one value.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminCreateUserRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    if "user_attributes" in value:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["UserAttributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
                value["user_attributes"]
            )
        )
    if "validation_data" in value:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["ValidationData"] = (
            capo_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
                value["validation_data"]
            )
        )
    if "temporary_password" in value:
        out["TemporaryPassword"] = value["temporary_password"]
    out["ForceAliasCreation"] = value.get("force_alias_creation", False)
    if "message_action" in value:
        import capo_cognito_identity_provider.types.message_action_type

        out["MessageAction"] = (
            capo_cognito_identity_provider.types.message_action_type.serialize_aws_json_1_1(
                value["message_action"]
            )
        )
    if "desired_delivery_mediums" in value:
        import capo_cognito_identity_provider.types.delivery_medium_list_type

        out["DesiredDeliveryMediums"] = (
            capo_cognito_identity_provider.types.delivery_medium_list_type.serialize_aws_json_1_1(
                value["desired_delivery_mediums"]
            )
        )
    if "client_metadata" in value:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["ClientMetadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.serialize_aws_json_1_1(
                value["client_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminCreateUserRequest:
    out: AdminCreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminCreateUserRequest.user_pool_id required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminCreateUserRequest.username required")
    if data.get("UserAttributes") is not None:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["user_attributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["UserAttributes"]
            )
        )
    if data.get("ValidationData") is not None:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["validation_data"] = (
            capo_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["ValidationData"]
            )
        )
    if data.get("TemporaryPassword") is not None:
        out["temporary_password"] = data["TemporaryPassword"]
    if data.get("ForceAliasCreation") is not None:
        out["force_alias_creation"] = data["ForceAliasCreation"]
    else:
        out["force_alias_creation"] = False
    if data.get("MessageAction") is not None:
        import capo_cognito_identity_provider.types.message_action_type

        out["message_action"] = (
            capo_cognito_identity_provider.types.message_action_type.deserialize_aws_json_1_1(
                data["MessageAction"]
            )
        )
    if data.get("DesiredDeliveryMediums") is not None:
        import capo_cognito_identity_provider.types.delivery_medium_list_type

        out["desired_delivery_mediums"] = (
            capo_cognito_identity_provider.types.delivery_medium_list_type.deserialize_aws_json_1_1(
                data["DesiredDeliveryMediums"]
            )
        )
    if data.get("ClientMetadata") is not None:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["client_metadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.deserialize_aws_json_1_1(
                data["ClientMetadata"]
            )
        )
    return out
