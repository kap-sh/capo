"""Generated from Smithy shape ``com.amazonaws.comprehend#TextSegment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_comprehend.errors import DeserializationError

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string


class TextSegment(TypedDict, closed=True):
    text: "capo_comprehend.types.customer_input_string.CustomerInputString"
    """<p>The text content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextSegment) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TextSegment:
    out: TextSegment = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("TextSegment.text required")
    return out


def redact_sensitive(value: TextSegment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
