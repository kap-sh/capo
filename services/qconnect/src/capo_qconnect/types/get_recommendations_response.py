"""Generated from Smithy shape ``com.amazonaws.qconnect#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_list
    import capo_qconnect.types.recommendation_trigger_list


class GetRecommendationsResponse(TypedDict, closed=True):
    recommendations: "capo_qconnect.types.recommendation_list.RecommendationList"
    """<p>The recommendations.</p>"""
    triggers: NotRequired[
        "capo_qconnect.types.recommendation_trigger_list.RecommendationTriggerList"
    ]
    """<p>The triggers corresponding to recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.recommendation_list

    out["recommendations"] = capo_qconnect.types.recommendation_list.serialize_json(
        value["recommendations"]
    )
    if "triggers" in value:
        import capo_qconnect.types.recommendation_trigger_list

        out["triggers"] = (
            capo_qconnect.types.recommendation_trigger_list.serialize_json(
                value["triggers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendations") is not None:
        import capo_qconnect.types.recommendation_list

        out["recommendations"] = (
            capo_qconnect.types.recommendation_list.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        out["recommendations"] = []
    if data.get("triggers") is not None:
        import capo_qconnect.types.recommendation_trigger_list

        out["triggers"] = (
            capo_qconnect.types.recommendation_trigger_list.deserialize_json(
                data["triggers"]
            )
        )
    return out


def redact_sensitive(value: GetRecommendationsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "recommendations" in value:
        import capo_qconnect.types.recommendation_list

        out["recommendations"] = (
            capo_qconnect.types.recommendation_list.redact_sensitive(
                value["recommendations"]
            )
        )
    if "triggers" in value:
        import capo_qconnect.types.recommendation_trigger_list

        out["triggers"] = (
            capo_qconnect.types.recommendation_trigger_list.redact_sensitive(
                value["triggers"]
            )
        )
    return out
