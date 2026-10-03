"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminInitiateAuthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.authentication_result_type
    import capo_cognito_identity_provider.types.available_challenge_list_type
    import capo_cognito_identity_provider.types.challenge_name_type
    import capo_cognito_identity_provider.types.challenge_parameters_type
    import capo_cognito_identity_provider.types.session_type


class AdminInitiateAuthResponse(TypedDict, closed=True):
    challenge_name: NotRequired[
        "capo_cognito_identity_provider.types.challenge_name_type.ChallengeNameType"
    ]
    """<p>The name of the challenge that you're responding to with this call. This is returned in the <code>AdminInitiateAuth</code> response if you must pass another challenge.</p> <p>Possible challenges include the following:</p> <note> <p>All of the following challenges require <code>USERNAME</code> and, when the app client has a client secret, <code>SECRET_HASH</code> in the parameters. Include a <code>DEVICE_KEY</code> for device authentication.</p> </note> <ul> <li> <p> <code>WEB_AUTHN</code>: Respond to the challenge with the results of a successful authentication with a WebAuthn authenticator, or passkey, as <code>CREDENTIAL</code>. Examples of WebAuthn authenticators include biometric devices and security keys.</p> </li> <li> <p> <code>PASSWORD</code>: Respond with the user's password as <code>PASSWORD</code>.</p> </li> <li> <p> <code>PASSWORD_SRP</code>: Respond with the initial SRP secret as <code>SRP_A</code>.</p> </li> <li> <p> <code>SELECT_CHALLENGE</code>: Respond with a challenge selection as <code>ANSWER</code>. It must be one of the challenge types in the <code>AvailableChallenges</code> response parameter. Add the parameters of the selected challenge, for example <code>USERNAME</code> and <code>SMS_OTP</code>.</p> </li> <li> <p> <code>SMS_MFA</code>: Respond with the code that your user pool delivered in an SMS message, as <code>SMS_MFA_CODE</code> </p> </li> <li> <p> <code>EMAIL_MFA</code>: Respond with the code that your user pool delivered in an email message, as <code>EMAIL_MFA_CODE</code> </p> </li> <li> <p> <code>EMAIL_OTP</code>: Respond with the code that your user pool delivered in an email message, as <code>EMAIL_OTP_CODE</code> .</p> </li> <li> <p> <code>SMS_OTP</code>: Respond with the code that your user pool delivered in an SMS message, as <code>SMS_OTP_CODE</code>.</p> </li> <li> <p> <code>PASSWORD_VERIFIER</code>: Respond with the second stage of SRP secrets as <code>PASSWORD_CLAIM_SIGNATURE</code>, <code>PASSWORD_CLAIM_SECRET_BLOCK</code>, and <code>TIMESTAMP</code>.</p> </li> <li> <p> <code>CUSTOM_CHALLENGE</code>: This is returned if your custom authentication flow determines that the user should pass another challenge before tokens are issued. The parameters of the challenge are determined by your Lambda function and issued in the <code>ChallengeParameters</code> of a challenge response.</p> </li> <li> <p> <code>DEVICE_SRP_AUTH</code>: Respond with the initial parameters of device SRP authentication. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device">Signing in with a device</a>.</p> </li> <li> <p> <code>DEVICE_PASSWORD_VERIFIER</code>: Respond with <code>PASSWORD_CLAIM_SIGNATURE</code>, <code>PASSWORD_CLAIM_SECRET_BLOCK</code>, and <code>TIMESTAMP</code> after client-side SRP calculations. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html#user-pools-remembered-devices-signing-in-with-a-device">Signing in with a device</a>.</p> </li> <li> <p> <code>NEW_PASSWORD_REQUIRED</code>: For users who are required to change their passwords after successful first login. Respond to this challenge with <code>NEW_PASSWORD</code> and any required attributes that Amazon Cognito returned in the <code>requiredAttributes</code> parameter. You can also set values for attributes that aren't required by your user pool and that your app client can write.</p> <p>Amazon Cognito only returns this challenge for users who have temporary passwords. When you create passwordless users, you must provide values for all required attributes.</p> <note> <p>In a <code>NEW_PASSWORD_REQUIRED</code> challenge response, you can't modify a required attribute that already has a value. In <code>AdminRespondToAuthChallenge</code> or <code>RespondToAuthChallenge</code>, set a value for any keys that Amazon Cognito returned in the <code>requiredAttributes</code> parameter, then use the <code>AdminUpdateUserAttributes</code> or <code>UpdateUserAttributes</code> API operation to modify the value of any additional attributes.</p> </note> </li> <li> <p> <code>MFA_SETUP</code>: For users who are required to setup an MFA factor before they can sign in. The MFA types activated for the user pool will be listed in the challenge parameters <code>MFAS_CAN_SETUP</code> value. </p> <p>To set up time-based one-time password (TOTP) MFA, use the session returned in this challenge from <code>InitiateAuth</code> or <code>AdminInitiateAuth</code> as an input to <code>AssociateSoftwareToken</code>. Then, use the session returned by <code>VerifySoftwareToken</code> as an input to <code>RespondToAuthChallenge</code> or <code>AdminRespondToAuthChallenge</code> with challenge name <code>MFA_SETUP</code> to complete sign-in. </p> <p>To set up SMS or email MFA, collect a <code>phone_number</code> or <code>email</code> attribute for the user. Then restart the authentication flow with an <code>InitiateAuth</code> or <code>AdminInitiateAuth</code> request. </p> </li> </ul>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The session that must be passed to challenge-response requests. If an <code>AdminInitiateAuth</code> or <code>AdminRespondToAuthChallenge</code> API request results in another authentication challenge, Amazon Cognito returns a session ID and the parameters of the next challenge. Pass this session ID in the <code>Session</code> parameter of <code>AdminRespondToAuthChallenge</code>.</p>"""
    challenge_parameters: NotRequired[
        "capo_cognito_identity_provider.types.challenge_parameters_type.ChallengeParametersType"
    ]
    """<p>The parameters of an authentication challenge. Amazon Cognito returns challenge parameters as a guide to the responses your user or application must provide for the returned <code>ChallengeName</code>. Calculate responses to the challenge parameters and pass them in the <code>ChallengeParameters</code> of <code>AdminRespondToAuthChallenge</code>.</p> <p>All challenges require <code>USERNAME</code> and, when the app client has a client secret, <code>SECRET_HASH</code>.</p> <p>In SRP challenges, Amazon Cognito returns the <code>username</code> attribute in <code>USER_ID_FOR_SRP</code> instead of any email address, preferred username, or phone number alias that you might have specified in your <code>AdminInitiateAuth</code> request. You must use the username and not an alias in the <code>ChallengeResponses</code> of your challenge response.</p>"""
    authentication_result: NotRequired[
        "capo_cognito_identity_provider.types.authentication_result_type.AuthenticationResultType"
    ]
    """<p>The outcome of successful authentication. This is only returned if the user pool has no additional challenges to return. If Amazon Cognito returns another challenge, the response includes <code>ChallengeName</code>, <code>ChallengeParameters</code>, and <code>Session</code> so that your user can answer the challenge.</p>"""
    available_challenges: NotRequired[
        "capo_cognito_identity_provider.types.available_challenge_list_type.AvailableChallengeListType"
    ]
    """<p>This response parameter lists the available authentication challenges that users can select from in <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice">choice-based authentication</a>. For example, they might be able to choose between passkey authentication, a one-time password from an SMS message, and a traditional password.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminInitiateAuthResponse) -> dict:
    out: dict = {}
    if "challenge_name" in value:
        import capo_cognito_identity_provider.types.challenge_name_type

        out["ChallengeName"] = (
            capo_cognito_identity_provider.types.challenge_name_type.serialize_aws_json_1_1(
                value["challenge_name"]
            )
        )
    if "session" in value:
        out["Session"] = value["session"]
    if "challenge_parameters" in value:
        import capo_cognito_identity_provider.types.challenge_parameters_type

        out["ChallengeParameters"] = (
            capo_cognito_identity_provider.types.challenge_parameters_type.serialize_aws_json_1_1(
                value["challenge_parameters"]
            )
        )
    if "authentication_result" in value:
        import capo_cognito_identity_provider.types.authentication_result_type

        out["AuthenticationResult"] = (
            capo_cognito_identity_provider.types.authentication_result_type.serialize_aws_json_1_1(
                value["authentication_result"]
            )
        )
    if "available_challenges" in value:
        import capo_cognito_identity_provider.types.available_challenge_list_type

        out["AvailableChallenges"] = (
            capo_cognito_identity_provider.types.available_challenge_list_type.serialize_aws_json_1_1(
                value["available_challenges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminInitiateAuthResponse:
    out: AdminInitiateAuthResponse = {}  # type: ignore[typeddict-item]
    if data.get("ChallengeName") is not None:
        import capo_cognito_identity_provider.types.challenge_name_type

        out["challenge_name"] = (
            capo_cognito_identity_provider.types.challenge_name_type.deserialize_aws_json_1_1(
                data["ChallengeName"]
            )
        )
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    if data.get("ChallengeParameters") is not None:
        import capo_cognito_identity_provider.types.challenge_parameters_type

        out["challenge_parameters"] = (
            capo_cognito_identity_provider.types.challenge_parameters_type.deserialize_aws_json_1_1(
                data["ChallengeParameters"]
            )
        )
    if data.get("AuthenticationResult") is not None:
        import capo_cognito_identity_provider.types.authentication_result_type

        out["authentication_result"] = (
            capo_cognito_identity_provider.types.authentication_result_type.deserialize_aws_json_1_1(
                data["AuthenticationResult"]
            )
        )
    if data.get("AvailableChallenges") is not None:
        import capo_cognito_identity_provider.types.available_challenge_list_type

        out["available_challenges"] = (
            capo_cognito_identity_provider.types.available_challenge_list_type.deserialize_aws_json_1_1(
                data["AvailableChallenges"]
            )
        )
    return out
