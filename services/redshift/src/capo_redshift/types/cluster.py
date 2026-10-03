"""Generated from Smithy shape ``com.amazonaws.redshift#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.aqua_configuration
    import capo_redshift.types.boolean
    import capo_redshift.types.cluster_iam_role_list
    import capo_redshift.types.cluster_nodes_list
    import capo_redshift.types.cluster_parameter_group_status_list
    import capo_redshift.types.cluster_security_group_membership_list
    import capo_redshift.types.cluster_snapshot_copy_status
    import capo_redshift.types.data_transfer_progress
    import capo_redshift.types.deferred_maintenance_windows_list
    import capo_redshift.types.elastic_ip_status
    import capo_redshift.types.endpoint
    import capo_redshift.types.hsm_status
    import capo_redshift.types.integer
    import capo_redshift.types.logging_publish_status
    import capo_redshift.types.long_optional
    import capo_redshift.types.pending_actions_list
    import capo_redshift.types.pending_modified_values
    import capo_redshift.types.reserved_node_exchange_status
    import capo_redshift.types.resize_info
    import capo_redshift.types.restore_status
    import capo_redshift.types.schedule_state
    import capo_redshift.types.secondary_cluster_info
    import capo_redshift.types.string
    import capo_redshift.types.t_stamp
    import capo_redshift.types.tag_list
    import capo_redshift.types.vpc_security_group_membership_list


class Cluster(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster.</p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type for the nodes in the cluster.</p>"""
    cluster_status: NotRequired["capo_redshift.types.string.String"]
    """<p> The current state of the cluster. Possible values are the following:</p> <ul> <li> <p> <code>available</code> </p> </li> <li> <p> <code>available, prep-for-resize</code> </p> </li> <li> <p> <code>available, resize-cleanup</code> </p> </li> <li> <p> <code>cancelling-resize</code> </p> </li> <li> <p> <code>creating</code> </p> </li> <li> <p> <code>deleting</code> </p> </li> <li> <p> <code>final-snapshot</code> </p> </li> <li> <p> <code>hardware-failure</code> </p> </li> <li> <p> <code>incompatible-hsm</code> </p> </li> <li> <p> <code>incompatible-network</code> </p> </li> <li> <p> <code>incompatible-parameters</code> </p> </li> <li> <p> <code>incompatible-restore</code> </p> </li> <li> <p> <code>modifying</code> </p> </li> <li> <p> <code>paused</code> </p> </li> <li> <p> <code>rebooting</code> </p> </li> <li> <p> <code>renaming</code> </p> </li> <li> <p> <code>resizing</code> </p> </li> <li> <p> <code>rotating-keys</code> </p> </li> <li> <p> <code>storage-full</code> </p> </li> <li> <p> <code>updating-hsm</code> </p> </li> </ul>"""
    cluster_availability_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The availability status of the cluster for queries. Possible values are the following:</p> <ul> <li> <p>Available - The cluster is available for queries. </p> </li> <li> <p>Unavailable - The cluster is not available for queries.</p> </li> <li> <p>Maintenance - The cluster is intermittently available for queries due to maintenance activities.</p> </li> <li> <p>Modifying - The cluster is intermittently available for queries due to changes that modify the cluster.</p> </li> <li> <p>Failed - The cluster failed and is not available for queries.</p> </li> </ul>"""
    modify_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of a modify operation, if any, initiated for the cluster.</p>"""
    master_username: NotRequired["capo_redshift.types.string.String"]
    """<p>The admin user name for the cluster. This name is used to connect to the database that is specified in the <b>DBName</b> parameter. </p>"""
    db_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the initial database that was created when the cluster was created. This same name is returned for the life of the cluster. If an initial database was not specified, a database named <code>dev</code>dev was created by default. </p>"""
    endpoint: NotRequired["capo_redshift.types.endpoint.Endpoint"]
    """<p>The connection endpoint.</p>"""
    cluster_create_time: NotRequired["capo_redshift.types.t_stamp.TStamp"]
    """<p>The date and time that the cluster was created.</p>"""
    automated_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer.Integer"
    ]
    """<p>The number of days that automatic cluster snapshots are retained.</p>"""
    manual_snapshot_retention_period: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    cluster_security_groups: NotRequired[
        "capo_redshift.types.cluster_security_group_membership_list.ClusterSecurityGroupMembershipList"
    ]
    """<p>A list of cluster security group that are associated with the cluster. Each security group is represented by an element that contains <code>ClusterSecurityGroup.Name</code> and <code>ClusterSecurityGroup.Status</code> subelements. </p> <p>Cluster security groups are used when the cluster is not created in an Amazon Virtual Private Cloud (VPC). Clusters that are created in a VPC use VPC security groups, which are listed by the <b>VpcSecurityGroups</b> parameter. </p>"""
    vpc_security_groups: NotRequired[
        "capo_redshift.types.vpc_security_group_membership_list.VpcSecurityGroupMembershipList"
    ]
    """<p>A list of Amazon Virtual Private Cloud (Amazon VPC) security groups that are associated with the cluster. This parameter is returned only if the cluster is in a VPC.</p>"""
    cluster_parameter_groups: NotRequired[
        "capo_redshift.types.cluster_parameter_group_status_list.ClusterParameterGroupStatusList"
    ]
    """<p>The list of cluster parameter groups that are associated with this cluster. Each parameter group in the list is returned with its status.</p>"""
    cluster_subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the subnet group that is associated with the cluster. This parameter is valid only when the cluster is in a VPC.</p>"""
    vpc_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the VPC the cluster is in, if the cluster is in a VPC.</p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the Availability Zone in which the cluster is located.</p>"""
    preferred_maintenance_window: NotRequired["capo_redshift.types.string.String"]
    """<p>The weekly time range, in Universal Coordinated Time (UTC), during which system maintenance can occur.</p>"""
    pending_modified_values: NotRequired[
        "capo_redshift.types.pending_modified_values.PendingModifiedValues"
    ]
    """<p>A value that, if present, indicates that changes to the cluster are pending. Specific pending changes are identified by subelements.</p>"""
    cluster_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The version ID of the Amazon Redshift engine that is running on the cluster.</p>"""
    allow_version_upgrade: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean value that, if <code>true</code>, indicates that major version upgrades will be applied automatically to the cluster during the maintenance window. </p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer.Integer"]
    """<p>The number of compute nodes in the cluster.</p>"""
    publicly_accessible: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean value that, if <code>true</code>, indicates that the cluster can be accessed from a public network.</p> <p>Default: false</p>"""
    encrypted: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>A boolean value that, if <code>true</code>, indicates that data in the cluster is encrypted at rest.</p>"""
    restore_status: NotRequired["capo_redshift.types.restore_status.RestoreStatus"]
    """<p>A value that describes the status of a cluster restore action. This parameter returns null if the cluster was not created by restoring a snapshot.</p>"""
    data_transfer_progress: NotRequired[
        "capo_redshift.types.data_transfer_progress.DataTransferProgress"
    ]
    """<p></p>"""
    hsm_status: NotRequired["capo_redshift.types.hsm_status.HsmStatus"]
    """<p>A value that reports whether the Amazon Redshift cluster has finished applying any hardware security module (HSM) settings changes specified in a modify cluster command.</p> <p>Values: active, applying</p>"""
    cluster_snapshot_copy_status: NotRequired[
        "capo_redshift.types.cluster_snapshot_copy_status.ClusterSnapshotCopyStatus"
    ]
    """<p>A value that returns the destination region and retention period that are configured for cross-region snapshot copy.</p>"""
    cluster_public_key: NotRequired["capo_redshift.types.string.String"]
    """<p>The public key for the cluster.</p>"""
    cluster_nodes: NotRequired[
        "capo_redshift.types.cluster_nodes_list.ClusterNodesList"
    ]
    """<p>The nodes in the cluster.</p>"""
    elastic_ip_status: NotRequired[
        "capo_redshift.types.elastic_ip_status.ElasticIpStatus"
    ]
    """<p>The status of the elastic IP (EIP) address.</p>"""
    cluster_revision_number: NotRequired["capo_redshift.types.string.String"]
    """<p>The specific revision number of the database in the cluster.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>The list of tags for the cluster.</p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key ID of the encryption key used to encrypt data in the cluster.</p>"""
    enhanced_vpc_routing: NotRequired["capo_redshift.types.boolean.Boolean"]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    iam_roles: NotRequired[
        "capo_redshift.types.cluster_iam_role_list.ClusterIamRoleList"
    ]
    """<p>A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services.</p>"""
    pending_actions: NotRequired[
        "capo_redshift.types.pending_actions_list.PendingActionsList"
    ]
    """<p>Cluster operations that are waiting to be started.</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the maintenance track for the cluster.</p>"""
    elastic_resize_number_of_node_options: NotRequired[
        "capo_redshift.types.string.String"
    ]
    """<p>The number of nodes that you can resize the cluster to with the elastic resize method. </p>"""
    deferred_maintenance_windows: NotRequired[
        "capo_redshift.types.deferred_maintenance_windows_list.DeferredMaintenanceWindowsList"
    ]
    """<p>Describes a group of <code>DeferredMaintenanceWindow</code> objects.</p>"""
    snapshot_schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the cluster snapshot schedule.</p>"""
    snapshot_schedule_state: NotRequired[
        "capo_redshift.types.schedule_state.ScheduleState"
    ]
    """<p>The current state of the cluster snapshot schedule.</p>"""
    expected_next_snapshot_schedule_time: NotRequired[
        "capo_redshift.types.t_stamp.TStamp"
    ]
    """<p>The date and time when the next snapshot is expected to be taken for clusters with a valid snapshot schedule and backups enabled. </p>"""
    expected_next_snapshot_schedule_time_status: NotRequired[
        "capo_redshift.types.string.String"
    ]
    """<p> The status of next expected snapshot for clusters having a valid snapshot schedule and backups enabled. Possible values are the following:</p> <ul> <li> <p>OnTrack - The next snapshot is expected to be taken on time. </p> </li> <li> <p>Pending - The next snapshot is pending to be taken. </p> </li> </ul>"""
    next_maintenance_window_start_time: NotRequired[
        "capo_redshift.types.t_stamp.TStamp"
    ]
    """<p>The date and time in UTC when system maintenance can begin.</p>"""
    resize_info: NotRequired["capo_redshift.types.resize_info.ResizeInfo"]
    """<p>Returns the following:</p> <ul> <li> <p>AllowCancelResize: a boolean value indicating if the resize operation can be cancelled.</p> </li> <li> <p>ResizeType: Returns ClassicResize</p> </li> </ul>"""
    availability_zone_relocation_status: NotRequired[
        "capo_redshift.types.string.String"
    ]
    """<p>Describes the status of the Availability Zone relocation operation.</p>"""
    cluster_namespace_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The namespace Amazon Resource Name (ARN) of the cluster.</p>"""
    total_storage_capacity_in_mega_bytes: NotRequired[
        "capo_redshift.types.long_optional.LongOptional"
    ]
    """<p>The total storage capacity of the cluster in megabytes. </p>"""
    aqua_configuration: NotRequired[
        "capo_redshift.types.aqua_configuration.AquaConfiguration"
    ]
    """<p>This field is retired. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""
    default_iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role set as default for the cluster.</p>"""
    reserved_node_exchange_status: NotRequired[
        "capo_redshift.types.reserved_node_exchange_status.ReservedNodeExchangeStatus"
    ]
    """<p>The status of the reserved-node exchange request. Statuses include in-progress and requested.</p>"""
    custom_domain_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The custom domain name associated with the cluster.</p>"""
    custom_domain_certificate_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The certificate Amazon Resource Name (ARN) for the custom domain name.</p>"""
    custom_domain_certificate_expiry_date: NotRequired[
        "capo_redshift.types.t_stamp.TStamp"
    ]
    """<p>The expiration date for the certificate associated with the custom domain name.</p>"""
    master_password_secret_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the cluster's admin user credentials secret.</p>"""
    master_password_secret_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret.</p>"""
    ip_address_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP address type for the cluster. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    multi_az: NotRequired["capo_redshift.types.string.String"]
    """<p>A boolean value that, if true, indicates that the cluster is deployed in two Availability Zones.</p>"""
    multi_az_secondary: NotRequired[
        "capo_redshift.types.secondary_cluster_info.SecondaryClusterInfo"
    ]
    """<p>The secondary compute unit of a cluster, if Multi-AZ deployment is turned on.</p>"""
    lakehouse_registration_status: NotRequired["capo_redshift.types.string.String"]
    """<p>The status of the lakehouse registration for the cluster. Indicates whether the cluster is successfully registered with Amazon Redshift federated permissions.</p>"""
    catalog_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Glue data catalog associated with the cluster enabled with Amazon Redshift federated permissions.</p>"""
    extra_compute_for_automatic_optimization: NotRequired[
        "capo_redshift.types.string.String"
    ]
    """<p>A boolean value that, if <code>true</code>, indicates that the cluster allocates additional compute resources to run automatic optimization operations.</p> <p>Default: false</p>"""
    logging_publish_status: NotRequired[
        "capo_redshift.types.logging_publish_status.LoggingPublishStatus"
    ]
    """<p>The status of system table publishing for the cluster. This field is present only when system table publishing is configured.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Cluster, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "cluster_status" in value:
        pairs.append((f"{key_prefix}ClusterStatus", str(value["cluster_status"])))
    if "cluster_availability_status" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterAvailabilityStatus",
                str(value["cluster_availability_status"]),
            )
        )
    if "modify_status" in value:
        pairs.append((f"{key_prefix}ModifyStatus", str(value["modify_status"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "endpoint" in value:
        import capo_redshift.types.endpoint

        capo_redshift.types.endpoint.serialize_query(
            value["endpoint"], pairs, f"{key_prefix}Endpoint"
        )
    if "cluster_create_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["cluster_create_time"], pairs, f"{key_prefix}ClusterCreateTime"
        )
    if "automated_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}AutomatedSnapshotRetentionPeriod",
                str(value["automated_snapshot_retention_period"]),
            )
        )
    if "manual_snapshot_retention_period" in value:
        pairs.append(
            (
                f"{key_prefix}ManualSnapshotRetentionPeriod",
                str(value["manual_snapshot_retention_period"]),
            )
        )
    if "cluster_security_groups" in value:
        import capo_redshift.types.cluster_security_group_membership_list

        capo_redshift.types.cluster_security_group_membership_list.serialize_query(
            value["cluster_security_groups"],
            pairs,
            f"{key_prefix}ClusterSecurityGroups",
        )
    if "vpc_security_groups" in value:
        import capo_redshift.types.vpc_security_group_membership_list

        capo_redshift.types.vpc_security_group_membership_list.serialize_query(
            value["vpc_security_groups"], pairs, f"{key_prefix}VpcSecurityGroups"
        )
    if "cluster_parameter_groups" in value:
        import capo_redshift.types.cluster_parameter_group_status_list

        capo_redshift.types.cluster_parameter_group_status_list.serialize_query(
            value["cluster_parameter_groups"],
            pairs,
            f"{key_prefix}ClusterParameterGroups",
        )
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )
    if "vpc_id" in value:
        pairs.append((f"{key_prefix}VpcId", str(value["vpc_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
        )
    if "pending_modified_values" in value:
        import capo_redshift.types.pending_modified_values

        capo_redshift.types.pending_modified_values.serialize_query(
            value["pending_modified_values"],
            pairs,
            f"{key_prefix}PendingModifiedValues",
        )
    if "cluster_version" in value:
        pairs.append((f"{key_prefix}ClusterVersion", str(value["cluster_version"])))
    if "allow_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AllowVersionUpgrade",
                "true" if value["allow_version_upgrade"] else "false",
            )
        )
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "restore_status" in value:
        import capo_redshift.types.restore_status

        capo_redshift.types.restore_status.serialize_query(
            value["restore_status"], pairs, f"{key_prefix}RestoreStatus"
        )
    if "data_transfer_progress" in value:
        import capo_redshift.types.data_transfer_progress

        capo_redshift.types.data_transfer_progress.serialize_query(
            value["data_transfer_progress"], pairs, f"{key_prefix}DataTransferProgress"
        )
    if "hsm_status" in value:
        import capo_redshift.types.hsm_status

        capo_redshift.types.hsm_status.serialize_query(
            value["hsm_status"], pairs, f"{key_prefix}HsmStatus"
        )
    if "cluster_snapshot_copy_status" in value:
        import capo_redshift.types.cluster_snapshot_copy_status

        capo_redshift.types.cluster_snapshot_copy_status.serialize_query(
            value["cluster_snapshot_copy_status"],
            pairs,
            f"{key_prefix}ClusterSnapshotCopyStatus",
        )
    if "cluster_public_key" in value:
        pairs.append(
            (f"{key_prefix}ClusterPublicKey", str(value["cluster_public_key"]))
        )
    if "cluster_nodes" in value:
        import capo_redshift.types.cluster_nodes_list

        capo_redshift.types.cluster_nodes_list.serialize_query(
            value["cluster_nodes"], pairs, f"{key_prefix}ClusterNodes"
        )
    if "elastic_ip_status" in value:
        import capo_redshift.types.elastic_ip_status

        capo_redshift.types.elastic_ip_status.serialize_query(
            value["elastic_ip_status"], pairs, f"{key_prefix}ElasticIpStatus"
        )
    if "cluster_revision_number" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterRevisionNumber",
                str(value["cluster_revision_number"]),
            )
        )
    if "tags" in value:
        import capo_redshift.types.tag_list

        capo_redshift.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "enhanced_vpc_routing" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedVpcRouting",
                "true" if value["enhanced_vpc_routing"] else "false",
            )
        )
    if "iam_roles" in value:
        import capo_redshift.types.cluster_iam_role_list

        capo_redshift.types.cluster_iam_role_list.serialize_query(
            value["iam_roles"], pairs, f"{key_prefix}IamRoles"
        )
    if "pending_actions" in value:
        import capo_redshift.types.pending_actions_list

        capo_redshift.types.pending_actions_list.serialize_query(
            value["pending_actions"], pairs, f"{key_prefix}PendingActions"
        )
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{key_prefix}MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "elastic_resize_number_of_node_options" in value:
        pairs.append(
            (
                f"{key_prefix}ElasticResizeNumberOfNodeOptions",
                str(value["elastic_resize_number_of_node_options"]),
            )
        )
    if "deferred_maintenance_windows" in value:
        import capo_redshift.types.deferred_maintenance_windows_list

        capo_redshift.types.deferred_maintenance_windows_list.serialize_query(
            value["deferred_maintenance_windows"],
            pairs,
            f"{key_prefix}DeferredMaintenanceWindows",
        )
    if "snapshot_schedule_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotScheduleIdentifier",
                str(value["snapshot_schedule_identifier"]),
            )
        )
    if "snapshot_schedule_state" in value:
        import capo_redshift.types.schedule_state

        capo_redshift.types.schedule_state.serialize_query(
            value["snapshot_schedule_state"],
            pairs,
            f"{key_prefix}SnapshotScheduleState",
        )
    if "expected_next_snapshot_schedule_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["expected_next_snapshot_schedule_time"],
            pairs,
            f"{key_prefix}ExpectedNextSnapshotScheduleTime",
        )
    if "expected_next_snapshot_schedule_time_status" in value:
        pairs.append(
            (
                f"{key_prefix}ExpectedNextSnapshotScheduleTimeStatus",
                str(value["expected_next_snapshot_schedule_time_status"]),
            )
        )
    if "next_maintenance_window_start_time" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["next_maintenance_window_start_time"],
            pairs,
            f"{key_prefix}NextMaintenanceWindowStartTime",
        )
    if "resize_info" in value:
        import capo_redshift.types.resize_info

        capo_redshift.types.resize_info.serialize_query(
            value["resize_info"], pairs, f"{key_prefix}ResizeInfo"
        )
    if "availability_zone_relocation_status" in value:
        pairs.append(
            (
                f"{key_prefix}AvailabilityZoneRelocationStatus",
                str(value["availability_zone_relocation_status"]),
            )
        )
    if "cluster_namespace_arn" in value:
        pairs.append(
            (f"{key_prefix}ClusterNamespaceArn", str(value["cluster_namespace_arn"]))
        )
    if "total_storage_capacity_in_mega_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}TotalStorageCapacityInMegaBytes",
                str(value["total_storage_capacity_in_mega_bytes"]),
            )
        )
    if "aqua_configuration" in value:
        import capo_redshift.types.aqua_configuration

        capo_redshift.types.aqua_configuration.serialize_query(
            value["aqua_configuration"], pairs, f"{key_prefix}AquaConfiguration"
        )
    if "default_iam_role_arn" in value:
        pairs.append(
            (f"{key_prefix}DefaultIamRoleArn", str(value["default_iam_role_arn"]))
        )
    if "reserved_node_exchange_status" in value:
        import capo_redshift.types.reserved_node_exchange_status

        capo_redshift.types.reserved_node_exchange_status.serialize_query(
            value["reserved_node_exchange_status"],
            pairs,
            f"{key_prefix}ReservedNodeExchangeStatus",
        )
    if "custom_domain_name" in value:
        pairs.append(
            (f"{key_prefix}CustomDomainName", str(value["custom_domain_name"]))
        )
    if "custom_domain_certificate_arn" in value:
        pairs.append(
            (
                f"{key_prefix}CustomDomainCertificateArn",
                str(value["custom_domain_certificate_arn"]),
            )
        )
    if "custom_domain_certificate_expiry_date" in value:
        import capo_redshift.types.t_stamp

        capo_redshift.types.t_stamp.serialize_query(
            value["custom_domain_certificate_expiry_date"],
            pairs,
            f"{key_prefix}CustomDomainCertificateExpiryDate",
        )
    if "master_password_secret_arn" in value:
        pairs.append(
            (
                f"{key_prefix}MasterPasswordSecretArn",
                str(value["master_password_secret_arn"]),
            )
        )
    if "master_password_secret_kms_key_id" in value:
        pairs.append(
            (
                f"{key_prefix}MasterPasswordSecretKmsKeyId",
                str(value["master_password_secret_kms_key_id"]),
            )
        )
    if "ip_address_type" in value:
        pairs.append((f"{key_prefix}IpAddressType", str(value["ip_address_type"])))
    if "multi_az" in value:
        pairs.append((f"{key_prefix}MultiAZ", str(value["multi_az"])))
    if "multi_az_secondary" in value:
        import capo_redshift.types.secondary_cluster_info

        capo_redshift.types.secondary_cluster_info.serialize_query(
            value["multi_az_secondary"], pairs, f"{key_prefix}MultiAZSecondary"
        )
    if "lakehouse_registration_status" in value:
        pairs.append(
            (
                f"{key_prefix}LakehouseRegistrationStatus",
                str(value["lakehouse_registration_status"]),
            )
        )
    if "catalog_arn" in value:
        pairs.append((f"{key_prefix}CatalogArn", str(value["catalog_arn"])))
    if "extra_compute_for_automatic_optimization" in value:
        pairs.append(
            (
                f"{key_prefix}ExtraComputeForAutomaticOptimization",
                str(value["extra_compute_for_automatic_optimization"]),
            )
        )
    if "logging_publish_status" in value:
        import capo_redshift.types.logging_publish_status

        capo_redshift.types.logging_publish_status.serialize_query(
            value["logging_publish_status"], pairs, f"{key_prefix}LoggingPublishStatus"
        )


def deserialize_query(el: Element) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_cluster_status = el.find("ClusterStatus")
    if child_cluster_status is not None:
        out["cluster_status"] = str(child_cluster_status.text or "")
    child_cluster_availability_status = el.find("ClusterAvailabilityStatus")
    if child_cluster_availability_status is not None:
        out["cluster_availability_status"] = str(
            child_cluster_availability_status.text or ""
        )
    child_modify_status = el.find("ModifyStatus")
    if child_modify_status is not None:
        out["modify_status"] = str(child_modify_status.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_endpoint = el.find("Endpoint")
    if child_endpoint is not None:
        import capo_redshift.types.endpoint

        out["endpoint"] = capo_redshift.types.endpoint.deserialize_query(child_endpoint)
    child_cluster_create_time = el.find("ClusterCreateTime")
    if child_cluster_create_time is not None:
        import capo_redshift.types.t_stamp

        out["cluster_create_time"] = capo_redshift.types.t_stamp.deserialize_query(
            child_cluster_create_time
        )
    child_automated_snapshot_retention_period = el.find(
        "AutomatedSnapshotRetentionPeriod"
    )
    if child_automated_snapshot_retention_period is not None:
        out["automated_snapshot_retention_period"] = int(
            child_automated_snapshot_retention_period.text or ""
        )
    child_manual_snapshot_retention_period = el.find("ManualSnapshotRetentionPeriod")
    if child_manual_snapshot_retention_period is not None:
        out["manual_snapshot_retention_period"] = int(
            child_manual_snapshot_retention_period.text or ""
        )
    child_cluster_security_groups = el.find("ClusterSecurityGroups")
    if child_cluster_security_groups is not None:
        import capo_redshift.types.cluster_security_group_membership_list

        out["cluster_security_groups"] = (
            capo_redshift.types.cluster_security_group_membership_list.deserialize_query(
                child_cluster_security_groups
            )
        )
    child_vpc_security_groups = el.find("VpcSecurityGroups")
    if child_vpc_security_groups is not None:
        import capo_redshift.types.vpc_security_group_membership_list

        out["vpc_security_groups"] = (
            capo_redshift.types.vpc_security_group_membership_list.deserialize_query(
                child_vpc_security_groups
            )
        )
    child_cluster_parameter_groups = el.find("ClusterParameterGroups")
    if child_cluster_parameter_groups is not None:
        import capo_redshift.types.cluster_parameter_group_status_list

        out["cluster_parameter_groups"] = (
            capo_redshift.types.cluster_parameter_group_status_list.deserialize_query(
                child_cluster_parameter_groups
            )
        )
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    child_vpc_id = el.find("VpcId")
    if child_vpc_id is not None:
        out["vpc_id"] = str(child_vpc_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_pending_modified_values = el.find("PendingModifiedValues")
    if child_pending_modified_values is not None:
        import capo_redshift.types.pending_modified_values

        out["pending_modified_values"] = (
            capo_redshift.types.pending_modified_values.deserialize_query(
                child_pending_modified_values
            )
        )
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_allow_version_upgrade = el.find("AllowVersionUpgrade")
    if child_allow_version_upgrade is not None:
        out["allow_version_upgrade"] = (
            child_allow_version_upgrade.text or ""
        ).lower() == "true"
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_restore_status = el.find("RestoreStatus")
    if child_restore_status is not None:
        import capo_redshift.types.restore_status

        out["restore_status"] = capo_redshift.types.restore_status.deserialize_query(
            child_restore_status
        )
    child_data_transfer_progress = el.find("DataTransferProgress")
    if child_data_transfer_progress is not None:
        import capo_redshift.types.data_transfer_progress

        out["data_transfer_progress"] = (
            capo_redshift.types.data_transfer_progress.deserialize_query(
                child_data_transfer_progress
            )
        )
    child_hsm_status = el.find("HsmStatus")
    if child_hsm_status is not None:
        import capo_redshift.types.hsm_status

        out["hsm_status"] = capo_redshift.types.hsm_status.deserialize_query(
            child_hsm_status
        )
    child_cluster_snapshot_copy_status = el.find("ClusterSnapshotCopyStatus")
    if child_cluster_snapshot_copy_status is not None:
        import capo_redshift.types.cluster_snapshot_copy_status

        out["cluster_snapshot_copy_status"] = (
            capo_redshift.types.cluster_snapshot_copy_status.deserialize_query(
                child_cluster_snapshot_copy_status
            )
        )
    child_cluster_public_key = el.find("ClusterPublicKey")
    if child_cluster_public_key is not None:
        out["cluster_public_key"] = str(child_cluster_public_key.text or "")
    child_cluster_nodes = el.find("ClusterNodes")
    if child_cluster_nodes is not None:
        import capo_redshift.types.cluster_nodes_list

        out["cluster_nodes"] = capo_redshift.types.cluster_nodes_list.deserialize_query(
            child_cluster_nodes
        )
    child_elastic_ip_status = el.find("ElasticIpStatus")
    if child_elastic_ip_status is not None:
        import capo_redshift.types.elastic_ip_status

        out["elastic_ip_status"] = (
            capo_redshift.types.elastic_ip_status.deserialize_query(
                child_elastic_ip_status
            )
        )
    child_cluster_revision_number = el.find("ClusterRevisionNumber")
    if child_cluster_revision_number is not None:
        out["cluster_revision_number"] = str(child_cluster_revision_number.text or "")
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_redshift.types.tag_list

        out["tags"] = capo_redshift.types.tag_list.deserialize_query(child_tags)
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_enhanced_vpc_routing = el.find("EnhancedVpcRouting")
    if child_enhanced_vpc_routing is not None:
        out["enhanced_vpc_routing"] = (
            child_enhanced_vpc_routing.text or ""
        ).lower() == "true"
    child_iam_roles = el.find("IamRoles")
    if child_iam_roles is not None:
        import capo_redshift.types.cluster_iam_role_list

        out["iam_roles"] = capo_redshift.types.cluster_iam_role_list.deserialize_query(
            child_iam_roles
        )
    child_pending_actions = el.find("PendingActions")
    if child_pending_actions is not None:
        import capo_redshift.types.pending_actions_list

        out["pending_actions"] = (
            capo_redshift.types.pending_actions_list.deserialize_query(
                child_pending_actions
            )
        )
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_elastic_resize_number_of_node_options = el.find(
        "ElasticResizeNumberOfNodeOptions"
    )
    if child_elastic_resize_number_of_node_options is not None:
        out["elastic_resize_number_of_node_options"] = str(
            child_elastic_resize_number_of_node_options.text or ""
        )
    child_deferred_maintenance_windows = el.find("DeferredMaintenanceWindows")
    if child_deferred_maintenance_windows is not None:
        import capo_redshift.types.deferred_maintenance_windows_list

        out["deferred_maintenance_windows"] = (
            capo_redshift.types.deferred_maintenance_windows_list.deserialize_query(
                child_deferred_maintenance_windows
            )
        )
    child_snapshot_schedule_identifier = el.find("SnapshotScheduleIdentifier")
    if child_snapshot_schedule_identifier is not None:
        out["snapshot_schedule_identifier"] = str(
            child_snapshot_schedule_identifier.text or ""
        )
    child_snapshot_schedule_state = el.find("SnapshotScheduleState")
    if child_snapshot_schedule_state is not None:
        import capo_redshift.types.schedule_state

        out["snapshot_schedule_state"] = (
            capo_redshift.types.schedule_state.deserialize_query(
                child_snapshot_schedule_state
            )
        )
    child_expected_next_snapshot_schedule_time = el.find(
        "ExpectedNextSnapshotScheduleTime"
    )
    if child_expected_next_snapshot_schedule_time is not None:
        import capo_redshift.types.t_stamp

        out["expected_next_snapshot_schedule_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_expected_next_snapshot_schedule_time
            )
        )
    child_expected_next_snapshot_schedule_time_status = el.find(
        "ExpectedNextSnapshotScheduleTimeStatus"
    )
    if child_expected_next_snapshot_schedule_time_status is not None:
        out["expected_next_snapshot_schedule_time_status"] = str(
            child_expected_next_snapshot_schedule_time_status.text or ""
        )
    child_next_maintenance_window_start_time = el.find("NextMaintenanceWindowStartTime")
    if child_next_maintenance_window_start_time is not None:
        import capo_redshift.types.t_stamp

        out["next_maintenance_window_start_time"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_next_maintenance_window_start_time
            )
        )
    child_resize_info = el.find("ResizeInfo")
    if child_resize_info is not None:
        import capo_redshift.types.resize_info

        out["resize_info"] = capo_redshift.types.resize_info.deserialize_query(
            child_resize_info
        )
    child_availability_zone_relocation_status = el.find(
        "AvailabilityZoneRelocationStatus"
    )
    if child_availability_zone_relocation_status is not None:
        out["availability_zone_relocation_status"] = str(
            child_availability_zone_relocation_status.text or ""
        )
    child_cluster_namespace_arn = el.find("ClusterNamespaceArn")
    if child_cluster_namespace_arn is not None:
        out["cluster_namespace_arn"] = str(child_cluster_namespace_arn.text or "")
    child_total_storage_capacity_in_mega_bytes = el.find(
        "TotalStorageCapacityInMegaBytes"
    )
    if child_total_storage_capacity_in_mega_bytes is not None:
        out["total_storage_capacity_in_mega_bytes"] = int(
            child_total_storage_capacity_in_mega_bytes.text or ""
        )
    child_aqua_configuration = el.find("AquaConfiguration")
    if child_aqua_configuration is not None:
        import capo_redshift.types.aqua_configuration

        out["aqua_configuration"] = (
            capo_redshift.types.aqua_configuration.deserialize_query(
                child_aqua_configuration
            )
        )
    child_default_iam_role_arn = el.find("DefaultIamRoleArn")
    if child_default_iam_role_arn is not None:
        out["default_iam_role_arn"] = str(child_default_iam_role_arn.text or "")
    child_reserved_node_exchange_status = el.find("ReservedNodeExchangeStatus")
    if child_reserved_node_exchange_status is not None:
        import capo_redshift.types.reserved_node_exchange_status

        out["reserved_node_exchange_status"] = (
            capo_redshift.types.reserved_node_exchange_status.deserialize_query(
                child_reserved_node_exchange_status
            )
        )
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    child_custom_domain_certificate_arn = el.find("CustomDomainCertificateArn")
    if child_custom_domain_certificate_arn is not None:
        out["custom_domain_certificate_arn"] = str(
            child_custom_domain_certificate_arn.text or ""
        )
    child_custom_domain_certificate_expiry_date = el.find(
        "CustomDomainCertificateExpiryDate"
    )
    if child_custom_domain_certificate_expiry_date is not None:
        import capo_redshift.types.t_stamp

        out["custom_domain_certificate_expiry_date"] = (
            capo_redshift.types.t_stamp.deserialize_query(
                child_custom_domain_certificate_expiry_date
            )
        )
    child_master_password_secret_arn = el.find("MasterPasswordSecretArn")
    if child_master_password_secret_arn is not None:
        out["master_password_secret_arn"] = str(
            child_master_password_secret_arn.text or ""
        )
    child_master_password_secret_kms_key_id = el.find("MasterPasswordSecretKmsKeyId")
    if child_master_password_secret_kms_key_id is not None:
        out["master_password_secret_kms_key_id"] = str(
            child_master_password_secret_kms_key_id.text or ""
        )
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        out["ip_address_type"] = str(child_ip_address_type.text or "")
    child_multi_az = el.find("MultiAZ")
    if child_multi_az is not None:
        out["multi_az"] = str(child_multi_az.text or "")
    child_multi_az_secondary = el.find("MultiAZSecondary")
    if child_multi_az_secondary is not None:
        import capo_redshift.types.secondary_cluster_info

        out["multi_az_secondary"] = (
            capo_redshift.types.secondary_cluster_info.deserialize_query(
                child_multi_az_secondary
            )
        )
    child_lakehouse_registration_status = el.find("LakehouseRegistrationStatus")
    if child_lakehouse_registration_status is not None:
        out["lakehouse_registration_status"] = str(
            child_lakehouse_registration_status.text or ""
        )
    child_catalog_arn = el.find("CatalogArn")
    if child_catalog_arn is not None:
        out["catalog_arn"] = str(child_catalog_arn.text or "")
    child_extra_compute_for_automatic_optimization = el.find(
        "ExtraComputeForAutomaticOptimization"
    )
    if child_extra_compute_for_automatic_optimization is not None:
        out["extra_compute_for_automatic_optimization"] = str(
            child_extra_compute_for_automatic_optimization.text or ""
        )
    child_logging_publish_status = el.find("LoggingPublishStatus")
    if child_logging_publish_status is not None:
        import capo_redshift.types.logging_publish_status

        out["logging_publish_status"] = (
            capo_redshift.types.logging_publish_status.deserialize_query(
                child_logging_publish_status
            )
        )
    return out
