"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ConfigRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.assessment_compliance
    import capo_resiliencehub.types.config_recommendation_optimization_type
    import capo_resiliencehub.types.cost
    import capo_resiliencehub.types.entity_description
    import capo_resiliencehub.types.entity_id
    import capo_resiliencehub.types.entity_name
    import capo_resiliencehub.types.ha_architecture
    import capo_resiliencehub.types.recommendation_compliance
    import capo_resiliencehub.types.spec_reference_id
    import capo_resiliencehub.types.suggested_changes_list


class ConfigRecommendation(TypedDict, closed=True):
    cost: NotRequired["capo_resiliencehub.types.cost.Cost"]
    """<p>The cost for the application.</p>"""
    app_component_name: NotRequired["capo_resiliencehub.types.entity_id.EntityId"]
    """<p>Name of the Application Component.</p>"""
    compliance: NotRequired[
        "capo_resiliencehub.types.assessment_compliance.AssessmentCompliance"
    ]
    """<p>The current compliance against the resiliency policy before applying the configuration change.</p>"""
    recommendation_compliance: NotRequired[
        "capo_resiliencehub.types.recommendation_compliance.RecommendationCompliance"
    ]
    """<p>The expected compliance against the resiliency policy after applying the configuration change.</p>"""
    optimization_type: "capo_resiliencehub.types.config_recommendation_optimization_type.ConfigRecommendationOptimizationType"
    """<p>The type of optimization.</p>"""
    name: "capo_resiliencehub.types.entity_name.EntityName"
    """<p>The name of the recommendation configuration.</p>"""
    description: NotRequired[
        "capo_resiliencehub.types.entity_description.EntityDescription"
    ]
    """<p>The optional description for an app.</p>"""
    suggested_changes: NotRequired[
        "capo_resiliencehub.types.suggested_changes_list.SuggestedChangesList"
    ]
    """<p>List of the suggested configuration changes.</p>"""
    ha_architecture: NotRequired[
        "capo_resiliencehub.types.ha_architecture.HaArchitecture"
    ]
    """<p>The architecture type.</p>"""
    reference_id: "capo_resiliencehub.types.spec_reference_id.SpecReferenceId"
    """<p>Reference identifier for the recommendation configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigRecommendation) -> dict:
    out: dict = {}
    if "cost" in value:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.serialize_json(value["cost"])
    if "app_component_name" in value:
        out["appComponentName"] = value["app_component_name"]
    if "compliance" in value:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.serialize_json(
                value["compliance"]
            )
        )
    if "recommendation_compliance" in value:
        import capo_resiliencehub.types.recommendation_compliance

        out["recommendationCompliance"] = (
            capo_resiliencehub.types.recommendation_compliance.serialize_json(
                value["recommendation_compliance"]
            )
        )
    import capo_resiliencehub.types.config_recommendation_optimization_type

    out["optimizationType"] = (
        capo_resiliencehub.types.config_recommendation_optimization_type.serialize_json(
            value["optimization_type"]
        )
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "suggested_changes" in value:
        import capo_resiliencehub.types.suggested_changes_list

        out["suggestedChanges"] = (
            capo_resiliencehub.types.suggested_changes_list.serialize_json(
                value["suggested_changes"]
            )
        )
    if "ha_architecture" in value:
        import capo_resiliencehub.types.ha_architecture

        out["haArchitecture"] = capo_resiliencehub.types.ha_architecture.serialize_json(
            value["ha_architecture"]
        )
    out["referenceId"] = value["reference_id"]
    return out


def deserialize_json(data: dict) -> ConfigRecommendation:
    out: ConfigRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("cost") is not None:
        import capo_resiliencehub.types.cost

        out["cost"] = capo_resiliencehub.types.cost.deserialize_json(data["cost"])
    if data.get("appComponentName") is not None:
        out["app_component_name"] = data["appComponentName"]
    if data.get("compliance") is not None:
        import capo_resiliencehub.types.assessment_compliance

        out["compliance"] = (
            capo_resiliencehub.types.assessment_compliance.deserialize_json(
                data["compliance"]
            )
        )
    if data.get("recommendationCompliance") is not None:
        import capo_resiliencehub.types.recommendation_compliance

        out["recommendation_compliance"] = (
            capo_resiliencehub.types.recommendation_compliance.deserialize_json(
                data["recommendationCompliance"]
            )
        )
    if data.get("optimizationType") is not None:
        import capo_resiliencehub.types.config_recommendation_optimization_type

        out["optimization_type"] = (
            capo_resiliencehub.types.config_recommendation_optimization_type.deserialize_json(
                data["optimizationType"]
            )
        )
    else:
        import typing

        out["optimization_type"] = typing.cast(
            "capo_resiliencehub.types.config_recommendation_optimization_type.ConfigRecommendationOptimizationType",
            "",
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("suggestedChanges") is not None:
        import capo_resiliencehub.types.suggested_changes_list

        out["suggested_changes"] = (
            capo_resiliencehub.types.suggested_changes_list.deserialize_json(
                data["suggestedChanges"]
            )
        )
    if data.get("haArchitecture") is not None:
        import capo_resiliencehub.types.ha_architecture

        out["ha_architecture"] = (
            capo_resiliencehub.types.ha_architecture.deserialize_json(
                data["haArchitecture"]
            )
        )
    if data.get("referenceId") is not None:
        out["reference_id"] = data["referenceId"]
    else:
        out["reference_id"] = ""
    return out
