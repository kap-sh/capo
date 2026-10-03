"""Generated from Smithy shape ``com.amazonaws.wafv2#TextTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.text_transformation_priority
    import capo_wafv2.types.text_transformation_type


class TextTransformation(TypedDict, closed=True):
    priority: "capo_wafv2.types.text_transformation_priority.TextTransformationPriority"
    """<p>Sets the relative processing order for multiple transformations. WAF processes all transformations, from lowest priority to highest, before inspecting the transformed content. The priorities don't need to be consecutive, but they must all be different. </p>"""
    type: "capo_wafv2.types.text_transformation_type.TextTransformationType"
    """<p>For detailed descriptions of each of the transformation types, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-transformation.html">Text transformations</a> in the <i>WAF Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTransformation) -> dict:
    out: dict = {}
    out["Priority"] = value.get("priority", 0)
    import capo_wafv2.types.text_transformation_type

    out["Type"] = capo_wafv2.types.text_transformation_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextTransformation:
    out: TextTransformation = {}  # type: ignore[typeddict-item]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("Type") is not None:
        import capo_wafv2.types.text_transformation_type

        out["type"] = (
            capo_wafv2.types.text_transformation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TextTransformation.type required")
    return out
