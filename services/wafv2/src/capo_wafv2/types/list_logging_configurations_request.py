"""Generated from Smithy shape ``com.amazonaws.wafv2#ListLoggingConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.log_scope
    import capo_wafv2.types.next_marker
    import capo_wafv2.types.pagination_limit
    import capo_wafv2.types.scope


class ListLoggingConfigurationsRequest(TypedDict, closed=True):
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    next_marker: NotRequired["capo_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    limit: NotRequired["capo_wafv2.types.pagination_limit.PaginationLimit"]
    """<p>The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a <code>NextMarker</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    log_scope: NotRequired["capo_wafv2.types.log_scope.LogScope"]
    """<p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLoggingConfigurationsRequest) -> dict:
    out: dict = {}
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "log_scope" in value:
        import capo_wafv2.types.log_scope

        out["LogScope"] = capo_wafv2.types.log_scope.serialize_aws_json_1_1(
            value["log_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLoggingConfigurationsRequest:
    out: ListLoggingConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("ListLoggingConfigurationsRequest.scope required")
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    if data.get("LogScope") is not None:
        import capo_wafv2.types.log_scope

        out["log_scope"] = capo_wafv2.types.log_scope.deserialize_aws_json_1_1(
            data["LogScope"]
        )
    return out
