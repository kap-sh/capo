"""Generated from Smithy shape ``com.amazonaws.comprehend#DetectDominantLanguageRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.customer_input_string


class DetectDominantLanguageRequest(TypedDict, closed=True):
    text: "capo_comprehend.types.customer_input_string.CustomerInputString"
    """<p>A UTF-8 text string. The string must contain at least 20 characters. The maximum string size is 100 KB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectDominantLanguageRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectDominantLanguageRequest:
    out: DetectDominantLanguageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    return out


def redact_sensitive(value: DetectDominantLanguageRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
