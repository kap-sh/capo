"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSEffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_savings_estimation_mode
    import capo_compute_optimizer.types.look_back_period_preference


class ECSEffectiveRecommendationPreferences(TypedDict, closed=True):
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.ecs_savings_estimation_mode.ECSSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode preference applied for calculating savings opportunity for Amazon ECS services. </p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The number of days the Amazon ECS service utilization metrics were analyzed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.ecs_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.ecs_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    if "look_back_period" in value:
        import capo_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            capo_compute_optimizer.types.look_back_period_preference.serialize_aws_json_1_0(
                value["look_back_period"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSEffectiveRecommendationPreferences:
    out: ECSEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.ecs_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.ecs_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    if data.get("lookBackPeriod") is not None:
        import capo_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            capo_compute_optimizer.types.look_back_period_preference.deserialize_aws_json_1_0(
                data["lookBackPeriod"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.ecs_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.ecs_savings_estimation_mode.serialize_cbor(
                value["savings_estimation_mode"]
            )
        )
    if "look_back_period" in value:
        import capo_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            capo_compute_optimizer.types.look_back_period_preference.serialize_cbor(
                value["look_back_period"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ECSEffectiveRecommendationPreferences:
    out: ECSEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.ecs_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.ecs_savings_estimation_mode.deserialize_cbor(
                data["savingsEstimationMode"]
            )
        )
    if data.get("lookBackPeriod") is not None:
        import capo_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            capo_compute_optimizer.types.look_back_period_preference.deserialize_cbor(
                data["lookBackPeriod"]
            )
        )
    return out
