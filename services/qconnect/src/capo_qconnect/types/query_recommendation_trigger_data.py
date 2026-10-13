"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryRecommendationTriggerData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.query_text


class QueryRecommendationTriggerData(TypedDict, closed=True):
    text: NotRequired["capo_qconnect.types.query_text.QueryText"]
    """<p>The text associated with the recommendation trigger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryRecommendationTriggerData) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> QueryRecommendationTriggerData:
    out: QueryRecommendationTriggerData = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    return out


def redact_sensitive(value: QueryRecommendationTriggerData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
