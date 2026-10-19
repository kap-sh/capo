"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserSettingsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.mfa_option_list_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminSetUserSettingsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the user whose options you're setting.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    mfa_options: (
        "capo_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    )
    """<p>You can use this parameter only to set an SMS configuration that uses SMS for delivery.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserSettingsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    import capo_cognito_identity_provider.types.mfa_option_list_type

    out["MFAOptions"] = (
        capo_cognito_identity_provider.types.mfa_option_list_type.serialize_aws_json_1_1(
            value["mfa_options"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserSettingsRequest:
    out: AdminSetUserSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("MFAOptions") is not None:
        import capo_cognito_identity_provider.types.mfa_option_list_type

        out["mfa_options"] = (
            capo_cognito_identity_provider.types.mfa_option_list_type.deserialize_aws_json_1_1(
                data["MFAOptions"]
            )
        )
    else:
        out["mfa_options"] = []
    return out


def redact_sensitive(value: AdminSetUserSettingsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
