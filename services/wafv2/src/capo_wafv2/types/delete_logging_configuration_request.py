"""Generated from Smithy shape ``com.amazonaws.wafv2#DeleteLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.log_scope
    import capo_wafv2.types.log_type
    import capo_wafv2.types.resource_arn


class DeleteLoggingConfigurationRequest(TypedDict, closed=True):
    resource_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL from which you want to delete the <a>LoggingConfiguration</a>.</p>"""
    log_type: NotRequired["capo_wafv2.types.log_type.LogType"]
    """<p>Used to distinguish between various logging options. Currently, there is one option.</p> <p>Default: <code>WAF_LOGS</code> </p>"""
    log_scope: NotRequired["capo_wafv2.types.log_scope.LogScope"]
    """<p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "log_type" in value:
        import capo_wafv2.types.log_type

        out["LogType"] = capo_wafv2.types.log_type.serialize_aws_json_1_1(
            value["log_type"]
        )
    if "log_scope" in value:
        import capo_wafv2.types.log_scope

        out["LogScope"] = capo_wafv2.types.log_scope.serialize_aws_json_1_1(
            value["log_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLoggingConfigurationRequest:
    out: DeleteLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError(
            "DeleteLoggingConfigurationRequest.resource_arn required"
        )
    if data.get("LogType") is not None:
        import capo_wafv2.types.log_type

        out["log_type"] = capo_wafv2.types.log_type.deserialize_aws_json_1_1(
            data["LogType"]
        )
    if data.get("LogScope") is not None:
        import capo_wafv2.types.log_scope

        out["log_scope"] = capo_wafv2.types.log_scope.deserialize_aws_json_1_1(
            data["LogScope"]
        )
    return out
