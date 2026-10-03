"""Generated from Smithy shape ``com.amazonaws.devopsguru#RecommendationRelatedAnomalyResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendation_related_anomaly_resource_name
    import capo_devops_guru.types.recommendation_related_anomaly_resource_type


class RecommendationRelatedAnomalyResource(TypedDict, closed=True):
    name: NotRequired[
        "capo_devops_guru.types.recommendation_related_anomaly_resource_name.RecommendationRelatedAnomalyResourceName"
    ]
    """<p> The name of the resource. </p>"""
    type: NotRequired[
        "capo_devops_guru.types.recommendation_related_anomaly_resource_type.RecommendationRelatedAnomalyResourceType"
    ]
    """<p> The type of the resource. Resource types take the same form that is used by Amazon Web Services CloudFormation resource type identifiers, <code>service-provider::service-name::data-type-name</code>. For example, <code>AWS::RDS::DBCluster</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>Amazon Web Services CloudFormation User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationRelatedAnomalyResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> RecommendationRelatedAnomalyResource:
    out: RecommendationRelatedAnomalyResource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
