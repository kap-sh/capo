"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_compute_optimizer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_compute_optimizer.types.max_results
    import capo_compute_optimizer.types.next_token
    import capo_compute_optimizer.types.resource_type
    import capo_compute_optimizer.types.scope


class GetRecommendationPreferencesRequest(TypedDict, closed=True):
    resource_type: "capo_compute_optimizer.types.resource_type.ResourceType"
    """<p>The target resource type of the recommendation preference for which to return preferences.</p> <p>The <code>Ec2Instance</code> option encompasses standalone instances and instances that are part of Auto Scaling groups. The <code>AutoScalingGroup</code> option encompasses only instances that are part of an Auto Scaling group.</p>"""
    scope: NotRequired["capo_compute_optimizer.types.scope.Scope"]
    """<p>An object that describes the scope of the recommendation preference to return.</p> <p>You can return recommendation preferences that are created at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see <a href="https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html">Activating enhanced infrastructure metrics</a> in the <i>Compute Optimizer User Guide</i>.</p>"""
    next_token: NotRequired["capo_compute_optimizer.types.next_token.NextToken"]
    """<p>The token to advance to the next page of recommendation preferences.</p>"""
    max_results: NotRequired["capo_compute_optimizer.types.max_results.MaxResults"]
    """<p>The maximum number of recommendation preferences to return with a single request.</p> <p>To retrieve the remaining results, make another request with the returned <code>nextToken</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationPreferencesRequest) -> dict:
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
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationPreferencesRequest:
    out: GetRecommendationPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        import capo_compute_optimizer.types.resource_type

        out["resource_type"] = (
            capo_compute_optimizer.types.resource_type.deserialize_aws_json_1_0(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationPreferencesRequest.resource_type required"
        )
    if data.get("scope") is not None:
        import capo_compute_optimizer.types.scope

        out["scope"] = capo_compute_optimizer.types.scope.deserialize_aws_json_1_0(
            data["scope"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
