"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.account_recovery_setting_type
    import capo_cognito_identity_provider.types.acr_configuration_type
    import capo_cognito_identity_provider.types.admin_create_user_config_type
    import capo_cognito_identity_provider.types.alias_attributes_list_type
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.deletion_protection_type
    import capo_cognito_identity_provider.types.device_configuration_type
    import capo_cognito_identity_provider.types.domain_type
    import capo_cognito_identity_provider.types.email_configuration_type
    import capo_cognito_identity_provider.types.email_verification_message_type
    import capo_cognito_identity_provider.types.email_verification_subject_type
    import capo_cognito_identity_provider.types.integer_type
    import capo_cognito_identity_provider.types.issuer_configuration_type
    import capo_cognito_identity_provider.types.key_configuration_type
    import capo_cognito_identity_provider.types.lambda_config_type
    import capo_cognito_identity_provider.types.schema_attributes_list_type
    import capo_cognito_identity_provider.types.sms_configuration_type
    import capo_cognito_identity_provider.types.sms_verification_message_type
    import capo_cognito_identity_provider.types.status_type
    import capo_cognito_identity_provider.types.string_type
    import capo_cognito_identity_provider.types.user_attribute_update_settings_type
    import capo_cognito_identity_provider.types.user_pool_add_ons_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.user_pool_mfa_type
    import capo_cognito_identity_provider.types.user_pool_name_type
    import capo_cognito_identity_provider.types.user_pool_policy_type
    import capo_cognito_identity_provider.types.user_pool_tags_type
    import capo_cognito_identity_provider.types.user_pool_tier_type
    import capo_cognito_identity_provider.types.username_attributes_list_type
    import capo_cognito_identity_provider.types.username_configuration_type
    import capo_cognito_identity_provider.types.verification_message_template_type
    import capo_cognito_identity_provider.types.verified_attributes_list_type


