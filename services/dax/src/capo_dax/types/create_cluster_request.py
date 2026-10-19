"""Generated from Smithy shape ``com.amazonaws.dax#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dax.types.availability_zone_list
    import capo_dax.types.cluster_endpoint_encryption_type
    import capo_dax.types.integer
    import capo_dax.types.network_type
    import capo_dax.types.security_group_identifier_list
    import capo_dax.types.sse_specification
    import capo_dax.types.string
    import capo_dax.types.tag_list


class CreateClusterRequest(TypedDict, closed=True):
    cluster_name: "capo_dax.types.string.String"
    """<p>The cluster identifier. This parameter is stored as a lowercase string.</p> <p> <b>Constraints:</b> </p> <ul> <li> <p>A name must contain from 1 to 20 alphanumeric characters or hyphens.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>A name cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    node_type: "capo_dax.types.string.String"
    """<p>The compute and memory capacity of the nodes in the cluster.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the cluster.</p>"""
    replication_factor: "capo_dax.types.integer.Integer"
    """<p>The number of nodes in the DAX cluster. A replication factor of 1 will create a single-node cluster, without any read replicas. For additional fault tolerance, you can create a multiple node cluster with one or more read replicas. To do this, set <code>ReplicationFactor</code> to a number between 3 (one primary and two read replicas) and 10 (one primary and nine read replicas). <code>If the AvailabilityZones</code> parameter is provided, its length must equal the <code>ReplicationFactor</code>.</p> <note> <p>Amazon Web Services recommends that you have at least two read replicas per cluster.</p> </note>"""
    availability_zones: NotRequired[
        "capo_dax.types.availability_zone_list.AvailabilityZoneList"
    ]
    """<p>The Availability Zones (AZs) in which the cluster nodes will reside after the cluster has been created or updated. If provided, the length of this list must equal the <code>ReplicationFactor</code> parameter. If you omit this parameter, DAX will spread the nodes across Availability Zones for the highest availability.</p>"""
    subnet_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the subnet group to be used for the replication group.</p> <important> <p>DAX clusters can only run in an Amazon VPC environment. All of the subnets that you specify in a subnet group must exist in the same VPC.</p> </important>"""
    security_group_ids: NotRequired[
        "capo_dax.types.security_group_identifier_list.SecurityGroupIdentifierList"
    ]
    """<p>A list of security group IDs to be assigned to each node in the DAX cluster. (Each of the security group ID is system-generated.)</p> <p>If this parameter is not specified, DAX assigns the default VPC security group to each node.</p>"""
    preferred_maintenance_window: NotRequired["capo_dax.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the DAX cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period. Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:05:00-sun:09:00</code> </p> <note> <p>If you don't specify a preferred maintenance window when you create or modify a cache cluster, DAX assigns a 60-minute maintenance window on a randomly selected day of the week.</p> </note>"""
    notification_topic_arn: NotRequired["capo_dax.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic to which notifications will be sent.</p> <note> <p>The Amazon SNS topic owner must be same as the DAX cluster owner.</p> </note>"""
    iam_role_arn: "capo_dax.types.string.String"
    """<p>A valid Amazon Resource Name (ARN) that identifies an IAM role. At runtime, DAX will assume this role and use the role's permissions to access DynamoDB on your behalf.</p>"""
    parameter_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The parameter group to be associated with the DAX cluster.</p>"""
    tags: NotRequired["capo_dax.types.tag_list.TagList"]
    """<p>A set of tags to associate with the DAX cluster. </p>"""
    sse_specification: NotRequired["capo_dax.types.sse_specification.SSESpecification"]
    """<p>Represents the settings used to enable server-side encryption on the cluster.</p>"""
    cluster_endpoint_encryption_type: NotRequired[
        "capo_dax.types.cluster_endpoint_encryption_type.ClusterEndpointEncryptionType"
    ]
    """<p>The type of encryption the cluster's endpoint should support. Values are:</p> <ul> <li> <p> <code>NONE</code> for no encryption</p> </li> <li> <p> <code>TLS</code> for Transport Layer Security</p> </li> </ul>"""
    network_type: NotRequired["capo_dax.types.network_type.NetworkType"]
    """<p>Specifies the IP protocol(s) the cluster uses for network communications. Values are:</p> <ul> <li> <p> <code>ipv4</code> - The cluster is accessible only through IPv4 addresses</p> </li> <li> <p> <code>ipv6</code> - The cluster is accessible only through IPv6 addresses</p> </li> <li> <p> <code>dual_stack</code> - The cluster is accessible through both IPv4 and IPv6 addresses.</p> </li> </ul> <note> <p>If no explicit <code>NetworkType</code> is provided, the network type is derived based on the subnet group's configuration.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NodeType"] = value["node_type"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ReplicationFactor"] = value["replication_factor"]
    if "availability_zones" in value:
        import capo_dax.types.availability_zone_list

        out["AvailabilityZones"] = (
            capo_dax.types.availability_zone_list.serialize_aws_json_1_1(
                value["availability_zones"]
            )
        )
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "security_group_ids" in value:
        import capo_dax.types.security_group_identifier_list

        out["SecurityGroupIds"] = (
            capo_dax.types.security_group_identifier_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "preferred_maintenance_window" in value:
        out["PreferredMaintenanceWindow"] = value["preferred_maintenance_window"]
    if "notification_topic_arn" in value:
        out["NotificationTopicArn"] = value["notification_topic_arn"]
    out["IamRoleArn"] = value["iam_role_arn"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "tags" in value:
        import capo_dax.types.tag_list

        out["Tags"] = capo_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "sse_specification" in value:
        import capo_dax.types.sse_specification

        out["SSESpecification"] = (
            capo_dax.types.sse_specification.serialize_aws_json_1_1(
                value["sse_specification"]
            )
        )
    if "cluster_endpoint_encryption_type" in value:
        import capo_dax.types.cluster_endpoint_encryption_type

        out["ClusterEndpointEncryptionType"] = (
            capo_dax.types.cluster_endpoint_encryption_type.serialize_aws_json_1_1(
                value["cluster_endpoint_encryption_type"]
            )
        )
    if "network_type" in value:
        import capo_dax.types.network_type

        out["NetworkType"] = capo_dax.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("CreateClusterRequest.cluster_name required")
    if data.get("NodeType") is not None:
        out["node_type"] = data["NodeType"]
    else:
        raise DeserializationError("CreateClusterRequest.node_type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ReplicationFactor") is not None:
        out["replication_factor"] = data["ReplicationFactor"]
    else:
        raise DeserializationError("CreateClusterRequest.replication_factor required")
    if data.get("AvailabilityZones") is not None:
        import capo_dax.types.availability_zone_list

        out["availability_zones"] = (
            capo_dax.types.availability_zone_list.deserialize_aws_json_1_1(
                data["AvailabilityZones"]
            )
        )
    if data.get("SubnetGroupName") is not None:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if data.get("SecurityGroupIds") is not None:
        import capo_dax.types.security_group_identifier_list

        out["security_group_ids"] = (
            capo_dax.types.security_group_identifier_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if data.get("PreferredMaintenanceWindow") is not None:
        out["preferred_maintenance_window"] = data["PreferredMaintenanceWindow"]
    if data.get("NotificationTopicArn") is not None:
        out["notification_topic_arn"] = data["NotificationTopicArn"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    else:
        raise DeserializationError("CreateClusterRequest.iam_role_arn required")
    if data.get("ParameterGroupName") is not None:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if data.get("Tags") is not None:
        import capo_dax.types.tag_list

        out["tags"] = capo_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("SSESpecification") is not None:
        import capo_dax.types.sse_specification

        out["sse_specification"] = (
            capo_dax.types.sse_specification.deserialize_aws_json_1_1(
                data["SSESpecification"]
            )
        )
    if data.get("ClusterEndpointEncryptionType") is not None:
        import capo_dax.types.cluster_endpoint_encryption_type

        out["cluster_endpoint_encryption_type"] = (
            capo_dax.types.cluster_endpoint_encryption_type.deserialize_aws_json_1_1(
                data["ClusterEndpointEncryptionType"]
            )
        )
    if data.get("NetworkType") is not None:
        import capo_dax.types.network_type

        out["network_type"] = capo_dax.types.network_type.deserialize_aws_json_1_1(
            data["NetworkType"]
        )
    return out
