"""Generated from Smithy shape ``com.amazonaws.elementalinference#YesNoQuestion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.question_name
    import capo_elementalinference.types.question_text


class YesNoQuestion(TypedDict, closed=True):
    name: "capo_elementalinference.types.question_name.QuestionName"
    """<p>A name for the question. The name must be unique among all the questions in the version, across all question types. The name can be up to 64 characters. It must start with a letter or an underscore, and can contain only the letters A-Z and a-z, the digits 0-9, and underscores. </p>"""
    question: "capo_elementalinference.types.question_text.QuestionText"
    """<p>The text of the question. The text can be up to 256 bytes, encoded in UTF-8. It can contain letters in any language, combining marks, digits, spaces, and the following characters: <code>. , ? ! ' " ( ) - : ; / &amp; %</code>, plus the curly apostrophe and quotation marks (U+2019, U+201C, and U+201D). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: YesNoQuestion) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["question"] = value["question"]
    return out


def deserialize_json(data: dict) -> YesNoQuestion:
    out: YesNoQuestion = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("question") is not None:
        out["question"] = data["question"]
    else:
        out["question"] = ""
    return out
