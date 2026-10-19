"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DetectPHIRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.bounded_length_string


class DetectPHIRequest(TypedDict, closed=True):
    text: "capo_comprehendmedical.types.bounded_length_string.BoundedLengthString"
    """<p>A UTF-8 text string containing the clinical content being examined for PHI entities.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectPHIRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectPHIRequest:
    out: DetectPHIRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    return out
