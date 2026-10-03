"""Generated from Smithy shape ``com.amazonaws.waf#GetSampledRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.get_sampled_requests_max_items
    import capo_waf.types.resource_id
    import capo_waf.types.time_window


class GetSampledRequestsRequest(TypedDict, closed=True):
    web_acl_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>WebACLId</code> of the <code>WebACL</code> for which you want <code>GetSampledRequests</code> to return a sample of requests.</p>"""
    rule_id: "capo_waf.types.resource_id.ResourceId"
    """<p> <code>RuleId</code> is one of three values:</p> <ul> <li> <p>The <code>RuleId</code> of the <code>Rule</code> or the <code>RuleGroupId</code> of the <code>RuleGroup</code> for which you want <code>GetSampledRequests</code> to return a sample of requests.</p> </li> <li> <p> <code>Default_Action</code>, which causes <code>GetSampledRequests</code> to return a sample of the requests that didn't match any of the rules in the specified <code>WebACL</code>.</p> </li> </ul>"""
    time_window: "capo_waf.types.time_window.TimeWindow"
    """<p>The start date and time and the end date and time of the range for which you want <code>GetSampledRequests</code> to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, <code>Z</code>. For example, <code>"2016-09-27T14:50Z"</code>. You can specify any time range in the previous three hours.</p>"""
    max_items: (
        "capo_waf.types.get_sampled_requests_max_items.GetSampledRequestsMaxItems"
    )
    """<p>The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of <code>MaxItems</code>, <code>GetSampledRequests</code> returns information about all of them. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSampledRequestsRequest) -> dict:
    out: dict = {}
    out["WebAclId"] = value["web_acl_id"]
    out["RuleId"] = value["rule_id"]
    import capo_waf.types.time_window

    out["TimeWindow"] = capo_waf.types.time_window.serialize_aws_json_1_1(
        value["time_window"]
    )
    out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSampledRequestsRequest:
    out: GetSampledRequestsRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebAclId") is not None:
        out["web_acl_id"] = data["WebAclId"]
    else:
        raise DeserializationError("GetSampledRequestsRequest.web_acl_id required")
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("GetSampledRequestsRequest.rule_id required")
    if data.get("TimeWindow") is not None:
        import capo_waf.types.time_window

        out["time_window"] = capo_waf.types.time_window.deserialize_aws_json_1_1(
            data["TimeWindow"]
        )
    else:
        raise DeserializationError("GetSampledRequestsRequest.time_window required")
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    else:
        raise DeserializationError("GetSampledRequestsRequest.max_items required")
    return out
