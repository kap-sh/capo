"""Generated from Smithy shape ``com.amazonaws.transcribe#UpdateCallAnalyticsCategoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.category_name
    import capo_transcribe.types.input_type
    import capo_transcribe.types.rule_list


class UpdateCallAnalyticsCategoryRequest(TypedDict, closed=True):
    category_name: "capo_transcribe.types.category_name.CategoryName"
    """<p>The name of the Call Analytics category you want to update. Category names are case sensitive.</p>"""
    rules: "capo_transcribe.types.rule_list.RuleList"
    """<p>The rules used for the updated Call Analytics category. The rules you provide in this field replace the ones that are currently being used in the specified category.</p>"""
    input_type: NotRequired["capo_transcribe.types.input_type.InputType"]
    """<p>Choose whether you want to update a real-time or a post-call category. The input type you specify must match the input type specified when the category was created. For example, if you created a category with the <code>POST_CALL</code> input type, you must use <code>POST_CALL</code> as the input type when updating this category.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCallAnalyticsCategoryRequest) -> dict:
    out: dict = {}
    out["CategoryName"] = value["category_name"]
    import capo_transcribe.types.rule_list

    out["Rules"] = capo_transcribe.types.rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    if "input_type" in value:
        import capo_transcribe.types.input_type

        out["InputType"] = capo_transcribe.types.input_type.serialize_aws_json_1_1(
            value["input_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCallAnalyticsCategoryRequest:
    out: UpdateCallAnalyticsCategoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("CategoryName") is not None:
        out["category_name"] = data["CategoryName"]
    else:
        out["category_name"] = ""
    if data.get("Rules") is not None:
        import capo_transcribe.types.rule_list

        out["rules"] = capo_transcribe.types.rule_list.deserialize_aws_json_1_1(
            data["Rules"]
        )
    else:
        out["rules"] = []
    if data.get("InputType") is not None:
        import capo_transcribe.types.input_type

        out["input_type"] = capo_transcribe.types.input_type.deserialize_aws_json_1_1(
            data["InputType"]
        )
    return out
