"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRDSDatabaseRecommendationProjectedMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics


class GetRDSDatabaseRecommendationProjectedMetricsResponse(TypedDict, closed=True):
    recommended_option_projected_metrics: NotRequired[
        "capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics.RDSDatabaseRecommendedOptionProjectedMetrics"
    ]
    """<p> An array of objects that describes the projected metrics. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: GetRDSDatabaseRecommendationProjectedMetricsResponse,
) -> dict:
    out: dict = {}
    if "recommended_option_projected_metrics" in value:
        import capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics

        out["recommendedOptionProjectedMetrics"] = (
            capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics.serialize_aws_json_1_0(
                value["recommended_option_projected_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetRDSDatabaseRecommendationProjectedMetricsResponse:
    out: GetRDSDatabaseRecommendationProjectedMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedOptionProjectedMetrics") is not None:
        import capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics

        out["recommended_option_projected_metrics"] = (
            capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics.deserialize_aws_json_1_0(
                data["recommendedOptionProjectedMetrics"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetRDSDatabaseRecommendationProjectedMetricsResponse) -> dict:
    out: dict = {}
    if "recommended_option_projected_metrics" in value:
        import capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics

        out["recommendedOptionProjectedMetrics"] = (
            capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics.serialize_cbor(
                value["recommended_option_projected_metrics"]
            )
        )
    return out


def deserialize_cbor(
    data: dict,
) -> GetRDSDatabaseRecommendationProjectedMetricsResponse:
    out: GetRDSDatabaseRecommendationProjectedMetricsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recommendedOptionProjectedMetrics") is not None:
        import capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics

        out["recommended_option_projected_metrics"] = (
            capo_compute_optimizer.types.rds_database_recommended_option_projected_metrics.deserialize_cbor(
                data["recommendedOptionProjectedMetrics"]
            )
        )
    return out
