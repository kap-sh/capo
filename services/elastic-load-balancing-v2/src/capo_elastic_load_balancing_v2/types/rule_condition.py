"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RuleCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.condition_field_name
    import capo_elastic_load_balancing_v2.types.host_header_condition_config
    import capo_elastic_load_balancing_v2.types.http_header_condition_config
    import capo_elastic_load_balancing_v2.types.http_request_method_condition_config
    import capo_elastic_load_balancing_v2.types.list_of_string
    import capo_elastic_load_balancing_v2.types.path_pattern_condition_config
    import capo_elastic_load_balancing_v2.types.query_string_condition_config
    import capo_elastic_load_balancing_v2.types.source_ip_condition_config


class RuleCondition(TypedDict, closed=True):
    field: NotRequired[
        "capo_elastic_load_balancing_v2.types.condition_field_name.ConditionFieldName"
    ]
    """<p>The name of the field. The possible values are:</p> <ul> <li> <p> <code>http-header</code> – [ALB] Matches on an HTTP header field.</p> </li> <li> <p> <code>http-request-method</code> – [ALB] Matches on the HTTP request method.</p> </li> <li> <p> <code>host-header</code> – [ALB] Matches on the host header.</p> </li> <li> <p> <code>path-pattern</code> – [ALB] Matches on the URL path of the request.</p> </li> <li> <p> <code>query-string</code> – [ALB] Matches on a query string parameter.</p> </li> <li> <p> <code>source-ip</code> – [ALB, NLB] Matches on the source IP address. For ALB, use <code>SourceIpConfig</code> with <code>Values</code> to specify CIDR ranges. For NLB, use <code>SourceIpConfig</code> with <code>IpAddressType</code> to match the IP address type (<code>ipv4</code> or <code>ipv6</code>).</p> </li> </ul>"""
    values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The condition value. Specify only when <code>Field</code> is <code>host-header</code> or <code>path-pattern</code>. Alternatively, to specify multiple host names or multiple path patterns, use <code>HostHeaderConfig</code> or <code>PathPatternConfig</code>.</p> <p>If <code>Field</code> is <code>host-header</code> and you are not using <code>HostHeaderConfig</code>, you can specify a single host name (for example, my.example.com) in <code>Values</code>. A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.</p> <ul> <li> <p>A-Z, a-z, 0-9</p> </li> <li> <p>- .</p> </li> <li> <p>* (matches 0 or more characters)</p> </li> <li> <p>? (matches exactly 1 character)</p> </li> </ul> <p>If <code>Field</code> is <code>path-pattern</code> and you are not using <code>PathPatternConfig</code>, you can specify a single path pattern (for example, /img/*) in <code>Values</code>. A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.</p> <ul> <li> <p>A-Z, a-z, 0-9</p> </li> <li> <p>_ - . $ / ~ " ' @ : +</p> </li> <li> <p>& (using &amp;)</p> </li> <li> <p>* (matches 0 or more characters)</p> </li> <li> <p>? (matches exactly 1 character)</p> </li> </ul>"""
    host_header_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.host_header_condition_config.HostHeaderConditionConfig"
    ]
    """<p>Information for a host header condition. Specify only when <code>Field</code> is <code>host-header</code>.</p>"""
    path_pattern_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.path_pattern_condition_config.PathPatternConditionConfig"
    ]
    """<p>Information for a path pattern condition. Specify only when <code>Field</code> is <code>path-pattern</code>.</p>"""
    http_header_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.http_header_condition_config.HttpHeaderConditionConfig"
    ]
    """<p>Information for an HTTP header condition. Specify only when <code>Field</code> is <code>http-header</code>.</p>"""
    query_string_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.query_string_condition_config.QueryStringConditionConfig"
    ]
    """<p>Information for a query string condition. Specify only when <code>Field</code> is <code>query-string</code>.</p>"""
    http_request_method_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.http_request_method_condition_config.HttpRequestMethodConditionConfig"
    ]
    """<p>Information for an HTTP method condition. Specify only when <code>Field</code> is <code>http-request-method</code>.</p>"""
    source_ip_config: NotRequired[
        "capo_elastic_load_balancing_v2.types.source_ip_condition_config.SourceIpConditionConfig"
    ]
    """<p>Information for a source IP condition. Specify only when <code>Field</code> is <code>source-ip</code>.</p>"""
    regex_values: NotRequired[
        "capo_elastic_load_balancing_v2.types.list_of_string.ListOfString"
    ]
    """<p>The regular expressions to match against the condition field. The maximum length of each string is 128 characters. Specify only when <code>Field</code> is <code>http-header</code>, <code>host-header</code>, or <code>path-pattern</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RuleCondition, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "field" in value:
        pairs.append((f"{key_prefix}Field", str(value["field"])))
    if "values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )
    if "host_header_config" in value:
        import capo_elastic_load_balancing_v2.types.host_header_condition_config

        capo_elastic_load_balancing_v2.types.host_header_condition_config.serialize_query(
            value["host_header_config"], pairs, f"{key_prefix}HostHeaderConfig"
        )
    if "path_pattern_config" in value:
        import capo_elastic_load_balancing_v2.types.path_pattern_condition_config

        capo_elastic_load_balancing_v2.types.path_pattern_condition_config.serialize_query(
            value["path_pattern_config"], pairs, f"{key_prefix}PathPatternConfig"
        )
    if "http_header_config" in value:
        import capo_elastic_load_balancing_v2.types.http_header_condition_config

        capo_elastic_load_balancing_v2.types.http_header_condition_config.serialize_query(
            value["http_header_config"], pairs, f"{key_prefix}HttpHeaderConfig"
        )
    if "query_string_config" in value:
        import capo_elastic_load_balancing_v2.types.query_string_condition_config

        capo_elastic_load_balancing_v2.types.query_string_condition_config.serialize_query(
            value["query_string_config"], pairs, f"{key_prefix}QueryStringConfig"
        )
    if "http_request_method_config" in value:
        import capo_elastic_load_balancing_v2.types.http_request_method_condition_config

        capo_elastic_load_balancing_v2.types.http_request_method_condition_config.serialize_query(
            value["http_request_method_config"],
            pairs,
            f"{key_prefix}HttpRequestMethodConfig",
        )
    if "source_ip_config" in value:
        import capo_elastic_load_balancing_v2.types.source_ip_condition_config

        capo_elastic_load_balancing_v2.types.source_ip_condition_config.serialize_query(
            value["source_ip_config"], pairs, f"{key_prefix}SourceIpConfig"
        )
    if "regex_values" in value:
        import capo_elastic_load_balancing_v2.types.list_of_string

        capo_elastic_load_balancing_v2.types.list_of_string.serialize_query(
            value["regex_values"], pairs, f"{key_prefix}RegexValues"
        )


def deserialize_query(el: Element) -> RuleCondition:
    out: RuleCondition = {}  # type: ignore[typeddict-item]
    child_field = el.find("Field")
    if child_field is not None:
        out["field"] = str(child_field.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_values
            )
        )
    child_host_header_config = el.find("HostHeaderConfig")
    if child_host_header_config is not None:
        import capo_elastic_load_balancing_v2.types.host_header_condition_config

        out["host_header_config"] = (
            capo_elastic_load_balancing_v2.types.host_header_condition_config.deserialize_query(
                child_host_header_config
            )
        )
    child_path_pattern_config = el.find("PathPatternConfig")
    if child_path_pattern_config is not None:
        import capo_elastic_load_balancing_v2.types.path_pattern_condition_config

        out["path_pattern_config"] = (
            capo_elastic_load_balancing_v2.types.path_pattern_condition_config.deserialize_query(
                child_path_pattern_config
            )
        )
    child_http_header_config = el.find("HttpHeaderConfig")
    if child_http_header_config is not None:
        import capo_elastic_load_balancing_v2.types.http_header_condition_config

        out["http_header_config"] = (
            capo_elastic_load_balancing_v2.types.http_header_condition_config.deserialize_query(
                child_http_header_config
            )
        )
    child_query_string_config = el.find("QueryStringConfig")
    if child_query_string_config is not None:
        import capo_elastic_load_balancing_v2.types.query_string_condition_config

        out["query_string_config"] = (
            capo_elastic_load_balancing_v2.types.query_string_condition_config.deserialize_query(
                child_query_string_config
            )
        )
    child_http_request_method_config = el.find("HttpRequestMethodConfig")
    if child_http_request_method_config is not None:
        import capo_elastic_load_balancing_v2.types.http_request_method_condition_config

        out["http_request_method_config"] = (
            capo_elastic_load_balancing_v2.types.http_request_method_condition_config.deserialize_query(
                child_http_request_method_config
            )
        )
    child_source_ip_config = el.find("SourceIpConfig")
    if child_source_ip_config is not None:
        import capo_elastic_load_balancing_v2.types.source_ip_condition_config

        out["source_ip_config"] = (
            capo_elastic_load_balancing_v2.types.source_ip_condition_config.deserialize_query(
                child_source_ip_config
            )
        )
    child_regex_values = el.find("RegexValues")
    if child_regex_values is not None:
        import capo_elastic_load_balancing_v2.types.list_of_string

        out["regex_values"] = (
            capo_elastic_load_balancing_v2.types.list_of_string.deserialize_query(
                child_regex_values
            )
        )
    return out
