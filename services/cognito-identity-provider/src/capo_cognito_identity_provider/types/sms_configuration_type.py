"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SmsConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.eums_sms_configuration_type
    import capo_cognito_identity_provider.types.optional_arn_type
    import capo_cognito_identity_provider.types.region_code_type
    import capo_cognito_identity_provider.types.string_type


class SmsConfigurationType(TypedDict, closed=True):
    sns_caller_arn: (
        "capo_cognito_identity_provider.types.optional_arn_type.OptionalArnType"
    )
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your Amazon Web Services account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html">spending limit</a>. </p>"""
    external_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The external ID provides additional security for your IAM role. You can use an <code>ExternalId</code> with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an <code>ExternalId</code>, your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the <code>ExternalID</code>. If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the <code>ExternalId</code>.</p> <p>For more information about the <code>ExternalId</code> of a role, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">How to use an external ID when granting access to your Amazon Web Services resources to a third party</a>.</p>"""
    sns_region: NotRequired[
        "capo_cognito_identity_provider.types.region_code_type.RegionCodeType"
    ]
    """<p>The Amazon Web Services Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported <b>Legacy Amazon SNS alternate Region</b>. </p> <p> Amazon Cognito resources in the Asia Pacific (Seoul) Amazon Web Services Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html">SMS message settings for Amazon Cognito user pools</a>.</p>"""
    eums_sms: NotRequired[
        "capo_cognito_identity_provider.types.eums_sms_configuration_type.EumsSmsConfigurationType"
    ]
    """<p>The configuration for sending SMS messages through Amazon Web Services End User Messaging SMS, as an alternative to Amazon SNS. In a user pool, provide either the Amazon SNS configuration (<code>SnsCallerArn</code>) or this configuration, but not both. In Amazon Web Services Regions where Amazon SNS is not available, this configuration is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmsConfigurationType) -> dict:
    out: dict = {}
    out["SnsCallerArn"] = value.get("sns_caller_arn", "")
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "sns_region" in value:
        out["SnsRegion"] = value["sns_region"]
    if "eums_sms" in value:
        import capo_cognito_identity_provider.types.eums_sms_configuration_type

        out["EumsSms"] = (
            capo_cognito_identity_provider.types.eums_sms_configuration_type.serialize_aws_json_1_1(
                value["eums_sms"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SmsConfigurationType:
    out: SmsConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("SnsCallerArn") is not None:
        out["sns_caller_arn"] = data["SnsCallerArn"]
    else:
        out["sns_caller_arn"] = ""
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("SnsRegion") is not None:
        out["sns_region"] = data["SnsRegion"]
    if data.get("EumsSms") is not None:
        import capo_cognito_identity_provider.types.eums_sms_configuration_type

        out["eums_sms"] = (
            capo_cognito_identity_provider.types.eums_sms_configuration_type.deserialize_aws_json_1_1(
                data["EumsSms"]
            )
        )
    return out
