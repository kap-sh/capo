"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSEffectiveRecommendationPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.cpu_vendor_architectures
    import capo_compute_optimizer.types.enhanced_infrastructure_metrics
    import capo_compute_optimizer.types.look_back_period_preference
    import capo_compute_optimizer.types.rds_savings_estimation_mode


class RDSEffectiveRecommendationPreferences(TypedDict, closed=True):
    cpu_vendor_architectures: NotRequired[
        "capo_compute_optimizer.types.cpu_vendor_architectures.CpuVendorArchitectures"
    ]
    """<p> Describes the CPU vendor and architecture for DB instance recommendations. </p>"""
    enhanced_infrastructure_metrics: NotRequired[
        "capo_compute_optimizer.types.enhanced_infrastructure_metrics.EnhancedInfrastructureMetrics"
    ]
    """<p>Describes the activation status of the enhanced infrastructure metrics preference. </p> <p>A status of <code>Active</code> confirms that the preference is applied in the latest recommendation refresh, and a status of <code>Inactive</code> confirms that it's not yet applied to recommendations. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>. </p>"""
    look_back_period: NotRequired[
        "capo_compute_optimizer.types.look_back_period_preference.LookBackPeriodPreference"
    ]
    """<p> The number of days the utilization metrics of the DB instance are analyzed. </p>"""
    savings_estimation_mode: NotRequired[
        "capo_compute_optimizer.types.rds_savings_estimation_mode.RDSSavingsEstimationMode"
    ]
    """<p> Describes the savings estimation mode preference applied for calculating savings opportunity for DB instances. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSEffectiveRecommendationPreferences) -> dict:
    out: dict = {}
    if "cpu_vendor_architectures" in value:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpuVendorArchitectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.serialize_aws_json_1_0(
                value["cpu_vendor_architectures"]
            )
        )
    if "enhanced_infrastructure_metrics" in value:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhancedInfrastructureMetrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.serialize_aws_json_1_0(
                value["enhanced_infrastructure_metrics"]
            )
        )
    if "look_back_period" in value:
        import capo_compute_optimizer.types.look_back_period_preference

        out["lookBackPeriod"] = (
            capo_compute_optimizer.types.look_back_period_preference.serialize_aws_json_1_0(
                value["look_back_period"]
            )
        )
    if "savings_estimation_mode" in value:
        import capo_compute_optimizer.types.rds_savings_estimation_mode

        out["savingsEstimationMode"] = (
            capo_compute_optimizer.types.rds_savings_estimation_mode.serialize_aws_json_1_0(
                value["savings_estimation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RDSEffectiveRecommendationPreferences:
    out: RDSEffectiveRecommendationPreferences = {}  # type: ignore[typeddict-item]
    if data.get("cpuVendorArchitectures") is not None:
        import capo_compute_optimizer.types.cpu_vendor_architectures

        out["cpu_vendor_architectures"] = (
            capo_compute_optimizer.types.cpu_vendor_architectures.deserialize_aws_json_1_0(
                data["cpuVendorArchitectures"]
            )
        )
    if data.get("enhancedInfrastructureMetrics") is not None:
        import capo_compute_optimizer.types.enhanced_infrastructure_metrics

        out["enhanced_infrastructure_metrics"] = (
            capo_compute_optimizer.types.enhanced_infrastructure_metrics.deserialize_aws_json_1_0(
                data["enhancedInfrastructureMetrics"]
            )
        )
    if data.get("lookBackPeriod") is not None:
        import capo_compute_optimizer.types.look_back_period_preference

        out["look_back_period"] = (
            capo_compute_optimizer.types.look_back_period_preference.deserialize_aws_json_1_0(
                data["lookBackPeriod"]
            )
        )
    if data.get("savingsEstimationMode") is not None:
        import capo_compute_optimizer.types.rds_savings_estimation_mode

        out["savings_estimation_mode"] = (
            capo_compute_optimizer.types.rds_savings_estimation_mode.deserialize_aws_json_1_0(
                data["savingsEstimationMode"]
            )
        )
    return out
