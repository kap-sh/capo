"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.license_recommendation

LicenseRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.license_recommendation.LicenseRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendations) -> list:
    import capo_compute_optimizer.types.license_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseRecommendations:
    import capo_compute_optimizer.types.license_recommendation

    out: LicenseRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendations) -> list:
    import capo_compute_optimizer.types.license_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.license_recommendation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> LicenseRecommendations:
    import capo_compute_optimizer.types.license_recommendation

    out: LicenseRecommendations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.license_recommendation.deserialize_cbor(item)
        )
    return out
