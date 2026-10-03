"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.boolean_optional
    import capo_redshift.types.cluster_security_group_name_list
    import capo_redshift.types.integer_optional
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.string
    import capo_redshift.types.vpc_security_group_id_list


class ModifyClusterMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster to be modified.</p> <p>Example: <code>examplecluster</code> </p>"""
    cluster_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The new cluster type.</p> <p>When you submit your cluster resize request, your existing cluster goes into a read-only mode. After Amazon Redshift provisions a new cluster based on your resize requirements, there will be outage for a period while the old cluster is deleted and your connection is switched to the new cluster. You can use <a>DescribeResize</a> to track the progress of the resize request. </p> <p>Valid Values: <code> multi-node | single-node </code> </p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The new node type of the cluster. If you specify a new node type, you must also specify the number of nodes parameter.</p> <p> For more information about resizing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html">Resizing Clusters in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Valid Values: <code>dc2.large</code> | <code>dc2.8xlarge</code> | <code>rg.large</code> | <code>rg.xlarge</code> | <code>rg.4xlarge</code> | <code>rg.12xlarge</code> | <code>ra3.large</code> | <code>ra3.xlplus</code> | <code>ra3.4xlarge</code> | <code>ra3.16xlarge</code> </p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The new number of nodes of the cluster. If you specify a new number of nodes, you must also specify the node type parameter.</p> <p> For more information about resizing clusters, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/rs-resize-tutorial.html">Resizing Clusters in Amazon Redshift</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Valid Values: Integer greater than <code>0</code>.</p>"""
    cluster_security_groups: NotRequired[
        "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
    ]
    """<p>A list of cluster security groups to be authorized on this cluster. This change is asynchronously applied as soon as possible.</p> <p>Security groups currently associated with the cluster, and not in the list of groups to apply, will be revoked from the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens</p> </li> <li> <p>First character must be a letter</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens</p> </li> </ul>"""
    vpc_security_group_ids: NotRequired[
        "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of virtual private cloud (VPC) security groups to be associated with the cluster. This change is asynchronously applied as soon as possible.</p>"""
    master_user_password: NotRequired[
        "capo_redshift.types.sensitive_string.SensitiveString"
    ]
    r"""<p>The new password for the cluster admin user. This change is asynchronously applied as soon as possible. Between the time of the request and the completion of the request, the <code>MasterUserPassword</code> element exists in the <code>PendingModifiedValues</code> element of the operation response. </p> <p>You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is <code>true</code>.</p> <note> <p>Operations never return the password, so this operation provides a way to regain access to the admin user account for a cluster if the password is lost.</p> </note> <p>Default: Uses existing setting.</p> <p>Constraints:</p> <ul> <li> <p>Must be between 8 and 64 characters in length.</p> </li> <li> <p>Must contain at least one uppercase letter.</p> </li> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Must contain one number.</p> </li> <li> <p>Can be any printable ASCII character (ASCII code 33-126) except <code>'</code> (single quote), <code>"</code> (double quote), <code>\</code>, <code>/</code>, or <code>@</code>.</p> </li> </ul>"""
    cluster_parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the cluster parameter group to apply to this cluster. This change is applied only after the cluster is rebooted. To reboot a cluster use <a>RebootCluster</a>. </p> <p>Default: Uses existing setting.</p> <p>Constraints: The cluster parameter group must be in the same parameter group family that matches the cluster version.</p>"""
    automated_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>If you decrease the automated snapshot retention period from its current value, existing automated snapshots that fall outside of the new retention period will be immediately deleted.</p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: Uses existing setting.</p> <p>Constraints: Must be a value from 0 to 35.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The default for number of days that a newly created manual snapshot is retained. If the value is -1, the manual snapshot is retained indefinitely. This value doesn't retroactively change the retention periods of existing manual snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p> <p>The default value is -1.</p>"""
    preferred_maintenance_window: NotRequired["capo_redshift.types.string.String"]
    """<p>The weekly time range (in UTC) during which system maintenance can occur, if necessary. If system maintenance is necessary during the window, it may result in an outage.</p> <p>This maintenance window change is made immediately. If the new maintenance window indicates the current time, there must be at least 120 minutes between the current time and end of the window in order to ensure that pending changes are applied.</p> <p>Default: Uses existing setting.</p> <p>Format: ddd:hh24:mi-ddd:hh24:mi, for example <code>wed:07:30-wed:08:00</code>.</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Must be at least 30 minutes.</p>"""
    cluster_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The new version number of the Amazon Redshift engine to upgrade to.</p> <p>For major version upgrades, if a non-default cluster parameter group is currently in use, a new cluster parameter group in the cluster parameter group family for the new version must be specified. The new cluster parameter group can be the default for that cluster parameter group family. For more information about parameters and parameter groups, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Amazon Redshift Parameter Groups</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p> <p>Example: <code>1.0</code> </p>"""
    allow_version_upgrade: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, major version upgrades will be applied automatically to the cluster during the maintenance window. </p> <p>Default: <code>false</code> </p>"""
    hsm_client_certificate_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>"""
    hsm_configuration_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>"""
    new_cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The new identifier for the cluster.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul> <p>Example: <code>examplecluster</code> </p>"""
    publicly_accessible: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, the cluster can be accessed from a public network. Only clusters in VPCs can be set to be publicly available.</p> <p>Default: false</p>"""
    elastic_ip: NotRequired["capo_redshift.types.string.String"]
    """<p>The Elastic IP (EIP) address for the cluster.</p> <p>Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. For more information about provisioning clusters in EC2-VPC, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms">Supported Platforms to Launch Your Cluster</a> in the Amazon Redshift Cluster Management Guide.</p>"""
    enhanced_vpc_routing: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the <code>PendingModifiedValues</code> for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.</p>"""
    encrypted: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>Indicates whether the cluster is encrypted. If the value is encrypted (true) and you provide a value for the <code>KmsKeyId</code> parameter, we encrypt the cluster with the provided <code>KmsKeyId</code>. If you don't provide a <code>KmsKeyId</code>, we encrypt with the default key. </p> <p>If the value is not encrypted (false), then the cluster is decrypted. </p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</p>"""
    availability_zone_relocation: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.</p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The option to initiate relocation for an Amazon Redshift cluster to the target Availability Zone.</p>"""
    port: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The option to change the port of an Amazon Redshift cluster.</p> <p>Valid Values: </p> <ul> <li> <p>For clusters with RG or RA3 nodes - Select a port within the ranges <code>5431-5455</code> or <code>8191-8215</code>. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)</p> </li> <li> <p>For clusters with dc2 nodes - Select a port within the range <code>1150-65535</code>.</p> </li> </ul>"""
    manage_master_password: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage this cluster's admin credentials. You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is true. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses <code>MasterUserPassword</code> for the admin user account's password. </p>"""
    master_password_secret_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>"""
    ip_address_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP address types that the cluster supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    multi_az: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If true and the cluster is currently only deployed in a single Availability Zone, the cluster will be modified to be deployed in two Availability Zones.</p>"""
    extra_compute_for_automatic_optimization: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "cluster_type" in value:
        pairs.append((f"{key_prefix}ClusterType", str(value["cluster_type"])))
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "number_of_nodes" in value:
        pairs.append((f"{key_prefix}NumberOfNodes", str(value["number_of_nodes"])))
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
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
        )
    if "cluster_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterParameterGroupName",
                str(value["cluster_parameter_group_name"]),
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
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
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
    if "new_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}NewClusterIdentifier", str(value["new_cluster_identifier"]))
        )
    if "publicly_accessible" in value:
        pairs.append(
            (
                f"{key_prefix}PubliclyAccessible",
                "true" if value["publicly_accessible"] else "false",
            )
        )
    if "elastic_ip" in value:
        pairs.append((f"{key_prefix}ElasticIp", str(value["elastic_ip"])))
    if "enhanced_vpc_routing" in value:
        pairs.append(
            (
                f"{key_prefix}EnhancedVpcRouting",
                "true" if value["enhanced_vpc_routing"] else "false",
            )
        )
    if "maintenance_track_name" in value:
        pairs.append(
            (f"{key_prefix}MaintenanceTrackName", str(value["maintenance_track_name"]))
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "availability_zone_relocation" in value:
        pairs.append(
            (
                f"{key_prefix}AvailabilityZoneRelocation",
                "true" if value["availability_zone_relocation"] else "false",
            )
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
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
    if "extra_compute_for_automatic_optimization" in value:
        pairs.append(
            (
                f"{key_prefix}ExtraComputeForAutomaticOptimization",
                "true"
                if value["extra_compute_for_automatic_optimization"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> ModifyClusterMessage:
    out: ModifyClusterMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_cluster_type = el.find("ClusterType")
    if child_cluster_type is not None:
        out["cluster_type"] = str(child_cluster_type.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_number_of_nodes = el.find("NumberOfNodes")
    if child_number_of_nodes is not None:
        out["number_of_nodes"] = int(child_number_of_nodes.text or "")
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
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
    child_cluster_parameter_group_name = el.find("ClusterParameterGroupName")
    if child_cluster_parameter_group_name is not None:
        out["cluster_parameter_group_name"] = str(
            child_cluster_parameter_group_name.text or ""
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
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
    child_cluster_version = el.find("ClusterVersion")
    if child_cluster_version is not None:
        out["cluster_version"] = str(child_cluster_version.text or "")
    child_allow_version_upgrade = el.find("AllowVersionUpgrade")
    if child_allow_version_upgrade is not None:
        out["allow_version_upgrade"] = (
            child_allow_version_upgrade.text or ""
        ).lower() == "true"
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
    child_new_cluster_identifier = el.find("NewClusterIdentifier")
    if child_new_cluster_identifier is not None:
        out["new_cluster_identifier"] = str(child_new_cluster_identifier.text or "")
    child_publicly_accessible = el.find("PubliclyAccessible")
    if child_publicly_accessible is not None:
        out["publicly_accessible"] = (
            child_publicly_accessible.text or ""
        ).lower() == "true"
    child_elastic_ip = el.find("ElasticIp")
    if child_elastic_ip is not None:
        out["elastic_ip"] = str(child_elastic_ip.text or "")
    child_enhanced_vpc_routing = el.find("EnhancedVpcRouting")
    if child_enhanced_vpc_routing is not None:
        out["enhanced_vpc_routing"] = (
            child_enhanced_vpc_routing.text or ""
        ).lower() == "true"
    child_maintenance_track_name = el.find("MaintenanceTrackName")
    if child_maintenance_track_name is not None:
        out["maintenance_track_name"] = str(child_maintenance_track_name.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_availability_zone_relocation = el.find("AvailabilityZoneRelocation")
    if child_availability_zone_relocation is not None:
        out["availability_zone_relocation"] = (
            child_availability_zone_relocation.text or ""
        ).lower() == "true"
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
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
    child_extra_compute_for_automatic_optimization = el.find(
        "ExtraComputeForAutomaticOptimization"
    )
    if child_extra_compute_for_automatic_optimization is not None:
        out["extra_compute_for_automatic_optimization"] = (
            child_extra_compute_for_automatic_optimization.text or ""
        ).lower() == "true"
    return out
