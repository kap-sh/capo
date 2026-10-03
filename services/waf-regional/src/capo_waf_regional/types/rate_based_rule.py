"""Generated from Smithy shape ``com.amazonaws.wafregional#RateBasedRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.metric_name
    import capo_waf_regional.types.predicates
    import capo_waf_regional.types.rate_key
    import capo_waf_regional.types.rate_limit
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.resource_name


class RateBasedRule(TypedDict, closed=True):
    rule_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>RateBasedRule</code>. You use <code>RuleId</code> to get more information about a <code>RateBasedRule</code> (see <a>GetRateBasedRule</a>), update a <code>RateBasedRule</code> (see <a>UpdateRateBasedRule</a>), insert a <code>RateBasedRule</code> into a <code>WebACL</code> or delete one from a <code>WebACL</code> (see <a>UpdateWebACL</a>), or delete a <code>RateBasedRule</code> from AWS WAF (see <a>DeleteRateBasedRule</a>).</p>"""
    name: NotRequired["capo_waf_regional.types.resource_name.ResourceName"]
    """<p>A friendly name or description for a <code>RateBasedRule</code>. You can't change the name of a <code>RateBasedRule</code> after you create it.</p>"""
    metric_name: NotRequired["capo_waf_regional.types.metric_name.MetricName"]
    """<p>A friendly name or description for the metrics for a <code>RateBasedRule</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change the name of the metric after you create the <code>RateBasedRule</code>.</p>"""
    match_predicates: "capo_waf_regional.types.predicates.Predicates"
    """<p>The <code>Predicates</code> object contains one <code>Predicate</code> element for each <a>ByteMatchSet</a>, <a>IPSet</a>, or <a>SqlInjectionMatchSet</a> object that you want to include in a <code>RateBasedRule</code>.</p>"""
    rate_key: "capo_waf_regional.types.rate_key.RateKey"
    """<p>The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for <code>RateKey</code> is <code>IP</code>. <code>IP</code> indicates that requests arriving from the same IP address are subject to the <code>RateLimit</code> that is specified in the <code>RateBasedRule</code>.</p>"""
    rate_limit: "capo_waf_regional.types.rate_limit.RateLimit"
    """<p>The maximum number of requests, which have an identical value in the field specified by the <code>RateKey</code>, allowed in a five-minute period. If the number of requests exceeds the <code>RateLimit</code> and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedRule) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    import capo_waf_regional.types.predicates

    out["MatchPredicates"] = capo_waf_regional.types.predicates.serialize_aws_json_1_1(
        value["match_predicates"]
    )
    import capo_waf_regional.types.rate_key

    out["RateKey"] = capo_waf_regional.types.rate_key.serialize_aws_json_1_1(
        value["rate_key"]
    )
    out["RateLimit"] = value["rate_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RateBasedRule:
    out: RateBasedRule = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("RateBasedRule.rule_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("MatchPredicates") is not None:
        import capo_waf_regional.types.predicates

        out["match_predicates"] = (
            capo_waf_regional.types.predicates.deserialize_aws_json_1_1(
                data["MatchPredicates"]
            )
        )
    else:
        raise DeserializationError("RateBasedRule.match_predicates required")
    if data.get("RateKey") is not None:
        import capo_waf_regional.types.rate_key

        out["rate_key"] = capo_waf_regional.types.rate_key.deserialize_aws_json_1_1(
            data["RateKey"]
        )
    else:
        raise DeserializationError("RateBasedRule.rate_key required")
    if data.get("RateLimit") is not None:
        out["rate_limit"] = data["RateLimit"]
    else:
        raise DeserializationError("RateBasedRule.rate_limit required")
    return out
