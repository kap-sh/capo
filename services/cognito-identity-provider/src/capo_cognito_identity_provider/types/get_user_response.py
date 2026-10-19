"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.attribute_list_type
    import capo_cognito_identity_provider.types.mfa_option_list_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.user_mfa_setting_list_type
    import capo_cognito_identity_provider.types.username_type


class GetUserResponse(TypedDict, closed=True):
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you requested.</p>"""
    user_attributes: (
        "capo_cognito_identity_provider.types.attribute_list_type.AttributeListType"
    )
    """<p>An array of name-value pairs representing user attributes.</p> <p>Custom attributes are prepended with the <code>custom:</code> prefix.</p>"""
    mfa_options: NotRequired[
        "capo_cognito_identity_provider.types.mfa_option_list_type.MFAOptionListType"
    ]
    """<p> <i>This response parameter is no longer supported.</i> It provides information only about SMS MFA configurations. It doesn't provide information about time-based one-time password (TOTP) software token MFA configurations. To look up information about either type of MFA configuration, use UserMFASettingList instead.</p>"""
    preferred_mfa_setting: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The user's preferred MFA. Users can prefer SMS message, email message, or TOTP MFA.</p>"""
    user_mfa_setting_list: NotRequired[
        "capo_cognito_identity_provider.types.user_mfa_setting_list_type.UserMFASettingListType"
    ]
    """<p>The MFA options that are activated for the user. The possible values in this list are <code>SMS_MFA</code>, <code>EMAIL_OTP</code>, and <code>SOFTWARE_TOKEN_MFA</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserResponse) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    import capo_cognito_identity_provider.types.attribute_list_type

    out["UserAttributes"] = (
        capo_cognito_identity_provider.types.attribute_list_type.serialize_aws_json_1_1(
            value["user_attributes"]
        )
    )
    if "mfa_options" in value:
        import capo_cognito_identity_provider.types.mfa_option_list_type

        out["MFAOptions"] = (
            capo_cognito_identity_provider.types.mfa_option_list_type.serialize_aws_json_1_1(
                value["mfa_options"]
            )
        )
    if "preferred_mfa_setting" in value:
        out["PreferredMfaSetting"] = value["preferred_mfa_setting"]
    if "user_mfa_setting_list" in value:
        import capo_cognito_identity_provider.types.user_mfa_setting_list_type

        out["UserMFASettingList"] = (
            capo_cognito_identity_provider.types.user_mfa_setting_list_type.serialize_aws_json_1_1(
                value["user_mfa_setting_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    if data.get("UserAttributes") is not None:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["user_attributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.deserialize_aws_json_1_1(
                data["UserAttributes"]
            )
        )
    else:
        out["user_attributes"] = []
    if data.get("MFAOptions") is not None:
        import capo_cognito_identity_provider.types.mfa_option_list_type

        out["mfa_options"] = (
            capo_cognito_identity_provider.types.mfa_option_list_type.deserialize_aws_json_1_1(
                data["MFAOptions"]
            )
        )
    if data.get("PreferredMfaSetting") is not None:
        out["preferred_mfa_setting"] = data["PreferredMfaSetting"]
    if data.get("UserMFASettingList") is not None:
        import capo_cognito_identity_provider.types.user_mfa_setting_list_type

        out["user_mfa_setting_list"] = (
            capo_cognito_identity_provider.types.user_mfa_setting_list_type.deserialize_aws_json_1_1(
                data["UserMFASettingList"]
            )
        )
    return out


def redact_sensitive(value: GetUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "user_attributes" in value:
        import capo_cognito_identity_provider.types.attribute_list_type

        out["user_attributes"] = (
            capo_cognito_identity_provider.types.attribute_list_type.redact_sensitive(
                value["user_attributes"]
            )
        )
    return out
