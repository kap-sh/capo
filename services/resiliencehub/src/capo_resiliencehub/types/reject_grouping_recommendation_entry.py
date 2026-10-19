"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RejectGroupingRecommendationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.grouping_recommendation_rejection_reason
    import capo_resiliencehub.types.string255


class RejectGroupingRecommendationEntry(TypedDict, closed=True):
    grouping_recommendation_id: "capo_resiliencehub.types.string255.String255"
    """<p>Indicates the identifier of the grouping recommendation.</p>"""
    rejection_reason: NotRequired[
        "capo_resiliencehub.types.grouping_recommendation_rejection_reason.GroupingRecommendationRejectionReason"
    ]
    """<p>Indicates the reason you had selected while rejecting a grouping recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectGroupingRecommendationEntry) -> dict:
    out: dict = {}
    out["groupingRecommendationId"] = value["grouping_recommendation_id"]
    if "rejection_reason" in value:
        import capo_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejectionReason"] = (
            capo_resiliencehub.types.grouping_recommendation_rejection_reason.serialize_json(
                value["rejection_reason"]
            )
        )
    return out


def deserialize_json(data: dict) -> RejectGroupingRecommendationEntry:
    out: RejectGroupingRecommendationEntry = {}  # type: ignore[typeddict-item]
    if data.get("groupingRecommendationId") is not None:
        out["grouping_recommendation_id"] = data["groupingRecommendationId"]
    else:
        out["grouping_recommendation_id"] = ""
    if data.get("rejectionReason") is not None:
        import capo_resiliencehub.types.grouping_recommendation_rejection_reason

        out["rejection_reason"] = (
            capo_resiliencehub.types.grouping_recommendation_rejection_reason.deserialize_json(
                data["rejectionReason"]
            )
        )
    return out
