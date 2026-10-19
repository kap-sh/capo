"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ComponentRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.config_recommendation_list
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.recommendation_compliance_status


class ComponentRecommendation(TypedDict, closed=True):
    app_component_name: "capo_resiliencehub.types.entity_id.EntityId"
    """<p>Name of the Application Component.</p>"""
    recommendation_status: "capo_resiliencehub.types.recommendation_compliance_status.RecommendationComplianceStatus"
    """<p>Status of the recommendation.</p>"""
    config_recommendations: (
        "capo_resiliencehub.types.config_recommendation_list.ConfigRecommendationList"
    )
    """<p>List of recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentRecommendation) -> dict:
    out: dict = {}
    out["appComponentName"] = value["app_component_name"]
    import capo_resiliencehub.types.recommendation_compliance_status

    out["recommendationStatus"] = (
        capo_resiliencehub.types.recommendation_compliance_status.serialize_json(
            value["recommendation_status"]
        )
    )
    import capo_resiliencehub.types.config_recommendation_list

    out["configRecommendations"] = (
        capo_resiliencehub.types.config_recommendation_list.serialize_json(
            value["config_recommendations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ComponentRecommendation:
    out: ComponentRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("appComponentName") is not None:
        out["app_component_name"] = data["appComponentName"]
    else:
        out["app_component_name"] = ""
    if data.get("recommendationStatus") is not None:
        import capo_resiliencehub.types.recommendation_compliance_status

        out["recommendation_status"] = (
            capo_resiliencehub.types.recommendation_compliance_status.deserialize_json(
                data["recommendationStatus"]
            )
        )
    else:
        import typing

        out["recommendation_status"] = typing.cast(
            "capo_resiliencehub.types.recommendation_compliance_status.RecommendationComplianceStatus",
            "",
        )
    if data.get("configRecommendations") is not None:
        import capo_resiliencehub.types.config_recommendation_list

        out["config_recommendations"] = (
            capo_resiliencehub.types.config_recommendation_list.deserialize_json(
                data["configRecommendations"]
            )
        )
    else:
        out["config_recommendations"] = []
    return out
