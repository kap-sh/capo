"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#DeleteRecommendationPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.recommendation_preference_names
    import capo_compute_optimizer.types.resource_type
    import capo_compute_optimizer.types.scope


class DeleteRecommendationPreferencesRequest(TypedDict, closed=True):
    resource_type: "capo_compute_optimizer.types.resource_type.ResourceType"
    """<p>The target resource type of the recommendation preference to delete.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>"""
    scope: NotRequired["capo_compute_optimizer.types.scope.Scope"]
    """<p>An object that describes the scope of the recommendation preference to delete.</p> <p>You can delete recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    recommendation_preference_names: "capo_compute_optimizer.types.recommendation_preference_names.RecommendationPreferenceNames"
    """<p>The name of the recommendation preference to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRecommendationPreferencesRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer.types.resource_type

    out["resourceType"] = (
        capo_compute_optimizer.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    if "scope" in value:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.serialize_aws_json_1_0(
            value["scope"]
        )
    import capo_compute_optimizer.types.recommendation_preference_names

    out["recommendationPreferenceNames"] = (
        capo_compute_optimizer.types.recommendation_preference_names.serialize_aws_json_1_0(
            value["recommendation_preference_names"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRecommendationPreferencesRequest:
    out: DeleteRecommendationPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRecommendationPreferencesRequest.resource_type required"
        )
    if data.get("scope") is not None:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.deserialize_aws_json_1_0(
            data["scope"]
        )
    if data.get("recommendationPreferenceNames") is not None:
        import capo_compute_optimizer.types.recommendation_preference_names

        out["recommendation_preference_names"] = (
            capo_compute_optimizer.types.recommendation_preference_names.deserialize_aws_json_1_0(
                data["recommendationPreferenceNames"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRecommendationPreferencesRequest.recommendation_preference_names required"
        )
    return out
