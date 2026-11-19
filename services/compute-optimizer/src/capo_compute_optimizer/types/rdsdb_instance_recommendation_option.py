"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBInstanceRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.db_instance_class
    import capo_compute_optimizer.types.performance_risk
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts
    import capo_compute_optimizer.types.rdsdb_projected_utilization_metrics
    import capo_compute_optimizer.types.savings_opportunity


class RDSDBInstanceRecommendationOption(TypedDict, closed=True):
    db_instance_class: NotRequired[
        "capo_compute_optimizer.types.db_instance_class.DBInstanceClass"
    ]
    """<p> Describes the DB instance class recommendation option for your Amazon Aurora or RDS database. </p>"""
    projected_utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.rdsdb_projected_utilization_metrics.RDSDBProjectedUtilizationMetrics"
    ]
    """<p> An array of objects that describe the projected utilization metrics of the DB instance recommendation option. </p>"""
    performance_risk: "capo_compute_optimizer.types.performance_risk.PerformanceRisk"
    """<p> The performance risk of the DB instance recommendation option. </p>"""
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p> The rank identifier of the DB instance recommendation option. </p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]
    savings_opportunity_after_discounts: NotRequired[
        "capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.RDSInstanceSavingsOpportunityAfterDiscounts"
    ]
    """<p> Describes the savings opportunity for Amazon Aurora and RDS database recommendations or for the recommendation option. </p> <p>Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBInstanceRecommendationOption) -> dict:
    out: dict = {}
    if "db_instance_class" in value:
        out["dbInstanceClass"] = value["db_instance_class"]
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.rdsdb_projected_utilization_metrics.serialize_aws_json_1_0(
                value["projected_utilization_metrics"]
            )
        )
    out["performanceRisk"] = (
        "NaN"
        if value.get("performance_risk", 0) != value.get("performance_risk", 0)
        else "Infinity"
        if value.get("performance_risk", 0) == float("inf")
        else "-Infinity"
        if value.get("performance_risk", 0) == float("-inf")
        else value.get("performance_risk", 0)
    )
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.serialize_aws_json_1_0(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDBInstanceRecommendationOption:
    out: RDSDBInstanceRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("dbInstanceClass") is not None:
        out["db_instance_class"] = data["dbInstanceClass"]
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.rdsdb_projected_utilization_metrics.deserialize_aws_json_1_0(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("performanceRisk") is not None:
        out["performance_risk"] = float(data["performanceRisk"])
    else:
        out["performance_risk"] = 0
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.deserialize_aws_json_1_0(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSDBInstanceRecommendationOption) -> dict:
    out: dict = {}
    if "db_instance_class" in value:
        out["dbInstanceClass"] = value["db_instance_class"]
    if "projected_utilization_metrics" in value:
        import capo_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projectedUtilizationMetrics"] = (
            capo_compute_optimizer.types.rdsdb_projected_utilization_metrics.serialize_cbor(
                value["projected_utilization_metrics"]
            )
        )
    out["performanceRisk"] = value.get("performance_risk", 0)
    out["rank"] = value.get("rank", 0)
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    if "savings_opportunity_after_discounts" in value:
        import capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savingsOpportunityAfterDiscounts"] = (
            capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.serialize_cbor(
                value["savings_opportunity_after_discounts"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RDSDBInstanceRecommendationOption:
    out: RDSDBInstanceRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("dbInstanceClass") is not None:
        out["db_instance_class"] = data["dbInstanceClass"]
    if data.get("projectedUtilizationMetrics") is not None:
        import capo_compute_optimizer.types.rdsdb_projected_utilization_metrics

        out["projected_utilization_metrics"] = (
            capo_compute_optimizer.types.rdsdb_projected_utilization_metrics.deserialize_cbor(
                data["projectedUtilizationMetrics"]
            )
        )
    if data.get("performanceRisk") is not None:
        out["performance_risk"] = float(data["performanceRisk"])
    else:
        out["performance_risk"] = 0
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    if data.get("savingsOpportunityAfterDiscounts") is not None:
        import capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts

        out["savings_opportunity_after_discounts"] = (
            capo_compute_optimizer.types.rds_instance_savings_opportunity_after_discounts.deserialize_cbor(
                data["savingsOpportunityAfterDiscounts"]
            )
        )
    return out
