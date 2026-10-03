"""Generated from Smithy shape ``com.amazonaws.waf#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.metric_name
    import capo_waf.types.predicates
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class Rule(TypedDict, closed=True):
    rule_id: "capo_waf.types.resource_id.ResourceId"
    """<p>A unique identifier for a <code>Rule</code>. You use <code>RuleId</code> to get more information about a <code>Rule</code> (see <a>GetRule</a>), update a <code>Rule</code> (see <a>UpdateRule</a>), insert a <code>Rule</code> into a <code>WebACL</code> or delete a one from a <code>WebACL</code> (see <a>UpdateWebACL</a>), or delete a <code>Rule</code> from AWS WAF (see <a>DeleteRule</a>).</p> <p> <code>RuleId</code> is returned by <a>CreateRule</a> and by <a>ListRules</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>The friendly name or description for the <code>Rule</code>. You can't change the name of a <code>Rule</code> after you create it.</p>"""
    metric_name: NotRequired["capo_waf.types.metric_name.MetricName"]
    """<p>A friendly name or description for the metrics for this <code>Rule</code>. The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It can't contain whitespace or metric names reserved for AWS WAF, including "All" and "Default_Action." You can't change <code>MetricName</code> after you create the <code>Rule</code>.</p>"""
    predicates: "capo_waf.types.predicates.Predicates"
    """<p>The <code>Predicates</code> object contains one <code>Predicate</code> element for each <a>ByteMatchSet</a>, <a>IPSet</a>, or <a>SqlInjectionMatchSet</a> object that you want to include in a <code>Rule</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Rule) -> dict:
    out: dict = {}
    out["RuleId"] = value["rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    import capo_waf.types.predicates

    out["Predicates"] = capo_waf.types.predicates.serialize_aws_json_1_1(
        value["predicates"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("RuleId") is not None:
        out["rule_id"] = data["RuleId"]
    else:
        raise DeserializationError("Rule.rule_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("MetricName") is not None:
        out["metric_name"] = data["MetricName"]
    if data.get("Predicates") is not None:
        import capo_waf.types.predicates

        out["predicates"] = capo_waf.types.predicates.deserialize_aws_json_1_1(
            data["Predicates"]
        )
    else:
        raise DeserializationError("Rule.predicates required")
    return out
