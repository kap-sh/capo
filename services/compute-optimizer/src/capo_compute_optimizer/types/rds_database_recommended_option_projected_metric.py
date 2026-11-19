"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDatabaseRecommendedOptionProjectedMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.rds_database_projected_metrics
    import capo_compute_optimizer.types.recommended_db_instance_class


class RDSDatabaseRecommendedOptionProjectedMetric(TypedDict, closed=True):
    recommended_db_instance_class: NotRequired[
        "capo_compute_optimizer.types.recommended_db_instance_class.RecommendedDBInstanceClass"
    ]
    """<p> The recommended DB instance class for the Amazon Aurora or RDS database. </p>"""
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p> The rank identifier of the Amazon Aurora or RDS DB instance recommendation option. </p>"""
    projected_metrics: NotRequired[
        "capo_compute_optimizer.types.rds_database_projected_metrics.RDSDatabaseProjectedMetrics"
    ]
    """<p> An array of objects that describe the projected metric. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDatabaseRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_db_instance_class" in value:
        out["recommendedDBInstanceClass"] = value["recommended_db_instance_class"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.serialize_aws_json_1_0(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDatabaseRecommendedOptionProjectedMetric:
    out: RDSDatabaseRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedDBInstanceClass") is not None:
        out["recommended_db_instance_class"] = data["recommendedDBInstanceClass"]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.deserialize_aws_json_1_0(
                data["projectedMetrics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSDatabaseRecommendedOptionProjectedMetric) -> dict:
    out: dict = {}
    if "recommended_db_instance_class" in value:
        out["recommendedDBInstanceClass"] = value["recommended_db_instance_class"]
    out["rank"] = value.get("rank", 0)
    if "projected_metrics" in value:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projectedMetrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.serialize_cbor(
                value["projected_metrics"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RDSDatabaseRecommendedOptionProjectedMetric:
    out: RDSDatabaseRecommendedOptionProjectedMetric = {}  # type: ignore[typeddict-item]
    if data.get("recommendedDBInstanceClass") is not None:
        out["recommended_db_instance_class"] = data["recommendedDBInstanceClass"]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("projectedMetrics") is not None:
        import capo_compute_optimizer.types.rds_database_projected_metrics

        out["projected_metrics"] = (
            capo_compute_optimizer.types.rds_database_projected_metrics.deserialize_cbor(
                data["projectedMetrics"]
            )
        )
    return out
