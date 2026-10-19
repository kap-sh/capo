"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetEffectiveRecommendationPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.resource_arn


class GetEffectiveRecommendationPreferencesRequest(TypedDict, closed=True):
    resource_arn: "capo_compute_optimizer.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource for which to confirm effective recommendation preferences. Only EC2 instance and Auto Scaling group ARNs are currently supported.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEffectiveRecommendationPreferencesRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> GetEffectiveRecommendationPreferencesRequest:
    out: GetEffectiveRecommendationPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
