"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToMatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.all_query_arguments
    import capo_wafv2.types.body
    import capo_wafv2.types.cookies
    import capo_wafv2.types.header_order
    import capo_wafv2.types.headers
    import capo_wafv2.types.ja3_fingerprint
    import capo_wafv2.types.ja4_fingerprint
    import capo_wafv2.types.json_body
    import capo_wafv2.types.method
    import capo_wafv2.types.query_string
    import capo_wafv2.types.single_header
    import capo_wafv2.types.single_query_argument
    import capo_wafv2.types.uri_fragment
    import capo_wafv2.types.uri_path


class FieldToMatch(TypedDict, closed=True):
    single_header: NotRequired["capo_wafv2.types.single_header.SingleHeader"]
    """<p>Inspect a single header. Provide the name of the header to inspect, for example, <code>User-Agent</code> or <code>Referer</code>. This setting isn't case sensitive.</p> <p>Example JSON: <code>"SingleHeader": { "Name": "haystack" }</code> </p> <p>Alternately, you can filter and inspect all headers with the <code>Headers</code> <code>FieldToMatch</code> setting. </p>"""
    single_query_argument: NotRequired[
        "capo_wafv2.types.single_query_argument.SingleQueryArgument"
    ]
    """<p>Inspect a single query argument. Provide the name of the query argument to inspect, such as <i>UserName</i> or <i>SalesRegion</i>. The name can be up to 30 characters long and isn't case sensitive. </p> <p>Example JSON: <code>"SingleQueryArgument": { "Name": "myArgument" }</code> </p>"""
    all_query_arguments: NotRequired[
        "capo_wafv2.types.all_query_arguments.AllQueryArguments"
    ]
    """<p>Inspect all query arguments. </p>"""
    uri_path: NotRequired["capo_wafv2.types.uri_path.UriPath"]
    """<p>Inspect the request URI path. This is the part of the web request that identifies a resource, for example, <code>/images/daily-ad.jpg</code>.</p>"""
    query_string: NotRequired["capo_wafv2.types.query_string.QueryString"]
    """<p>Inspect the query string. This is the part of a URL that appears after a <code>?</code> character, if any.</p>"""
    body: NotRequired["capo_wafv2.types.body.Body"]
    """<p>Inspect the request body as plain text. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. </p> <p>WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection. </p> <ul> <li> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p> </li> <li> <p>For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL <code>AssociationConfig</code>, for additional processing fees. </p> </li> <li> <p>For Amplify, use the CloudFront limit.</p> </li> </ul> <p>For information about how to handle oversized request bodies, see the <code>Body</code> object configuration. </p>"""
    method: NotRequired["capo_wafv2.types.method.Method"]
    """<p>Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform. </p>"""
    json_body: NotRequired["capo_wafv2.types.json_body.JsonBody"]
    """<p>Inspect the request body as JSON. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form. </p> <p>WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection. </p> <ul> <li> <p>For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).</p> </li> <li> <p>For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL <code>AssociationConfig</code>, for additional processing fees. </p> </li> <li> <p>For Amplify, use the CloudFront limit.</p> </li> </ul> <p>For information about how to handle oversized request bodies, see the <code>JsonBody</code> object configuration. </p>"""
    headers: NotRequired["capo_wafv2.types.headers.Headers"]
    """<p>Inspect the request headers. You must configure scope and pattern matching filters in the <code>Headers</code> object, to define the set of headers to and the parts of the headers that WAF inspects. </p> <p>Only the first 8 KB (8192 bytes) of a request's headers and only the first 200 headers are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize header content in the <code>Headers</code> object. WAF applies the pattern matching filters to the headers that it receives from the underlying host service. </p>"""
    cookies: NotRequired["capo_wafv2.types.cookies.Cookies"]
    """<p>Inspect the request cookies. You must configure scope and pattern matching filters in the <code>Cookies</code> object, to define the set of cookies and the parts of the cookies that WAF inspects. </p> <p>Only the first 8 KB (8192 bytes) of a request's cookies and only the first 200 cookies are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize cookie content in the <code>Cookies</code> object. WAF applies the pattern matching filters to the cookies that it receives from the underlying host service. </p>"""
    header_order: NotRequired["capo_wafv2.types.header_order.HeaderOrder"]
    """<p>Inspect a string containing the list of the request's header names, ordered as they appear in the web request that WAF receives for inspection. WAF generates the string and then uses that as the field to match component in its inspection. WAF separates the header names in the string using colons and no added spaces, for example <code>host:user-agent:accept:authorization:referer</code>.</p>"""
    ja3_fingerprint: NotRequired["capo_wafv2.types.ja3_fingerprint.JA3Fingerprint"]
    """<p>Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.</p> <note> <p>You can use this choice only with a string match <code>ByteMatchStatement</code> with the <code>PositionalConstraint</code> set to <code>EXACTLY</code>. </p> </note> <p>You can obtain the JA3 fingerprint for client requests from the web ACL logs. If WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html">Log fields</a> in the <i>WAF Developer Guide</i>. </p> <p>Provide the JA3 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.</p>"""
    ja4_fingerprint: NotRequired["capo_wafv2.types.ja4_fingerprint.JA4Fingerprint"]
    """<p>Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA4 fingerprint. The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.</p> <note> <p>You can use this choice only with a string match <code>ByteMatchStatement</code> with the <code>PositionalConstraint</code> set to <code>EXACTLY</code>. </p> </note> <p>You can obtain the JA4 fingerprint for client requests from the web ACL logs. If WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html">Log fields</a> in the <i>WAF Developer Guide</i>. </p> <p>Provide the JA4 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.</p>"""
    uri_fragment: NotRequired["capo_wafv2.types.uri_fragment.UriFragment"]
    """<p>Inspect fragments of the request URI. You must configure scope and pattern matching filters in the <code>UriFragment</code> object, to define the fragment of a URI that WAF inspects. </p> <p>Only the first 8 KB (8192 bytes) of a request's URI fragments and only the first 200 URI fragments are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize URI fragment content in the <code>UriFragment</code> object. WAF applies the pattern matching filters to the cookies that it receives from the underlying host service. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldToMatch) -> dict:
    out: dict = {}
    if "single_header" in value:
        import capo_wafv2.types.single_header

        out["SingleHeader"] = capo_wafv2.types.single_header.serialize_aws_json_1_1(
            value["single_header"]
        )
    if "single_query_argument" in value:
        import capo_wafv2.types.single_query_argument

        out["SingleQueryArgument"] = (
            capo_wafv2.types.single_query_argument.serialize_aws_json_1_1(
                value["single_query_argument"]
            )
        )
    if "all_query_arguments" in value:
        import capo_wafv2.types.all_query_arguments

        out["AllQueryArguments"] = (
            capo_wafv2.types.all_query_arguments.serialize_aws_json_1_1(
                value["all_query_arguments"]
            )
        )
    if "uri_path" in value:
        import capo_wafv2.types.uri_path

        out["UriPath"] = capo_wafv2.types.uri_path.serialize_aws_json_1_1(
            value["uri_path"]
        )
    if "query_string" in value:
        import capo_wafv2.types.query_string

        out["QueryString"] = capo_wafv2.types.query_string.serialize_aws_json_1_1(
            value["query_string"]
        )
    if "body" in value:
        import capo_wafv2.types.body

        out["Body"] = capo_wafv2.types.body.serialize_aws_json_1_1(value["body"])
    if "method" in value:
        import capo_wafv2.types.method

        out["Method"] = capo_wafv2.types.method.serialize_aws_json_1_1(value["method"])
    if "json_body" in value:
        import capo_wafv2.types.json_body

        out["JsonBody"] = capo_wafv2.types.json_body.serialize_aws_json_1_1(
            value["json_body"]
        )
    if "headers" in value:
        import capo_wafv2.types.headers

        out["Headers"] = capo_wafv2.types.headers.serialize_aws_json_1_1(
            value["headers"]
        )
    if "cookies" in value:
        import capo_wafv2.types.cookies

        out["Cookies"] = capo_wafv2.types.cookies.serialize_aws_json_1_1(
            value["cookies"]
        )
    if "header_order" in value:
        import capo_wafv2.types.header_order

        out["HeaderOrder"] = capo_wafv2.types.header_order.serialize_aws_json_1_1(
            value["header_order"]
        )
    if "ja3_fingerprint" in value:
        import capo_wafv2.types.ja3_fingerprint

        out["JA3Fingerprint"] = capo_wafv2.types.ja3_fingerprint.serialize_aws_json_1_1(
            value["ja3_fingerprint"]
        )
    if "ja4_fingerprint" in value:
        import capo_wafv2.types.ja4_fingerprint

        out["JA4Fingerprint"] = capo_wafv2.types.ja4_fingerprint.serialize_aws_json_1_1(
            value["ja4_fingerprint"]
        )
    if "uri_fragment" in value:
        import capo_wafv2.types.uri_fragment

        out["UriFragment"] = capo_wafv2.types.uri_fragment.serialize_aws_json_1_1(
            value["uri_fragment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldToMatch:
    out: FieldToMatch = {}  # type: ignore[typeddict-item]
    if data.get("SingleHeader") is not None:
        import capo_wafv2.types.single_header

        out["single_header"] = capo_wafv2.types.single_header.deserialize_aws_json_1_1(
            data["SingleHeader"]
        )
    if data.get("SingleQueryArgument") is not None:
        import capo_wafv2.types.single_query_argument

        out["single_query_argument"] = (
            capo_wafv2.types.single_query_argument.deserialize_aws_json_1_1(
                data["SingleQueryArgument"]
            )
        )
    if data.get("AllQueryArguments") is not None:
        import capo_wafv2.types.all_query_arguments

        out["all_query_arguments"] = (
            capo_wafv2.types.all_query_arguments.deserialize_aws_json_1_1(
                data["AllQueryArguments"]
            )
        )
    if data.get("UriPath") is not None:
        import capo_wafv2.types.uri_path

        out["uri_path"] = capo_wafv2.types.uri_path.deserialize_aws_json_1_1(
            data["UriPath"]
        )
    if data.get("QueryString") is not None:
        import capo_wafv2.types.query_string

        out["query_string"] = capo_wafv2.types.query_string.deserialize_aws_json_1_1(
            data["QueryString"]
        )
    if data.get("Body") is not None:
        import capo_wafv2.types.body

        out["body"] = capo_wafv2.types.body.deserialize_aws_json_1_1(data["Body"])
    if data.get("Method") is not None:
        import capo_wafv2.types.method

        out["method"] = capo_wafv2.types.method.deserialize_aws_json_1_1(data["Method"])
    if data.get("JsonBody") is not None:
        import capo_wafv2.types.json_body

        out["json_body"] = capo_wafv2.types.json_body.deserialize_aws_json_1_1(
            data["JsonBody"]
        )
    if data.get("Headers") is not None:
        import capo_wafv2.types.headers

        out["headers"] = capo_wafv2.types.headers.deserialize_aws_json_1_1(
            data["Headers"]
        )
    if data.get("Cookies") is not None:
        import capo_wafv2.types.cookies

        out["cookies"] = capo_wafv2.types.cookies.deserialize_aws_json_1_1(
            data["Cookies"]
        )
    if data.get("HeaderOrder") is not None:
        import capo_wafv2.types.header_order

        out["header_order"] = capo_wafv2.types.header_order.deserialize_aws_json_1_1(
            data["HeaderOrder"]
        )
    if data.get("JA3Fingerprint") is not None:
        import capo_wafv2.types.ja3_fingerprint

        out["ja3_fingerprint"] = (
            capo_wafv2.types.ja3_fingerprint.deserialize_aws_json_1_1(
                data["JA3Fingerprint"]
            )
        )
    if data.get("JA4Fingerprint") is not None:
        import capo_wafv2.types.ja4_fingerprint

        out["ja4_fingerprint"] = (
            capo_wafv2.types.ja4_fingerprint.deserialize_aws_json_1_1(
                data["JA4Fingerprint"]
            )
        )
    if data.get("UriFragment") is not None:
        import capo_wafv2.types.uri_fragment

        out["uri_fragment"] = capo_wafv2.types.uri_fragment.deserialize_aws_json_1_1(
            data["UriFragment"]
        )
    return out
