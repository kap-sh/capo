"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminConfirmSignUpRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminConfirmSignUpRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to confirm a user's sign-up request.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminConfirmSignUpRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    if "client_metadata" in value:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["ClientMetadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.serialize_aws_json_1_1(
                value["client_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminConfirmSignUpRequest:
    out: AdminConfirmSignUpRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminConfirmSignUpRequest.user_pool_id required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminConfirmSignUpRequest.username required")
    if data.get("ClientMetadata") is not None:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["client_metadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.deserialize_aws_json_1_1(
                data["ClientMetadata"]
            )
        )
    return out
