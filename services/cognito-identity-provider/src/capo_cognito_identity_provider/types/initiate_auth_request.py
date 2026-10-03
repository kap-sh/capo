"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InitiateAuthRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.analytics_metadata_type
    import capo_cognito_identity_provider.types.auth_flow_type
    import capo_cognito_identity_provider.types.auth_parameters_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_metadata_type
    import capo_cognito_identity_provider.types.session_type
    import capo_cognito_identity_provider.types.user_context_data_type


class InitiateAuthRequest(TypedDict, closed=True):
    auth_flow: "capo_cognito_identity_provider.types.auth_flow_type.AuthFlowType"
    """<p>The authentication flow that you want to initiate. Each <code>AuthFlow</code> has linked <code>AuthParameters</code> that you must submit. The following are some example flows.</p> <dl> <dt>USER_AUTH</dt> <dd> <p>The entry point for <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice">choice-based authentication</a> with passwords, one-time passwords, and WebAuthn authenticators. Request a preferred authentication type or review available authentication types. From the offered authentication types, select one in a challenge response and then authenticate with that method in an additional challenge response. To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p> </dd> <dt>USER_SRP_AUTH</dt> <dd> <p>Username-password authentication with the Secure Remote Password (SRP) protocol. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow.html#Using-SRP-password-verification-in-custom-authentication-flow">Use SRP password verification in custom authentication flow</a>.</p> </dd> <dt>REFRESH_TOKEN_AUTH and REFRESH_TOKEN</dt> <dd> <p>Receive new ID and access tokens when you pass a <code>REFRESH_TOKEN</code> parameter with a valid refresh token as the value. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html">Using the refresh token</a>.</p> </dd> <dt>CUSTOM_AUTH</dt> <dd> <p>Custom authentication with Lambda triggers. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html">Custom authentication challenge Lambda triggers</a>.</p> </dd> <dt>USER_PASSWORD_AUTH</dt> <dd> <p>Client-side username-password authentication with the password sent directly in the request. For more information about client-side and server-side authentication, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-public-server-side.html">SDK authorization models</a>.</p> </dd> </dl> <p> <code>ADMIN_USER_PASSWORD_AUTH</code> is a flow type of <code>AdminInitiateAuth</code> and isn't valid for InitiateAuth. <code>ADMIN_NO_SRP_AUTH</code> is a legacy server-side username-password flow and isn't valid for InitiateAuth.</p>"""
    auth_parameters: NotRequired[
        "capo_cognito_identity_provider.types.auth_parameters_type.AuthParametersType"
    ]
    """<p>The authentication parameters. These are inputs corresponding to the <code>AuthFlow</code> that you're invoking.</p> <p>The following are some authentication flows and their parameters. Add a <code>SECRET_HASH</code> parameter if your app client has a client secret. Add <code>DEVICE_KEY</code> if you want to bypass multi-factor authentication with a remembered device. </p> <dl> <dt>USER_AUTH</dt> <dd> <ul> <li> <p> <code>USERNAME</code> (required)</p> </li> <li> <p> <code>PREFERRED_CHALLENGE</code>. If you don't provide a value for <code>PREFERRED_CHALLENGE</code>, Amazon Cognito responds with the <code>AvailableChallenges</code> parameter that specifies the available sign-in methods.</p> </li> </ul> </dd> <dt>USER_SRP_AUTH</dt> <dd> <ul> <li> <p> <code>USERNAME</code> (required)</p> </li> <li> <p> <code>SRP_A</code> (required)</p> </li> </ul> </dd> <dt>USER_PASSWORD_AUTH</dt> <dd> <ul> <li> <p> <code>USERNAME</code> (required)</p> </li> <li> <p> <code>PASSWORD</code> (required)</p> </li> </ul> </dd> <dt>REFRESH_TOKEN_AUTH/REFRESH_TOKEN</dt> <dd> <ul> <li> <p> <code>REFRESH_TOKEN</code>(required)</p> </li> </ul> </dd> <dt>CUSTOM_AUTH</dt> <dd> <ul> <li> <p> <code>USERNAME</code> (required)</p> </li> <li> <p> <code>ChallengeName: SRP_A</code> (when doing SRP authentication before custom challenges)</p> </li> <li> <p> <code>SRP_A: (An SRP_A value)</code> (when doing SRP authentication before custom challenges)</p> </li> </ul> </dd> </dl> <p>For more information about <code>SECRET_HASH</code>, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#cognito-user-pools-computing-secret-hash">Computing secret hash values</a>. For information about <code>DEVICE_KEY</code>, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html">Working with user devices in your user pool</a>.</p>"""
    client_metadata: NotRequired[
        "capo_cognito_identity_provider.types.client_metadata_type.ClientMetadataType"
    ]
    """<p>A map of custom key-value pairs that you can provide as input for any custom workflows that this action triggers. You create custom workflows by assigning Lambda functions to user pool triggers.</p> <p>When Amazon Cognito invokes any of these functions, it passes a JSON payload, which the function receives as input. This payload contains a <code>clientMetadata</code> attribute that provides the data that you assigned to the ClientMetadata parameter in your request. In your function code, you can process the <code>clientMetadata</code> value to enhance your workflow for your specific needs.</p> <p>To review the Lambda trigger types that Amazon Cognito invokes at runtime with API requests, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html#lambda-triggers-by-event"> Connecting API actions to Lambda triggers</a> in the <i>Amazon Cognito Developer Guide</i>.</p> <p>The <code>ClientMetadata</code> value is passed as input to the functions for only the following triggers:</p> <ul> <li> <p>Pre signup</p> </li> <li> <p>Pre authentication</p> </li> <li> <p>User migration</p> </li> </ul> <p>This request also invokes the functions for the following triggers, but doesn't pass <code>ClientMetadata</code>:</p> <ul> <li> <p>Post authentication</p> </li> <li> <p>Custom message</p> </li> <li> <p>Pre token generation</p> </li> <li> <p>Create auth challenge</p> </li> <li> <p>Define auth challenge</p> </li> <li> <p>Custom email sender</p> </li> <li> <p>Custom SMS sender</p> </li> </ul> <note> <p>When you use the <code>ClientMetadata</code> parameter, note that Amazon Cognito won't do the following:</p> <ul> <li> <p>Store the <code>ClientMetadata</code> value. This data is available only to Lambda triggers that are assigned to a user pool to support custom workflows. If your user pool configuration doesn't include triggers, the <code>ClientMetadata</code> parameter serves no purpose.</p> </li> <li> <p>Validate the <code>ClientMetadata</code> value.</p> </li> <li> <p>Encrypt the <code>ClientMetadata</code> value. Don't send sensitive information in this parameter.</p> </li> </ul> </note>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that your user wants to sign in to.</p>"""
    analytics_metadata: NotRequired[
        "capo_cognito_identity_provider.types.analytics_metadata_type.AnalyticsMetadataType"
    ]
    """<p>Information that supports analytics outcomes with Amazon Pinpoint, including the user's endpoint ID. The endpoint ID is a destination for Amazon Pinpoint push notifications, for example a device identifier, email address, or phone number.</p>"""
    user_context_data: NotRequired[
        "capo_cognito_identity_provider.types.user_context_data_type.UserContextDataType"
    ]
    """<p>Contextual data about your user session like the device fingerprint, IP address, or location. Amazon Cognito threat protection evaluates the risk of an authentication event based on the context that your app generates and passes to Amazon Cognito when it makes API requests.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-viewing-threat-protection-app.html">Collecting data for threat protection in applications</a>.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The optional session ID from a <code>ConfirmSignUp</code> API request. You can sign in a user directly from the sign-up process with the <code>USER_AUTH</code> authentication flow. When you pass the session ID to <code>InitiateAuth</code>, Amazon Cognito assumes the SMS or email message one-time verification password from <code>ConfirmSignUp</code> as the primary authentication factor. You're not required to submit this code a second time. This option is only valid for users who have confirmed their sign-up and are signing in for the first time within the authentication flow session duration of the session ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InitiateAuthRequest) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.auth_flow_type

    out["AuthFlow"] = (
        capo_cognito_identity_provider.types.auth_flow_type.serialize_aws_json_1_1(
            value["auth_flow"]
        )
    )
    if "auth_parameters" in value:
        import capo_cognito_identity_provider.types.auth_parameters_type

        out["AuthParameters"] = (
            capo_cognito_identity_provider.types.auth_parameters_type.serialize_aws_json_1_1(
                value["auth_parameters"]
            )
        )
    if "client_metadata" in value:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["ClientMetadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.serialize_aws_json_1_1(
                value["client_metadata"]
            )
        )
    out["ClientId"] = value["client_id"]
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
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InitiateAuthRequest:
    out: InitiateAuthRequest = {}  # type: ignore[typeddict-item]
    if data.get("AuthFlow") is not None:
        import capo_cognito_identity_provider.types.auth_flow_type

        out["auth_flow"] = (
            capo_cognito_identity_provider.types.auth_flow_type.deserialize_aws_json_1_1(
                data["AuthFlow"]
            )
        )
    else:
        raise DeserializationError("InitiateAuthRequest.auth_flow required")
    if data.get("AuthParameters") is not None:
        import capo_cognito_identity_provider.types.auth_parameters_type

        out["auth_parameters"] = (
            capo_cognito_identity_provider.types.auth_parameters_type.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    if data.get("ClientMetadata") is not None:
        import capo_cognito_identity_provider.types.client_metadata_type

        out["client_metadata"] = (
            capo_cognito_identity_provider.types.client_metadata_type.deserialize_aws_json_1_1(
                data["ClientMetadata"]
            )
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("InitiateAuthRequest.client_id required")
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
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    return out
