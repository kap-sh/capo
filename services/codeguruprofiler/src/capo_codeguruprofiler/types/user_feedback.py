"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UserFeedback``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.feedback_type


class UserFeedback(TypedDict, closed=True):
    type: "capo_codeguruprofiler.types.feedback_type.FeedbackType"
    """<p>Optional <code>Positive</code> or <code>Negative</code> feedback submitted by the user about whether the recommendation is useful or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserFeedback) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> UserFeedback:
    out: UserFeedback = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
