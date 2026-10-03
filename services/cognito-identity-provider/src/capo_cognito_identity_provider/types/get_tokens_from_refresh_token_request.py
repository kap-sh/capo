"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetTokensFromRefreshTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.client_secret_type
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.token_model_type


class GetTokensFromRefreshTokenRequest(TypedDict, closed=True):
    refresh_token: (
        "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    )
    """<p>A valid refresh token that can authorize the request for new tokens. When refresh token rotation is active in the requested app client, this token is invalidated after the request is complete and after an optional grace period.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The app client that issued the refresh token to the user who wants to request new tokens.</p>"""
    client_secret: NotRequired[
        "capo_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The client secret of the requested app client, if the client has a secret.</p>"""
    device_key: NotRequired[
        "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    ]
    """<p>When you enable device remembering, Amazon Cognito issues a device key that you can use for device authentication that bypasses multi-factor authentication (MFA). To implement <code>GetTokensFromRefreshToken</code> in a user pool with device remembering, you must capture the device key from the initial authentication request. If your application doesn't provide the key of a registered device, Amazon Cognito issues a new one. You must provide the confirmed device key in this request if device remembering is enabled in your user pool.</p> <p>For more information about device remembering, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html">Working with devices</a>.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTokensFromRefreshTokenRequest) -> dict:
    out: dict = {}
    out["RefreshToken"] = value["refresh_token"]
    out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "device_key" in value:
        out["DeviceKey"] = value["device_key"]
    if "client_metadata" in value:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["ClientMetadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.serialize_aws_json_1_1(
                value["client_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTokensFromRefreshTokenRequest:
    out: GetTokensFromRefreshTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("RefreshToken") is not None:
        out["refresh_token"] = data["RefreshToken"]
    else:
        raise DeserializationError(
            "GetTokensFromRefreshTokenRequest.refresh_token required"
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "GetTokensFromRefreshTokenRequest.client_id required"
        )
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("DeviceKey") is not None:
        out["device_key"] = data["DeviceKey"]
    if data.get("ClientMetadata") is not None:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["client_metadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.deserialize_aws_json_1_1(
                data["ClientMetadata"]
            )
        )
    return out
