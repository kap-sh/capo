"""Generated from Smithy shape ``com.amazonaws.emr#Cluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.application_list
    import capo_emr.types.arn_type
    import capo_emr.types.boolean
    import capo_emr.types.boolean_object
    import capo_emr.types.cluster_id
    import capo_emr.types.cluster_status
    import capo_emr.types.configuration_list
    import capo_emr.types.ec2_instance_attributes
    import capo_emr.types.instance_collection_type
    import capo_emr.types.integer
    import capo_emr.types.kerberos_attributes
    import capo_emr.types.monitoring_configuration
    import capo_emr.types.optional_arn_type
    import capo_emr.types.placement_group_config_list
    import capo_emr.types.repo_upgrade_on_boot
    import capo_emr.types.scale_down_behavior
    import capo_emr.types.string
    import capo_emr.types.tag_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class Cluster(TypedDict, closed=True):
    id: NotRequired["capo_emr.types.cluster_id.ClusterId"]
    """<p>The unique identifier for the cluster.</p>"""
    name: NotRequired["capo_emr.types.string.String"]
    """<p>The name of the cluster. This parameter can't contain the characters <, >, $, |, or ` (backtick).</p>"""
    status: NotRequired["capo_emr.types.cluster_status.ClusterStatus"]
    """<p>The current status details about the cluster.</p>"""
    ec2_instance_attributes: NotRequired[
        "capo_emr.types.ec2_instance_attributes.Ec2InstanceAttributes"
    ]
    """<p>Provides information about the Amazon EC2 instances in a cluster grouped by category. For example, key name, subnet ID, IAM instance profile, and so on.</p>"""
    instance_collection_type: NotRequired[
        "capo_emr.types.instance_collection_type.InstanceCollectionType"
    ]
    """<note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note> <p>The instance group configuration of the cluster. A value of <code>INSTANCE_GROUP</code> indicates a uniform instance group configuration. A value of <code>INSTANCE_FLEET</code> indicates an instance fleets configuration.</p>"""
    log_uri: NotRequired["capo_emr.types.string.String"]
    """<p>The path to the Amazon S3 location where logs for this cluster are stored.</p>"""
    log_encryption_kms_key_id: NotRequired["capo_emr.types.string.String"]
    """<p> The KMS key used for encrypting log files. This attribute is only available with Amazon EMR 5.30.0 and later, excluding Amazon EMR 6.0.0. </p>"""
    requested_ami_version: NotRequired["capo_emr.types.string.String"]
    """<p>The AMI version requested for this cluster.</p>"""
    running_ami_version: NotRequired["capo_emr.types.string.String"]
    """<p>The AMI version running on this cluster.</p>"""
    release_label: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release version such as <code>emr-5.14.0</code>. For more information about Amazon EMR release versions and included application versions and features, see <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/">https://docs.aws.amazon.com/emr/latest/ReleaseGuide/</a>. The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use <code>AmiVersion</code>.</p>"""
    auto_terminate: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Specifies whether the cluster should terminate after completing all steps.</p>"""
    termination_protected: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether Amazon EMR will lock the cluster to prevent the Amazon EC2 instances from being terminated by an API call or user intervention, or in the event of a cluster error.</p>"""
    unhealthy_node_replacement: NotRequired[
        "capo_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether Amazon EMR should gracefully replace Amazon EC2 core instances that have degraded within the cluster.</p>"""
    visible_to_all_users: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Indicates whether the cluster is visible to IAM principals in the Amazon Web Services account associated with the cluster. When <code>true</code>, IAM principals in the Amazon Web Services account can perform Amazon EMR cluster actions on the cluster that their IAM policies allow. When <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions, regardless of IAM permissions policies attached to other IAM principals.</p> <p>The default value is <code>true</code> if a value is not provided when creating a cluster using the Amazon EMR API <a>RunJobFlow</a> command, the CLI <a href="https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html">create-cluster</a> command, or the Amazon Web Services Management Console.</p>"""
    applications: NotRequired["capo_emr.types.application_list.ApplicationList"]
    """<p>The applications installed on this cluster.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>A list of tags associated with a cluster.</p>"""
    service_role: NotRequired["capo_emr.types.string.String"]
    """<p>The IAM role that Amazon EMR assumes in order to access Amazon Web Services resources on your behalf.</p>"""
    normalized_instance_hours: NotRequired["capo_emr.types.integer.Integer"]
    """<p>An approximation of the cost of the cluster, represented in m1.small/hours. This value is incremented one time for every hour an m1.small instance runs. Larger instances are weighted more, so an Amazon EC2 instance that is roughly four times more expensive would result in the normalized instance hours being incremented by four. This result is only an approximation and does not reflect the actual billing rate.</p>"""
    master_public_dns_name: NotRequired["capo_emr.types.string.String"]
    """<p>The DNS name of the master node. If the cluster is on a private subnet, this is the private DNS name. On a public subnet, this is the public DNS name.</p>"""
    configurations: NotRequired["capo_emr.types.configuration_list.ConfigurationList"]
    """<p>Applies only to Amazon EMR releases 4.x and later. The list of configurations that are supplied to the Amazon EMR cluster.</p>"""
    security_configuration: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of the security configuration applied to the cluster.</p>"""
    auto_scaling_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>An IAM role for automatic scaling policies. The default role is <code>EMR_AutoScaling_DefaultRole</code>. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.</p>"""
    scale_down_behavior: NotRequired[
        "capo_emr.types.scale_down_behavior.ScaleDownBehavior"
    ]
    """<p>The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. <code>TERMINATE_AT_INSTANCE_HOUR</code> indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. <code>TERMINATE_AT_TASK_COMPLETION</code> indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. <code>TERMINATE_AT_TASK_COMPLETION</code> is available only in Amazon EMR releases 4.1.0 and later, and is the default for versions of Amazon EMR earlier than 5.1.0.</p>"""
    custom_ami_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI if the cluster uses a custom AMI.</p>"""
    ebs_root_volume_size: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.</p>"""
    repo_upgrade_on_boot: NotRequired[
        "capo_emr.types.repo_upgrade_on_boot.RepoUpgradeOnBoot"
    ]
    """<p>Applies only when <code>CustomAmiID</code> is used. Specifies the type of updates that the Amazon Linux AMI package repositories apply when an instance boots using the AMI.</p>"""
    kerberos_attributes: NotRequired[
        "capo_emr.types.kerberos_attributes.KerberosAttributes"
    ]
    """<p>Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html">Use Kerberos Authentication</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    cluster_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name of the cluster.</p>"""
    outpost_arn: NotRequired["capo_emr.types.optional_arn_type.OptionalArnType"]
    """<p> The Amazon Resource Name (ARN) of the Outpost where the cluster is launched. </p>"""
    step_concurrency_level: NotRequired["capo_emr.types.integer.Integer"]
    """<p>Specifies the number of steps that can be executed concurrently.</p>"""
    placement_groups: NotRequired[
        "capo_emr.types.placement_group_config_list.PlacementGroupConfigList"
    ]
    """<p>Placement group configured for an Amazon EMR cluster.</p>"""
    os_release_label: NotRequired["capo_emr.types.string.String"]
    """<p>The Amazon Linux release specified in a cluster launch RunJobFlow request. If no Amazon Linux release was specified, the default Amazon Linux release is shown in the response.</p>"""
    ebs_root_volume_iops: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    ebs_root_volume_throughput: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    extended_support: NotRequired["capo_emr.types.boolean_object.BooleanObject"]
    """<p>Reserved.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains Cloudwatch log configuration metadata and settings.</p>"""
    session_enabled: NotRequired["capo_emr.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Spark Connect sessions are enabled on the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Cluster) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_emr.types.cluster_status

        out["Status"] = capo_emr.types.cluster_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "ec2_instance_attributes" in value:
        import capo_emr.types.ec2_instance_attributes

        out["Ec2InstanceAttributes"] = (
            capo_emr.types.ec2_instance_attributes.serialize_aws_json_1_1(
                value["ec2_instance_attributes"]
            )
        )
    if "instance_collection_type" in value:
        import capo_emr.types.instance_collection_type

        out["InstanceCollectionType"] = (
            capo_emr.types.instance_collection_type.serialize_aws_json_1_1(
                value["instance_collection_type"]
            )
        )
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "log_encryption_kms_key_id" in value:
        out["LogEncryptionKmsKeyId"] = value["log_encryption_kms_key_id"]
    if "requested_ami_version" in value:
        out["RequestedAmiVersion"] = value["requested_ami_version"]
    if "running_ami_version" in value:
        out["RunningAmiVersion"] = value["running_ami_version"]
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "auto_terminate" in value:
        out["AutoTerminate"] = value["auto_terminate"]
    if "termination_protected" in value:
        out["TerminationProtected"] = value["termination_protected"]
    if "unhealthy_node_replacement" in value:
        out["UnhealthyNodeReplacement"] = value["unhealthy_node_replacement"]
    if "visible_to_all_users" in value:
        out["VisibleToAllUsers"] = value["visible_to_all_users"]
    if "applications" in value:
        import capo_emr.types.application_list

        out["Applications"] = capo_emr.types.application_list.serialize_aws_json_1_1(
            value["applications"]
        )
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "normalized_instance_hours" in value:
        out["NormalizedInstanceHours"] = value["normalized_instance_hours"]
    if "master_public_dns_name" in value:
        out["MasterPublicDnsName"] = value["master_public_dns_name"]
    if "configurations" in value:
        import capo_emr.types.configuration_list

        out["Configurations"] = (
            capo_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "security_configuration" in value:
        out["SecurityConfiguration"] = value["security_configuration"]
    if "auto_scaling_role" in value:
        out["AutoScalingRole"] = value["auto_scaling_role"]
    if "scale_down_behavior" in value:
        import capo_emr.types.scale_down_behavior

        out["ScaleDownBehavior"] = (
            capo_emr.types.scale_down_behavior.serialize_aws_json_1_1(
                value["scale_down_behavior"]
            )
        )
    if "custom_ami_id" in value:
        out["CustomAmiId"] = value["custom_ami_id"]
    if "ebs_root_volume_size" in value:
        out["EbsRootVolumeSize"] = value["ebs_root_volume_size"]
    if "repo_upgrade_on_boot" in value:
        import capo_emr.types.repo_upgrade_on_boot

        out["RepoUpgradeOnBoot"] = (
            capo_emr.types.repo_upgrade_on_boot.serialize_aws_json_1_1(
                value["repo_upgrade_on_boot"]
            )
        )
    if "kerberos_attributes" in value:
        import capo_emr.types.kerberos_attributes

        out["KerberosAttributes"] = (
            capo_emr.types.kerberos_attributes.serialize_aws_json_1_1(
                value["kerberos_attributes"]
            )
        )
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "outpost_arn" in value:
        out["OutpostArn"] = value["outpost_arn"]
    if "step_concurrency_level" in value:
        out["StepConcurrencyLevel"] = value["step_concurrency_level"]
    if "placement_groups" in value:
        import capo_emr.types.placement_group_config_list

        out["PlacementGroups"] = (
            capo_emr.types.placement_group_config_list.serialize_aws_json_1_1(
                value["placement_groups"]
            )
        )
    if "os_release_label" in value:
        out["OSReleaseLabel"] = value["os_release_label"]
    if "ebs_root_volume_iops" in value:
        out["EbsRootVolumeIops"] = value["ebs_root_volume_iops"]
    if "ebs_root_volume_throughput" in value:
        out["EbsRootVolumeThroughput"] = value["ebs_root_volume_throughput"]
    if "extended_support" in value:
        out["ExtendedSupport"] = value["extended_support"]
    if "monitoring_configuration" in value:
        import capo_emr.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            capo_emr.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "session_enabled" in value:
        out["SessionEnabled"] = value["session_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Cluster:
    out: Cluster = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_emr.types.cluster_status

        out["status"] = capo_emr.types.cluster_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("Ec2InstanceAttributes") is not None:
        import capo_emr.types.ec2_instance_attributes

        out["ec2_instance_attributes"] = (
            capo_emr.types.ec2_instance_attributes.deserialize_aws_json_1_1(
                data["Ec2InstanceAttributes"]
            )
        )
    if data.get("InstanceCollectionType") is not None:
        import capo_emr.types.instance_collection_type

        out["instance_collection_type"] = (
            capo_emr.types.instance_collection_type.deserialize_aws_json_1_1(
                data["InstanceCollectionType"]
            )
        )
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("LogEncryptionKmsKeyId") is not None:
        out["log_encryption_kms_key_id"] = data["LogEncryptionKmsKeyId"]
    if data.get("RequestedAmiVersion") is not None:
        out["requested_ami_version"] = data["RequestedAmiVersion"]
    if data.get("RunningAmiVersion") is not None:
        out["running_ami_version"] = data["RunningAmiVersion"]
    if data.get("ReleaseLabel") is not None:
        out["release_label"] = data["ReleaseLabel"]
    if data.get("AutoTerminate") is not None:
        out["auto_terminate"] = data["AutoTerminate"]
    if data.get("TerminationProtected") is not None:
        out["termination_protected"] = data["TerminationProtected"]
    if data.get("UnhealthyNodeReplacement") is not None:
        out["unhealthy_node_replacement"] = data["UnhealthyNodeReplacement"]
    if data.get("VisibleToAllUsers") is not None:
        out["visible_to_all_users"] = data["VisibleToAllUsers"]
    if data.get("Applications") is not None:
        import capo_emr.types.application_list

        out["applications"] = capo_emr.types.application_list.deserialize_aws_json_1_1(
            data["Applications"]
        )
    if data.get("Tags") is not None:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("NormalizedInstanceHours") is not None:
        out["normalized_instance_hours"] = data["NormalizedInstanceHours"]
    if data.get("MasterPublicDnsName") is not None:
        out["master_public_dns_name"] = data["MasterPublicDnsName"]
    if data.get("Configurations") is not None:
        import capo_emr.types.configuration_list

        out["configurations"] = (
            capo_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if data.get("SecurityConfiguration") is not None:
        out["security_configuration"] = data["SecurityConfiguration"]
    if data.get("AutoScalingRole") is not None:
        out["auto_scaling_role"] = data["AutoScalingRole"]
    if data.get("ScaleDownBehavior") is not None:
        import capo_emr.types.scale_down_behavior

        out["scale_down_behavior"] = (
            capo_emr.types.scale_down_behavior.deserialize_aws_json_1_1(
                data["ScaleDownBehavior"]
            )
        )
    if data.get("CustomAmiId") is not None:
        out["custom_ami_id"] = data["CustomAmiId"]
    if data.get("EbsRootVolumeSize") is not None:
        out["ebs_root_volume_size"] = data["EbsRootVolumeSize"]
    if data.get("RepoUpgradeOnBoot") is not None:
        import capo_emr.types.repo_upgrade_on_boot

        out["repo_upgrade_on_boot"] = (
            capo_emr.types.repo_upgrade_on_boot.deserialize_aws_json_1_1(
                data["RepoUpgradeOnBoot"]
            )
        )
    if data.get("KerberosAttributes") is not None:
        import capo_emr.types.kerberos_attributes

        out["kerberos_attributes"] = (
            capo_emr.types.kerberos_attributes.deserialize_aws_json_1_1(
                data["KerberosAttributes"]
            )
        )
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("OutpostArn") is not None:
        out["outpost_arn"] = data["OutpostArn"]
    if data.get("StepConcurrencyLevel") is not None:
        out["step_concurrency_level"] = data["StepConcurrencyLevel"]
    if data.get("PlacementGroups") is not None:
        import capo_emr.types.placement_group_config_list

        out["placement_groups"] = (
            capo_emr.types.placement_group_config_list.deserialize_aws_json_1_1(
                data["PlacementGroups"]
            )
        )
    if data.get("OSReleaseLabel") is not None:
        out["os_release_label"] = data["OSReleaseLabel"]
    if data.get("EbsRootVolumeIops") is not None:
        out["ebs_root_volume_iops"] = data["EbsRootVolumeIops"]
    if data.get("EbsRootVolumeThroughput") is not None:
        out["ebs_root_volume_throughput"] = data["EbsRootVolumeThroughput"]
    if data.get("ExtendedSupport") is not None:
        out["extended_support"] = data["ExtendedSupport"]
    if data.get("MonitoringConfiguration") is not None:
        import capo_emr.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_emr.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if data.get("SessionEnabled") is not None:
        out["session_enabled"] = data["SessionEnabled"]
    return out
