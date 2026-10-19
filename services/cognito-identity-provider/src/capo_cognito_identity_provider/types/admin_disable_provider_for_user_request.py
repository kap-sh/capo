"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDisableProviderForUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.provider_user_identifier_type
    import capo_cognito_identity_provider.types.string_type


class AdminDisableProviderForUserRequest(TypedDict, closed=True):
    user_pool_id: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The ID of the user pool where you want to delete the user's linked identities.</p>"""
    user: "capo_cognito_identity_provider.types.provider_user_identifier_type.ProviderUserIdentifierType"
    """<p>The user profile that you want to delete a linked identity from.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDisableProviderForUserRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    import capo_cognito_identity_provider.types.provider_user_identifier_type

    out["User"] = (
        capo_cognito_identity_provider.types.provider_user_identifier_type.serialize_aws_json_1_1(
            value["user"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDisableProviderForUserRequest:
    out: AdminDisableProviderForUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("User") is not None:
        import capo_cognito_identity_provider.types.provider_user_identifier_type

        out["user"] = (
            capo_cognito_identity_provider.types.provider_user_identifier_type.deserialize_aws_json_1_1(
                data["User"]
            )
        )
    else:
        raise DeserializationError("AdminDisableProviderForUserRequest.user required")
    return out
