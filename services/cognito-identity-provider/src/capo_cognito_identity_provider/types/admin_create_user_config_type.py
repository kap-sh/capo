"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminCreateUserConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.admin_create_user_unused_account_validity_days_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.message_template_type


class AdminCreateUserConfigType(TypedDict, closed=True):
    allow_admin_create_user_only: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>The setting for allowing self-service sign-up. When <code>true</code>, only administrators can create new user profiles. When <code>false</code>, users can register themselves and create a new user profile with the <code>SignUp</code> operation.</p>"""
    unused_account_validity_days: "capo_cognito_identity_provider.types.admin_create_user_unused_account_validity_days_type.AdminCreateUserUnusedAccountValidityDaysType"
    """<p>This parameter is no longer in use.</p> <p>The password expiration limit in days for administrator-created users. When this time expires, the user can't sign in with their temporary password. To reset the account after that time limit, you must call <code>AdminCreateUser</code> again, specifying <code>RESEND</code> for the <code>MessageAction</code> parameter. </p> <p>The default value for this parameter is 7.</p>"""
    invite_message_template: NotRequired[
        "capo_cognito_identity_provider.types.message_template_type.MessageTemplateType"
    ]
    """<p>The template for the welcome message to new users. This template must include the <code>{####}</code> temporary password placeholder if you are creating users with passwords. If your users don't have passwords, you can omit the placeholder.</p> <p>See also <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-message-customizations.html#cognito-user-pool-settings-user-invitation-message-customization">Customizing User Invitation Messages</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminCreateUserConfigType) -> dict:
    out: dict = {}
    out["AllowAdminCreateUserOnly"] = value.get("allow_admin_create_user_only", False)
    out["UnusedAccountValidityDays"] = value.get("unused_account_validity_days", 0)
    if "invite_message_template" in value:
        import capo_cognito_identity_provider.types.message_template_type

        out["InviteMessageTemplate"] = (
            capo_cognito_identity_provider.types.message_template_type.serialize_aws_json_1_1(
                value["invite_message_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminCreateUserConfigType:
    out: AdminCreateUserConfigType = {}  # type: ignore[typeddict-item]
    if data.get("AllowAdminCreateUserOnly") is not None:
        out["allow_admin_create_user_only"] = data["AllowAdminCreateUserOnly"]
    else:
        out["allow_admin_create_user_only"] = False
    if data.get("UnusedAccountValidityDays") is not None:
        out["unused_account_validity_days"] = data["UnusedAccountValidityDays"]
    else:
        out["unused_account_validity_days"] = 0
    if data.get("InviteMessageTemplate") is not None:
        import capo_cognito_identity_provider.types.message_template_type

        out["invite_message_template"] = (
            capo_cognito_identity_provider.types.message_template_type.deserialize_aws_json_1_1(
                data["InviteMessageTemplate"]
            )
        )
    return out
