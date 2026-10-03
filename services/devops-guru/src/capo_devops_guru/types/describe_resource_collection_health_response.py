"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeResourceCollectionHealthResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.cloud_formation_healths
    import capo_devops_guru.types.service_healths
    import capo_devops_guru.types.tag_healths
    import capo_devops_guru.types.uuid_next_token


class DescribeResourceCollectionHealthResponse(TypedDict, closed=True):
    cloud_formation: NotRequired[
        "capo_devops_guru.types.cloud_formation_healths.CloudFormationHealths"
    ]
    """<p> The returned <code>CloudFormationHealthOverview</code> object that contains an <code>InsightHealthOverview</code> object with the requested system health information. </p>"""
    service: NotRequired["capo_devops_guru.types.service_healths.ServiceHealths"]
    """<p>An array of <code>ServiceHealth</code> objects that describes the health of the Amazon Web Services services associated with the resources in the collection.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""
    tags: NotRequired["capo_devops_guru.types.tag_healths.TagHealths"]
    """<p>The Amazon Web Services tags that are used by resources in the resource collection.</p> <p>Tags help you identify and organize your Amazon Web Services resources. Many Amazon Web Services services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an Lambda function. For more information about using tags, see the <a href="https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html">Tagging best practices</a> whitepaper. </p> <p>Each Amazon Web Services tag has two parts. </p> <ul> <li> <p>A tag <i>key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag <i>keys</i> are case-sensitive.</p> </li> <li> <p>An optional field known as a tag <i>value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag <i>value</i> is the same as using an empty string. Like tag <i>keys</i>, tag <i>values</i> are case-sensitive.</p> </li> </ul> <p>Together these are known as <i>key</i>-<i>value</i> pairs.</p> <important> <p>The string used for a <i>key</i> in a tag that you use to define your resource coverage must begin with the prefix <code>Devops-guru-</code>. The tag <i>key</i> might be <code>DevOps-Guru-deployment-application</code> or <code>devops-guru-rds-application</code>. When you create a <i>key</i>, the case of characters in the <i>key</i> can be whatever you choose. After you create a <i>key</i>, it is case-sensitive. For example, DevOps Guru works with a <i>key</i> named <code>devops-guru-rds</code> and a <i>key</i> named <code>DevOps-Guru-RDS</code>, and these act as two different <i>keys</i>. Possible <i>key</i>/<i>value</i> pairs in your application might be <code>Devops-Guru-production-application/RDS</code> or <code>Devops-Guru-production-application/containers</code>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeResourceCollectionHealthResponse) -> dict:
    out: dict = {}
    if "cloud_formation" in value:
        import capo_devops_guru.types.cloud_formation_healths

        out["CloudFormation"] = (
            capo_devops_guru.types.cloud_formation_healths.serialize_json(
                value["cloud_formation"]
            )
        )
    if "service" in value:
        import capo_devops_guru.types.service_healths

        out["Service"] = capo_devops_guru.types.service_healths.serialize_json(
            value["service"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "tags" in value:
        import capo_devops_guru.types.tag_healths

        out["Tags"] = capo_devops_guru.types.tag_healths.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeResourceCollectionHealthResponse:
    out: DescribeResourceCollectionHealthResponse = {}  # type: ignore[typeddict-item]
    if data.get("CloudFormation") is not None:
        import capo_devops_guru.types.cloud_formation_healths

        out["cloud_formation"] = (
            capo_devops_guru.types.cloud_formation_healths.deserialize_json(
                data["CloudFormation"]
            )
        )
    if data.get("Service") is not None:
        import capo_devops_guru.types.service_healths

        out["service"] = capo_devops_guru.types.service_healths.deserialize_json(
            data["Service"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Tags") is not None:
        import capo_devops_guru.types.tag_healths

        out["tags"] = capo_devops_guru.types.tag_healths.deserialize_json(data["Tags"])
    return out
