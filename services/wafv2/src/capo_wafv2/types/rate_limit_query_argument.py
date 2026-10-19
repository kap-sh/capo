"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitQueryArgument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_match_data
    import capo_wafv2.types.text_transformations


class RateLimitQueryArgument(TypedDict, closed=True):
    name: "capo_wafv2.types.field_to_match_data.FieldToMatchData"
    """<p>The name of the query argument to use. </p>"""
    text_transformations: "capo_wafv2.types.text_transformations.TextTransformations"
    """<p>Text transformations eliminate some of the unusual formatting that attackers use in web requests in an effort to bypass detection. Text transformations are used in rule match statements, to transform the <code>FieldToMatch</code> request component before inspecting it, and they're used in rate-based rule statements, to transform request components before using them as custom aggregation keys. If you specify one or more transformations to apply, WAF performs all transformations on the specified content, starting from the lowest priority setting, and then uses the transformed component contents. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitQueryArgument) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.text_transformations

    out["TextTransformations"] = (
        capo_wafv2.types.text_transformations.serialize_aws_json_1_1(
            value["text_transformations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitQueryArgument:
    out: RateLimitQueryArgument = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("TextTransformations") is not None:
        import capo_wafv2.types.text_transformations

        out["text_transformations"] = (
            capo_wafv2.types.text_transformations.deserialize_aws_json_1_1(
                data["TextTransformations"]
            )
        )
    else:
        out["text_transformations"] = []
    return out
