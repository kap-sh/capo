"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationExportJobs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_export_job

RecommendationExportJobs: TypeAlias = list[
    "capo_compute_optimizer.types.recommendation_export_job.RecommendationExportJob"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationExportJobs) -> list:
    import capo_compute_optimizer.types.recommendation_export_job

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_export_job.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendationExportJobs:
    import capo_compute_optimizer.types.recommendation_export_job

    out: RecommendationExportJobs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_export_job.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationExportJobs) -> list:
    import capo_compute_optimizer.types.recommendation_export_job

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.recommendation_export_job.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> RecommendationExportJobs:
    import capo_compute_optimizer.types.recommendation_export_job

    out: RecommendationExportJobs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.recommendation_export_job.deserialize_cbor(
                item
            )
        )
    return out
