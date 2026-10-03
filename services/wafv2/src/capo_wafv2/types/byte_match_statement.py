"""Generated from Smithy shape ``com.amazonaws.wafv2#ByteMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_match
    import capo_wafv2.types.positional_constraint
    import capo_wafv2.types.pre_parse_text_transformations
    import capo_wafv2.types.search_string
    import capo_wafv2.types.text_transformations


class ByteMatchStatement(TypedDict, closed=True):
    search_string: "capo_wafv2.types.search_string.SearchString"
    """<p>A string value that you want WAF to search for. WAF searches only in the part of web requests that you designate for inspection in <a>FieldToMatch</a>. The maximum length of the value is 200 bytes.</p> <p>Valid values depend on the component that you specify for inspection in <code>FieldToMatch</code>:</p> <ul> <li> <p> <code>Method</code>: The HTTP method that you want WAF to search for. This indicates the type of operation specified in the request. </p> </li> <li> <p> <code>UriPath</code>: The value that you want WAF to search for in the URI path, for example, <code>/images/daily-ad.jpg</code>. </p> </li> <li> <p> <code>JA3Fingerprint</code>: Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the request's JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the client's TLS configuration. You can use this choice only with a string match <code>ByteMatchStatement</code> with the <code>PositionalConstraint</code> set to <code>EXACTLY</code>. </p> <p>You can obtain the JA3 fingerprint for client requests from the web ACL logs. If WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html">Log fields</a> in the <i>WAF Developer Guide</i>. </p> </li> <li> <p> <code>HeaderOrder</code>: The list of header names to match for. WAF creates a string that contains the ordered list of header names, from the headers in the web request, and then matches against that string. </p> </li> </ul> <p>If <code>SearchString</code> includes alphabetic characters A-Z and a-z, note that the value is case sensitive.</p> <p> <b>If you're using the WAF API</b> </p> <p>Specify a base64-encoded version of the value. The maximum length of the value before you base64-encode it is 200 bytes.</p> <p>For example, suppose the value of <code>Type</code> is <code>HEADER</code> and the value of <code>Data</code> is <code>User-Agent</code>. If you want to search the <code>User-Agent</code> header for the value <code>BadBot</code>, you base64-encode <code>BadBot</code> using MIME base64-encoding and include the resulting value, <code>QmFkQm90</code>, in the value of <code>SearchString</code>.</p> <p> <b>If you're using the CLI or one of the Amazon Web Services SDKs</b> </p> <p>The value that you want WAF to search for. The SDK automatically base64 encodes the value.</p>"""
    field_to_match: "capo_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    text_transformations: "capo_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""
    pre_parse_text_transformations: NotRequired[
        "capo_wafv2.types.pre_parse_text_transformations.PreParseTextTransformations"
    ]
    """<p>Pre-parse text transformations normalize the raw query string before WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when <code>FieldToMatch</code> is <code>SingleQueryArgument</code> or <code>AllQueryArguments</code>. You can specify up to 10 pre-parse text transformations per rule statement.</p>"""
    positional_constraint: "capo_wafv2.types.positional_constraint.PositionalConstraint"
    """<p>The area within the portion of the web request that you want WAF to search for <code>SearchString</code>. Valid values include the following:</p> <p> <b>CONTAINS</b> </p> <p>The specified part of the web request must include the value of <code>SearchString</code>, but the location doesn't matter.</p> <p> <b>CONTAINS_WORD</b> </p> <p>The specified part of the web request must include the value of <code>SearchString</code>, and <code>SearchString</code> must contain only alphanumeric characters or underscore (A-Z, a-z, 0-9, or _). In addition, <code>SearchString</code> must be a word, which means that both of the following are true:</p> <ul> <li> <p> <code>SearchString</code> is at the beginning of the specified part of the web request or is preceded by a character other than an alphanumeric character or underscore (_). Examples include the value of a header and <code>;BadBot</code>.</p> </li> <li> <p> <code>SearchString</code> is at the end of the specified part of the web request or is followed by a character other than an alphanumeric character or underscore (_), for example, <code>BadBot;</code> and <code>-BadBot;</code>.</p> </li> </ul> <p> <b>EXACTLY</b> </p> <p>The value of the specified part of the web request must exactly match the value of <code>SearchString</code>.</p> <p> <b>STARTS_WITH</b> </p> <p>The value of <code>SearchString</code> must appear at the beginning of the specified part of the web request.</p> <p> <b>ENDS_WITH</b> </p> <p>The value of <code>SearchString</code> must appear at the end of the specified part of the web request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.search_string

    out["SearchString"] = capo_wafv2.types.search_string.serialize_aws_json_1_1(
        value["search_string"]
    )
    import capo_wafv2.types.field_to_match

    out["FieldToMatch"] = capo_wafv2.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import capo_wafv2.types.text_transformations

    out["TextTransformations"] = (
        capo_wafv2.types.text_transformations.serialize_aws_json_1_1(
            value["text_transformations"]
        )
    )
    if "pre_parse_text_transformations" in value:
        import capo_wafv2.types.pre_parse_text_transformations

        out["PreParseTextTransformations"] = (
            capo_wafv2.types.pre_parse_text_transformations.serialize_aws_json_1_1(
                value["pre_parse_text_transformations"]
            )
        )
    import capo_wafv2.types.positional_constraint

    out["PositionalConstraint"] = (
        capo_wafv2.types.positional_constraint.serialize_aws_json_1_1(
            value["positional_constraint"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ByteMatchStatement:
    out: ByteMatchStatement = {}  # type: ignore[typeddict-item]
    if data.get("SearchString") is not None:
        import capo_wafv2.types.search_string

        out["search_string"] = capo_wafv2.types.search_string.deserialize_aws_json_1_1(
            data["SearchString"]
        )
    else:
        raise DeserializationError("ByteMatchStatement.search_string required")
    if data.get("FieldToMatch") is not None:
        import capo_wafv2.types.field_to_match

        out["field_to_match"] = (
            capo_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("ByteMatchStatement.field_to_match required")
    if data.get("TextTransformations") is not None:
        import capo_wafv2.types.text_transformations

        out["text_transformations"] = (
            capo_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError("ByteMatchStatement.text_transformations required")
    if data.get("PreParseTextTransformations") is not None:
        import capo_wafv2.types.pre_parse_text_transformations

        out["pre_parse_text_transformations"] = (
            capo_wafv2.types.pre_parse_text_transformations.deserialize_aws_json_1_1(
                data["PreParseTextTransformations"]
            )
        )
    if data.get("PositionalConstraint") is not None:
        import capo_wafv2.types.positional_constraint

        out["positional_constraint"] = (
            capo_wafv2.types.positional_constraint.deserialize_aws_json_1_1(
                data["PositionalConstraint"]
            )
        )
    else:
        raise DeserializationError("ByteMatchStatement.positional_constraint required")
    return out
