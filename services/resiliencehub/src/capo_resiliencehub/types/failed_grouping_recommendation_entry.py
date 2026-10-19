"""Generated from Smithy shape ``com.amazonaws.resiliencehub#FailedGroupingRecommendationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.error_message
    import capo_resiliencehub.types.string255


class FailedGroupingRecommendationEntry(TypedDict, closed=True):
    grouping_recommendation_id: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the identifier of the grouping recommendation.</p>"""
    error_message: "capo_resiliencehub.types.error_message.ErrorMessage"
    """<p>Indicates the error that occurred while implementing a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedGroupingRecommendationEntry) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedGroupingRecommendationEntry:
    out: FailedGroupingRecommendationEntry = {}  # type: ignore[typeddict-item]
    if data.get("groupingRecommendationId") is not None:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        out["grouping_recommendation_id"] = ""
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    else:
        out["error_message"] = ""
    return out
