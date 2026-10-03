"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SignUpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.analytics_metadata_type
    import capo_cognito_identity_provider.types.attribute_list_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.password_type
    import capo_cognito_identity_provider.types.secret_hash_type
    import capo_cognito_identity_provider.types.user_context_data_type
    import capo_cognito_identity_provider.types.username_type


class SignUpRequest(TypedDict, closed=True):
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client where the user wants to sign up.</p>"""
    secret_hash: NotRequired[
        "capo_cognito_identity_provider.types.secret_hash_type.SecretHashType"
    ]
    """<p>A keyed-hash message authentication code (HMAC) calculated using the secret key of a user pool client and username plus the client ID in the message. For more information about <code>SecretHash</code>, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash">Computing secret hash values</a>.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The username of the user that you want to sign up. The value of this parameter is typically a username, but can be any alias attribute in your user pool.</p>"""
    password: NotRequired[
        "capo_cognito_identity_provider.types.password_type.PasswordType"
    ]
    """<p>The user's proposed password. The password must comply with the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/managing-users-passwords.html">password requirements</a> of your user pool.</p> <p>Users can sign up without a password when your user pool supports passwordless sign-in with email or SMS OTPs. To create a user with no password, omit this parameter or submit a blank value. You can only create a passwordless user when passwordless sign-in is available.</p>"""
    user_attributes: NotRequired[
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>An array of name-value pairs representing user attributes.</p> <p>For custom attributes, include a <code>custom:</code> prefix in the attribute name, for example <code>custom:department</code>.</p>"""
    validation_data: NotRequired[
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    ]
    """<p>Temporary user attributes that contribute to the outcomes of your pre sign-up Lambda trigger. This set of key-value pairs are for custom validation of information that you collect from your users but don't need to retain.</p> <p>Your Lambda function can analyze this additional data and act on it. Your function can automatically confirm and verify select users or perform external API operations like logging user attributes and validation data to Amazon CloudWatch Logs.</p> <p>For more information about the pre sign-up Lambda trigger, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html">Pre sign-up Lambda trigger</a>.</p>"""
    analytics_metadata: NotRequired[
        "capo_cognito_identity_provider.types.analytics_metadata_type.AnalyticsMetadataType"
    ]
    """<p>Information that supports analytics outcomes with Amazon Pinpoint, including the user's endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.</p>"""
    user_context_data: NotRequired[
        "capo_cognito_identity_provider.types.user_context_data_type.UserContextDataType"
    ]
    """<p>Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html">Collecting data for threat protection in applications</a>.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignUpRequest) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    if "secret_hash" in value:
        out["SecretHash"] = value["secret_hash"]
    out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
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
    if "analytics_metadata" in value:
        import capo_cognito_identity_provider.types.analytics_metadata_type

        out["AnalyticsMetadata"] = (
            capo_cognito_identity_provider.types.analytics_metadata_type.serialize_aws_json_1_1(
                value["analytics_metadata"]
            )
        )
    if "user_context_data" in value:
        import capo_cognito_identity_provider.types.user_context_data_type

        out["UserContextData"] = (
            capo_cognito_identity_provider.types.user_context_data_type.serialize_aws_json_1_1(
                value["user_context_data"]
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


def deserialize_aws_json_1_1(data: dict) -> SignUpRequest:
    out: SignUpRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("SignUpRequest.client_id required")
    if data.get("SecretHash") is not None:
        out["secret_hash"] = data["SecretHash"]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("SignUpRequest.username required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
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
    if data.get("AnalyticsMetadata") is not None:
        import capo_cognito_identity_provider.types.analytics_metadata_type

        out["analytics_metadata"] = (
            capo_cognito_identity_provider.types.analytics_metadata_type.deserialize_aws_json_1_1(
                data["AnalyticsMetadata"]
            )
        )
    if data.get("UserContextData") is not None:
        import capo_cognito_identity_provider.types.user_context_data_type

        out["user_context_data"] = (
            capo_cognito_identity_provider.types.user_context_data_type.deserialize_aws_json_1_1(
                data["UserContextData"]
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
