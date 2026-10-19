"""Generated from Smithy shape ``com.amazonaws.wafv2#PreParseTextTransformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.pre_parse_text_transformation_priority
    import capo_wafv2.types.pre_parse_text_transformation_type


class PreParseTextTransformation(TypedDict, closed=True):
    priority: "capo_wafv2.types.pre_parse_text_transformation_priority.PreParseTextTransformationPriority"
    """<p>Sets the relative processing order for the pre-parse text transformations that you define. WAF processes all transformations, from lowest priority value to highest, before inspecting the transformed content. </p>"""
    type: "capo_wafv2.types.pre_parse_text_transformation_type.PreParseTextTransformationType"
    """<p>The type of pre-parse text transformation to apply to the raw query string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreParseTextTransformation) -> dict:
    out: dict = {}
    out["Priority"] = value.get("priority", 0)
    import capo_wafv2.types.pre_parse_text_transformation_type

    out["Type"] = (
        capo_wafv2.types.pre_parse_text_transformation_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PreParseTextTransformation:
    out: PreParseTextTransformation = {}  # type: ignore[typeddict-item]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    else:
        out["priority"] = 0
    if data.get("Type") is not None:
        import capo_wafv2.types.pre_parse_text_transformation_type

        out["type"] = (
            capo_wafv2.types.pre_parse_text_transformation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_wafv2.types.pre_parse_text_transformation_type.PreParseTextTransformationType",
            "",
        )
    return out
