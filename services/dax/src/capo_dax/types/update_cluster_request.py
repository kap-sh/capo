"""Generated from Smithy shape ``com.amazonaws.dax#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.security_group_identifier_list
    import capo_dax.types.string


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The name of the DAX cluster to be modified.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the changes being made to the cluster.</p>"""
    preferred_maintenance_window: NotRequired["capo_dax.types.string.String"]
    """<p>A range of time when maintenance of DAX cluster software will be performed. For example: <code>sun:01:00-sun:09:00</code>. Cluster maintenance normally takes less than 30 minutes, and is performed automatically within the maintenance window.</p>"""
    notification_topic_arn: NotRequired["capo_dax.types.string.String"]
    """<p>The Amazon Resource Name (ARN) that identifies the topic.</p>"""
    notification_topic_status: NotRequired["capo_dax.types.string.String"]
    """<p>The current state of the topic. A value of “active” means that notifications will be sent to the topic. A value of “inactive” means that notifications will not be sent to the topic.</p>"""
    parameter_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of a parameter group for this cluster.</p>"""
    security_group_ids: NotRequired[
        "capo_dax.types.security_group_identifier_list.SecurityGroupIdentifierList"
    ]
    """<p>A list of user-specified security group IDs to be assigned to each node in the DAX cluster. If this parameter is not specified, DAX assigns the default VPC security group to each node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "notification_topic_arn" in value:
        out["NotificationTopicArn"] = value["notification_topic_arn"]
    if "notification_topic_status" in value:
        out["NotificationTopicStatus"] = value["notification_topic_status"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "security_group_ids" in value:
        import capo_dax.types.security_group_identifier_list

        out["SecurityGroupIds"] = (
            capo_dax.types.security_group_identifier_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("NotificationTopicArn") is not None:
        out["notification_topic_arn"] = data["NotificationTopicArn"]
    if data.get("NotificationTopicStatus") is not None:
        out["notification_topic_status"] = data["NotificationTopicStatus"]
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if data.get("SecurityGroupIds") is not None:
        import capo_dax.types.security_group_identifier_list

        out["security_group_ids"] = (
            capo_dax.types.security_group_identifier_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    return out
