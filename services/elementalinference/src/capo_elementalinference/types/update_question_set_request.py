"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateQuestionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_question_list
    import capo_elementalinference.types.question_set_id
    import capo_elementalinference.types.resource_name
    import capo_elementalinference.types.yes_no_per_option_question_list
    import capo_elementalinference.types.yes_no_question_list


class UpdateQuestionSetRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.question_set_id.QuestionSetId"
    """<p>The ID of the question set to update.</p>"""
    yes_no: NotRequired[
        "capo_elementalinference.types.yes_no_question_list.YesNoQuestionList"
    ]
    """<p>An array of questions that Elemental Inference answers with yes or no, to replace all the yesNo questions in DRAFT. You can specify up to 50 yesNo questions. If not specified, the yesNo questions are not changed. To remove all the yesNo questions, specify an empty array. </p>"""
    yes_no_per_option: NotRequired[
        "capo_elementalinference.types.yes_no_per_option_question_list.YesNoPerOptionQuestionList"
    ]
    """<p>An array of questions that you ask about each of their options, to replace all the yesNoPerOption questions in DRAFT. You can specify up to 10 yesNoPerOption questions. If not specified, the yesNoPerOption questions are not changed. To remove all the yesNoPerOption questions, specify an empty array. </p>"""
    choose_one: NotRequired[
        "capo_elementalinference.types.choose_one_question_list.ChooseOneQuestionList"
    ]
    """<p>An array of questions that Elemental Inference answers by choosing one of their options, to replace all the chooseOne questions in DRAFT. You can specify up to 10 chooseOne questions. If not specified, the chooseOne questions are not changed. To remove all the chooseOne questions, specify an empty array. </p>"""
    name: NotRequired["capo_elementalinference.types.resource_name.ResourceName"]
    """<p>A new name for the question set. If not specified, the name is not changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuestionSetRequest) -> dict:
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
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateQuestionSetRequest:
    out: UpdateQuestionSetRequest = {}  # type: ignore[typeddict-item]
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
    return out
