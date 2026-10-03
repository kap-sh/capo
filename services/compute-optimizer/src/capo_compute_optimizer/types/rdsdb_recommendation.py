"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSDBRecommendation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.account_id
    import capo_compute_optimizer.types.current_db_instance_class
    import capo_compute_optimizer.types.db_cluster_identifier
    import capo_compute_optimizer.types.db_storage_configuration
    import capo_compute_optimizer.types.engine
    import capo_compute_optimizer.types.engine_version
    import capo_compute_optimizer.types.idle
    import capo_compute_optimizer.types.last_refresh_timestamp
    import capo_compute_optimizer.types.look_back_period_in_days
    import capo_compute_optimizer.types.promotion_tier
    import capo_compute_optimizer.types.rds_current_instance_performance_risk
    import capo_compute_optimizer.types.rds_effective_recommendation_preferences
    import capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation
    import capo_compute_optimizer.types.rds_instance_finding
    import capo_compute_optimizer.types.rds_instance_finding_reason_codes
    import capo_compute_optimizer.types.rds_storage_finding
    import capo_compute_optimizer.types.rds_storage_finding_reason_codes
    import capo_compute_optimizer.types.rdsdb_instance_recommendation_options
    import capo_compute_optimizer.types.rdsdb_storage_recommendation_options
    import capo_compute_optimizer.types.rdsdb_utilization_metrics
    import capo_compute_optimizer.types.resource_arn
    import capo_compute_optimizer.types.tags


