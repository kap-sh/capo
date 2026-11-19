"""Generated from Smithy shape ``com.amazonaws.mgn#InsightMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.insight_message_text


class InsightMessage(TypedDict, closed=True):
    code: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>A stable identifier for the kind of insight.</p>"""
    message: NotRequired["capo_mgn.types.insight_message_text.InsightMessageText"]
    """<p>The human-readable insight message.</p>"""
    topic: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>The topic that the insight relates to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightMessage) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    if "topic" in value:
        out["topic"] = value["topic"]
    return out


def deserialize_json(data: dict) -> InsightMessage:
    out: InsightMessage = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    return out
