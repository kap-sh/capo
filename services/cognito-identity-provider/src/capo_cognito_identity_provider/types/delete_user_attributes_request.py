"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserAttributesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_name_list_type
    import capo_cognito_identity_provider.types.token_model_type


class DeleteUserAttributesRequest(TypedDict, closed=True):
    user_attribute_names: "capo_cognito_identity_provider.types.attribute_name_list_type.AttributeNameListType"
    """<p>An array of strings representing the user attribute names you want to delete.</p> <p>For custom attributes, you must prepend the <code>custom:</code> prefix to the attribute name, for example <code>custom:department</code>.</p>"""
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserAttributesRequest) -> dict:
    out: dict = {}
    import capo_cognito_identity_provider.types.attribute_name_list_type

    out["UserAttributeNames"] = (
        capo_cognito_identity_provider.types.attribute_name_list_type.serialize_aws_json_1_1(
            value["user_attribute_names"]
        )
    )
    out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserAttributesRequest:
    out: DeleteUserAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserAttributeNames") is not None:
        import capo_cognito_identity_provider.types.attribute_name_list_type

        out["user_attribute_names"] = (
            capo_cognito_identity_provider.types.attribute_name_list_type.deserialize_aws_json_1_1(
                data["UserAttributeNames"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteUserAttributesRequest.user_attribute_names required"
        )
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("DeleteUserAttributesRequest.access_token required")
    return out


def redact_sensitive(value: DeleteUserAttributesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
