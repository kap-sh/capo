"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateQuestionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_question_list
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.tag_map
    import capo_elementalinference.types.yes_no_per_option_question_list
    import capo_elementalinference.types.yes_no_question_list


class CreateQuestionSetRequest(TypedDict, closed=True):
    yes_no: NotRequired[
        "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
    ]
    """<p>An array of questions that Elemental Inference answers with yes or no. You can specify up to 50 yesNo questions. An empty array is the same as omitting this property. </p>"""
    yes_no_per_option: NotRequired[
        "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
    ]
    """<p>An array of questions that you ask about each of their options. Elemental Inference answers yes or no for each option. You can specify up to 10 yesNoPerOption questions. An empty array is the same as omitting this property. </p>"""
    choose_one: NotRequired[
        "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
    ]
    """<p>An array of questions that Elemental Inference answers by choosing one of their options. You can specify up to 10 chooseOne questions. An empty array is the same as omitting this property. </p>"""
    name: "capo_elementalinference.types.resource_name.ResourceName"
    """<p>A user-friendly name for this question set.</p>"""
    tags: NotRequired["capo_elementalinference.types.tag_map.TagMap"]
    """<p>Optional tags to associate with the question set. You can also add tags later, using TagResource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuestionSetRequest) -> dict:
    out: dict = {}
    if "yes_no" in value:
        import capo_elementalinference.types.yes_no_question_list

        out["yesNo"] = (
            capo_elementalinference.types.yes_no_question_list.serialize_json(
                value["yes_no"]
            )
        )
    if "yes_no_per_option" in value:
        import capo_elementalinference.types.yes_no_per_option_question_list

        out["yesNoPerOption"] = (
            capo_elementalinference.types.yes_no_per_option_question_list.serialize_json(
                value["yes_no_per_option"]
            )
        )
    if "choose_one" in value:
        import capo_elementalinference.types.choose_one_question_list

        out["chooseOne"] = (
            capo_elementalinference.types.choose_one_question_list.serialize_json(
                value["choose_one"]
            )
        )
    out["name"] = value["name"]
    if "tags" in value:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateQuestionSetRequest:
    out: CreateQuestionSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("yesNo") is not None:
        import capo_elementalinference.types.yes_no_question_list

        out["yes_no"] = (
            capo_elementalinference.types.yes_no_question_list.deserialize_json(
                data["yesNo"]
            )
        )
    if data.get("yesNoPerOption") is not None:
        import capo_elementalinference.types.yes_no_per_option_question_list

        out["yes_no_per_option"] = (
            capo_elementalinference.types.yes_no_per_option_question_list.deserialize_json(
                data["yesNoPerOption"]
            )
        )
    if data.get("chooseOne") is not None:
        import capo_elementalinference.types.choose_one_question_list

        out["choose_one"] = (
            capo_elementalinference.types.choose_one_question_list.deserialize_json(
                data["chooseOne"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("tags") is not None:
        import capo_elementalinference.types.tag_map

        out["tags"] = capo_elementalinference.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
