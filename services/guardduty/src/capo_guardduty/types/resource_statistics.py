"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.integer
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class ResourceStatistics(TypedDict, closed=True):
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the Amazon Web Services account.</p>"""
    last_generated_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the statistics for this resource was last generated.</p>"""
    resource_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>ID associated with each resource. The following list provides the mapping of the resource type and resource ID.</p> <p class="title"> <b>Mapping of resource and resource ID</b> </p> <ul> <li> <p>AccessKey - <code>resource.accessKeyDetails.accessKeyId</code> </p> </li> <li> <p>Container - <code>resource.containerDetails.id</code> </p> </li> <li> <p>ECSCluster - <code>resource.ecsClusterDetails.name</code> </p> </li> <li> <p>EKSCluster - <code>resource.eksClusterDetails.name</code> </p> </li> <li> <p>Instance - <code>resource.instanceDetails.instanceId</code> </p> </li> <li> <p>KubernetesCluster - <code>resource.kubernetesDetails.kubernetesWorkloadDetails.name</code> </p> </li> <li> <p>Lambda - <code>resource.lambdaDetails.functionName</code> </p> </li> <li> <p>RDSDBInstance - <code>resource.rdsDbInstanceDetails.dbInstanceIdentifier</code> </p> </li> <li> <p>S3Bucket - <code>resource.s3BucketDetails.name</code> </p> </li> <li> <p>S3Object - <code>resource.s3BucketDetails.name</code> </p> </li> </ul>"""
    resource_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of resource.</p>"""
    total_findings: NotRequired["capo_guardduty.types.integer.Integer"]
    """<p>The total number of findings associated with this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatistics) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "last_generated_at" in value:
        import capo_guardduty.types.timestamp

        out["lastGeneratedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["last_generated_at"]
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "total_findings" in value:
        out["totalFindings"] = value["total_findings"]
    return out


def deserialize_json(data: dict) -> ResourceStatistics:
    out: ResourceStatistics = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("lastGeneratedAt") is not None:
        import capo_guardduty.types.timestamp

        out["last_generated_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["lastGeneratedAt"]
        )
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("totalFindings") is not None:
        out["total_findings"] = data["totalFindings"]
    return out
