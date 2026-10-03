"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.acgr_instance_arn
    import capo_connect.types.acgr_traffic_distribution_group_arn
    import capo_connect.types.acgr_traffic_distribution_group_id
    import capo_connect.types.boolean
    import capo_connect.types.name128
    import capo_connect.types.traffic_distribution_group_status


class TrafficDistributionGroupSummary(TypedDict, closed=True):
    id: NotRequired[
        "capo_connect.types.acgr_traffic_distribution_group_id.ACGRTrafficDistributionGroupId"
    ]
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.</p>"""
    arn: NotRequired[
        "capo_connect.types.acgr_traffic_distribution_group_arn.ACGRTrafficDistributionGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic distribution group.</p>"""
    name: NotRequired["capo_connect.types.name128.Name128"]
    """<p>The name of the traffic distribution group.</p>"""
    instance_arn: NotRequired["capo_connect.types.acgr_instance_arn.ACGRInstanceArn"]
    """<p>The Amazon Resource Name (ARN) of the instance.</p>"""
    status: NotRequired[
        "capo_connect.types.traffic_distribution_group_status.TrafficDistributionGroupStatus"
    ]
    """<p>The status of the traffic distribution group. </p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html">CreateTrafficDistributionGroup</a> operation is still in progress and has not yet completed.</p> </li> <li> <p> <code>ACTIVE</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html">CreateTrafficDistributionGroup</a> operation has succeeded.</p> </li> <li> <p> <code>CREATION_FAILED</code> indicates that the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html">CreateTrafficDistributionGroup</a> operation has failed.</p> </li> <li> <p> <code>PENDING_DELETION</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html">DeleteTrafficDistributionGroup</a> operation is still in progress and has not yet completed.</p> </li> <li> <p> <code>DELETION_FAILED</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html">DeleteTrafficDistributionGroup</a> operation has failed.</p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> means the previous <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistributionGroup.html">UpdateTrafficDistributionGroup</a> operation is still in progress and has not yet completed.</p> </li> </ul>"""
    is_default: "capo_connect.types.boolean.Boolean"
    """<p>Whether this is the default traffic distribution group created during instance replication. The default traffic distribution group cannot be deleted by the <code>DeleteTrafficDistributionGroup</code> API. The default traffic distribution group is deleted as part of the process for deleting a replica.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "status" in value:
        import capo_connect.types.traffic_distribution_group_status

        out["Status"] = (
            capo_connect.types.traffic_distribution_group_status.serialize_json(
                value["status"]
            )
        )
    out["IsDefault"] = value.get("is_default", False)
    return out


def deserialize_json(data: dict) -> TrafficDistributionGroupSummary:
    out: TrafficDistributionGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("Status") is not None:
        import capo_connect.types.traffic_distribution_group_status

        out["status"] = (
            capo_connect.types.traffic_distribution_group_status.deserialize_json(
                data["Status"]
            )
        )
    if data.get("IsDefault") is not None:
        out["is_default"] = data["IsDefault"]
    else:
        out["is_default"] = False
    return out