class UserPoolType(TypedDict, closed=True):
    id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool.</p>"""
    name: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_name_type.UserPoolNameType"
    ]
    """<p>The name of the user pool.</p>"""
    policies: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_policy_type.UserPoolPolicyType"
    ]
    """<p>A list of user pool policies. Contains the policy that sets password-complexity requirements.</p>"""
    deletion_protection: NotRequired[
        "capo_cognito_identity_provider.types.deletion_protection_type.DeletionProtectionType"
    ]
    """<p>When active, <code>DeletionProtection</code> prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.</p> <p>When you try to delete a protected user pool in a <code>DeleteUserPool</code> API request, Amazon Cognito returns an <code>InvalidParameterException</code> error. To delete a protected user pool, send a new <code>DeleteUserPool</code> request after you deactivate deletion protection in an <code>UpdateUserPool</code> API request.</p>"""
    lambda_config: NotRequired[
        "capo_cognito_identity_provider.types.lambda_config_type.LambdaConfigType"
    ]
    """<p>A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.</p>"""
    status: NotRequired["capo_cognito_identity_provider.types.status_type.StatusType"]
    """<p>This parameter is no longer used.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    schema_attributes: NotRequired[
        "capo_cognito_identity_provider.types.schema_attributes_list_type.SchemaAttributesListType"
    ]
    """<p>A list of the user attributes and their properties in your user pool. The attribute schema contains standard attributes, custom attributes with a <code>custom:</code> prefix, and developer attributes with a <code>dev:</code> prefix. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html">User pool attributes</a>.</p> <p>Developer-only attributes are a legacy feature of user pools, and are read-only to all app clients. You can create and update developer-only attributes only with IAM-authenticated API operations. Use app client read/write permissions instead.</p>"""
    auto_verified_attributes: NotRequired[
        "capo_cognito_identity_provider.types.verified_attributes_list_type.VerifiedAttributesListType"
    ]
    """<p>The attributes that are auto-verified in a user pool.</p>"""
    alias_attributes: NotRequired[
        "capo_cognito_identity_provider.types.alias_attributes_list_type.AliasAttributesListType"
    ]
    """<p>Attributes supported as an alias for this user pool. An alias is an attribute that users can enter as an alternative username. Possible values: <b>phone_number</b>, <b>email</b>, or <b>preferred_username</b>.</p>"""
    username_attributes: NotRequired[
        "capo_cognito_identity_provider.types.username_attributes_list_type.UsernameAttributesListType"
    ]
    """<p>Specifies whether a user can use an email address or phone number as a username when they sign up.</p>"""
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
    """<p>The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.</p>"""
    sms_authentication_message: NotRequired[
        "capo_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>The contents of the SMS authentication message.</p>"""
    user_attribute_update_settings: NotRequired[
        "capo_cognito_identity_provider.types.user_attribute_update_settings_type.UserAttributeUpdateSettingsType"
    ]
    """<p>The settings for updates to user attributes. These settings include the property <code>AttributesRequireVerificationBeforeUpdate</code>, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates"> Verifying updates to email addresses and phone numbers</a>.</p>"""
    mfa_configuration: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_mfa_type.UserPoolMfaType"
    ]
    """<p>Can be one of the following values:</p> <ul> <li> <p> <code>OFF</code> - MFA tokens aren't required and can't be specified during user registration.</p> </li> <li> <p> <code>ON</code> - MFA tokens are required for all user registrations. You can only specify required when you're initially creating a user pool.</p> </li> <li> <p> <code>OPTIONAL</code> - Users have the option when registering to create an MFA token.</p> </li> </ul>"""
    device_configuration: NotRequired[
        "capo_cognito_identity_provider.types.device_configuration_type.DeviceConfigurationType"
    ]
    """<p>The device-remembering configuration for a user pool. A null value indicates that you have deactivated device remembering in your user pool.</p> <note> <p>When you provide a value for any <code>DeviceConfiguration</code> field, you activate the Amazon Cognito device-remembering feature.</p> </note>"""
    estimated_number_of_users: (
        "capo_cognito_identity_provider.types.integer_type.IntegerType"
    )
    """<p>A number estimating the size of the user pool.</p>"""
    email_configuration: NotRequired[
        "capo_cognito_identity_provider.types.email_configuration_type.EmailConfigurationType"
    ]
    """<p>The email configuration of your user pool. The email configuration type sets your preferred sending method, Amazon Web Services Region, and sender for messages from your user pool.</p>"""
    sms_configuration: NotRequired[
        "capo_cognito_identity_provider.types.sms_configuration_type.SmsConfigurationType"
    ]
    """<p>User pool configuration for delivery of SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account.</p>"""
    user_pool_tags: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    ]
    """<p>The tags that are assigned to the user pool. A tag is a label that you can apply to user pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.</p>"""
    sms_configuration_failure: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The reason why the SMS configuration can't send the messages to your users.</p> <p>This message might include comma-separated values to describe why your SMS configuration can't send messages to user pool end users.</p> <dl> <dt>InvalidSmsRoleAccessPolicyException</dt> <dd> <p>The Identity and Access Management role that Amazon Cognito uses to send SMS messages isn't properly configured. For more information, see <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SmsConfigurationType.html">SmsConfigurationType</a>.</p> </dd> <dt>SNSSandbox</dt> <dd> <p>The Amazon Web Services account is in the SNS SMS Sandbox and messages will only reach verified end users. This parameter won’t get populated with SNSSandbox if the user creating the user pool doesn’t have SNS permissions. To learn how to move your Amazon Web Services account out of the sandbox, see <a href="https://docs.aws.amazon.com/sns/latest/dg/sns-sms-sandbox-moving-to-production.html">Moving out of the SMS sandbox</a>.</p> </dd> </dl>"""
    email_configuration_failure: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>Deprecated. Review error codes from API requests with <code>EventSource:cognito-idp.amazonaws.com</code> in CloudTrail for information about problems with user pool email configuration.</p>"""
    domain: NotRequired["capo_cognito_identity_provider.types.domain_type.DomainType"]
    """<p>The domain prefix, if the user pool has a domain associated with it.</p>"""
    custom_domain: NotRequired[
        "capo_cognito_identity_provider.types.domain_type.DomainType"
    ]
    """<p>A custom domain name that you provide to Amazon Cognito. This parameter applies only if you use a custom domain to host the sign-up and sign-in pages for your application. An example of a custom domain name might be <code>auth.example.com</code>.</p> <p>For more information about adding a custom domain to your user pool, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html">Using Your Own Domain for the Hosted UI</a>.</p>"""
    admin_create_user_config: NotRequired[
        "capo_cognito_identity_provider.types.admin_create_user_config_type.AdminCreateUserConfigType"
    ]
    """<p>The configuration for <code>AdminCreateUser</code> requests.</p>"""
    user_pool_add_ons: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_add_ons_type.UserPoolAddOnsType"
    ]
    """<p>Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to <code>AUDIT</code>. To configure automatic security responses to potentially unwanted traffic to your user pool, set to <code>ENFORCED</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html">Adding advanced security to a user pool</a>. To activate this setting, your user pool must be on the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html"> Plus tier</a>.</p>"""
    username_configuration: NotRequired[
        "capo_cognito_identity_provider.types.username_configuration_type.UsernameConfigurationType"
    ]
    """<p>Case sensitivity of the username input for the selected sign-in option. When case sensitivity is set to <code>False</code> (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, <code>username</code>, <code>USERNAME</code>, or <code>UserName</code>, or for email, <code>email@example.com</code> or <code>EMaiL@eXamplE.Com</code>. For most use cases, set case sensitivity to <code>False</code> (case insensitive) as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.</p>"""
    arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the user pool.</p>"""
    account_recovery_setting: NotRequired[
        "capo_cognito_identity_provider.types.account_recovery_setting_type.AccountRecoverySettingType"
    ]
    """<p>The available verified method a user can use to recover their password when they call <code>ForgotPassword</code>. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred through email.</p>"""
    user_pool_tier: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_tier_type.UserPoolTierType"
    ]
    """<p>The user pool <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html">feature plan</a>, or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to <code>ESSENTIALS</code>.</p>"""
    key_configuration: NotRequired[
        "capo_cognito_identity_provider.types.key_configuration_type.KeyConfigurationType"
    ]
    """<p>The key configuration for the user pool, including encryption settings.</p>"""
    issuer_configuration: NotRequired[
        "capo_cognito_identity_provider.types.issuer_configuration_type.IssuerConfigurationType"
    ]
    """<p>The issuer configuration for the user pool, including token issuing settings.</p>"""
    acr_configuration: NotRequired[
        "capo_cognito_identity_provider.types.acr_configuration_type.AcrConfigurationType"
    ]
    """<p>The names of the authentication context class reference (ACR) levels for the user pool. Amazon Cognito always returns the effective configuration, with default names merged in for any level that you haven't customized.</p> <p>Configuring custom ACR level names requires the Essentials or Plus feature plan. To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolType) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
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
    if "status" in value:
        import capo_cognito_identity_provider.types.status_type

        out["Status"] = (
            capo_cognito_identity_provider.types.status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "schema_attributes" in value:
        import capo_cognito_identity_provider.types.schema_attributes_list_type

        out["SchemaAttributes"] = (
            capo_cognito_identity_provider.types.schema_attributes_list_type.serialize_aws_json_1_1(
                value["schema_attributes"]
            )
        )
    if "auto_verified_attributes" in value:
        import capo_cognito_identity_provider.types.verified_attributes_list_type

        out["AutoVerifiedAttributes"] = (
            capo_cognito_identity_provider.types.verified_attributes_list_type.serialize_aws_json_1_1(
                value["auto_verified_attributes"]
            )
        )
    if "alias_attributes" in value:
        import capo_cognito_identity_provider.types.alias_attributes_list_type

        out["AliasAttributes"] = (
            capo_cognito_identity_provider.types.alias_attributes_list_type.serialize_aws_json_1_1(
                value["alias_attributes"]
            )
        )
    if "username_attributes" in value:
        import capo_cognito_identity_provider.types.username_attributes_list_type

        out["UsernameAttributes"] = (
            capo_cognito_identity_provider.types.username_attributes_list_type.serialize_aws_json_1_1(
                value["username_attributes"]
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
    out["EstimatedNumberOfUsers"] = value.get("estimated_number_of_users", 0)
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
    if "sms_configuration_failure" in value:
        out["SmsConfigurationFailure"] = value["sms_configuration_failure"]
    if "email_configuration_failure" in value:
        out["EmailConfigurationFailure"] = value["email_configuration_failure"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "custom_domain" in value:
        out["CustomDomain"] = value["custom_domain"]
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
    if "username_configuration" in value:
        import capo_cognito_identity_provider.types.username_configuration_type

        out["UsernameConfiguration"] = (
            capo_cognito_identity_provider.types.username_configuration_type.serialize_aws_json_1_1(
                value["username_configuration"]
            )
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "account_recovery_setting" in value:
        import capo_cognito_identity_provider.types.account_recovery_setting_type

        out["AccountRecoverySetting"] = (
            capo_cognito_identity_provider.types.account_recovery_setting_type.serialize_aws_json_1_1(
                value["account_recovery_setting"]
            )
        )
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
    if "acr_configuration" in value:
        import capo_cognito_identity_provider.types.acr_configuration_type

        out["AcrConfiguration"] = (
            capo_cognito_identity_provider.types.acr_configuration_type.serialize_aws_json_1_1(
                value["acr_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolType:
    out: UserPoolType = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
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
    if data.get("Status") is not None:
        import capo_cognito_identity_provider.types.status_type

        out["status"] = (
            capo_cognito_identity_provider.types.status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if data.get("SchemaAttributes") is not None:
        import capo_cognito_identity_provider.types.schema_attributes_list_type

        out["schema_attributes"] = (
            capo_cognito_identity_provider.types.schema_attributes_list_type.deserialize_aws_json_1_1(
                data["SchemaAttributes"]
            )
        )
    if data.get("AutoVerifiedAttributes") is not None:
        import capo_cognito_identity_provider.types.verified_attributes_list_type

        out["auto_verified_attributes"] = (
            capo_cognito_identity_provider.types.verified_attributes_list_type.deserialize_aws_json_1_1(
                data["AutoVerifiedAttributes"]
            )
        )
    if data.get("AliasAttributes") is not None:
        import capo_cognito_identity_provider.types.alias_attributes_list_type

        out["alias_attributes"] = (
            capo_cognito_identity_provider.types.alias_attributes_list_type.deserialize_aws_json_1_1(
                data["AliasAttributes"]
            )
        )
    if data.get("UsernameAttributes") is not None:
        import capo_cognito_identity_provider.types.username_attributes_list_type

        out["username_attributes"] = (
            capo_cognito_identity_provider.types.username_attributes_list_type.deserialize_aws_json_1_1(
                data["UsernameAttributes"]
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
    if data.get("EstimatedNumberOfUsers") is not None:
        out["estimated_number_of_users"] = data["EstimatedNumberOfUsers"]
    else:
        out["estimated_number_of_users"] = 0
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
    if data.get("SmsConfigurationFailure") is not None:
        out["sms_configuration_failure"] = data["SmsConfigurationFailure"]
    if data.get("EmailConfigurationFailure") is not None:
        out["email_configuration_failure"] = data["EmailConfigurationFailure"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("CustomDomain") is not None:
        out["custom_domain"] = data["CustomDomain"]
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
    if data.get("UsernameConfiguration") is not None:
        import capo_cognito_identity_provider.types.username_configuration_type

        out["username_configuration"] = (
            capo_cognito_identity_provider.types.username_configuration_type.deserialize_aws_json_1_1(
                data["UsernameConfiguration"]
            )
        )
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AccountRecoverySetting") is not None:
        import capo_cognito_identity_provider.types.account_recovery_setting_type

        out["account_recovery_setting"] = (
            capo_cognito_identity_provider.types.account_recovery_setting_type.deserialize_aws_json_1_1(
                data["AccountRecoverySetting"]
            )
        )
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
    if data.get("AcrConfiguration") is not None:
        import capo_cognito_identity_provider.types.acr_configuration_type

        out["acr_configuration"] = (
            capo_cognito_identity_provider.types.acr_configuration_type.deserialize_aws_json_1_1(
                data["AcrConfiguration"]
            )
        )
    return out
