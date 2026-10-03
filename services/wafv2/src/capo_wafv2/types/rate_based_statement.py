"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.evaluation_window_sec
    import capo_wafv2.types.forwarded_ip_config
    import capo_wafv2.types.rate_based_statement_aggregate_key_type
    import capo_wafv2.types.rate_based_statement_custom_keys
    import capo_wafv2.types.rate_limit
    import capo_wafv2.types.statement


class RateBasedStatement(TypedDict, closed=True):
    limit: "capo_wafv2.types.rate_limit.RateLimit"
    """<p>The limit on requests during the specified evaluation window for a single aggregation instance for the rate-based rule. If the rate-based statement includes a <code>ScopeDownStatement</code>, this limit is applied only to the requests that match the statement.</p> <p>Examples: </p> <ul> <li> <p>If you aggregate on just the IP address, this is the limit on requests from any single IP address. </p> </li> <li> <p>If you aggregate on the HTTP method and the query argument name "city", then this is the limit on requests for any single method, city pair. </p> </li> </ul>"""
    evaluation_window_sec: "capo_wafv2.types.evaluation_window_sec.EvaluationWindowSec"
    """<p>The amount of time, in seconds, that WAF should include in its request counts, looking back from the current time. For example, for a setting of 120, when WAF checks the rate, it counts the requests for the 2 minutes immediately preceding the current time. Valid settings are 60, 120, 300, and 600. </p> <p>This setting doesn't determine how often WAF checks the rate, but how far back it looks each time it checks. WAF checks the rate about every 10 seconds.</p> <p>Default: <code>300</code> (5 minutes)</p>"""
    aggregate_key_type: "capo_wafv2.types.rate_based_statement_aggregate_key_type.RateBasedStatementAggregateKeyType"
    """<p>Setting that indicates how to aggregate the request counts. </p> <note> <p>Web requests that are missing any of the components specified in the aggregation keys are omitted from the rate-based rule evaluation and handling. </p> </note> <ul> <li> <p> <code>CONSTANT</code> - Count and limit the requests that match the rate-based rule's scope-down statement. With this option, the counted requests aren't further aggregated. The scope-down statement is the only specification used. When the count of all requests that satisfy the scope-down statement goes over the limit, WAF applies the rule action to all requests that satisfy the scope-down statement. </p> <p>With this option, you must configure the <code>ScopeDownStatement</code> property. </p> </li> <li> <p> <code>CUSTOM_KEYS</code> - Aggregate the request counts using one or more web request components as the aggregate keys.</p> <p>With this option, you must specify the aggregate keys in the <code>CustomKeys</code> property. </p> <p>To aggregate on only the IP address or only the forwarded IP address, don't use custom keys. Instead, set the aggregate key type to <code>IP</code> or <code>FORWARDED_IP</code>.</p> </li> <li> <p> <code>FORWARDED_IP</code> - Aggregate the request counts on the first IP address in an HTTP header. </p> <p>With this option, you must specify the header to use in the <code>ForwardedIPConfig</code> property. </p> <p>To aggregate on a combination of the forwarded IP address with other aggregate keys, use <code>CUSTOM_KEYS</code>. </p> </li> <li> <p> <code>IP</code> - Aggregate the request counts on the IP address from the web request origin.</p> <p>To aggregate on a combination of the IP address with other aggregate keys, use <code>CUSTOM_KEYS</code>. </p> </li> </ul>"""
    scope_down_statement: NotRequired["capo_wafv2.types.statement.Statement"]
    """<p>An optional nested statement that narrows the scope of the web requests that are evaluated and managed by the rate-based statement. When you use a scope-down statement, the rate-based rule only tracks and rate limits requests that match the scope-down statement. You can use any nestable <a>Statement</a> in the scope-down statement, and you can nest statements at any level, the same as you can for a rule statement. </p>"""
    forwarded_ip_config: NotRequired[
        "capo_wafv2.types.forwarded_ip_config.ForwardedIPConfig"
    ]
    """<p>The configuration for inspecting IP addresses in an HTTP header that you specify, instead of using the IP address that's reported by the web request origin. Commonly, this is the X-Forwarded-For (XFF) header, but you can specify any header name. </p> <note> <p>If the specified header isn't present in the request, WAF doesn't apply the rule to the web request at all.</p> </note> <p>This is required if you specify a forwarded IP in the rule's aggregate key settings. </p>"""
    custom_keys: NotRequired[
        "capo_wafv2.types.rate_based_statement_custom_keys.RateBasedStatementCustomKeys"
    ]
    """<p>Specifies the aggregate keys to use in a rate-base rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedStatement) -> dict:
    out: dict = {}
    out["Limit"] = value["limit"]
    out["EvaluationWindowSec"] = value.get("evaluation_window_sec", 0)
    import capo_wafv2.types.rate_based_statement_aggregate_key_type

    out["AggregateKeyType"] = (
        capo_wafv2.types.rate_based_statement_aggregate_key_type.serialize_aws_json_1_1(
            value["aggregate_key_type"]
        )
    )
    if "scope_down_statement" in value:
        import capo_wafv2.types.statement

        out["ScopeDownStatement"] = capo_wafv2.types.statement.serialize_aws_json_1_1(
            value["scope_down_statement"]
        )
    if "forwarded_ip_config" in value:
        import capo_wafv2.types.forwarded_ip_config

        out["ForwardedIPConfig"] = (
            capo_wafv2.types.forwarded_ip_config.serialize_aws_json_1_1(
                value["forwarded_ip_config"]
            )
        )
    if "custom_keys" in value:
        import capo_wafv2.types.rate_based_statement_custom_keys

        out["CustomKeys"] = (
            capo_wafv2.types.rate_based_statement_custom_keys.serialize_aws_json_1_1(
                value["custom_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RateBasedStatement:
    out: RateBasedStatement = {}  # type: ignore[typeddict-item]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    else:
        raise DeserializationError("RateBasedStatement.limit required")
    if data.get("EvaluationWindowSec") is not None:
        out["evaluation_window_sec"] = data["EvaluationWindowSec"]
    else:
        out["evaluation_window_sec"] = 0
    if data.get("AggregateKeyType") is not None:
        import capo_wafv2.types.rate_based_statement_aggregate_key_type

        out["aggregate_key_type"] = (
            capo_wafv2.types.rate_based_statement_aggregate_key_type.deserialize_aws_json_1_1(
                data["AggregateKeyType"]
            )
        )
    else:
        raise DeserializationError("RateBasedStatement.aggregate_key_type required")
    if data.get("ScopeDownStatement") is not None:
        import capo_wafv2.types.statement

        out["scope_down_statement"] = (
            capo_wafv2.types.statement.deserialize_aws_json_1_1(
                data["ScopeDownStatement"]
            )
        )
    if data.get("ForwardedIPConfig") is not None:
        import capo_wafv2.types.forwarded_ip_config

        out["forwarded_ip_config"] = (
            capo_wafv2.types.forwarded_ip_config.deserialize_aws_json_1_1(
                data["ForwardedIPConfig"]
            )
        )
    if data.get("CustomKeys") is not None:
        import capo_wafv2.types.rate_based_statement_custom_keys

        out["custom_keys"] = (
            capo_wafv2.types.rate_based_statement_custom_keys.deserialize_aws_json_1_1(
                data["CustomKeys"]
            )
        )
    return out
