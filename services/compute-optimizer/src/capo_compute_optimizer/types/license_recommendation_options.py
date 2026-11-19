"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.license_recommendation_option

LicenseRecommendationOptions: TypeAlias = list[
    "capo_compute_optimizer.types.license_recommendation_option.LicenseRecommendationOption"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationOptions) -> list:
    import capo_compute_optimizer.types.license_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation_option.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseRecommendationOptions:
    import capo_compute_optimizer.types.license_recommendation_option

    out: LicenseRecommendationOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation_option.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendationOptions) -> list:
    import capo_compute_optimizer.types.license_recommendation_option

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation_option.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> LicenseRecommendationOptions:
    import capo_compute_optimizer.types.license_recommendation_option

    out: LicenseRecommendationOptions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation_option.deserialize_cbor(
                item
            )
        )
    return out
