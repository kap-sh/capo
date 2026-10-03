"""Generated from Smithy shape ``com.amazonaws.redshift#CreateClusterMessage``."""

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
    import capo_redshift.types.sensitive_string
    import capo_redshift.types.string
    import capo_redshift.types.tag_list
    import capo_redshift.types.vpc_security_group_id_list


class CreateClusterMessage(TypedDict, closed=True):
    db_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the first database to be created when the cluster is created.</p> <p>To create additional databases after the cluster is created, connect to the cluster with a SQL client and use SQL commands to create a database. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/dg/t_creating_database.html">Create a Database</a> in the Amazon Redshift Database Developer Guide. </p> <p>Default: <code>dev</code> </p> <p>Constraints:</p> <ul> <li> <p>Must contain 1 to 64 alphanumeric characters.</p> </li> <li> <p>Must contain only lowercase letters.</p> </li> <li> <p>Cannot be a word that is reserved by the service. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide. </p> </li> </ul>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. The identifier also appears in the Amazon Redshift console.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 1 to 63 alphanumeric characters or hyphens.</p> </li> <li> <p>Alphabetic characters must be lowercase.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Must be unique for all clusters within an Amazon Web Services account.</p> </li> </ul> <p>Example: <code>myexamplecluster</code> </p>"""
    cluster_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The type of the cluster. When cluster type is specified as</p> <ul> <li> <p> <code>single-node</code>, the <b>NumberOfNodes</b> parameter is not required.</p> </li> <li> <p> <code>multi-node</code>, the <b>NumberOfNodes</b> parameter is required.</p> </li> </ul> <p>Valid Values: <code>multi-node</code> | <code>single-node</code> </p> <p>Default: <code>multi-node</code> </p>"""
    node_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The node type to be provisioned for the cluster. For information about node types, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes"> Working with Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p> <p>Valid Values: <code>dc2.large</code> | <code>dc2.8xlarge</code> | <code>rg.large</code> | <code>rg.xlarge</code> | <code>rg.4xlarge</code> | <code>rg.12xlarge</code> | <code>ra3.large</code> | <code>ra3.xlplus</code> | <code>ra3.4xlarge</code> | <code>ra3.16xlarge</code> </p>"""
    master_username: NotRequired["capo_redshift.types.string.String"]
    """<p>The user name associated with the admin user account for the cluster that is being created.</p> <p>Constraints:</p> <ul> <li> <p>Must be 1 - 128 alphanumeric characters or hyphens. The user name can't be <code>PUBLIC</code>.</p> </li> <li> <p>Must contain only lowercase letters, numbers, underscore, plus sign, period (dot), at symbol (@), or hyphen.</p> </li> <li> <p>The first character must be a letter.</p> </li> <li> <p>Must not contain a colon (:) or a slash (/).</p> </li> <li> <p>Cannot be a reserved word. A list of reserved words can be found in <a href="https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html">Reserved Words</a> in the Amazon Redshift Database Developer Guide. </p> </li> </ul>"""
    master_user_password: NotRequired[
        "capo_redshift.types.sensitive_string.SensitiveString"
    ]
    r"""<p>The password associated with the admin user account for the cluster that is being created.</p> <p>You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is <code>true</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must be between 8 and 64 characters in length.</p> </li> <li> <p>Must contain at least one uppercase letter.</p> </li> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Must contain one number.</p> </li> <li> <p>Can be any printable ASCII character (ASCII code 33-126) except <code>'</code> (single quote), <code>"</code> (double quote), <code>\</code>, <code>/</code>, or <code>@</code>.</p> </li> </ul>"""
    cluster_security_groups: NotRequired[
        "capo_redshift.types.cluster_security_group_name_list.ClusterSecurityGroupNameList"
    ]
    """<p>A list of security groups to be associated with this cluster.</p> <p>Default: The default cluster security group for Amazon Redshift.</p>"""
    vpc_security_group_ids: NotRequired[
        "capo_redshift.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
    ]
    """<p>A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.</p> <p>Default: The default VPC security group is associated with the cluster.</p>"""
    cluster_subnet_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of a cluster subnet group to be associated with this cluster.</p> <p>If this parameter is not provided the resulting cluster will be deployed outside virtual private cloud (VPC).</p>"""
    availability_zone: NotRequired["capo_redshift.types.string.String"]
    """<p>The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. For example, if you have several EC2 instances running in a specific Availability Zone, then you might want the cluster to be provisioned in the same zone in order to decrease network latency.</p> <p>Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint.</p> <p>Example: <code>us-east-2d</code> </p> <p>Constraint: The specified Availability Zone must be in the same region as the current endpoint.</p>"""
    preferred_maintenance_window: NotRequired["capo_redshift.types.string.String"]
    """<p>The weekly time range (in UTC) during which automated cluster maintenance can occur.</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p> Default: A 30-minute window selected at random from an 8-hour block of time per region, occurring on a random day of the week. For more information about the time blocks for each region, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-maintenance-windows">Maintenance Windows</a> in Amazon Redshift Cluster Management Guide.</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Minimum 30-minute window.</p>"""
    cluster_parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the parameter group to be associated with this cluster.</p> <p>Default: The default Amazon Redshift cluster parameter group. For information about the default parameter group, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-parameter-groups.html">Working with Amazon Redshift Parameter Groups</a> </p> <p>Constraints:</p> <ul> <li> <p>Must be 1 to 255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    automated_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Even if automated snapshots are disabled, you can still create manual snapshots when you want with <a>CreateClusterSnapshot</a>. </p> <p>You can't disable automated snapshots for RG or RA3 node types. Set the automated retention period from 1-35 days.</p> <p>Default: <code>1</code> </p> <p>Constraints: Must be a value from 0 to 35.</p>"""
    manual_snapshot_retention_period: NotRequired[
        "capo_redshift.types.integer_optional.IntegerOptional"
    ]
    """<p>The default number of days to retain a manual snapshot. If the value is -1, the snapshot is retained indefinitely. This setting doesn't change the retention period of existing snapshots.</p> <p>The value must be either -1 or an integer between 1 and 3,653.</p>"""
    port: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The port number on which the cluster accepts incoming connections.</p> <p>The cluster is accessible only via the JDBC and ODBC connection strings. Part of the connection string requires the port on which the cluster will listen for incoming connections.</p> <p>Default: <code>5439</code> </p> <p>Valid Values: </p> <ul> <li> <p>For clusters with RG or RA3 nodes - Select a port within the ranges <code>5431-5455</code> or <code>8191-8215</code>. (If you have an existing cluster with RG or RA3 nodes, it isn't required that you change the port to these ranges.)</p> </li> <li> <p>For clusters with dc2 nodes - Select a port within the range <code>1150-65535</code>.</p> </li> </ul>"""
    cluster_version: NotRequired["capo_redshift.types.string.String"]
    """<p>The version of the Amazon Redshift engine software that you want to deploy on the cluster.</p> <p>The version selected runs on all the nodes in the cluster.</p> <p>Constraints: Only version 1.0 is currently available.</p> <p>Example: <code>1.0</code> </p>"""
    allow_version_upgrade: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster.</p> <p>When a new major version of the Amazon Redshift engine is released, you can request that the service automatically apply upgrades during the maintenance window to the Amazon Redshift engine that is running on your cluster.</p> <p>Default: <code>true</code> </p>"""
    number_of_nodes: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The number of compute nodes in the cluster. This parameter is required when the <b>ClusterType</b> parameter is specified as <code>multi-node</code>. </p> <p>For information about determining how many nodes you need, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#how-many-nodes"> Working with Clusters</a> in the <i>Amazon Redshift Cluster Management Guide</i>. </p> <p>If you don't specify this parameter, you get a single-node cluster. When requesting a multi-node cluster, you must specify the number of nodes that you want in the cluster.</p> <p>Default: <code>1</code> </p> <p>Constraints: Value must be at least 1 and no more than 100.</p>"""
    publicly_accessible: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, the cluster can be accessed from a public network. </p> <p>Default: false</p>"""
    encrypted: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If <code>true</code>, the data in the cluster is encrypted at rest. If you set the value on this parameter to <code>false</code>, the request will fail.</p> <p>Default: true</p>"""
    hsm_client_certificate_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM.</p>"""
    hsm_configuration_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.</p>"""
    elastic_ip: NotRequired["capo_redshift.types.string.String"]
    """<p>The Elastic IP (EIP) address for the cluster.</p> <p>Constraints: The cluster must be provisioned in EC2-VPC and publicly-accessible through an Internet gateway. Don't specify the Elastic IP address for a publicly accessible cluster with availability zone relocation turned on. For more information about provisioning clusters in EC2-VPC, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-platforms">Supported Platforms to Launch Your Cluster</a> in the Amazon Redshift Cluster Management Guide.</p>"""
    tags: NotRequired["capo_redshift.types.tag_list.TagList"]
    """<p>A list of tag instances.</p>"""
    kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.</p>"""
    enhanced_vpc_routing: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/enhanced-vpc-routing.html">Enhanced VPC Routing</a> in the Amazon Redshift Cluster Management Guide.</p> <p>If this option is <code>true</code>, enhanced VPC routing is enabled. </p> <p>Default: false</p>"""
    additional_info: NotRequired["capo_redshift.types.string.String"]
    """<p>Reserved.</p>"""
    iam_roles: NotRequired["capo_redshift.types.iam_role_arn_list.IamRoleArnList"]
    """<p>A list of Identity and Access Management (IAM) roles that can be used by the cluster to access other Amazon Web Services services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. </p> <p>The maximum number of IAM roles that you can associate is subject to a quota. For more information, go to <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html">Quotas and limits</a> in the <i>Amazon Redshift Cluster Management Guide</i>.</p>"""
    maintenance_track_name: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter for the name of the maintenance track for the cluster. If you don't provide a maintenance track name, the cluster is assigned to the <code>current</code> track.</p>"""
    snapshot_schedule_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>A unique identifier for the snapshot schedule.</p>"""
    availability_zone_relocation: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster is created.</p>"""
    aqua_configuration_status: NotRequired[
        "capo_redshift.types.aqua_configuration_status.AquaConfigurationStatus"
    ]
    """<p>This parameter is retired. It does not set the AQUA configuration status. Amazon Redshift automatically determines whether to use AQUA (Advanced Query Accelerator).</p>"""
    default_iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was created. </p>"""
    load_sample_data: NotRequired["capo_redshift.types.string.String"]
    """<p>A flag that specifies whether to load sample data once the cluster is created.</p>"""
    manage_master_password: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, Amazon Redshift uses Secrets Manager to manage this cluster's admin credentials. You can't use <code>MasterUserPassword</code> if <code>ManageMasterPassword</code> is true. If <code>ManageMasterPassword</code> is false or not set, Amazon Redshift uses <code>MasterUserPassword</code> for the admin user account's password. </p>"""
    master_password_secret_kms_key_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the cluster's admin credentials secret. You can only use this parameter if <code>ManageMasterPassword</code> is true.</p>"""
    ip_address_type: NotRequired["capo_redshift.types.string.String"]
    """<p>The IP address types that the cluster supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    multi_az: NotRequired["capo_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If true, Amazon Redshift will deploy the cluster in two Availability Zones (AZ).</p>"""
    redshift_idc_application_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon resource name (ARN) of the Amazon Redshift IAM Identity Center application.</p>"""
    catalog_name: NotRequired[
        "capo_redshift.types.catalog_name_string.CatalogNameString"
    ]
    """<p>The name of the Glue data catalog that will be associated with the cluster enabled with Amazon Redshift federated permissions.</p> <p>Constraints:</p> <ul> <li> <p>Must contain at least one lowercase letter.</p> </li> <li> <p>Can only contain lowercase letters (a-z), numbers (0-9), underscores (_), and hyphens (-).</p> </li> </ul> <p>Pattern: <code>^[a-z0-9_-]*[a-z]+[a-z0-9_-]*$</code> </p> <p>Example: <code>my-catalog_01</code> </p>"""
    extra_compute_for_automatic_optimization: NotRequired[
        "capo_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_name" in value:
        pairs.append((f"{key_prefix}DBName", str(value["db_name"])))
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "cluster_type" in value:
        pairs.append((f"{key_prefix}ClusterType", str(value["cluster_type"])))
    if "node_type" in value:
        pairs.append((f"{key_prefix}NodeType", str(value["node_type"])))
    if "master_username" in value:
        pairs.append((f"{key_prefix}MasterUsername", str(value["master_username"])))
    if "master_user_password" in value:
        pairs.append(
            (f"{key_prefix}MasterUserPassword", str(value["master_user_password"]))
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
    if "cluster_subnet_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}ClusterSubnetGroupName",
                str(value["cluster_subnet_group_name"]),
            )
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "preferred_maintenance_window" in value:
        pairs.append(
            (
                f"{key_prefix}PreferredMaintenanceWindow",
                str(value["preferred_maintenance_window"]),
            )
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
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
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
    if "load_sample_data" in value:
        pairs.append((f"{key_prefix}LoadSampleData", str(value["load_sample_data"])))
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
    if "redshift_idc_application_arn" in value:
        pairs.append(
            (
                f"{key_prefix}RedshiftIdcApplicationArn",
                str(value["redshift_idc_application_arn"]),
            )
        )
    if "catalog_name" in value:
        pairs.append((f"{key_prefix}CatalogName", str(value["catalog_name"])))
    if "extra_compute_for_automatic_optimization" in value:
        pairs.append(
            (
                f"{key_prefix}ExtraComputeForAutomaticOptimization",
                "true"
                if value["extra_compute_for_automatic_optimization"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> CreateClusterMessage:
    out: CreateClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_name = el.find("DBName")
    if child_db_name is not None:
        out["db_name"] = str(child_db_name.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_cluster_type = el.find("ClusterType")
    if child_cluster_type is not None:
        out["cluster_type"] = str(child_cluster_type.text or "")
    child_node_type = el.find("NodeType")
    if child_node_type is not None:
        out["node_type"] = str(child_node_type.text or "")
    child_master_username = el.find("MasterUsername")
    if child_master_username is not None:
        out["master_username"] = str(child_master_username.text or "")
    child_master_user_password = el.find("MasterUserPassword")
    if child_master_user_password is not None:
        out["master_user_password"] = str(child_master_user_password.text or "")
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
    child_cluster_subnet_group_name = el.find("ClusterSubnetGroupName")
    if child_cluster_subnet_group_name is not None:
        out["cluster_subnet_group_name"] = str(
            child_cluster_subnet_group_name.text or ""
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_preferred_maintenance_window = el.find("PreferredMaintenanceWindow")
    if child_preferred_maintenance_window is not None:
        out["preferred_maintenance_window"] = str(
            child_preferred_maintenance_window.text or ""
        )
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
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
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
    child_load_sample_data = el.find("LoadSampleData")
    if child_load_sample_data is not None:
        out["load_sample_data"] = str(child_load_sample_data.text or "")
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
    child_redshift_idc_application_arn = el.find("RedshiftIdcApplicationArn")
    if child_redshift_idc_application_arn is not None:
        out["redshift_idc_application_arn"] = str(
            child_redshift_idc_application_arn.text or ""
        )
    child_catalog_name = el.find("CatalogName")
    if child_catalog_name is not None:
        out["catalog_name"] = str(child_catalog_name.text or "")
    child_extra_compute_for_automatic_optimization = el.find(
        "ExtraComputeForAutomaticOptimization"
    )
    if child_extra_compute_for_automatic_optimization is not None:
        out["extra_compute_for_automatic_optimization"] = (
            child_extra_compute_for_automatic_optimization.text or ""
        ).lower() == "true"
    return out
