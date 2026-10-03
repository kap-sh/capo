"""Generated from Smithy shape ``com.amazonaws.waf#CreateRateBasedRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.change_token
    import capo_waf.types.metric_name
    import capo_waf.types.rate_key
    import capo_waf.types.rate_limit
    import capo_waf.types.resource_name
    import capo_waf.types.tag_list


class CreateRateBasedRuleRequest(TypedDict, closed=True):
    name: "capo_waf.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>RateBasedRule</a>. You can't change the name of a <code>RateBasedRule</code> after you create it.</p>"""
    metric_name: "capo_waf.types.metric_name.MetricName"
    """<p>A friendly name or description for the metrics for this <code>RateBasedRule</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>RateBasedRule</code>.</p>"""
    rate_key: "capo_waf.types.rate_key.RateKey"
    """<p>The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for <code>RateKey</code> is <code>IP</code>. <code>IP</code> indicates that requests that arrive from the same IP address are subject to the <code>RateLimit</code> that is specified in the <code>RateBasedRule</code>.</p>"""
    rate_limit: "capo_waf.types.rate_limit.RateLimit"
    """<p>The maximum number of requests, which have an identical value in the field that is specified by <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>"""
    change_token: "capo_waf.types.change_token.ChangeToken"
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRateBasedRule</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""
    tags: NotRequired["capo_waf.types.tag_list.TagList"]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRateBasedRuleRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["MetricName"] = value["metric_name"]
    import capo_waf.types.rate_key

    out["RateKey"] = capo_waf.types.rate_key.serialize_aws_json_1_1(value["rate_key"])
    out["RateLimit"] = value["rate_limit"]
    out["ChangeToken"] = value["change_token"]
    if "tags" in value:
        import capo_waf.types.tag_list

        out["Tags"] = capo_waf.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRateBasedRuleRequest:
    out: CreateRateBasedRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRateBasedRuleRequest.name required")
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    else:
        raise DeserializationError("CreateRateBasedRuleRequest.metric_name required")
    if data.get("RateKey") is not None:
        import capo_waf.types.rate_key

        out["rate_key"] = capo_waf.types.rate_key.deserialize_aws_json_1_1(
            data["RateKey"]
        )
    else:
        raise DeserializationError("CreateRateBasedRuleRequest.rate_key required")
    if data.get("RateLimit") is not None:
        out["rate_limit"] = data["RateLimit"]
    else:
        raise DeserializationError("CreateRateBasedRuleRequest.rate_limit required")
    if data.get("ChangeToken") is not None:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("CreateRateBasedRuleRequest.change_token required")
    if data.get("Tags") is not None:
        import capo_waf.types.tag_list

        out["tags"] = capo_waf.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
