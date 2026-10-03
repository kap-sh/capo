"""Generated from Smithy shape ``com.amazonaws.waf#SizeConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.comparison_operator
    import capo_waf.types.field_to_match
    import capo_waf.types.size
    import capo_waf.types.text_transformation


class SizeConstraint(TypedDict, closed=True):
    field_to_match: "capo_waf.types.field_to_match.FieldToMatch"
    """<p>Specifies where in a web request to look for the size constraint.</p>"""
    text_transformation: "capo_waf.types.text_transformation.TextTransformation"
    r"""<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass AWS WAF. If you specify a transformation, AWS WAF performs the transformation on <code>FieldToMatch</code> before inspecting it for a match.</p> <p>You can only specify a single type of TextTransformation.</p> <p>Note that if you choose <code>BODY</code> for the value of <code>Type</code>, you must choose <code>NONE</code> for <code>TextTransformation</code> because CloudFront forwards only the first 8192 bytes for inspection. </p> <p> <b>NONE</b> </p> <p>Specify <code>NONE</code> if you don't want to perform any text transformations.</p> <p> <b>CMD_LINE</b> </p> <p>When you're concerned that attackers are injecting an operating system command line command and using unusual formatting to disguise some or all of the command, use this option to perform the following transformations:</p> <ul> <li> <p>Delete the following characters: \ " ' ^</p> </li> <li> <p>Delete spaces before the following characters: / (</p> </li> <li> <p>Replace the following characters with a space: , ;</p> </li> <li> <p>Replace multiple spaces with one space</p> </li> <li> <p>Convert uppercase letters (A-Z) to lowercase (a-z)</p> </li> </ul> <p> <b>COMPRESS_WHITE_SPACE</b> </p> <p>Use this option to replace the following characters with a space character (decimal 32):</p> <ul> <li> <p>\f, formfeed, decimal 12</p> </li> <li> <p>\t, tab, decimal 9</p> </li> <li> <p>\n, newline, decimal 10</p> </li> <li> <p>\r, carriage return, decimal 13</p> </li> <li> <p>\v, vertical tab, decimal 11</p> </li> <li> <p>non-breaking space, decimal 160</p> </li> </ul> <p> <code>COMPRESS_WHITE_SPACE</code> also replaces multiple spaces with one space.</p> <p> <b>HTML_ENTITY_DECODE</b> </p> <p>Use this option to replace HTML-encoded characters with unencoded characters. <code>HTML_ENTITY_DECODE</code> performs the following operations:</p> <ul> <li> <p>Replaces <code>(ampersand)quot;</code> with <code>"</code> </p> </li> <li> <p>Replaces <code>(ampersand)nbsp;</code> with a non-breaking space, decimal 160</p> </li> <li> <p>Replaces <code>(ampersand)lt;</code> with a "less than" symbol</p> </li> <li> <p>Replaces <code>(ampersand)gt;</code> with <code>></code> </p> </li> <li> <p>Replaces characters that are represented in hexadecimal format, <code>(ampersand)#xhhhh;</code>, with the corresponding characters</p> </li> <li> <p>Replaces characters that are represented in decimal format, <code>(ampersand)#nnnn;</code>, with the corresponding characters</p> </li> </ul> <p> <b>LOWERCASE</b> </p> <p>Use this option to convert uppercase letters (A-Z) to lowercase (a-z).</p> <p> <b>URL_DECODE</b> </p> <p>Use this option to decode a URL-encoded value.</p>"""
    comparison_operator: "capo_waf.types.comparison_operator.ComparisonOperator"
    """<p>The type of comparison you want AWS WAF to perform. AWS WAF uses this in combination with the provided <code>Size</code> and <code>FieldToMatch</code> to build an expression in the form of "<code>Size</code> <code>ComparisonOperator</code> size in bytes of <code>FieldToMatch</code>". If that expression is true, the <code>SizeConstraint</code> is considered to match.</p> <p> <b>EQ</b>: Used to test if the <code>Size</code> is equal to the size of the <code>FieldToMatch</code> </p> <p> <b>NE</b>: Used to test if the <code>Size</code> is not equal to the size of the <code>FieldToMatch</code> </p> <p> <b>LE</b>: Used to test if the <code>Size</code> is less than or equal to the size of the <code>FieldToMatch</code> </p> <p> <b>LT</b>: Used to test if the <code>Size</code> is strictly less than the size of the <code>FieldToMatch</code> </p> <p> <b>GE</b>: Used to test if the <code>Size</code> is greater than or equal to the size of the <code>FieldToMatch</code> </p> <p> <b>GT</b>: Used to test if the <code>Size</code> is strictly greater than the size of the <code>FieldToMatch</code> </p>"""
    size: "capo_waf.types.size.Size"
    """<p>The size in bytes that you want AWS WAF to compare against the size of the specified <code>FieldToMatch</code>. AWS WAF uses this in combination with <code>ComparisonOperator</code> and <code>FieldToMatch</code> to build an expression in the form of "<code>Size</code> <code>ComparisonOperator</code> size in bytes of <code>FieldToMatch</code>". If that expression is true, the <code>SizeConstraint</code> is considered to match.</p> <p>Valid values for size are 0 - 21474836480 bytes (0 - 20 GB).</p> <p>If you specify <code>URI</code> for the value of <code>Type</code>, the / in the URI counts as one character. For example, the URI <code>/logo.jpg</code> is nine characters long.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraint) -> dict:
    out: dict = {}
    import capo_waf.types.field_to_match

    out["FieldToMatch"] = capo_waf.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import capo_waf.types.text_transformation

    out["TextTransformation"] = (
        capo_waf.types.text_transformation.serialize_aws_json_1_1(
            value["text_transformation"]
        )
    )
    import capo_waf.types.comparison_operator

    out["ComparisonOperator"] = (
        capo_waf.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    out["Size"] = value.get("size", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> SizeConstraint:
    out: SizeConstraint = {}  # type: ignore[typeddict-item]
    if data.get("FieldToMatch") is not None:
        import capo_waf.types.field_to_match

        out["field_to_match"] = capo_waf.types.field_to_match.deserialize_aws_json_1_1(
            data["FieldToMatch"]
        )
    else:
        raise DeserializationError("SizeConstraint.field_to_match required")
    if data.get("TextTransformation") is not None:
        import capo_waf.types.text_transformation

        out["text_transformation"] = (
            capo_waf.types.text_transformation.deserialize_aws_json_1_1(
                data["TextTransformation"]
            )
        )
    else:
        raise DeserializationError("SizeConstraint.text_transformation required")
    if data.get("ComparisonOperator") is not None:
        import capo_waf.types.comparison_operator

        out["comparison_operator"] = (
            capo_waf.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        raise DeserializationError("SizeConstraint.comparison_operator required")
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
