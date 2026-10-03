"""Generated from Smithy shape ``com.amazonaws.wafv2#GetSampledRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.list_max_items
    import capo_wafv2.types.metric_name
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.scope
    import capo_wafv2.types.time_window


class GetSampledRequestsRequest(TypedDict, closed=True):
    web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon resource name (ARN) of the <code>WebACL</code> for which you want a sample of requests.</p>"""
    rule_metric_name: "capo_wafv2.types.metric_name.MetricName"
    """<p>The metric name assigned to the <code>Rule</code> or <code>RuleGroup</code> dimension for which you want a sample of requests.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    time_window: "capo_wafv2.types.time_window.TimeWindow"
    """<p>The start date and time and the end date and time of the range for which you want <code>GetSampledRequests</code> to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours. If you specify a start time that's earlier than three hours ago, WAF sets it to three hours ago.</p>"""
    max_items: "capo_wafv2.types.list_max_items.ListMaxItems"
    """<p>The number of requests that you want WAF to return from among the first 5,000 requests that your Amazon Web Services resource received during the time range. If your resource received fewer requests than the value of <code>MaxItems</code>, <code>GetSampledRequests</code> returns information about all of them. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSampledRequestsRequest) -> dict:
    out: dict = {}
    out["WebAclArn"] = value["web_acl_arn"]
    out["RuleMetricName"] = value["rule_metric_name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    import capo_wafv2.types.time_window

    out["TimeWindow"] = capo_wafv2.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSampledRequestsRequest:
    out: GetSampledRequestsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebAclArn") is not None:
        out["web_acl_arn"] = data["WebAclArn"]
    else:
        raise DeserializationError("GetSampledRequestsRequest.web_acl_arn required")
    if data.get("RuleMetricName") is not None:
        out["rule_metric_name"] = data["RuleMetricName"]
    else:
        raise DeserializationError(
            "GetSampledRequestsRequest.rule_metric_name required"
        )
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        raise DeserializationError("GetSampledRequestsRequest.scope required")
    if data.get("TimeWindow") is not None:
        import capo_wafv2.types.time_window

        out["time_window"] = capo_wafv2.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError("GetSampledRequestsRequest.time_window required")
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    else:
        raise DeserializationError("GetSampledRequestsRequest.max_items required")
    return out
