"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourceCollectionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_formation_collection_filter
    import capo_devops_guru.types.tag_collection_filters


class ResourceCollectionFilter(TypedDict, closed=True):
    cloud_formation: NotRequired[
        "capo_devops_guru.types.cloud_formation_collection_filter.CloudFormationCollectionFilter"
    ]
    """<p> Information about Amazon Web Services CloudFormation stacks. You can use up to 500 stacks to specify which Amazon Web Services resources in your account to analyze. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html">Stacks</a> in the <i>Amazon Web Services CloudFormation User Guide</i>. </p>"""
    tags: NotRequired[
        "capo_devops_guru.types.tag_collection_filters.TagCollectionFilters"
    ]
    """<p>The Amazon Web Services tags used to filter the resources in the resource collection.</p> <p>Tags help you identify and organize your Amazon Web Services resources. Many Amazon Web Services services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an Lambda function. For more information about using tags, see the <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html">Tagging best practices</a> whitepaper. </p> <p>Each Amazon Web Services tag has two parts. </p> <ul> <li> <p>A tag <i>key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag <i>keys</i> are case-sensitive.</p> </li> <li> <p>An optional field known as a tag <i>value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag <i>value</i> is the same as using an empty string. Like tag <i>keys</i>, tag <i>values</i> are case-sensitive.</p> </li> </ul> <p>Together these are known as <i>key</i>-<i>value</i> pairs.</p> <important> <p>The string used for a <i>key</i> in a tag that you use to define your resource coverage must begin with the prefix <code>Devops-guru-</code>. The tag <i>key</i> might be <code>DevOps-Guru-deployment-application</code> or <code>devops-guru-rds-application</code>. When you create a <i>key</i>, the case of characters in the <i>key</i> can be whatever you choose. After you create a <i>key</i>, it is case-sensitive. For example, DevOps Guru works with a <i>key</i> named <code>devops-guru-rds</code> and a <i>key</i> named <code>DevOps-Guru-RDS</code>, and these act as two different <i>keys</i>. Possible <i>key</i>/<i>value</i> pairs in your application might be <code>Devops-Guru-production-application/RDS</code> or <code>Devops-Guru-production-application/containers</code>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceCollectionFilter) -> dict:
    out: dict = {}
    if "cloud_formation" in value:
        import capo_devops_guru.types.cloud_formation_collection_filter

        out["CloudFormation"] = (
            capo_devops_guru.types.cloud_formation_collection_filter.serialize_json(
                value["cloud_formation"]
            )
        )
    if "tags" in value:
        import capo_devops_guru.types.tag_collection_filters

        out["Tags"] = capo_devops_guru.types.tag_collection_filters.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ResourceCollectionFilter:
    out: ResourceCollectionFilter = {}  # type: ignore[typeddict-item]
    if data.get("CloudFormation") is not None:
        import capo_devops_guru.types.cloud_formation_collection_filter

        out["cloud_formation"] = (
            capo_devops_guru.types.cloud_formation_collection_filter.deserialize_json(
                data["CloudFormation"]
            )
        )
    if data.get("Tags") is not None:
        import capo_devops_guru.types.tag_collection_filters

        out["tags"] = capo_devops_guru.types.tag_collection_filters.deserialize_json(
            data["Tags"]
        )
    return out
