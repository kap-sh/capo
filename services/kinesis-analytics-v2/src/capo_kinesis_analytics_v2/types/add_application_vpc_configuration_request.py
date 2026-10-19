"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#AddApplicationVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.conditional_token
    import capo_kinesis_analytics_v2.types.vpc_configuration


class AddApplicationVpcConfigurationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of an existing application.</p>"""
    current_application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version of the application to which you want to add the VPC configuration. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    vpc_configuration: (
        "capo_kinesis_analytics_v2.types.vpc_configuration.VpcConfiguration"
    )
    """<p>Description of the VPC to add to the application.</p>"""
    conditional_token: NotRequired[
        "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates. You must provide the <code>ApplicationVersionID</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddApplicationVpcConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "current_application_version_id" in value:
        out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    import capo_kinesis_analytics_v2.types.vpc_configuration

    out["VpcConfiguration"] = (
        capo_kinesis_analytics_v2.types.vpc_configuration.serialize_aws_json_1_1(
            value["vpc_configuration"]
        )
    )
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddApplicationVpcConfigurationRequest:
    out: AddApplicationVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    if data.get("VpcConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_kinesis_analytics_v2.types.vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AddApplicationVpcConfigurationRequest.vpc_configuration required"
        )
    if data.get("ConditionalToken") is not None:
        out["conditional_token"] = data["ConditionalToken"]
    return out
