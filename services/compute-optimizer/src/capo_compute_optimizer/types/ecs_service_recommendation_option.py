"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.container_recommendations
    import capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts
    import capo_compute_optimizer.types.ecs_service_projected_utilization_metrics
    import capo_compute_optimizer.types.nullable_cpu
    import capo_compute_optimizer.types.nullable_memory
    import capo_compute_optimizer.types.savings_opportunity


class ECSServiceRecommendationOption(TypedDict, closed=True):
    memory: NotRequired["capo_compute_optimizer.types.nullable_memory.NullableMemory"]
    """<p> The memory size of the Amazon ECS service recommendation option. </p>"""
    cpu: NotRequired["capo_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The CPU size of the Amazon ECS service recommendation option. </p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    savings_opportunity_after_discounts: NotRequired[
        "capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts.ECSSavingsOpportunityAfterDiscounts"
    ]
    """<p> Describes the savings opportunity for Amazon ECS service recommendations or for the recommendation option. </p> <p>Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.</p>"""
    projected_utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.ecs_service_projected_utilization_metrics.ECSServiceProjectedUtilizationMetrics"
    ]
    """<p> An array of objects that describe the projected utilization metrics of the Amazon ECS service recommendation option. </p>"""
    container_recommendations: NotRequired[
        "capo_compute_optimizer.types.container_recommendations.ContainerRecommendations"
    ]
    """<p> The CPU and memory size recommendations for the containers within the task of your Amazon ECS service. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationOption) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    if "container_recommendations" in value:
        import capo_compute_optimizer.types.container_recommendations

        out["containerRecommendations"] = (
            capo_compute_optimizer.types.container_recommendations.serialize_aws_json_1_0(
                value["container_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ECSServiceRecommendationOption:
    out: ECSServiceRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("containerRecommendations") is not None:
        import capo_compute_optimizer.types.container_recommendations

        out["container_recommendations"] = (
            capo_compute_optimizer.types.container_recommendations.deserialize_aws_json_1_0(
                data["containerRecommendations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ECSServiceRecommendationOption) -> dict:
    out: dict = {}
    if "memory" in value:
        out["memory"] = value["memory"]
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts.serialize_cbor(
                value["savings_opportunity_after_discounts"]
            )
        )
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_utilization_metrics.serialize_cbor(
                value["projected_utilization_metrics"]
            )
        )
    if "container_recommendations" in value:
        import capo_compute_optimizer.types.container_recommendations

        out["containerRecommendations"] = (
            capo_compute_optimizer.types.container_recommendations.serialize_cbor(
                value["container_recommendations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ECSServiceRecommendationOption:
    out: ECSServiceRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        out["memory"] = data["memory"]
    if data.get("cpu") is not None:
        out["cpu"] = data["cpu"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.ecs_savings_opportunity_after_discounts.deserialize_cbor(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.ecs_service_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.ecs_service_projected_utilization_metrics.deserialize_cbor(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("containerRecommendations") is not None:
        import capo_compute_optimizer.types.container_recommendations

        out["container_recommendations"] = (
            capo_compute_optimizer.types.container_recommendations.deserialize_cbor(
                data["containerRecommendations"]
            )
        )
    return out
