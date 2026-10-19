"""Generated from Smithy shape ``com.amazonaws.wafv2#SizeConstraintStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.comparison_operator
    import capo_wafv2.types.field_to_match
    import capo_wafv2.types.pre_parse_text_transformations
    import capo_wafv2.types.size
    import capo_wafv2.types.text_transformations


class SizeConstraintStatement(TypedDict, closed=True):
    field_to_match: "capo_wafv2.types.field_to_match.FieldToMatch"
    """<p>The part of the web request that you want WAF to inspect. </p>"""
    comparison_operator: "capo_wafv2.types.comparison_operator.ComparisonOperator"
    """<p>The operator to use to compare the request part to the size setting. </p>"""
    size: "capo_wafv2.types.size.Size"
    """<p>The size, in byte, to compare to the request part, after any transformations.</p>"""
    text_transformations: "capo_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""
    pre_parse_text_transformations: NotRequired[
        "capo_wafv2.types.pre_parse_text_transformations.PreParseTextTransformations"
    ]
    """<p>Pre-parse text transformations normalize the raw query string before WAF parses it into individual query arguments. They are applied before the standard text transformations. Pre-parse text transformations are only supported when <code>FieldToMatch</code> is <code>SingleQueryArgument</code> or <code>AllQueryArguments</code>. You can specify up to 10 pre-parse text transformations per rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SizeConstraintStatement) -> dict:
    out: dict = {}
    import capo_wafv2.types.field_to_match

    out["FieldToMatch"] = capo_wafv2.types.field_to_match.serialize_aws_json_1_1(
        value["field_to_match"]
    )
    import capo_wafv2.types.comparison_operator

    out["ComparisonOperator"] = (
        capo_wafv2.types.comparison_operator.serialize_aws_json_1_1(
            value["comparison_operator"]
        )
    )
    out["Size"] = value.get("size", 0)
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


def deserialize_aws_json_1_1(data: dict) -> SizeConstraintStatement:
    out: SizeConstraintStatement = {}  # type: ignore[typeddict-item]
    if data.get("FieldToMatch") is not None:
        import capo_wafv2.types.field_to_match

        out["field_to_match"] = (
            capo_wafv2.types.field_to_match.deserialize_aws_json_1_1(
                data["FieldToMatch"]
            )
        )
    else:
        raise DeserializationError("SizeConstraintStatement.field_to_match required")
    if data.get("ComparisonOperator") is not None:
        import capo_wafv2.types.comparison_operator

        out["comparison_operator"] = (
            capo_wafv2.types.comparison_operator.deserialize_aws_json_1_1(
                data["ComparisonOperator"]
            )
        )
    else:
        import typing

        out["comparison_operator"] = typing.cast(
            "capo_wafv2.types.comparison_operator.ComparisonOperator", ""
        )
    if data.get("Size") is not None:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if data.get("TextTransformations") is not None:
        import capo_wafv2.types.text_transformations

        out["text_transformations"] = (
            capo_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        out["text_transformations"] = []
    if data.get("PreParseTextTransformations") is not None:
        import capo_wafv2.types.pre_parse_text_transformations

        out["pre_parse_text_transformations"] = (
            capo_wafv2.types.pre_parse_text_transformations.deserialize_aws_json_1_1(
                data["PreParseTextTransformations"]
            )
        )
    return out
