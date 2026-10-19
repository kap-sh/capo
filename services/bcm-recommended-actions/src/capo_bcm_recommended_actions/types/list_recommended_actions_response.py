"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ListRecommendedActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.next_token
    import capo_bcm_recommended_actions.types.recommended_actions


class ListRecommendedActionsResponse(TypedDict, closed=True):
    recommended_actions: (
        "capo_bcm_recommended_actions.types.recommended_actions.RecommendedActions"
    )
    """<p>The list of recommended actions that satisfy the filter criteria.</p>"""
    next_token: NotRequired["capo_bcm_recommended_actions.types.next_token.NextToken"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsResponse) -> dict:
    out: dict = {}
    import capo_bcm_recommended_actions.types.recommended_actions

    out["recommendedActions"] = (
        capo_bcm_recommended_actions.types.recommended_actions.serialize_aws_json_1_0(
            value["recommended_actions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionsResponse:
    out: ListRecommendedActionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedActions") is not None:
        import capo_bcm_recommended_actions.types.recommended_actions

        out["recommended_actions"] = (
            capo_bcm_recommended_actions.types.recommended_actions.deserialize_aws_json_1_0(
                data["recommendedActions"]
            )
        )
    else:
        out["recommended_actions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
