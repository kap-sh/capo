"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchTuple``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.field_to_match
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.text_transformation


class RegexMatchTuple(TypedDict, closed=True):
    field_to_match: "capo_waf_regional.types.field_to_match.FieldToMatch"
    """<p>Specifies where in a web request to look for the <code>RegexPatternSet</code>.</p>"""
    text_transformation: (
        "capo_waf_regional.types.text_transformation.TextTransformation"
    )
    r"""<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on <code>RegexPatternSet</code> before inspecting a request for a match.</p> <p>You can only specify a single type of TextTransformation.</p> <p> <b>CMD_LINE</b> </p> <p>When you're concerned that attackers are injecting an operating system commandline command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:</p> <ul> <li> <p>Delete the following characters: \ " ' ^</p> </li> <li> <p>Delete spaces before the following characters: / (</p> </li> <li> <p>Replace the following characters with a space: , ;</p> </li> <li> <p>Replace multiple spaces with one space</p> </li> <li> <p>Convert uppercase letters (A-Z) to lowercase (a-z)</p> </li> </ul> <p> <b>COMPRESS_WHITE_SPACE</b> </p> <p>Use this option to replace the following characters with a space character (decimal 32):</p> <ul> <li> <p>\f, formfeed, decimal 12</p> </li> <li> <p>\t, tab, decimal 9</p> </li> <li> <p>\n, newline, decimal 10</p> </li> <li> <p>\r, carriage return, decimal 13</p> </li> <li> <p>\v, vertical tab, decimal 11</p> </li> <li> <p>non-breaking space, decimal 160</p> </li> </ul> <p> <code>COMPRESS_WHITE_SPACE</code> also replaces multiple spaces with one space.</p> <p> <b>HTML_ENTITY_DECODE</b> </p> <p>Use this option to replace HTML-encoded characters with unencoded characters. <code>HTML_ENTITY_DECODE</code> performs the following operations:</p> <ul> <li> <p>Replaces <code>(ampersand)quot;</code> with <code>"</code> </p> </li> <li> <p>Replaces <code>(ampersand)nbsp;</code> with a non-breaking space, decimal 160</p> </li> <li> <p>Replaces <code>(ampersand)lt;</code> with a "less than" symbol</p> </li> <li> <p>Replaces <code>(ampersand)gt;</code> with <code>></code> </p> </li> <li> <p>Replaces characters that are represented in hexadecimal format, <code>(ampersand)#xhhhh;</code>, with the corresponding characters</p> </li> <li> <p>Replaces characters that are represented in decimal format, <code>(ampersand)#nnnn;</code>, with the corresponding characters</p> </li> </ul> <p> <b>LOWERCASE</b> </p> <p>Use this option to convert uppercase letters (A-Z) to lowercase (a-z).</p> <p> <b>URL_DECODE</b> </p> <p>Use this option to decode a URL-encoded value.</p> <p> <b>NONE</b> </p> <p>Specify <code>NONE</code> if you don't want to perform any text transformations.</p>"""
    regex_pattern_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> for a <code>RegexPatternSet</code>. You use <code>RegexPatternSetId</code> to get information about a <code>RegexPatternSet</code> (see <a>GetRegexPatternSet</a>), update a <code>RegexPatternSet</code> (see <a>UpdateRegexPatternSet</a>), insert a <code>RegexPatternSet</code> into a <code>RegexMatchSet</code> or delete one from a <code>RegexMatchSet</code> (see <a>UpdateRegexMatchSet</a>), and delete an <code>RegexPatternSet</code> from AWS WAF (see <a>DeleteRegexPatternSet</a>).</p> <p> <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchTuple) -> dict:
    out: dict = {}
    import capo_waf_regional.types.field_to_match

    out["FieldToMatch"] = capo_waf_regional.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import capo_waf_regional.types.text_transformation

    out["TextTransformation"] = (
        capo_waf_regional.types.text_transformation.serialize_aws_json_1_1(
            value["text_transformation"]
        )
    )
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchTuple:
    out: RegexMatchTuple = {}  # type: ignore[typeddict-item]
    if data.get("FieldToMatch") is not None:
        import capo_waf_regional.types.field_to_match

        out["field_to_match"] = (
            capo_waf_regional.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("RegexMatchTuple.field_to_match required")
    if data.get("TextTransformation") is not None:
        import capo_waf_regional.types.text_transformation

        out["text_transformation"] = (
            capo_waf_regional.types.text_transformation.deserialize_aws_json_1_1(
                data["TextTransformation"]
            )
        )
    else:
        raise DeserializationError("RegexMatchTuple.text_transformation required")
    if data.get("RegexPatternSetId") is not None:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        raise DeserializationError("RegexMatchTuple.regex_pattern_set_id required")
    return out
