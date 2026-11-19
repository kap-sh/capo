"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.current_performance_risk_ratings
    import capo_compute_optimizer.types.idle_summaries
    import capo_compute_optimizer.types.inferred_workload_savings
    import capo_compute_optimizer.types.recommendation_source_type
    import capo_compute_optimizer.types.savings_opportunity
    import capo_compute_optimizer.types.summaries


class RecommendationSummary(TypedDict, closed=True):
    summaries: NotRequired["capo_compute_optimizer.types.summaries.Summaries"]
    """<p>An array of objects that describe a recommendation summary.</p>"""
    idle_summaries: NotRequired[
        "capo_compute_optimizer.types.idle_summaries.IdleSummaries"
    ]
    """<p> Describes the findings summary of the idle resources. </p>"""
    recommendation_resource_type: NotRequired[
        "capo_compute_optimizer.types.recommendation_source_type.RecommendationSourceType"
    ]
    """<p>The resource type that the recommendation summary applies to.</p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the recommendation summary.</p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    """<p>An object that describes the savings opportunity for a given resource type. Savings opportunity includes the estimated monthly savings amount and percentage.</p>"""
    idle_savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    aggregated_savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    current_performance_risk_ratings: NotRequired[
        "capo_compute_optimizer.types.current_performance_risk_ratings.CurrentPerformanceRiskRatings"
    ]
    """<p>An object that describes the performance risk ratings for a given resource type.</p>"""
    inferred_workload_savings: NotRequired[
        "capo_compute_optimizer.types.inferred_workload_savings.InferredWorkloadSavings"
    ]
    """<p> An array of objects that describes the estimated monthly saving amounts for the instances running on the specified <code>inferredWorkloadTypes</code>. The array contains the top five savings opportunites for the instances that run inferred workload types. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSummary) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_compute_optimizer.types.summaries

        out["summaries"] = (
            capo_compute_optimizer.types.summaries.serialize_aws_json_1_0(
                value["summaries"]
            )
        )
    if "idle_summaries" in value:
        import capo_compute_optimizer.types.idle_summaries

        out["idleSummaries"] = (
            capo_compute_optimizer.types.idle_summaries.serialize_aws_json_1_0(
                value["idle_summaries"]
            )
        )
    if "recommendation_resource_type" in value:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendationResourceType"] = (
            capo_compute_optimizer.types.recommendation_source_type.serialize_aws_json_1_0(
                value["recommendation_resource_type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "idle_savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["idleSavingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["idle_savings_opportunity"]
            )
        )
    if "aggregated_savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["aggregatedSavingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["aggregated_savings_opportunity"]
            )
        )
    if "current_performance_risk_ratings" in value:
        import capo_compute_optimizer.types.current_performance_risk_ratings

        out["currentPerformanceRiskRatings"] = (
            capo_compute_optimizer.types.current_performance_risk_ratings.serialize_aws_json_1_0(
                value["current_performance_risk_ratings"]
            )
        )
    if "inferred_workload_savings" in value:
        import capo_compute_optimizer.types.inferred_workload_savings

        out["inferredWorkloadSavings"] = (
            capo_compute_optimizer.types.inferred_workload_savings.serialize_aws_json_1_0(
                value["inferred_workload_savings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationSummary:
    out: RecommendationSummary = {}  # type: ignore[typeddict-item]
    if data.get("summaries") is not None:
        import capo_compute_optimizer.types.summaries

        out["summaries"] = (
            capo_compute_optimizer.types.summaries.deserialize_aws_json_1_0(
                data["summaries"]
            )
        )
    if data.get("idleSummaries") is not None:
        import capo_compute_optimizer.types.idle_summaries

        out["idle_summaries"] = (
            capo_compute_optimizer.types.idle_summaries.deserialize_aws_json_1_0(
                data["idleSummaries"]
            )
        )
    if data.get("recommendationResourceType") is not None:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendation_resource_type"] = (
            capo_compute_optimizer.types.recommendation_source_type.deserialize_aws_json_1_0(
                data["recommendationResourceType"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("idleSavingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["idle_savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["idleSavingsOpportunity"]
            )
        )
    if data.get("aggregatedSavingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["aggregated_savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["aggregatedSavingsOpportunity"]
            )
        )
    if data.get("currentPerformanceRiskRatings") is not None:
        import capo_compute_optimizer.types.current_performance_risk_ratings

        out["current_performance_risk_ratings"] = (
            capo_compute_optimizer.types.current_performance_risk_ratings.deserialize_aws_json_1_0(
                data["currentPerformanceRiskRatings"]
            )
        )
    if data.get("inferredWorkloadSavings") is not None:
        import capo_compute_optimizer.types.inferred_workload_savings

        out["inferred_workload_savings"] = (
            capo_compute_optimizer.types.inferred_workload_savings.deserialize_aws_json_1_0(
                data["inferredWorkloadSavings"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationSummary) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_compute_optimizer.types.summaries

        out["summaries"] = capo_compute_optimizer.types.summaries.serialize_cbor(
            value["summaries"]
        )
    if "idle_summaries" in value:
        import capo_compute_optimizer.types.idle_summaries

        out["idleSummaries"] = (
            capo_compute_optimizer.types.idle_summaries.serialize_cbor(
                value["idle_summaries"]
            )
        )
    if "recommendation_resource_type" in value:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendationResourceType"] = (
            capo_compute_optimizer.types.recommendation_source_type.serialize_cbor(
                value["recommendation_resource_type"]
            )
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    if "idle_savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["idleSavingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["idle_savings_opportunity"]
            )
        )
    if "aggregated_savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["aggregatedSavingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["aggregated_savings_opportunity"]
            )
        )
    if "current_performance_risk_ratings" in value:
        import capo_compute_optimizer.types.current_performance_risk_ratings

        out["currentPerformanceRiskRatings"] = (
            capo_compute_optimizer.types.current_performance_risk_ratings.serialize_cbor(
                value["current_performance_risk_ratings"]
            )
        )
    if "inferred_workload_savings" in value:
        import capo_compute_optimizer.types.inferred_workload_savings

        out["inferredWorkloadSavings"] = (
            capo_compute_optimizer.types.inferred_workload_savings.serialize_cbor(
                value["inferred_workload_savings"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RecommendationSummary:
    out: RecommendationSummary = {}  # type: ignore[typeddict-item]
    if data.get("summaries") is not None:
        import capo_compute_optimizer.types.summaries

        out["summaries"] = capo_compute_optimizer.types.summaries.deserialize_cbor(
            data["summaries"]
        )
    if data.get("idleSummaries") is not None:
        import capo_compute_optimizer.types.idle_summaries

        out["idle_summaries"] = (
            capo_compute_optimizer.types.idle_summaries.deserialize_cbor(
                data["idleSummaries"]
            )
        )
    if data.get("recommendationResourceType") is not None:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendation_resource_type"] = (
            capo_compute_optimizer.types.recommendation_source_type.deserialize_cbor(
                data["recommendationResourceType"]
            )
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    if data.get("idleSavingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["idle_savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["idleSavingsOpportunity"]
            )
        )
    if data.get("aggregatedSavingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["aggregated_savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["aggregatedSavingsOpportunity"]
            )
        )
    if data.get("currentPerformanceRiskRatings") is not None:
        import capo_compute_optimizer.types.current_performance_risk_ratings

        out["current_performance_risk_ratings"] = (
            capo_compute_optimizer.types.current_performance_risk_ratings.deserialize_cbor(
                data["currentPerformanceRiskRatings"]
            )
        )
    if data.get("inferredWorkloadSavings") is not None:
        import capo_compute_optimizer.types.inferred_workload_savings

        out["inferred_workload_savings"] = (
            capo_compute_optimizer.types.inferred_workload_savings.deserialize_cbor(
                data["inferredWorkloadSavings"]
            )
        )
    return out
