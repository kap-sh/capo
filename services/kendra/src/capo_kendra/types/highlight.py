"""Generated from Smithy shape ``com.amazonaws.kendra#Highlight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean
    import capo_kendra.types.highlight_type
    import capo_kendra.types.integer


class Highlight(TypedDict, closed=True):
    begin_offset: "capo_kendra.types.integer.Integer"
    """<p>The zero-based location in the response string where the highlight starts.</p>"""
    end_offset: "capo_kendra.types.integer.Integer"
    """<p>The zero-based location in the response string where the highlight ends.</p>"""
    top_answer: "capo_kendra.types.boolean.Boolean"
    """<p>Indicates whether the response is the best response. True if this is the best response; otherwise, false.</p>"""
    type: NotRequired["capo_kendra.types.highlight_type.HighlightType"]
    """<p>The highlight type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Highlight) -> dict:
    out: dict = {}
    out["BeginOffset"] = value["begin_offset"]
    out["EndOffset"] = value["end_offset"]
    out["TopAnswer"] = value.get("top_answer", False)
    if "type" in value:
        import capo_kendra.types.highlight_type

        out["Type"] = capo_kendra.types.highlight_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Highlight:
    out: Highlight = {}  # type: ignore[typeddict-item]
    if data.get("BeginOffset") is not None:
        out["begin_offset"] = data["BeginOffset"]
    else:
        out["begin_offset"] = 0
    if data.get("EndOffset") is not None:
        out["end_offset"] = data["EndOffset"]
    else:
        out["end_offset"] = 0
    if data.get("TopAnswer") is not None:
        out["top_answer"] = data["TopAnswer"]
    else:
        out["top_answer"] = False
    if data.get("Type") is not None:
        import capo_kendra.types.highlight_type

        out["type"] = capo_kendra.types.highlight_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
