"""Generated from Smithy shape ``com.amazonaws.elementalinference#ChooseOneQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.choose_one_option_list
    import capo_elementalinference.types.question_name
    import capo_elementalinference.types.question_text


class ChooseOneQuestion(TypedDict, closed=True):
    name: "capo_elementalinference.types.question_name.QuestionName"
    """<p>A name for the question. The name must be unique among all the questions in the version, across all question types. The name can be up to 64 characters. It must start with a letter or an underscore, and can contain only the letters A-Z and a-z, the digits 0-9, and underscores. </p>"""
    question: "capo_elementalinference.types.question_text.QuestionText"
    """<p>The text of the question. The text can be up to 256 bytes, encoded in UTF-8. It can contain letters in any language, combining marks, digits, spaces, and the following characters: <code>. , ? ! ' " ( ) - : ; / &amp; %</code>, plus the curly apostrophe and quotation marks (U+2019, U+201C, and U+201D). </p>"""
    options: "capo_elementalinference.types.choose_one_option_list.ChooseOneOptionList"
    """<p>The options that Elemental Inference chooses from. You can specify from 2 to 26 options. The question counts as one item toward the limit of 100 scored items in a version, regardless of how many options it has. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChooseOneQuestion) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["question"] = value["question"]
    import capo_elementalinference.types.choose_one_option_list

    out["options"] = (
        capo_elementalinference.types.choose_one_option_list.serialize_json(
            value["options"]
        )
    )
    return out


def deserialize_json(data: dict) -> ChooseOneQuestion:
    out: ChooseOneQuestion = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("question") is not None:
        out["question"] = data["question"]
    else:
        out["question"] = ""
    if data.get("options") is not None:
        import capo_elementalinference.types.choose_one_option_list

        out["options"] = (
            capo_elementalinference.types.choose_one_option_list.deserialize_json(
                data["options"]
            )
        )
    else:
        out["options"] = []
    return out
