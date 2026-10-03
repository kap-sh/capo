"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SignUpResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.code_delivery_details_type
    import capo_cognito_identity_provider.types.session_type
    import capo_cognito_identity_provider.types.string_type


class SignUpResponse(TypedDict, closed=True):
    user_confirmed: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Indicates whether the user was automatically confirmed. You can auto-confirm users with a <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html">pre sign-up Lambda trigger</a>.</p>"""
    code_delivery_details: NotRequired[
        "capo_cognito_identity_provider.types.code_delivery_details_type.CodeDeliveryDetailsType"
    ]
    """<p>In user pools that automatically verify and confirm new users, Amazon Cognito sends users a message with a code or link that confirms ownership of the phone number or email address that they entered. The <code>CodeDeliveryDetails</code> object is information about the delivery destination for that link or code.</p>"""
    user_sub: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The unique identifier of the new user, for example <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>A session Id that you can pass to <code>ConfirmSignUp</code> when you want to immediately sign in your user with the <code>USER_AUTH</code> flow after they complete sign-up.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SignUpResponse) -> dict:
    out: dict = {}
    out["UserConfirmed"] = value.get("user_confirmed", False)
    if "code_delivery_details" in value:
        import capo_cognito_identity_provider.types.code_delivery_details_type

        out["CodeDeliveryDetails"] = (
            capo_cognito_identity_provider.types.code_delivery_details_type.serialize_aws_json_1_1(
                value["code_delivery_details"]
            )
        )
    out["UserSub"] = value["user_sub"]
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SignUpResponse:
    out: SignUpResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserConfirmed") is not None:
        out["user_confirmed"] = data["UserConfirmed"]
    else:
        out["user_confirmed"] = False
    if data.get("CodeDeliveryDetails") is not None:
        import capo_cognito_identity_provider.types.code_delivery_details_type

        out["code_delivery_details"] = (
            capo_cognito_identity_provider.types.code_delivery_details_type.deserialize_aws_json_1_1(
                data["CodeDeliveryDetails"]
            )
        )
    if data.get("UserSub") is not None:
        out["user_sub"] = data["UserSub"]
    else:
        raise DeserializationError("SignUpResponse.user_sub required")
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    return out
