"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EumsSmsConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.region_code_type
    import capo_cognito_identity_provider.types.string_type


class EumsSmsConfigurationType(TypedDict, closed=True):
    caller_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The ARN of the IAM role that Amazon Cognito assumes to send SMS messages through Amazon Web Services End User Messaging SMS. The role must grant permission to call the <code>sms-voice:SendTextMessage</code> operation.</p>"""
    external_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The external ID that Amazon Cognito includes when it assumes the <code>CallerArn</code> role. Use this value as a condition in the role trust policy to prevent the confused deputy problem.</p>"""
    origination_identity: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The origination identity that Amazon Web Services End User Messaging SMS uses to send messages to your users. This value can be one of the following:</p> <ul> <li> <p>A phone number – A long code, toll-free number, or short code that is assigned to your account.</p> </li> <li> <p>A sender ID – An alphabetic name that identifies the message sender in supported countries.</p> </li> <li> <p>A phone pool – A group of phone numbers that Amazon Web Services End User Messaging SMS selects from when it sends messages.</p> </li> </ul> <p>You can provide an E.164 phone number or the ARN of the phone number, sender ID, or phone pool. Amazon Web Services End User Messaging SMS evaluates IAM authorization with the value that you provide. If the permissions policy of your <code>CallerArn</code> role scopes the <code>sms-voice:SendTextMessage</code> resource to a specific ARN, provide that same ARN. If the formats do not match, requests fail with an <code>InvalidSmsRoleAccessPolicyException</code>.</p> <p>Depending on the destination country, you must provide an origination identity. For country-specific requirements, see <a href="https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html">Supported countries and regions for SMS messaging</a> in the Amazon Web Services End User Messaging SMS User Guide.</p>"""
    configuration_set_name: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The name of the Amazon Web Services End User Messaging SMS configuration set that Amazon Cognito applies to messages, for logging and event destinations. If you omit this member, Amazon Cognito sends messages without applying a configuration set.</p>"""
    in_entity_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The principal entity ID required by India's Distributed Ledger Technology (DLT) regulations for SMS messages.</p>"""
    in_template_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The registered template ID for the message template required by India's DLT regulations for SMS messages.</p>"""
    region: NotRequired[
        "capo_cognito_identity_provider.types.region_code_type.RegionCodeType"
    ]
    """<p>The Amazon Web Services Region of the Amazon Web Services End User Messaging SMS resources that Amazon Cognito uses to send messages. Amazon Web Services End User Messaging SMS must be available in your user pool's Region.</p> <p>If you omit this parameter, Amazon Cognito uses the same Region as your user pool. You can also set this parameter to your user pool's Region explicitly. Amazon Cognito rejects any other value with an <code>InvalidParameterException</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EumsSmsConfigurationType) -> dict:
    out: dict = {}
    out["CallerArn"] = value["caller_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "origination_identity" in value:
        out["OriginationIdentity"] = value["origination_identity"]
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    if "in_entity_id" in value:
        out["InEntityId"] = value["in_entity_id"]
    if "in_template_id" in value:
        out["InTemplateId"] = value["in_template_id"]
    if "region" in value:
        out["Region"] = value["region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EumsSmsConfigurationType:
    out: EumsSmsConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("CallerArn") is not None:
        out["caller_arn"] = data["CallerArn"]
    else:
        raise DeserializationError("EumsSmsConfigurationType.caller_arn required")
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("OriginationIdentity") is not None:
        out["origination_identity"] = data["OriginationIdentity"]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    if data.get("InEntityId") is not None:
        out["in_entity_id"] = data["InEntityId"]
    if data.get("InTemplateId") is not None:
        out["in_template_id"] = data["InTemplateId"]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    return out
