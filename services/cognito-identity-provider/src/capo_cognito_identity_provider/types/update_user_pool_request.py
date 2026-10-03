"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_recovery_setting_type
    import capo_cognito_identity_provider.types.admin_create_user_config_type
    import capo_cognito_identity_provider.types.deletion_protection_type
    import capo_cognito_identity_provider.types.device_configuration_type
    import capo_cognito_identity_provider.types.email_configuration_type
    import capo_cognito_identity_provider.types.email_verification_message_type
    import capo_cognito_identity_provider.types.email_verification_subject_type
    import capo_cognito_identity_provider.types.issuer_configuration_type
    import capo_cognito_identity_provider.types.key_configuration_type
    import capo_cognito_identity_provider.types.lambda_config_type
    import capo_cognito_identity_provider.types.sms_configuration_type
    import capo_cognito_identity_provider.types.sms_verification_message_type
    import capo_cognito_identity_provider.types.user_attribute_update_settings_type
    import capo_cognito_identity_provider.types.user_pool_add_ons_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.user_pool_mfa_type
    import capo_cognito_identity_provider.types.user_pool_name_type
    import capo_cognito_identity_provider.types.user_pool_policy_type
    import capo_cognito_identity_provider.types.user_pool_tags_type
    import capo_cognito_identity_provider.types.user_pool_tier_type
    import capo_cognito_identity_provider.types.verification_message_template_type
    import capo_cognito_identity_provider.types.verified_attributes_list_type


class UpdateUserPoolRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool you want to update.</p>"""
    policies: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_policy_type.UserPoolPolicyType"
    ]
    """<p>The password policy and sign-in policy in the user pool. The password policy sets options like password complexity requirements and password history. The sign-in policy sets the options available to applications in <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice">choice-based authentication</a>.</p>"""
    deletion_protection: NotRequired[
        "capo_cognito_identity_provider.types.deletion_protection_type.DeletionProtectionType"
    ]
    """<p>When active, <code>DeletionProtection</code> prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.</p> <p>When you try to delete a protected user pool in a <code>DeleteUserPool</code> API request, Amazon Cognito returns an <code>InvalidParameterException</code> error. To delete a protected user pool, send a new <code>DeleteUserPool</code> request after you deactivate deletion protection in an <code>UpdateUserPool</code> API request.</p>"""
    lambda_config: NotRequired[
        "capo_cognito_identity_provider.types.lambda_config_type.LambdaConfigType"
    ]
    """<p>A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.</p>"""
    auto_verified_attributes: NotRequired[
        "capo_cognito_identity_provider.types.verified_attributes_list_type.VerifiedAttributesListType"
    ]
    """<p>The attributes that you want your user pool to automatically verify. Possible values: <b>email</b>, <b>phone_number</b>. For more information see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#allowing-users-to-sign-up-and-confirm-themselves">Verifying contact information at sign-up</a>.</p>"""
    sms_verification_message: NotRequired[
        "capo_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>This parameter is no longer used.</p>"""
    email_verification_message: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_message_type.EmailVerificationMessageType"
    ]
    """<p>This parameter is no longer used.</p>"""
    email_verification_subject: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_subject_type.EmailVerificationSubjectType"
    ]
    """<p>This parameter is no longer used.</p>"""
    verification_message_template: NotRequired[
        "capo_cognito_identity_provider.types.verification_message_template_type.VerificationMessageTemplateType"
    ]
    """<p>The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.</p> <p>Set the email message type that corresponds to your <code>DefaultEmailOption</code> selection. For <code>CONFIRM_WITH_LINK</code>, specify an <code>EmailMessageByLink</code> and leave <code>EmailMessage</code> blank. For <code>CONFIRM_WITH_CODE</code>, specify an <code>EmailMessage</code> and leave <code>EmailMessageByLink</code> blank. When you supply both parameters with either choice, Amazon Cognito returns an error.</p>"""
    sms_authentication_message: NotRequired[
        "capo_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>The contents of the SMS message that your user pool sends to users in SMS authentication.</p>"""
    user_attribute_update_settings: NotRequired[
        "capo_cognito_identity_provider.types.user_attribute_update_settings_type.UserAttributeUpdateSettingsType"
    ]
    """<p>The settings for updates to user attributes. These settings include the property <code>AttributesRequireVerificationBeforeUpdate</code>, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates"> Verifying updates to email addresses and phone numbers</a>.</p>"""
    mfa_configuration: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_mfa_type.UserPoolMfaType"
    ]
    """<p>Sets multi-factor authentication (MFA) to be on, off, or optional. When <code>ON</code>, all users must set up MFA before they can sign in. When <code>OPTIONAL</code>, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose <code>OPTIONAL</code>.</p> <p>When <code>MfaConfiguration</code> is <code>OPTIONAL</code>, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.</p>"""
    device_configuration: NotRequired[
        "capo_cognito_identity_provider.types.device_configuration_type.DeviceConfigurationType"
    ]
    """<p>The device-remembering configuration for a user pool. Device remembering or device tracking is a "Remember me on this device" option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html">Working with user devices in your user pool</a>. A null value indicates that you have deactivated device remembering in your user pool.</p> <note> <p>When you provide a value for any <code>DeviceConfiguration</code> field, you activate the Amazon Cognito device-remembering feature. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html">Working with devices</a>.</p> </note>"""
    email_configuration: NotRequired[
        "capo_cognito_identity_provider.types.email_configuration_type.EmailConfigurationType"
    ]
    """<p>The email configuration of your user pool. The email configuration type sets your preferred sending method, Amazon Web Services Region, and sender for email invitation and verification messages from your user pool.</p>"""
    sms_configuration: NotRequired[
        "capo_cognito_identity_provider.types.sms_configuration_type.SmsConfigurationType"
    ]
    """<p>The SMS configuration with the settings for your Amazon Cognito user pool to send SMS message with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account. For more information see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html">SMS message settings</a>.</p>"""
    user_pool_tags: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    ]
    """<p>The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.</p>"""
    admin_create_user_config: NotRequired[
        "capo_cognito_identity_provider.types.admin_create_user_config_type.AdminCreateUserConfigType"
    ]
    """<p>The configuration for administrative creation of users. Includes the template for the invitation message for new users, the duration of temporary passwords, and permitting self-service sign-up.</p>"""
    user_pool_add_ons: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_add_ons_type.UserPoolAddOnsType"
    ]
    """<p>Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to <code>AUDIT</code>. To configure automatic security responses to potentially unwanted traffic to your user pool, set to <code>ENFORCED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html">Adding advanced security to a user pool</a>. To activate this setting, your user pool must be on the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html"> Plus tier</a>.</p>"""
    account_recovery_setting: NotRequired[
        "capo_cognito_identity_provider.types.account_recovery_setting_type.AccountRecoverySettingType"
    ]
    """<p>The available verified method a user can use to recover their password when they call <code>ForgotPassword</code>. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.</p>"""
    pool_name: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_name_type.UserPoolNameType"
    ]
    """<p>The updated name of your user pool.</p>"""
    user_pool_tier: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_tier_type.UserPoolTierType"
    ]
    """<p>The user pool <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html">feature plan</a>, or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to <code>ESSENTIALS</code>.</p>"""
    key_configuration: NotRequired[
        "capo_cognito_identity_provider.types.key_configuration_type.KeyConfigurationType"
    ]
    """<p>The key configuration for the user pool. In secondary regions, this parameter must match the existing configuration and cannot be modified.</p>"""
    issuer_configuration: NotRequired[
        "capo_cognito_identity_provider.types.issuer_configuration_type.IssuerConfigurationType"
    ]
    """<p>The issuer configuration for the user pool. In secondary regions, this parameter must match the existing configuration and cannot be modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "policies" in value:
        import capo_cognito_identity_provider.types.user_pool_policy_type

        out["Policies"] = (
            capo_cognito_identity_provider.types.user_pool_policy_type.serialize_aws_json_1_1(
                value["policies"]
            )
        )
    if "deletion_protection" in value:
        import capo_cognito_identity_provider.types.deletion_protection_type

        out["DeletionProtection"] = (
            capo_cognito_identity_provider.types.deletion_protection_type.serialize_aws_json_1_1(
                value["deletion_protection"]
            )
        )
    if "lambda_config" in value:
        import capo_cognito_identity_provider.types.lambda_config_type

        out["LambdaConfig"] = (
            capo_cognito_identity_provider.types.lambda_config_type.serialize_aws_json_1_1(
                value["lambda_config"]
            )
        )
    if "auto_verified_attributes" in value:
        import capo_cognito_identity_provider.types.verified_attributes_list_type

        out["AutoVerifiedAttributes"] = (
            capo_cognito_identity_provider.types.verified_attributes_list_type.serialize_aws_json_1_1(
                value["auto_verified_attributes"]
            )
        )
    if "sms_verification_message" in value:
        out["SmsVerificationMessage"] = value["sms_verification_message"]
    if "email_verification_message" in value:
        out["EmailVerificationMessage"] = value["email_verification_message"]
    if "email_verification_subject" in value:
        out["EmailVerificationSubject"] = value["email_verification_subject"]
    if "verification_message_template" in value:
        import capo_cognito_identity_provider.types.verification_message_template_type

        out["VerificationMessageTemplate"] = (
            capo_cognito_identity_provider.types.verification_message_template_type.serialize_aws_json_1_1(
                value["verification_message_template"]
            )
        )
    if "sms_authentication_message" in value:
        out["SmsAuthenticationMessage"] = value["sms_authentication_message"]
    if "user_attribute_update_settings" in value:
        import capo_cognito_identity_provider.types.user_attribute_update_settings_type

        out["UserAttributeUpdateSettings"] = (
            capo_cognito_identity_provider.types.user_attribute_update_settings_type.serialize_aws_json_1_1(
                value["user_attribute_update_settings"]
            )
        )
    if "mfa_configuration" in value:
        import capo_cognito_identity_provider.types.user_pool_mfa_type

        out["MfaConfiguration"] = (
            capo_cognito_identity_provider.types.user_pool_mfa_type.serialize_aws_json_1_1(
                value["mfa_configuration"]
            )
        )
    if "device_configuration" in value:
        import capo_cognito_identity_provider.types.device_configuration_type

        out["DeviceConfiguration"] = (
            capo_cognito_identity_provider.types.device_configuration_type.serialize_aws_json_1_1(
                value["device_configuration"]
            )
        )
    if "email_configuration" in value:
        import capo_cognito_identity_provider.types.email_configuration_type

        out["EmailConfiguration"] = (
            capo_cognito_identity_provider.types.email_configuration_type.serialize_aws_json_1_1(
                value["email_configuration"]
            )
        )
    if "sms_configuration" in value:
        import capo_cognito_identity_provider.types.sms_configuration_type

        out["SmsConfiguration"] = (
            capo_cognito_identity_provider.types.sms_configuration_type.serialize_aws_json_1_1(
                value["sms_configuration"]
            )
        )
    if "user_pool_tags" in value:
        import capo_cognito_identity_provider.types.user_pool_tags_type

        out["UserPoolTags"] = (
            capo_cognito_identity_provider.types.user_pool_tags_type.serialize_aws_json_1_1(
                value["user_pool_tags"]
            )
        )
    if "admin_create_user_config" in value:
        import capo_cognito_identity_provider.types.admin_create_user_config_type

        out["AdminCreateUserConfig"] = (
            capo_cognito_identity_provider.types.admin_create_user_config_type.serialize_aws_json_1_1(
                value["admin_create_user_config"]
            )
        )
    if "user_pool_add_ons" in value:
        import capo_cognito_identity_provider.types.user_pool_add_ons_type

        out["UserPoolAddOns"] = (
            capo_cognito_identity_provider.types.user_pool_add_ons_type.serialize_aws_json_1_1(
                value["user_pool_add_ons"]
            )
        )
    if "account_recovery_setting" in value:
        import capo_cognito_identity_provider.types.account_recovery_setting_type

        out["AccountRecoverySetting"] = (
            capo_cognito_identity_provider.types.account_recovery_setting_type.serialize_aws_json_1_1(
                value["account_recovery_setting"]
            )
        )
    if "pool_name" in value:
        out["PoolName"] = value["pool_name"]
    if "user_pool_tier" in value:
        import capo_cognito_identity_provider.types.user_pool_tier_type

        out["UserPoolTier"] = (
            capo_cognito_identity_provider.types.user_pool_tier_type.serialize_aws_json_1_1(
                value["user_pool_tier"]
            )
        )
    if "key_configuration" in value:
        import capo_cognito_identity_provider.types.key_configuration_type

        out["KeyConfiguration"] = (
            capo_cognito_identity_provider.types.key_configuration_type.serialize_aws_json_1_1(
                value["key_configuration"]
            )
        )
    if "issuer_configuration" in value:
        import capo_cognito_identity_provider.types.issuer_configuration_type

        out["IssuerConfiguration"] = (
            capo_cognito_identity_provider.types.issuer_configuration_type.serialize_aws_json_1_1(
                value["issuer_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolRequest:
    out: UpdateUserPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateUserPoolRequest.user_pool_id required")
    if data.get("Policies") is not None:
        import capo_cognito_identity_provider.types.user_pool_policy_type

        out["policies"] = (
            capo_cognito_identity_provider.types.user_pool_policy_type.deserialize_aws_json_1_1(
                data["Policies"]
            )
        )
    if data.get("DeletionProtection") is not None:
        import capo_cognito_identity_provider.types.deletion_protection_type

        out["deletion_protection"] = (
            capo_cognito_identity_provider.types.deletion_protection_type.deserialize_aws_json_1_1(
                data["DeletionProtection"]
            )
        )
    if data.get("LambdaConfig") is not None:
        import capo_cognito_identity_provider.types.lambda_config_type

        out["lambda_config"] = (
            capo_cognito_identity_provider.types.lambda_config_type.deserialize_aws_json_1_1(
                data["LambdaConfig"]
            )
        )
    if data.get("AutoVerifiedAttributes") is not None:
        import capo_cognito_identity_provider.types.verified_attributes_list_type

        out["auto_verified_attributes"] = (
            capo_cognito_identity_provider.types.verified_attributes_list_type.deserialize_aws_json_1_1(
                data["AutoVerifiedAttributes"]
            )
        )
    if data.get("SmsVerificationMessage") is not None:
        out["sms_verification_message"] = data["SmsVerificationMessage"]
    if data.get("EmailVerificationMessage") is not None:
        out["email_verification_message"] = data["EmailVerificationMessage"]
    if data.get("EmailVerificationSubject") is not None:
        out["email_verification_subject"] = data["EmailVerificationSubject"]
    if data.get("VerificationMessageTemplate") is not None:
        import capo_cognito_identity_provider.types.verification_message_template_type

        out["verification_message_template"] = (
            capo_cognito_identity_provider.types.verification_message_template_type.deserialize_aws_json_1_1(
                data["VerificationMessageTemplate"]
            )
        )
    if data.get("SmsAuthenticationMessage") is not None:
        out["sms_authentication_message"] = data["SmsAuthenticationMessage"]
    if data.get("UserAttributeUpdateSettings") is not None:
        import capo_cognito_identity_provider.types.user_attribute_update_settings_type

        out["user_attribute_update_settings"] = (
            capo_cognito_identity_provider.types.user_attribute_update_settings_type.deserialize_aws_json_1_1(
                data["UserAttributeUpdateSettings"]
            )
        )
    if data.get("MfaConfiguration") is not None:
        import capo_cognito_identity_provider.types.user_pool_mfa_type

        out["mfa_configuration"] = (
            capo_cognito_identity_provider.types.user_pool_mfa_type.deserialize_aws_json_1_1(
                data["MfaConfiguration"]
            )
        )
    if data.get("DeviceConfiguration") is not None:
        import capo_cognito_identity_provider.types.device_configuration_type

        out["device_configuration"] = (
            capo_cognito_identity_provider.types.device_configuration_type.deserialize_aws_json_1_1(
                data["DeviceConfiguration"]
            )
        )
    if data.get("EmailConfiguration") is not None:
        import capo_cognito_identity_provider.types.email_configuration_type

        out["email_configuration"] = (
            capo_cognito_identity_provider.types.email_configuration_type.deserialize_aws_json_1_1(
                data["EmailConfiguration"]
            )
        )
    if data.get("SmsConfiguration") is not None:
        import capo_cognito_identity_provider.types.sms_configuration_type

        out["sms_configuration"] = (
            capo_cognito_identity_provider.types.sms_configuration_type.deserialize_aws_json_1_1(
                data["SmsConfiguration"]
            )
        )
    if data.get("UserPoolTags") is not None:
        import capo_cognito_identity_provider.types.user_pool_tags_type

        out["user_pool_tags"] = (
            capo_cognito_identity_provider.types.user_pool_tags_type.deserialize_aws_json_1_1(
                data["UserPoolTags"]
            )
        )
    if data.get("AdminCreateUserConfig") is not None:
        import capo_cognito_identity_provider.types.admin_create_user_config_type

        out["admin_create_user_config"] = (
            capo_cognito_identity_provider.types.admin_create_user_config_type.deserialize_aws_json_1_1(
                data["AdminCreateUserConfig"]
            )
        )
    if data.get("UserPoolAddOns") is not None:
        import capo_cognito_identity_provider.types.user_pool_add_ons_type

        out["user_pool_add_ons"] = (
            capo_cognito_identity_provider.types.user_pool_add_ons_type.deserialize_aws_json_1_1(
                data["UserPoolAddOns"]
            )
        )
    if data.get("AccountRecoverySetting") is not None:
        import capo_cognito_identity_provider.types.account_recovery_setting_type

        out["account_recovery_setting"] = (
            capo_cognito_identity_provider.types.account_recovery_setting_type.deserialize_aws_json_1_1(
                data["AccountRecoverySetting"]
            )
        )
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    if data.get("UserPoolTier") is not None:
        import capo_cognito_identity_provider.types.user_pool_tier_type

        out["user_pool_tier"] = (
            capo_cognito_identity_provider.types.user_pool_tier_type.deserialize_aws_json_1_1(
                data["UserPoolTier"]
            )
        )
    if data.get("KeyConfiguration") is not None:
        import capo_cognito_identity_provider.types.key_configuration_type

        out["key_configuration"] = (
            capo_cognito_identity_provider.types.key_configuration_type.deserialize_aws_json_1_1(
                data["KeyConfiguration"]
            )
        )
    if data.get("IssuerConfiguration") is not None:
        import capo_cognito_identity_provider.types.issuer_configuration_type

        out["issuer_configuration"] = (
            capo_cognito_identity_provider.types.issuer_configuration_type.deserialize_aws_json_1_1(
                data["IssuerConfiguration"]
            )
        )
    return out
