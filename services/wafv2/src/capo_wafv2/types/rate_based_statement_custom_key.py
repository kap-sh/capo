"""Generated from Smithy shape ``com.amazonaws.wafv2#RateBasedStatementCustomKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.rate_limit_asn
    import capo_wafv2.types.rate_limit_cookie
    import capo_wafv2.types.rate_limit_forwarded_ip
    import capo_wafv2.types.rate_limit_header
    import capo_wafv2.types.rate_limit_http_method
    import capo_wafv2.types.rate_limit_ip
    import capo_wafv2.types.rate_limit_ja3_fingerprint
    import capo_wafv2.types.rate_limit_ja4_fingerprint
    import capo_wafv2.types.rate_limit_label_namespace
    import capo_wafv2.types.rate_limit_query_argument
    import capo_wafv2.types.rate_limit_query_string
    import capo_wafv2.types.rate_limit_uri_path


class RateBasedStatementCustomKey(TypedDict, closed=True):
    header: NotRequired["capo_wafv2.types.rate_limit_header.RateLimitHeader"]
    """<p>Use the value of a header in the request as an aggregate key. Each distinct value in the header contributes to the aggregation instance. If you use a single header as your custom key, then each value fully defines an aggregation instance. </p>"""
    cookie: NotRequired["capo_wafv2.types.rate_limit_cookie.RateLimitCookie"]
    """<p>Use the value of a cookie in the request as an aggregate key. Each distinct value in the cookie contributes to the aggregation instance. If you use a single cookie as your custom key, then each value fully defines an aggregation instance. </p>"""
    query_argument: NotRequired[
        "capo_wafv2.types.rate_limit_query_argument.RateLimitQueryArgument"
    ]
    """<p>Use the specified query argument as an aggregate key. Each distinct value for the named query argument contributes to the aggregation instance. If you use a single query argument as your custom key, then each value fully defines an aggregation instance. </p>"""
    query_string: NotRequired[
        "capo_wafv2.types.rate_limit_query_string.RateLimitQueryString"
    ]
    """<p>Use the request's query string as an aggregate key. Each distinct string contributes to the aggregation instance. If you use just the query string as your custom key, then each string fully defines an aggregation instance. </p>"""
    http_method: NotRequired[
        "capo_wafv2.types.rate_limit_http_method.RateLimitHTTPMethod"
    ]
    """<p>Use the request's HTTP method as an aggregate key. Each distinct HTTP method contributes to the aggregation instance. If you use just the HTTP method as your custom key, then each method fully defines an aggregation instance. </p>"""
    forwarded_ip: NotRequired[
        "capo_wafv2.types.rate_limit_forwarded_ip.RateLimitForwardedIP"
    ]
    """<p>Use the first IP address in an HTTP header as an aggregate key. Each distinct forwarded IP address contributes to the aggregation instance.</p> <p>When you specify an IP or forwarded IP in the custom key settings, you must also specify at least one other key to use. You can aggregate on only the forwarded IP address by specifying <code>FORWARDED_IP</code> in your rate-based statement's <code>AggregateKeyType</code>. </p> <p>With this option, you must specify the header to use in the rate-based rule's <code>ForwardedIPConfig</code> property. </p>"""
    ip: NotRequired["capo_wafv2.types.rate_limit_ip.RateLimitIP"]
    """<p>Use the request's originating IP address as an aggregate key. Each distinct IP address contributes to the aggregation instance.</p> <p>When you specify an IP or forwarded IP in the custom key settings, you must also specify at least one other key to use. You can aggregate on only the IP address by specifying <code>IP</code> in your rate-based statement's <code>AggregateKeyType</code>. </p>"""
    label_namespace: NotRequired[
        "capo_wafv2.types.rate_limit_label_namespace.RateLimitLabelNamespace"
    ]
    """<p>Use the specified label namespace as an aggregate key. Each distinct fully qualified label name that has the specified label namespace contributes to the aggregation instance. If you use just one label namespace as your custom key, then each label name fully defines an aggregation instance. </p> <p>This uses only labels that have been added to the request by rules that are evaluated before this rate-based rule in the web ACL. </p> <p>For information about label namespaces and names, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-requirements.html">Label syntax and naming requirements</a> in the <i>WAF Developer Guide</i>.</p>"""
    uri_path: NotRequired["capo_wafv2.types.rate_limit_uri_path.RateLimitUriPath"]
    """<p>Use the request's URI path as an aggregate key. Each distinct URI path contributes to the aggregation instance. If you use just the URI path as your custom key, then each URI path fully defines an aggregation instance. </p>"""
    ja3_fingerprint: NotRequired[
        "capo_wafv2.types.rate_limit_ja3_fingerprint.RateLimitJA3Fingerprint"
    ]
    """<p> Use the request's JA3 fingerprint as an aggregate key. If you use a single JA3 fingerprint as your custom key, then each value fully defines an aggregation instance. </p>"""
    ja4_fingerprint: NotRequired[
        "capo_wafv2.types.rate_limit_ja4_fingerprint.RateLimitJA4Fingerprint"
    ]
    """<p>Use the request's JA4 fingerprint as an aggregate key. If you use a single JA4 fingerprint as your custom key, then each value fully defines an aggregation instance. </p>"""
    asn: NotRequired["capo_wafv2.types.rate_limit_asn.RateLimitAsn"]
    """<p>Use an Autonomous System Number (ASN) derived from the request's originating or forwarded IP address as an aggregate key. Each distinct ASN contributes to the aggregation instance. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateBasedStatementCustomKey) -> dict:
    out: dict = {}
    if "header" in value:
        import capo_wafv2.types.rate_limit_header

        out["Header"] = capo_wafv2.types.rate_limit_header.serialize_aws_json_1_1(
            value["header"]
        )
    if "cookie" in value:
        import capo_wafv2.types.rate_limit_cookie

        out["Cookie"] = capo_wafv2.types.rate_limit_cookie.serialize_aws_json_1_1(
            value["cookie"]
        )
    if "query_argument" in value:
        import capo_wafv2.types.rate_limit_query_argument

        out["QueryArgument"] = (
            capo_wafv2.types.rate_limit_query_argument.serialize_aws_json_1_1(
                value["query_argument"]
            )
        )
    if "query_string" in value:
        import capo_wafv2.types.rate_limit_query_string

        out["QueryString"] = (
            capo_wafv2.types.rate_limit_query_string.serialize_aws_json_1_1(
                value["query_string"]
            )
        )
    if "http_method" in value:
        import capo_wafv2.types.rate_limit_http_method

        out["HTTPMethod"] = (
            capo_wafv2.types.rate_limit_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "forwarded_ip" in value:
        import capo_wafv2.types.rate_limit_forwarded_ip

        out["ForwardedIP"] = (
            capo_wafv2.types.rate_limit_forwarded_ip.serialize_aws_json_1_1(
                value["forwarded_ip"]
            )
        )
    if "ip" in value:
        import capo_wafv2.types.rate_limit_ip

        out["IP"] = capo_wafv2.types.rate_limit_ip.serialize_aws_json_1_1(value["ip"])
    if "label_namespace" in value:
        import capo_wafv2.types.rate_limit_label_namespace

        out["LabelNamespace"] = (
            capo_wafv2.types.rate_limit_label_namespace.serialize_aws_json_1_1(
                value["label_namespace"]
            )
        )
    if "uri_path" in value:
        import capo_wafv2.types.rate_limit_uri_path

        out["UriPath"] = capo_wafv2.types.rate_limit_uri_path.serialize_aws_json_1_1(
            value["uri_path"]
        )
    if "ja3_fingerprint" in value:
        import capo_wafv2.types.rate_limit_ja3_fingerprint

        out["JA3Fingerprint"] = (
            capo_wafv2.types.rate_limit_ja3_fingerprint.serialize_aws_json_1_1(
                value["ja3_fingerprint"]
            )
        )
    if "ja4_fingerprint" in value:
        import capo_wafv2.types.rate_limit_ja4_fingerprint

        out["JA4Fingerprint"] = (
            capo_wafv2.types.rate_limit_ja4_fingerprint.serialize_aws_json_1_1(
                value["ja4_fingerprint"]
            )
        )
    if "asn" in value:
        import capo_wafv2.types.rate_limit_asn

        out["ASN"] = capo_wafv2.types.rate_limit_asn.serialize_aws_json_1_1(
            value["asn"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RateBasedStatementCustomKey:
    out: RateBasedStatementCustomKey = {}  # type: ignore[typeddict-item]
    if data.get("Header") is not None:
        import capo_wafv2.types.rate_limit_header

        out["header"] = capo_wafv2.types.rate_limit_header.deserialize_aws_json_1_1(
            data["Header"]
        )
    if data.get("Cookie") is not None:
        import capo_wafv2.types.rate_limit_cookie

        out["cookie"] = capo_wafv2.types.rate_limit_cookie.deserialize_aws_json_1_1(
            data["Cookie"]
        )
    if data.get("QueryArgument") is not None:
        import capo_wafv2.types.rate_limit_query_argument

        out["query_argument"] = (
            capo_wafv2.types.rate_limit_query_argument.deserialize_aws_json_1_1(
                data["QueryArgument"]
            )
        )
    if data.get("QueryString") is not None:
        import capo_wafv2.types.rate_limit_query_string

        out["query_string"] = (
            capo_wafv2.types.rate_limit_query_string.deserialize_aws_json_1_1(
                data["QueryString"]
            )
        )
    if data.get("HTTPMethod") is not None:
        import capo_wafv2.types.rate_limit_http_method

        out["http_method"] = (
            capo_wafv2.types.rate_limit_http_method.deserialize_aws_json_1_1(
                data["HTTPMethod"]
            )
        )
    if data.get("ForwardedIP") is not None:
        import capo_wafv2.types.rate_limit_forwarded_ip

        out["forwarded_ip"] = (
            capo_wafv2.types.rate_limit_forwarded_ip.deserialize_aws_json_1_1(
                data["ForwardedIP"]
            )
        )
    if data.get("IP") is not None:
        import capo_wafv2.types.rate_limit_ip

        out["ip"] = capo_wafv2.types.rate_limit_ip.deserialize_aws_json_1_1(data["IP"])
    if data.get("LabelNamespace") is not None:
        import capo_wafv2.types.rate_limit_label_namespace

        out["label_namespace"] = (
            capo_wafv2.types.rate_limit_label_namespace.deserialize_aws_json_1_1(
                data["LabelNamespace"]
            )
        )
    if data.get("UriPath") is not None:
        import capo_wafv2.types.rate_limit_uri_path

        out["uri_path"] = capo_wafv2.types.rate_limit_uri_path.deserialize_aws_json_1_1(
            data["UriPath"]
        )
    if data.get("JA3Fingerprint") is not None:
        import capo_wafv2.types.rate_limit_ja3_fingerprint

        out["ja3_fingerprint"] = (
            capo_wafv2.types.rate_limit_ja3_fingerprint.deserialize_aws_json_1_1(
                data["JA3Fingerprint"]
            )
        )
    if data.get("JA4Fingerprint") is not None:
        import capo_wafv2.types.rate_limit_ja4_fingerprint

        out["ja4_fingerprint"] = (
            capo_wafv2.types.rate_limit_ja4_fingerprint.deserialize_aws_json_1_1(
                data["JA4Fingerprint"]
            )
        )
    if data.get("ASN") is not None:
        import capo_wafv2.types.rate_limit_asn

        out["asn"] = capo_wafv2.types.rate_limit_asn.deserialize_aws_json_1_1(
            data["ASN"]
        )
    return out
