"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_source_arn
    import capo_compute_optimizer.types.recommendation_source_type


class RecommendationSource(TypedDict, closed=True):
    recommendation_source_arn: NotRequired[
        "capo_compute_optimizer.types.recommendation_source_arn.RecommendationSourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the recommendation source.</p>"""
    recommendation_source_type: NotRequired[
        "capo_compute_optimizer.types.recommendation_source_type.RecommendationSourceType"
    ]
    """<p>The resource type of the recommendation source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationSource) -> dict:
    out: dict = {}
    if "recommendation_source_arn" in value:
        out["recommendationSourceArn"] = value["recommendation_source_arn"]
    if "recommendation_source_type" in value:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendationSourceType"] = (
            capo_compute_optimizer.types.recommendation_source_type.serialize_aws_json_1_0(
                value["recommendation_source_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationSource:
    out: RecommendationSource = {}  # type: ignore[typeddict-item]
    if data.get("recommendationSourceArn") is not None:
        out["recommendation_source_arn"] = data["recommendationSourceArn"]
    if data.get("recommendationSourceType") is not None:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendation_source_type"] = (
            capo_compute_optimizer.types.recommendation_source_type.deserialize_aws_json_1_0(
                data["recommendationSourceType"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecommendationSource) -> dict:
    out: dict = {}
    if "recommendation_source_arn" in value:
        out["recommendationSourceArn"] = value["recommendation_source_arn"]
    if "recommendation_source_type" in value:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendationSourceType"] = (
            capo_compute_optimizer.types.recommendation_source_type.serialize_cbor(
                value["recommendation_source_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> RecommendationSource:
    out: RecommendationSource = {}  # type: ignore[typeddict-item]
    if data.get("recommendationSourceArn") is not None:
        out["recommendation_source_arn"] = data["recommendationSourceArn"]
    if data.get("recommendationSourceType") is not None:
        import capo_compute_optimizer.types.recommendation_source_type

        out["recommendation_source_type"] = (
            capo_compute_optimizer.types.recommendation_source_type.deserialize_cbor(
                data["recommendationSourceType"]
            )
        )
    return out
