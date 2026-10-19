"""Generated from Smithy shape ``com.amazonaws.costexplorer#RightsizingRecommendationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.generic_boolean
    import capo_cost_explorer.types.recommendation_target


class RightsizingRecommendationConfiguration(TypedDict, closed=True):
    recommendation_target: (
        "capo_cost_explorer.types.recommendation_target.RecommendationTarget"
    )
    """<p>The option to see recommendations within the same instance family or recommendations for instances across other families. The default value is <code>SAME_INSTANCE_FAMILY</code>. </p>"""
    benefits_considered: "capo_cost_explorer.types.generic_boolean.GenericBoolean"
    """<p>The option to consider RI or Savings Plans discount benefits in your savings calculation. The default value is <code>TRUE</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RightsizingRecommendationConfiguration) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.recommendation_target

    out["RecommendationTarget"] = (
        capo_cost_explorer.types.recommendation_target.serialize_aws_json_1_1(
            value["recommendation_target"]
        )
    )
    out["BenefitsConsidered"] = value.get("benefits_considered", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> RightsizingRecommendationConfiguration:
    out: RightsizingRecommendationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RecommendationTarget") is not None:
        import capo_cost_explorer.types.recommendation_target

        out["recommendation_target"] = (
            capo_cost_explorer.types.recommendation_target.deserialize_aws_json_1_1(
                data["RecommendationTarget"]
            )
        )
    else:
        import typing

        out["recommendation_target"] = typing.cast(
            "capo_cost_explorer.types.recommendation_target.RecommendationTarget", ""
        )
    if data.get("BenefitsConsidered") is not None:
        out["benefits_considered"] = data["BenefitsConsidered"]
    else:
        out["benefits_considered"] = False
    return out
