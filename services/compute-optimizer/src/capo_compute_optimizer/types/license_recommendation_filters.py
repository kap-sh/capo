"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.license_recommendation_filter

LicenseRecommendationFilters: TypeAlias = list[
    "capo_compute_optimizer.types.license_recommendation_filter.LicenseRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationFilters) -> list:
    import capo_compute_optimizer.types.license_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseRecommendationFilters:
    import capo_compute_optimizer.types.license_recommendation_filter

    out: LicenseRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendationFilters) -> list:
    import capo_compute_optimizer.types.license_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation_filter.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> LicenseRecommendationFilters:
    import capo_compute_optimizer.types.license_recommendation_filter

    out: LicenseRecommendationFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation_filter.deserialize_cbor(
                item
            )
        )
    return out
