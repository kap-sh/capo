"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerificationMessageTemplateType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.default_email_option_type
    import capo_cognito_identity_provider.types.email_verification_message_by_link_type
    import capo_cognito_identity_provider.types.email_verification_message_type
    import capo_cognito_identity_provider.types.email_verification_subject_by_link_type
    import capo_cognito_identity_provider.types.email_verification_subject_type
    import capo_cognito_identity_provider.types.sms_verification_message_type


class VerificationMessageTemplateType(TypedDict, closed=True):
    sms_message: NotRequired[
        "capo_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>The template for SMS messages that Amazon Cognito sends to your users.</p>"""
    email_message: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_message_type.EmailVerificationMessageType"
    ]
    """<p>The template for email messages that Amazon Cognito sends to your users. You can set an <code>EmailMessage</code> template only if the value of <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount"> EmailSendingAccount</a> is <code>DEVELOPER</code>. When your <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount">EmailSendingAccount</a> is <code>DEVELOPER</code>, your user pool sends email messages with your own Amazon SES configuration.</p>"""
    email_subject: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_subject_type.EmailVerificationSubjectType"
    ]
    """<p>The subject line for the email message template. You can set an <code>EmailSubject</code> template only if the value of <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount"> EmailSendingAccount</a> is <code>DEVELOPER</code>. When your <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount">EmailSendingAccount</a> is <code>DEVELOPER</code>, your user pool sends email messages with your own Amazon SES configuration.</p>"""
    email_message_by_link: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_message_by_link_type.EmailVerificationMessageByLinkType"
    ]
    """<p>The email message template for sending a confirmation link to the user. You can set an <code>EmailMessageByLink</code> template only if the value of <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount"> EmailSendingAccount</a> is <code>DEVELOPER</code>. When your <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount">EmailSendingAccount</a> is <code>DEVELOPER</code>, your user pool sends email messages with your own Amazon SES configuration.</p>"""
    email_subject_by_link: NotRequired[
        "capo_cognito_identity_provider.types.email_verification_subject_by_link_type.EmailVerificationSubjectByLinkType"
    ]
    """<p>The subject line for the email message template for sending a confirmation link to the user. You can set an <code>EmailSubjectByLink</code> template only if the value of <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount"> EmailSendingAccount</a> is <code>DEVELOPER</code>. When your <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_EmailConfigurationType.html#CognitoUserPools-Type-EmailConfigurationType-EmailSendingAccount">EmailSendingAccount</a> is <code>DEVELOPER</code>, your user pool sends email messages with your own Amazon SES configuration.</p>"""
    default_email_option: NotRequired[
        "capo_cognito_identity_provider.types.default_email_option_type.DefaultEmailOptionType"
    ]
    """<p>The configuration of verification emails to contain a clickable link or a verification code.</p> <p>For link, your template body must contain link text in the format <code>{##Click here##}</code>. "Click here" in the example is a customizable string. For code, your template body must contain a code placeholder in the format <code>{####}</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerificationMessageTemplateType) -> dict:
    out: dict = {}
    if "sms_message" in value:
        out["SmsMessage"] = value["sms_message"]
    if "email_message" in value:
        out["EmailMessage"] = value["email_message"]
    if "email_subject" in value:
        out["EmailSubject"] = value["email_subject"]
    if "email_message_by_link" in value:
        out["EmailMessageByLink"] = value["email_message_by_link"]
    if "email_subject_by_link" in value:
        out["EmailSubjectByLink"] = value["email_subject_by_link"]
    if "default_email_option" in value:
        import capo_cognito_identity_provider.types.default_email_option_type

        out["DefaultEmailOption"] = (
            capo_cognito_identity_provider.types.default_email_option_type.serialize_aws_json_1_1(
                value["default_email_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VerificationMessageTemplateType:
    out: VerificationMessageTemplateType = {}  # type: ignore[typeddict-item]
    if data.get("SmsMessage") is not None:
        out["sms_message"] = data["SmsMessage"]
    if data.get("EmailMessage") is not None:
        out["email_message"] = data["EmailMessage"]
    if data.get("EmailSubject") is not None:
        out["email_subject"] = data["EmailSubject"]
    if data.get("EmailMessageByLink") is not None:
        out["email_message_by_link"] = data["EmailMessageByLink"]
    if data.get("EmailSubjectByLink") is not None:
        out["email_subject_by_link"] = data["EmailSubjectByLink"]
    if data.get("DefaultEmailOption") is not None:
        import capo_cognito_identity_provider.types.default_email_option_type

        out["default_email_option"] = (
            capo_cognito_identity_provider.types.default_email_option_type.deserialize_aws_json_1_1(
                data["DefaultEmailOption"]
            )
        )
    return out
