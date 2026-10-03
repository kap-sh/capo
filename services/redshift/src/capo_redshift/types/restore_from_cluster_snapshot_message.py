"""Generated from Smithy shape ``com.amazonaws.redshift#RestoreFromClusterSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.aqua_configuration_status
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.catalog_name_string
    import capo_redshift.types.cluster_security_group_name_list
    import capo_redshift.types.iam_role_arn_list
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string
    import capo_redshift.types.vpc_security_group_id_list


class RestoreFromClusterSnapshotMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster that will be created from restoring the snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul>"""
    snapshot_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot from which to create the new cluster. This parameter isn't case sensitive. You must specify this parameter or <code>snapshotArn</code>, but not both.</p> <p>Example: <code>my-snapshot-id</code> </p>"""
    snapshot_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot associated with the message to restore from a cluster. You must specify this parameter or <code>snapshotIdentifier</code>, but not both.</p>"""
    snapshot_cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster the source snapshot was created from. This parameter is required if your IAM user has a policy containing a snapshot resource element that specifies anything other than * for the cluster name.</p>"""
    port: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the cluster accepts connections.</p> <p>Default: The same port as the original cluster.</p> <p>Valid values: For clusters with DC2 nodes, must be within the range <code>1150</code>-<code>65535</code>. For clusters with RG or RA3 nodes, must be within the ranges <code>5431</code>-<code>5455</code> or <code>8191</code>-<code>8215</code>.</p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon EC2 Availability Zone in which to restore the cluster.</p> <p>Default: A random, system-chosen Availability Zone.</p> <p>Example: <code>us-east-2a</code> </p>"""
    allow_version_upgrade: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. </p> <p>Default: <code>true</code> </p>"""
    cluster_subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the subnet group where you want to cluster restored.</p> <p>A snapshot of cluster in VPC can be restored only in VPC. Therefore, you must provide subnet group name where you want the cluster restored.</p>"""
    publicly_accessible: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, the cluster can be accessed from a public network. </p> <p>Default: false</p>"""
    owner_account: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account used to create or copy the snapshot. Required if you are restoring a snapshot you do not own, optional if you own the snapshot.</p>"""
    hsm_client_certificate_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>"""
    hsm_configuration_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>"""
    elastic_ip: NotRequired["capo_redshift.types.string.String"]
    """<p>The Elastic IP (EIP) address for the cluster. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on.</p>"""
    cluster_parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the parameter group to be associated with this cluster.</p> <p>Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Working with Amazon Redshift Parameter Groups</a>.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    cluster_security_groups: NotRequired[
        "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
    ]
    """<p>A list of security groups to be associated with this cluster.</p> <p>Default: The default cluster security group for Amazon Redshift.</p> <p>Cluster security groups only apply to clusters outside of VPCs.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</p> <p>Default: The default VPC security group is associated with the cluster.</p> <p>VPC security groups only apply to clusters in VPCs.</p>"""
    preferred_maintenance_window: NotRequired["capo_redshift.types.string.String"]
    """<p>The weekly time range (in UTC) during which automated cluster maintenance can occur.</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> Default: The value selected for the cluster from which the snapshot was taken. For more information about the time blocks for each region, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows">Maintenance Windows</a> in Amazon Redshift Cluster Management Guide. </p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Minimum 30-minute window.</p>"""
    automated_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: The value selected for the cluster from which the snapshot was taken.</p> <p>Constraints: Must be a value from 0 to 35.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key ID of the encryption key that encrypts data in the cluster restored from a shared snapshot. You can also provide the key ID when you restore from an unencrypted snapshot to an encrypted cluster in the same account. Additionally, you can specify a new KMS key ID when you restore from an encrypted snapshot in the same account in order to change it. In that case, the restored cluster is encrypted with the new KMS key ID.</p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type that the restored cluster will be provisioned with.</p> <p>If you have a DC instance type, you must restore into that same instance type and size. In other words, you can only restore a dc2.large node type into another dc2 type. For more information about node types, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-about-clusters-and-nodes"> About Clusters and Nodes</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p>"""
    enhanced_vpc_routing: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    additional_info: NotRequired["capo_redshift.types.string.String"]
    """<p>Reserved.</p>"""
    iam_roles: NotRequired["capo_redshift.types.iam_role_arn_list.IamRoleArnList"]
    """<p>A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. </p> <p>The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Quotas and limits</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the maintenance track for the restored cluster. When you take a snapshot, the snapshot inherits the <code>MaintenanceTrack</code> value from the cluster. The snapshot might be on a different track than the cluster that was the source for the snapshot. For example, suppose that you take a snapshot of a cluster that is on the current track and then change the cluster to be on the trailing track. In this case, the snapshot and the source cluster are on different tracks.</p>"""
    snapshot_schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the snapshot schedule.</p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The number of nodes specified when provisioning the restored cluster.</p>"""
    availability_zone_relocation: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is restored.</p>"""
    aqua_configuration_status: NotRequired[
        "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
    ]
    """<p>This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""
    default_iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified while it was restored from a snapshot.</p>"""
    reserved_node_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the target reserved node offering.</p>"""
    target_reserved_node_offering_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the target reserved node offering.</p>"""
    encrypted: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>Enables support for restoring an unencrypted snapshot to a cluster encrypted with Key Management Service (KMS) and a customer managed key.</p>"""
    manage_master_password: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage the restored cluster's admin credentials. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses the admin credentials the cluster had at the time the snapshot was taken.</p>"""
    master_password_secret_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>"""
    ip_address_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP address type for the cluster. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    multi_az: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If true, the snapshot will be restored to a cluster deployed in two Availability Zones.</p>"""
    catalog_name: NotRequired[
        "capo_redshift.types.catalog_name_string.CatalogNameString"
    ]
    """<p>The name of the Glue Data Catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>"""
    redshift_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application used for enabling Amazon Web Services IAM Identity Center trusted identity propagation on a cluster enabled with Amazon Redshift federated permissions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RestoreFromClusterSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "snapshot_identifier" in value:
        pairs.append(
            (f"{key_prefix}SnapshotIdentifier", str(value["snapshot_identifier"]))
        )
    if "snapshot_arn" in value:
        pairs.append((f"{key_prefix}SnapshotArn", str(value["snapshot_arn"])))
    if "snapshot_cluster_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotClusterIdentifier",
                str(value["snapshot_cluster_identifier"]),
            )
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "allow_version_upgrade" in value:
        pairs.append(
            (
                f"{key_prefix}AllowVersionUpgrade",
                "true" if value["allow_version_upgrade"] else "false",
            )
        )
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "owner_account" in value:
        pairs.append((f"{key_prefix}OwnerAccount", str(value["owner_account"])))
    if "hsm_client_certificate_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}HsmClientCertificateIdentifier",
                str(value["hsm_client_certificate_identifier"]),
            )
        )
    if "hsm_configuration_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}HsmConfigurationIdentifier",
                str(value["hsm_configuration_identifier"]),
            )
        )
    if "elastic_ip" in value:
        pairs.append((f"{key_prefix}ElasticIp", str(value["elastic_ip"])))
    if "cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterParameterGroupName",
                str(value["cluster_parameter_group_name"]),
            )
        )
    if "cluster_security_groups" in value:
        import capo_redshift.types.cluster_security_group_name_list

        capo_redshift.types.cluster_security_group_name_list.serialize_query(
            value["cluster_security_groups"],
            pairs,
            f"{key_prefix}ClusterSecurityGroups",
        )
    if "vpc_security_group_ids" in value:
        import capo_redshift.types.vpc_security_group_id_list

        capo_redshift.types.vpc_security_group_id_list.serialize_query(
            value["vpc_security_group_ids"], pairs, f"{key_prefix}VpcSecurityGroupIds"
        )
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
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
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "enhanced_vpc_routing" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedVpcRouting",
                "true" if value["enhanced_vpc_routing"] else "false",
            )
        )
    if "additional_info" in value:
        pairs.append((f"{key_prefix}AdditionalInfo", str(value["additional_info"])))
    if "iam_roles" in value:
        import capo_redshift.types.iam_role_arn_list

        capo_redshift.types.iam_role_arn_list.serialize_query(
            value["iam_roles"], pairs, f"{key_prefix}IamRoles"
        )
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{key_prefix}MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "snapshot_schedule_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotScheduleIdentifier",
                str(value["snapshot_schedule_identifier"]),
            )
        )
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
    if "availability_zone_relocation" in value:
        pairs.append(
            (
                f"{key_prefix}AvailabilityZoneRelocation",
                "true" if value["availability_zone_relocation"] else "false",
            )
        )
    if "aqua_configuration_status" in value:
        import capo_redshift.types.aqua_configuration_status

        capo_redshift.types.aqua_configuration_status.serialize_query(
            value["aqua_configuration_status"],
            pairs,
            f"{key_prefix}AquaConfigurationStatus",
        )
    if "default_iam_role_arn" in value:
        pairs.append(
            (f"{key_prefix}DefaultIamRoleArn", str(value["default_iam_role_arn"]))
        )
    if "reserved_node_id" in value:
        pairs.append((f"{key_prefix}ReservedNodeId", str(value["reserved_node_id"])))
    if "target_reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{key_prefix}TargetReservedNodeOfferingId",
                str(value["target_reserved_node_offering_id"]),
            )
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "manage_master_password" in value:
        pairs.append(
            (
                f"{key_prefix}ManageMasterPassword",
                "true" if value["manage_master_password"] else "false",
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
        pairs.append((f"{key_prefix}MultiAZ", "true" if value["multi_az"] else "false"))
    if "catalog_name" in value:
        pairs.append((f"{key_prefix}CatalogName", str(value["catalog_name"])))
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{key_prefix}RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )


def deserialize_query(el: Element) -> RestoreFromClusterSnapshotMessage:
    out: RestoreFromClusterSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_snapshot_identifier = el.find("SnapshotIdentifier")
    if child_snapshot_identifier is not None:
        out["snapshot_identifier"] = str(child_snapshot_identifier.text or "")
    child_snapshot_arn = el.find("SnapshotArn")
    if child_snapshot_arn is not None:
        out["snapshot_arn"] = str(child_snapshot_arn.text or "")
    child_snapshot_cluster_identifier = el.find("SnapshotClusterIdentifier")
    if child_snapshot_cluster_identifier is not None:
        out["snapshot_cluster_identifier"] = str(
            child_snapshot_cluster_identifier.text or ""
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_allow_version_upgrade = el.find("AllowVersionUpgrade")
    if child_allow_version_upgrade is not None:
        out["allow_version_upgrade"] = (
            child_allow_version_upgrade.text or ""
        ).lower() == "true"
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_owner_account = el.find("OwnerAccount")
    if child_owner_account is not None:
        out["owner_account"] = str(child_owner_account.text or "")
    child_hsm_client_certificate_identifier = el.find("HsmClientCertificateIdentifier")
    if child_hsm_client_certificate_identifier is not None:
        out["hsm_client_certificate_identifier"] = str(
            child_hsm_client_certificate_identifier.text or ""
        )
    child_hsm_configuration_identifier = el.find("HsmConfigurationIdentifier")
    if child_hsm_configuration_identifier is not None:
        out["hsm_configuration_identifier"] = str(
            child_hsm_configuration_identifier.text or ""
        )
    child_elastic_ip = el.find("ElasticIp")
    if child_elastic_ip is not None:
        out["elastic_ip"] = str(child_elastic_ip.text or "")
    child_cluster_parameter_group_name = el.find("ClusterParameterGroupName")
    if child_cluster_parameter_group_name is not None:
        out["cluster_parameter_group_name"] = str(
            child_cluster_parameter_group_name.text or ""
        )
    child_cluster_security_groups = el.find("ClusterSecurityGroups")
    if child_cluster_security_groups is not None:
        import capo_redshift.types.cluster_security_group_name_list

        out["cluster_security_groups"] = (
            capo_redshift.types.cluster_security_group_name_list.deserialize_query(
                child_cluster_security_groups
            )
        )
    child_vpc_security_group_ids = el.find("VpcSecurityGroupIds")
    if child_vpc_security_group_ids is not None:
        import capo_redshift.types.vpc_security_group_id_list

        out["vpc_security_group_ids"] = (
            capo_redshift.types.vpc_security_group_id_list.deserialize_query(
                child_vpc_security_group_ids
            )
        )
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
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
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_enhanced_vpc_routing = el.find("EnhancedVpcRouting")
    if child_enhanced_vpc_routing is not None:
        out["enhanced_vpc_routing"] = (
            child_enhanced_vpc_routing.text or ""
        ).lower() == "true"
    child_additional_info = el.find("AdditionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_iam_roles = el.find("IamRoles")
    if child_iam_roles is not None:
        import capo_redshift.types.iam_role_arn_list

        out["iam_roles"] = capo_redshift.types.iam_role_arn_list.deserialize_query(
            child_iam_roles
        )
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_snapshot_schedule_identifier = el.find("SnapshotScheduleIdentifier")
    if child_snapshot_schedule_identifier is not None:
        out["snapshot_schedule_identifier"] = str(
            child_snapshot_schedule_identifier.text or ""
        )
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
    child_availability_zone_relocation = el.find("AvailabilityZoneRelocation")
    if child_availability_zone_relocation is not None:
        out["availability_zone_relocation"] = (
            child_availability_zone_relocation.text or ""
        ).lower() == "true"
    child_aqua_configuration_status = el.find("AquaConfigurationStatus")
    if child_aqua_configuration_status is not None:
        import capo_redshift.types.aqua_configuration_status

        out["aqua_configuration_status"] = (
            capo_redshift.types.aqua_configuration_status.deserialize_query(
                child_aqua_configuration_status
            )
        )
    child_default_iam_role_arn = el.find("DefaultIamRoleArn")
    if child_default_iam_role_arn is not None:
        out["default_iam_role_arn"] = str(child_default_iam_role_arn.text or "")
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_target_reserved_node_offering_id = el.find("TargetReservedNodeOfferingId")
    if child_target_reserved_node_offering_id is not None:
        out["target_reserved_node_offering_id"] = str(
            child_target_reserved_node_offering_id.text or ""
        )
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_manage_master_password = el.find("ManageMasterPassword")
    if child_manage_master_password is not None:
        out["manage_master_password"] = (
            child_manage_master_password.text or ""
        ).lower() == "true"
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
        out["multi_az"] = (child_multi_az.text or "").lower() == "true"
    child_catalog_name = el.find("CatalogName")
    if child_catalog_name is not None:
        out["catalog_name"] = str(child_catalog_name.text or "")
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    return out
