"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AnalyticsConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.hex_string_type
    import capo_cognito_identity_provider.types.string_type


class AnalyticsConfigurationType(TypedDict, closed=True):
    application_id: NotRequired[
        "capo_cognito_identity_provider.types.hex_string_type.HexStringType"
    ]
    """<p>Your Amazon Pinpoint project ID.</p>"""
    application_arn: NotRequired[
        "capo_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The Amazon Resource Name (ARN) of an Amazon Pinpoint project that you want to connect to your user pool app client. Amazon Cognito publishes events to the Amazon Pinpoint project that <code>ApplicationArn</code> declares. You can also configure your application to pass an endpoint ID in the <code>AnalyticsMetadata</code> parameter of sign-in operations. The endpoint ID is information about the destination for push notifications</p>"""
    role_arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The ARN of an Identity and Access Management role that has the permissions required for Amazon Cognito to publish events to Amazon Pinpoint analytics.</p>"""
    external_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html">external ID</a> of the role that Amazon Cognito assumes to send analytics data to Amazon Pinpoint.</p>"""
    user_data_shared: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>If <code>UserDataShared</code> is <code>true</code>, Amazon Cognito includes user data in the events that it publishes to Amazon Pinpoint analytics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnalyticsConfigurationType) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    out["UserDataShared"] = value.get("user_data_shared", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AnalyticsConfigurationType:
    out: AnalyticsConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    if data.get("UserDataShared") is not None:
        out["user_data_shared"] = data["UserDataShared"]
    else:
        out["user_data_shared"] = False
    return out
