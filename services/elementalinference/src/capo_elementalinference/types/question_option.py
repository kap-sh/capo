"""Generated from Smithy shape ``com.amazonaws.elementalinference#QuestionOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.option_name
    import capo_elementalinference.types.option_text


class QuestionOption(TypedDict, closed=True):
    name: "capo_elementalinference.types.option_name.OptionName"
    """<p>A name for the option. The name must be unique among the options of the question. The name can be up to 64 characters. It must start with a letter or an underscore, and can contain only the letters A-Z and a-z, the digits 0-9, and underscores. </p>"""
    text: "capo_elementalinference.types.option_text.OptionText"
    """<p>The text of the option. The text must be unique among the options of the question, ignoring case. The text can be up to 16 bytes, encoded in UTF-8. It can contain the same characters as the text of a question. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuestionOption) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QuestionOption:
    out: QuestionOption = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("text") is not None:
        out["text"] = data["text"]
    else:
        out["text"] = ""
    return out
