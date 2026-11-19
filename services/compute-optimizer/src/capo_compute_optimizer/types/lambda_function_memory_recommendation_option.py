"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LambdaFunctionMemoryRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.lambda_function_memory_projected_metrics
    import capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts
    import capo_compute_optimizer.types.memory_size
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.savings_opportunity


class LambdaFunctionMemoryRecommendationOption(TypedDict, closed=True):
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p>The rank of the function recommendation option.</p> <p>The top recommendation option is ranked as <code>1</code>.</p>"""
    memory_size: "capo_compute_optimizer.types.memory_size.MemorySize"
    """<p>The memory size, in MB, of the function recommendation option.</p>"""
    projected_utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.lambda_function_memory_projected_metrics.LambdaFunctionMemoryProjectedMetrics"
    ]
    """<p>An array of objects that describe the projected utilization metrics of the function recommendation option.</p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for the Lambda function recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    savings_opportunity_after_discounts: NotRequired[
        "capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts.LambdaSavingsOpportunityAfterDiscounts"
    ]
    """<p> An object that describes the savings opportunity for the Lambda recommendation option which includes Saving Plans discounts. Savings opportunity includes the estimated monthly savings and percentage. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaFunctionMemoryRecommendationOption) -> dict:
    out: dict = {}
    out["rank"] = value.get("rank", 0)
    out["memorySize"] = value.get("memory_size", 0)
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.lambda_function_memory_projected_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LambdaFunctionMemoryRecommendationOption:
    out: LambdaFunctionMemoryRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("memorySize") is not None:
        out["memory_size"] = data["memorySize"]
    else:
        out["memory_size"] = 0
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.lambda_function_memory_projected_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaFunctionMemoryRecommendationOption) -> dict:
    out: dict = {}
    out["rank"] = value.get("rank", 0)
    out["memorySize"] = value.get("memory_size", 0)
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.lambda_function_memory_projected_metrics.serialize_cbor(
                value["projected_utilization_metrics"]
            )
        )
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts.serialize_cbor(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LambdaFunctionMemoryRecommendationOption:
    out: LambdaFunctionMemoryRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("memorySize") is not None:
        out["memory_size"] = data["memorySize"]
    else:
        out["memory_size"] = 0
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.lambda_function_memory_projected_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.lambda_function_memory_projected_metrics.deserialize_cbor(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.lambda_savings_opportunity_after_discounts.deserialize_cbor(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out
