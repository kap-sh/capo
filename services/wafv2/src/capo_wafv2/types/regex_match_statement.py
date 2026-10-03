"""Generated from Smithy shape ``com.amazonaws.wafv2#RegexMatchStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_match
    import capo_wafv2.types.pre_parse_text_transformations
    import capo_wafv2.types.regex_pattern_string
    import capo_wafv2.types.text_transformations


class RegexMatchStatement(TypedDict, closed=True):
    regex_string: "capo_wafv2.types.regex_pattern_string.RegexPatternString"
    """<p>The string representing the regular expression. WAF enforces a quota on the maximum number of characters in a regex pattern. For the current limit, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>.</p>"""
    field_to_match: "capo_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    text_transformations: "capo_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""
    pre_parse_text_transformations: NotRequired[
        "capo_wafv2.types.pre_parse_text_transformations.PreParseTextTransformations"
    ]
    """<p>Pre-parse text transformations normalize the raw query string before WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when <code>FieldToMatch</code> is <code>SingleQueryArgument</code> or <code>AllQueryArguments</code>. You can specify up to 10 pre-parse text transformations per rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchStatement) -> dict:
    out: dict = {}
    out["RegexString"] = value["regex_string"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchStatement:
    out: RegexMatchStatement = {}  # type: ignore[typeddict-item]
    if data.get("RegexString") is not None:
        out["regex_string"] = data["RegexString"]
    else:
        raise DeserializationError("RegexMatchStatement.regex_string required")
    if data.get("FieldToMatch") is not None:
        import capo_wafv2.types.field_to_match

        out["field_to_match"] = (
            capo_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("RegexMatchStatement.field_to_match required")
    if data.get("TextTransformations") is not None:
        import capo_wafv2.types.text_transformations

        out["text_transformations"] = (
            capo_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        raise DeserializationError("RegexMatchStatement.text_transformations required")
    if data.get("PreParseTextTransformations") is not None:
        import capo_wafv2.types.pre_parse_text_transformations

        out["pre_parse_text_transformations"] = (
            capo_wafv2.types.pre_parse_text_transformations.deserialize_aws_json_1_1(
                data["PreParseTextTransformations"]
            )
        )
    return out
