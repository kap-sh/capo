"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationVpcConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.conditional_token
    import capo_kinesis_analytics_v2.types.id


class DeleteApplicationVpcConfigurationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of an existing application.</p>"""
    current_application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The current application version ID. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    vpc_configuration_id: "capo_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the VPC configuration to delete.</p>"""
    conditional_token: NotRequired[
        "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationVpcConfigurationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "current_application_version_id" in value:
        out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["VpcConfigurationId"] = value["vpc_configuration_id"]
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationVpcConfigurationRequest:
    out: DeleteApplicationVpcConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    if data.get("VpcConfigurationId") is not None:
        out["vpc_configuration_id"] = data["VpcConfigurationId"]
    else:
        out["vpc_configuration_id"] = ""
    if data.get("ConditionalToken") is not None:
        out["conditional_token"] = data["ConditionalToken"]
    return out
