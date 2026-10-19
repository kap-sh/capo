"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppComponentRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.component_recommendation_list
    import capo_resiliencehub.types.next_token


class ListAppComponentRecommendationsResponse(TypedDict, closed=True):
    component_recommendations: "capo_resiliencehub.types.component_recommendation_list.ComponentRecommendationList"
    """<p>The recommendations for an Resilience Hub Application Component, returned as an object. This object contains the names of the Application Components, configuration recommendations, and recommendation statuses.</p>"""
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppComponentRecommendationsResponse) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.component_recommendation_list

    out["componentRecommendations"] = (
        capo_resiliencehub.types.component_recommendation_list.serialize_json(
            value["component_recommendations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppComponentRecommendationsResponse:
    out: ListAppComponentRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("componentRecommendations") is not None:
        import capo_resiliencehub.types.component_recommendation_list

        out["component_recommendations"] = (
            capo_resiliencehub.types.component_recommendation_list.deserialize_json(
                data["componentRecommendations"]
            )
        )
    else:
        out["component_recommendations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