class RDSDBRecommendation(TypedDict, closed=True):
    resource_arn: NotRequired["capo_compute_optimizer.types.resource_arn.ResourceArn"]
    """<p> The ARN of the current Amazon Aurora or RDS database. </p> <p> The following is the format of the ARN: </p> <p> <code>arn:aws:rds:{region}:{accountId}:db:{resourceName}</code> </p>"""
    account_id: NotRequired["capo_compute_optimizer.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID of the Amazon Aurora or RDS database. </p>"""
    engine: NotRequired["capo_compute_optimizer.types.engine.Engine"]
    """<p> The engine of the DB instance. </p>"""
    engine_version: NotRequired[
        "capo_compute_optimizer.types.engine_version.EngineVersion"
    ]
    """<p> The database engine version. </p>"""
    promotion_tier: NotRequired[
        "capo_compute_optimizer.types.promotion_tier.PromotionTier"
    ]
    """<p>The promotion tier for the Aurora instance.</p>"""
    current_db_instance_class: NotRequired[
        "capo_compute_optimizer.types.current_db_instance_class.CurrentDBInstanceClass"
    ]
    """<p> The DB instance class of the current Aurora or RDS DB instance. </p>"""
    current_storage_configuration: NotRequired[
        "capo_compute_optimizer.types.db_storage_configuration.DBStorageConfiguration"
    ]
    """<p> The configuration of the current DB storage. </p>"""
    db_cluster_identifier: NotRequired[
        "capo_compute_optimizer.types.db_cluster_identifier.DBClusterIdentifier"
    ]
    """<p>The identifier for DB cluster.</p>"""
    idle: NotRequired["capo_compute_optimizer.types.idle.Idle"]
    """<p> This indicates if the DB instance is idle or not. </p>"""
    instance_finding: NotRequired[
        "capo_compute_optimizer.types.rds_instance_finding.RDSInstanceFinding"
    ]
    """<p> The finding classification of an Amazon Aurora and RDS DB instance. </p> <p>For more information about finding classifications, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html#rds-recommendations-findings"> Finding classifications for Aurora and RDS databases</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    storage_finding: NotRequired[
        "capo_compute_optimizer.types.rds_storage_finding.RDSStorageFinding"
    ]
    """<p> The finding classification of Amazon RDS DB instance storage. </p> <p>For more information about finding classifications, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html#rds-recommendations-findings"> Finding classifications for Aurora and RDS databases</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    instance_finding_reason_codes: NotRequired[
        "capo_compute_optimizer.types.rds_instance_finding_reason_codes.RDSInstanceFindingReasonCodes"
    ]
    """<p> The reason for the finding classification of a DB instance. </p>"""
    current_instance_performance_risk: NotRequired[
        "capo_compute_optimizer.types.rds_current_instance_performance_risk.RDSCurrentInstancePerformanceRisk"
    ]
    """<p>The performance risk for the current DB instance.</p>"""
    current_storage_estimated_monthly_volume_io_ps_cost_variation: NotRequired[
        "capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.RDSEstimatedMonthlyVolumeIOPsCostVariation"
    ]
    """<p> The level of variation in monthly I/O costs for the current DB storage configuration. </p>"""
    storage_finding_reason_codes: NotRequired[
        "capo_compute_optimizer.types.rds_storage_finding_reason_codes.RDSStorageFindingReasonCodes"
    ]
    """<p> The reason for the finding classification of RDS DB instance storage. </p>"""
    instance_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.rdsdb_instance_recommendation_options.RDSDBInstanceRecommendationOptions"
    ]
    """<p> An array of objects that describe the recommendation options for the RDS DB instance. </p>"""
    storage_recommendation_options: NotRequired[
        "capo_compute_optimizer.types.rdsdb_storage_recommendation_options.RDSDBStorageRecommendationOptions"
    ]
    """<p> An array of objects that describe the recommendation options for DB instance storage. </p>"""
    utilization_metrics: NotRequired[
        "capo_compute_optimizer.types.rdsdb_utilization_metrics.RDSDBUtilizationMetrics"
    ]
    """<p> An array of objects that describe the utilization metrics of the DB instance. </p>"""
    effective_recommendation_preferences: NotRequired[
        "capo_compute_optimizer.types.rds_effective_recommendation_preferences.RDSEffectiveRecommendationPreferences"
    ]
    """<p> Describes the effective recommendation preferences for DB instances. </p>"""
    lookback_period_in_days: (
        "capo_compute_optimizer.types.look_back_period_in_days.LookBackPeriodInDays"
    )
    """<p> The number of days the DB instance utilization metrics were analyzed. </p>"""
    last_refresh_timestamp: NotRequired[
        "capo_compute_optimizer.types.last_refresh_timestamp.LastRefreshTimestamp"
    ]
    """<p> The timestamp of when the DB instance recommendation was last generated. </p>"""
    tags: NotRequired["capo_compute_optimizer.types.tags.Tags"]
    """<p> A list of tags assigned to your DB instance recommendations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSDBRecommendation) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["resourceArn"] = value["resource_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "engine" in value:
        out["engine"] = value["engine"]
    if "engine_version" in value:
        out["engineVersion"] = value["engine_version"]
    if "promotion_tier" in value:
        out["promotionTier"] = value["promotion_tier"]
    if "current_db_instance_class" in value:
        out["currentDBInstanceClass"] = value["current_db_instance_class"]
    if "current_storage_configuration" in value:
        import capo_compute_optimizer.types.db_storage_configuration

        out["currentStorageConfiguration"] = (
            capo_compute_optimizer.types.db_storage_configuration.serialize_aws_json_1_0(
                value["current_storage_configuration"]
            )
        )
    if "db_cluster_identifier" in value:
        out["dbClusterIdentifier"] = value["db_cluster_identifier"]
    if "idle" in value:
        import capo_compute_optimizer.types.idle

        out["idle"] = capo_compute_optimizer.types.idle.serialize_aws_json_1_0(
            value["idle"]
        )
    if "instance_finding" in value:
        import capo_compute_optimizer.types.rds_instance_finding

        out["instanceFinding"] = (
            capo_compute_optimizer.types.rds_instance_finding.serialize_aws_json_1_0(
                value["instance_finding"]
            )
        )
    if "storage_finding" in value:
        import capo_compute_optimizer.types.rds_storage_finding

        out["storageFinding"] = (
            capo_compute_optimizer.types.rds_storage_finding.serialize_aws_json_1_0(
                value["storage_finding"]
            )
        )
    if "instance_finding_reason_codes" in value:
        import capo_compute_optimizer.types.rds_instance_finding_reason_codes

        out["instanceFindingReasonCodes"] = (
            capo_compute_optimizer.types.rds_instance_finding_reason_codes.serialize_aws_json_1_0(
                value["instance_finding_reason_codes"]
            )
        )
    if "current_instance_performance_risk" in value:
        import capo_compute_optimizer.types.rds_current_instance_performance_risk

        out["currentInstancePerformanceRisk"] = (
            capo_compute_optimizer.types.rds_current_instance_performance_risk.serialize_aws_json_1_0(
                value["current_instance_performance_risk"]
            )
        )
    if "current_storage_estimated_monthly_volume_io_ps_cost_variation" in value:
        import capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation

        out["currentStorageEstimatedMonthlyVolumeIOPsCostVariation"] = (
            capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.serialize_aws_json_1_0(
                value["current_storage_estimated_monthly_volume_io_ps_cost_variation"]
            )
        )
    if "storage_finding_reason_codes" in value:
        import capo_compute_optimizer.types.rds_storage_finding_reason_codes

        out["storageFindingReasonCodes"] = (
            capo_compute_optimizer.types.rds_storage_finding_reason_codes.serialize_aws_json_1_0(
                value["storage_finding_reason_codes"]
            )
        )
    if "instance_recommendation_options" in value:
        import capo_compute_optimizer.types.rdsdb_instance_recommendation_options

        out["instanceRecommendationOptions"] = (
            capo_compute_optimizer.types.rdsdb_instance_recommendation_options.serialize_aws_json_1_0(
                value["instance_recommendation_options"]
            )
        )
    if "storage_recommendation_options" in value:
        import capo_compute_optimizer.types.rdsdb_storage_recommendation_options

        out["storageRecommendationOptions"] = (
            capo_compute_optimizer.types.rdsdb_storage_recommendation_options.serialize_aws_json_1_0(
                value["storage_recommendation_options"]
            )
        )
    if "utilization_metrics" in value:
        import capo_compute_optimizer.types.rdsdb_utilization_metrics

        out["utilizationMetrics"] = (
            capo_compute_optimizer.types.rdsdb_utilization_metrics.serialize_aws_json_1_0(
                value["utilization_metrics"]
            )
        )
    if "effective_recommendation_preferences" in value:
        import capo_compute_optimizer.types.rds_effective_recommendation_preferences

        out["effectiveRecommendationPreferences"] = (
            capo_compute_optimizer.types.rds_effective_recommendation_preferences.serialize_aws_json_1_0(
                value["effective_recommendation_preferences"]
            )
        )
    out["lookbackPeriodInDays"] = (
        "NaN"
        if value.get("lookback_period_in_days", 0)
        != value.get("lookback_period_in_days", 0)
        else "Infinity"
        if value.get("lookback_period_in_days", 0) == float("inf")
        else "-Infinity"
        if value.get("lookback_period_in_days", 0) == float("-inf")
        else value.get("lookback_period_in_days", 0)
    )
    if "last_refresh_timestamp" in value:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["lastRefreshTimestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.serialize_aws_json_1_0(
                value["last_refresh_timestamp"]
            )
        )
    if "tags" in value:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSDBRecommendation:
    out: RDSDBRecommendation = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("engine") is not None:
        out["engine"] = data["engine"]
    if data.get("engineVersion") is not None:
        out["engine_version"] = data["engineVersion"]
    if data.get("promotionTier") is not None:
        out["promotion_tier"] = data["promotionTier"]
    if data.get("currentDBInstanceClass") is not None:
        out["current_db_instance_class"] = data["currentDBInstanceClass"]
    if data.get("currentStorageConfiguration") is not None:
        import capo_compute_optimizer.types.db_storage_configuration

        out["current_storage_configuration"] = (
            capo_compute_optimizer.types.db_storage_configuration.deserialize_aws_json_1_0(
                data["currentStorageConfiguration"]
            )
        )
    if data.get("dbClusterIdentifier") is not None:
        out["db_cluster_identifier"] = data["dbClusterIdentifier"]
    if data.get("idle") is not None:
        import capo_compute_optimizer.types.idle

        out["idle"] = capo_compute_optimizer.types.idle.deserialize_aws_json_1_0(
            data["idle"]
        )
    if data.get("instanceFinding") is not None:
        import capo_compute_optimizer.types.rds_instance_finding

        out["instance_finding"] = (
            capo_compute_optimizer.types.rds_instance_finding.deserialize_aws_json_1_0(
                data["instanceFinding"]
            )
        )
    if data.get("storageFinding") is not None:
        import capo_compute_optimizer.types.rds_storage_finding

        out["storage_finding"] = (
            capo_compute_optimizer.types.rds_storage_finding.deserialize_aws_json_1_0(
                data["storageFinding"]
            )
        )
    if data.get("instanceFindingReasonCodes") is not None:
        import capo_compute_optimizer.types.rds_instance_finding_reason_codes

        out["instance_finding_reason_codes"] = (
            capo_compute_optimizer.types.rds_instance_finding_reason_codes.deserialize_aws_json_1_0(
                data["instanceFindingReasonCodes"]
            )
        )
    if data.get("currentInstancePerformanceRisk") is not None:
        import capo_compute_optimizer.types.rds_current_instance_performance_risk

        out["current_instance_performance_risk"] = (
            capo_compute_optimizer.types.rds_current_instance_performance_risk.deserialize_aws_json_1_0(
                data["currentInstancePerformanceRisk"]
            )
        )
    if data.get("currentStorageEstimatedMonthlyVolumeIOPsCostVariation") is not None:
        import capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation

        out["current_storage_estimated_monthly_volume_io_ps_cost_variation"] = (
            capo_compute_optimizer.types.rds_estimated_monthly_volume_io_ps_cost_variation.deserialize_aws_json_1_0(
                data["currentStorageEstimatedMonthlyVolumeIOPsCostVariation"]
            )
        )
    if data.get("storageFindingReasonCodes") is not None:
        import capo_compute_optimizer.types.rds_storage_finding_reason_codes

        out["storage_finding_reason_codes"] = (
            capo_compute_optimizer.types.rds_storage_finding_reason_codes.deserialize_aws_json_1_0(
                data["storageFindingReasonCodes"]
            )
        )
    if data.get("instanceRecommendationOptions") is not None:
        import capo_compute_optimizer.types.rdsdb_instance_recommendation_options

        out["instance_recommendation_options"] = (
            capo_compute_optimizer.types.rdsdb_instance_recommendation_options.deserialize_aws_json_1_0(
                data["instanceRecommendationOptions"]
            )
        )
    if data.get("storageRecommendationOptions") is not None:
        import capo_compute_optimizer.types.rdsdb_storage_recommendation_options

        out["storage_recommendation_options"] = (
            capo_compute_optimizer.types.rdsdb_storage_recommendation_options.deserialize_aws_json_1_0(
                data["storageRecommendationOptions"]
            )
        )
    if data.get("utilizationMetrics") is not None:
        import capo_compute_optimizer.types.rdsdb_utilization_metrics

        out["utilization_metrics"] = (
            capo_compute_optimizer.types.rdsdb_utilization_metrics.deserialize_aws_json_1_0(
                data["utilizationMetrics"]
            )
        )
    if data.get("effectiveRecommendationPreferences") is not None:
        import capo_compute_optimizer.types.rds_effective_recommendation_preferences

        out["effective_recommendation_preferences"] = (
            capo_compute_optimizer.types.rds_effective_recommendation_preferences.deserialize_aws_json_1_0(
                data["effectiveRecommendationPreferences"]
            )
        )
    if data.get("lookbackPeriodInDays") is not None:
        out["lookback_period_in_days"] = float(data["lookbackPeriodInDays"])
    else:
        out["lookback_period_in_days"] = 0
    if data.get("lastRefreshTimestamp") is not None:
        import capo_compute_optimizer.types.last_refresh_timestamp

        out["last_refresh_timestamp"] = (
            capo_compute_optimizer.types.last_refresh_timestamp.deserialize_aws_json_1_0(
                data["lastRefreshTimestamp"]
            )
        )
    if data.get("tags") is not None:
        import capo_compute_optimizer.types.tags

        out["tags"] = capo_compute_optimizer.types.tags.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
