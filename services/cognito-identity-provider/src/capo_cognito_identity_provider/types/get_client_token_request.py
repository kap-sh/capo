"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetClientTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.client_secret_type
    import capo_cognito_identity_provider.types.scope_list_type


class GetClientTokenRequest(TypedDict, closed=True):
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that requests the access token. The app client must have a client secret and the <code>ALLOW_CLIENT_TOKEN_AUTH</code> authentication flow.</p>"""
    secret: "capo_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    """<p>An active secret for the app client.</p>"""
    scopes: NotRequired[
        "capo_cognito_identity_provider.types.scope_list_type.ScopeListType"
    ]
    """<p>The custom scopes to authorize in the access token, in the format <code>resource-server-identifier/scope-name</code>. Each scope must belong to a resource server in your user pool. If you don't specify any scopes, Amazon Cognito authorizes the scopes that are configured for the app client.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClientTokenRequest) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["Secret"] = value["secret"]
    if "scopes" in value:
        import capo_cognito_identity_provider.types.scope_list_type

        out["Scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
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


def deserialize_aws_json_1_1(data: dict) -> GetClientTokenRequest:
    out: GetClientTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("GetClientTokenRequest.client_id required")
    if data.get("Secret") is not None:
        out["secret"] = data["Secret"]
    else:
        raise DeserializationError("GetClientTokenRequest.secret required")
    if data.get("Scopes") is not None:
        import capo_cognito_identity_provider.types.scope_list_type

        out["scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
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
