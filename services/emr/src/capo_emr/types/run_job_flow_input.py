"""Generated from Smithy shape ``com.amazonaws.emr#RunJobFlowInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.application_list
    import capo_emr.types.arn_type
    import capo_emr.types.auto_termination_policy
    import capo_emr.types.boolean
    import capo_emr.types.boolean_object
    import capo_emr.types.bootstrap_action_config_list
    import capo_emr.types.configuration_list
    import capo_emr.types.integer
    import capo_emr.types.job_flow_instances_config
    import capo_emr.types.kerberos_attributes
    import capo_emr.types.managed_scaling_policy
    import capo_emr.types.monitoring_configuration
    import capo_emr.types.new_supported_products_list
    import capo_emr.types.placement_group_config_list
    import capo_emr.types.repo_upgrade_on_boot
    import capo_emr.types.scale_down_behavior
    import capo_emr.types.step_config_list
    import capo_emr.types.supported_products_list
    import capo_emr.types.tag_list
    import capo_emr.types.xml_string
    import capo_emr.types.xml_string_max_len256


class RunJobFlowInput(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the job flow.</p>"""
    log_uri: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The location in Amazon S3 to write the log files of the job flow. If a value is not provided, logs are not created.</p>"""
    log_encryption_kms_key_id: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The KMS key used for encrypting log files. If a value is not provided, the logs remain encrypted by AES-256. This attribute is only available with Amazon EMR releases 5.30.0 and later, excluding Amazon EMR 6.0.0.</p>"""
    additional_info: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>A JSON string for selecting additional features.</p>"""
    ami_version: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>Applies only to Amazon EMR AMI versions 3.x and 2.x. For Amazon EMR releases 4.0 and later, <code>ReleaseLabel</code> is used. To specify a custom AMI, use <code>CustomAmiID</code>.</p>"""
    release_label: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The Amazon EMR release label, which determines the version of open-source application packages installed on the cluster. Release labels are in the form <code>emr-x.x.x</code>, where x.x.x is an Amazon EMR release version such as <code>emr-5.14.0</code>. For more information about Amazon EMR release versions and included application versions and features, see <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/">https://docs.aws.amazon.com/emr/latest/ReleaseGuide/</a>. The release label applies only to Amazon EMR releases version 4.0 and later. Earlier versions use <code>AmiVersion</code>.</p>"""
    instances: NotRequired[
        "capo_emr.types.job_flow_instances_config.JobFlowInstancesConfig"
    ]
    """<p>A specification of the number and type of Amazon EC2 instances.</p>"""
    steps: NotRequired["capo_emr.types.step_config_list.StepConfigList"]
    """<p>A list of steps to run.</p>"""
    step_execution_role_arn: NotRequired["capo_emr.types.arn_type.ArnType"]
    """<p>The Amazon Resource Name (ARN) of the runtime role for steps specified in the RunJobFlow request. The runtime role can be a cross-account IAM role. The runtime role ARN is a combination of account ID, role name, and role type using the following format: <code>arn:partition:iam::account-id:role/role-name</code>.</p> <p>For example, <code>arn:aws:iam::1234567890:role/ReadOnly</code> is a correctly formatted runtime role ARN.</p> <p>This parameter applies only to steps included in the <code>Steps</code> parameter of this RunJobFlow request. It does not apply to steps added later to the cluster.</p>"""
    bootstrap_actions: NotRequired[
        "capo_emr.types.bootstrap_action_config_list.BootstrapActionConfigList"
    ]
    """<p>A list of bootstrap actions to run before Hadoop starts on the cluster nodes.</p>"""
    supported_products: NotRequired[
        "capo_emr.types.supported_products_list.SupportedProductsList"
    ]
    """<note> <p>For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.</p> </note> <p>A list of strings that indicates third-party software to use. For more information, see the <a href="https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf">Amazon EMR Developer Guide</a>. Currently supported values are:</p> <ul> <li> <p>"mapr-m3" - launch the job flow using MapR M3 Edition.</p> </li> <li> <p>"mapr-m5" - launch the job flow using MapR M5 Edition.</p> </li> </ul>"""
    new_supported_products: NotRequired[
        "capo_emr.types.new_supported_products_list.NewSupportedProductsList"
    ]
    """<note> <p>For Amazon EMR releases 3.x and 2.x. For Amazon EMR releases 4.x and later, use Applications.</p> </note> <p>A list of strings that indicates third-party software to use with the job flow that accepts a user argument list. Amazon EMR accepts and forwards the argument list to the corresponding installation script as bootstrap action arguments. For more information, see "Launch a Job Flow on the MapR Distribution for Hadoop" in the <a href="https://docs.aws.amazon.com/emr/latest/DeveloperGuide/emr-dg.pdf">Amazon EMR Developer Guide</a>. Supported values are:</p> <ul> <li> <p>"mapr-m3" - launch the cluster using MapR M3 Edition.</p> </li> <li> <p>"mapr-m5" - launch the cluster using MapR M5 Edition.</p> </li> <li> <p>"mapr" with the user arguments specifying "--edition,m3" or "--edition,m5" - launch the job flow using MapR M3 or M5 Edition respectively.</p> </li> <li> <p>"mapr-m7" - launch the cluster using MapR M7 Edition.</p> </li> <li> <p>"hunk" - launch the cluster with the Hunk Big Data Analytics Platform.</p> </li> <li> <p>"hue"- launch the cluster with Hue installed.</p> </li> <li> <p>"spark" - launch the cluster with Apache Spark installed.</p> </li> <li> <p>"ganglia" - launch the cluster with the Ganglia Monitoring System installed.</p> </li> </ul>"""
    applications: NotRequired["capo_emr.types.application_list.ApplicationList"]
    """<p>Applies to Amazon EMR releases 4.0 and later. A case-insensitive list of applications for Amazon EMR to install and configure when launching the cluster. For a list of applications available for each Amazon EMR release version, see the <a href="https://docs.aws.amazon.com/emr/latest/ReleaseGuide/">Amazon EMRRelease Guide</a>.</p>"""
    configurations: NotRequired["capo_emr.types.configuration_list.ConfigurationList"]
    """<p>For Amazon EMR releases 4.0 and later. The list of configurations supplied for the Amazon EMR cluster that you are creating.</p>"""
    visible_to_all_users: NotRequired["capo_emr.types.boolean.Boolean"]
    """<important> <p>The VisibleToAllUsers parameter is no longer supported. By default, the value is set to <code>true</code>. Setting it to <code>false</code> now has no effect.</p> </important> <p>Set this value to <code>true</code> so that IAM principals in the Amazon Web Services account associated with the cluster can perform Amazon EMR actions on the cluster that their IAM policies allow. This value defaults to <code>true</code> for clusters created using the Amazon EMR API or the CLI <a href="https://docs.aws.amazon.com/cli/latest/reference/emr/create-cluster.html">create-cluster</a> command.</p> <p>When set to <code>false</code>, only the IAM principal that created the cluster and the Amazon Web Services account root user can perform Amazon EMR actions for the cluster, regardless of the IAM permissions policies attached to other IAM principals. For more information, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_IAM_emr-with-IAM.html#security_set_visible_to_all_users">Understanding the Amazon EMR cluster VisibleToAllUsers setting</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    job_flow_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>Also called instance profile and Amazon EC2 role. An IAM role for an Amazon EMR cluster. The Amazon EC2 instances of the cluster assume this role. The default role is <code>EMR_EC2_DefaultRole</code>. In order to use the default role, you must have already created it using the CLI or console.</p>"""
    service_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The IAM role that Amazon EMR assumes in order to access Amazon Web Services resources on your behalf. If you've created a custom service role path, you must specify it for the service role when you launch your cluster.</p>"""
    tags: NotRequired["capo_emr.types.tag_list.TagList"]
    """<p>A list of tags to associate with a cluster and propagate to Amazon EC2 instances.</p>"""
    security_configuration: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>The name of a security configuration to apply to the cluster.</p>"""
    auto_scaling_role: NotRequired["capo_emr.types.xml_string.XmlString"]
    """<p>An IAM role for automatic scaling policies. The default role is <code>EMR_AutoScaling_DefaultRole</code>. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate Amazon EC2 instances in an instance group.</p>"""
    scale_down_behavior: NotRequired[
        "capo_emr.types.scale_down_behavior.ScaleDownBehavior"
    ]
    """<p>Specifies the way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an instance group is resized. <code>TERMINATE_AT_INSTANCE_HOUR</code> indicates that Amazon EMR terminates nodes at the instance-hour boundary, regardless of when the request to terminate the instance was submitted. This option is only available with Amazon EMR 5.1.0 and later and is the default for clusters created using that version. <code>TERMINATE_AT_TASK_COMPLETION</code> indicates that Amazon EMR adds nodes to a deny list and drains tasks from nodes before terminating the Amazon EC2 instances, regardless of the instance-hour boundary. With either behavior, Amazon EMR removes the least active nodes first and blocks instance termination if it could lead to HDFS corruption. <code>TERMINATE_AT_TASK_COMPLETION</code> available only in Amazon EMR releases 4.1.0 and later, and is the default for releases of Amazon EMR earlier than 5.1.0.</p>"""
    custom_ami_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Available only in Amazon EMR releases 5.7.0 and later. The ID of a custom Amazon EBS-backed Linux AMI. If specified, Amazon EMR uses this AMI when it launches cluster Amazon EC2 instances. For more information about custom AMIs in Amazon EMR, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-custom-ami.html">Using a Custom AMI</a> in the <i>Amazon EMR Management Guide</i>. If omitted, the cluster uses the base Linux AMI for the <code>ReleaseLabel</code> specified. For Amazon EMR releases 2.x and 3.x, use <code>AmiVersion</code> instead.</p> <p>For information about creating a custom AMI, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html">Creating an Amazon EBS-Backed Linux AMI</a> in the <i>Amazon Elastic Compute Cloud User Guide for Linux Instances</i>. For information about finding an AMI ID, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html">Finding a Linux AMI</a>. </p>"""
    ebs_root_volume_size: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The size, in GiB, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 4.x and later.</p>"""
    repo_upgrade_on_boot: NotRequired[
        "capo_emr.types.repo_upgrade_on_boot.RepoUpgradeOnBoot"
    ]
    """<p>Applies only when <code>CustomAmiID</code> is used. Specifies which updates from the Amazon Linux AMI package repositories to apply automatically when the instance boots using the AMI. If omitted, the default is <code>SECURITY</code>, which indicates that only security updates are applied. If <code>NONE</code> is specified, no updates are applied, and all updates must be applied manually.</p>"""
    kerberos_attributes: NotRequired[
        "capo_emr.types.kerberos_attributes.KerberosAttributes"
    ]
    """<p>Attributes for Kerberos configuration when Kerberos authentication is enabled using a security configuration. For more information see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-kerberos.html">Use Kerberos Authentication</a> in the <i>Amazon EMR Management Guide</i>.</p>"""
    step_concurrency_level: NotRequired["capo_emr.types.integer.Integer"]
    """<p>Specifies the number of steps that can be executed concurrently. The default value is <code>1</code>. The maximum value is <code>256</code>.</p>"""
    managed_scaling_policy: NotRequired[
        "capo_emr.types.managed_scaling_policy.ManagedScalingPolicy"
    ]
    """<p> The specified managed scaling policy for an Amazon EMR cluster. </p>"""
    placement_group_configs: NotRequired[
        "capo_emr.types.placement_group_config_list.PlacementGroupConfigList"
    ]
    """<p>The specified placement group configuration for an Amazon EMR cluster.</p>"""
    auto_termination_policy: NotRequired[
        "capo_emr.types.auto_termination_policy.AutoTerminationPolicy"
    ]
    os_release_label: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Specifies a particular Amazon Linux release for all nodes in a cluster launch RunJobFlow request. If a release is not specified, Amazon EMR uses the latest validated Amazon Linux release for cluster launch.</p>"""
    ebs_root_volume_iops: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The IOPS, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    ebs_root_volume_throughput: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The throughput, in MiB/s, of the Amazon EBS root device volume of the Linux AMI that is used for each Amazon EC2 instance. Available in Amazon EMR releases 6.15.0 and later.</p>"""
    extended_support: NotRequired["capo_emr.types.boolean_object.BooleanObject"]
    """<p>Reserved.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Contains CloudWatch log configuration metadata and settings.</p>"""
    session_enabled: NotRequired["capo_emr.types.boolean_object.BooleanObject"]
    """<p>Indicates whether Spark Connect sessions are enabled on the cluster. When set to <code>true</code>, you can start Spark Connect sessions using the <code>StartSession</code> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunJobFlowInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "log_encryption_kms_key_id" in value:
        out["LogEncryptionKmsKeyId"] = value["log_encryption_kms_key_id"]
    if "additional_info" in value:
        out["AdditionalInfo"] = value["additional_info"]
    if "ami_version" in value:
        out["AmiVersion"] = value["ami_version"]
    if "release_label" in value:
        out["ReleaseLabel"] = value["release_label"]
    if "instances" in value:
        import capo_emr.types.job_flow_instances_config

        out["Instances"] = (
            capo_emr.types.job_flow_instances_config.serialize_aws_json_1_1(
                value["instances"]
            )
        )
    if "steps" in value:
        import capo_emr.types.step_config_list

        out["Steps"] = capo_emr.types.step_config_list.serialize_aws_json_1_1(
            value["steps"]
        )
    if "step_execution_role_arn" in value:
        out["StepExecutionRoleArn"] = value["step_execution_role_arn"]
    if "bootstrap_actions" in value:
        import capo_emr.types.bootstrap_action_config_list

        out["BootstrapActions"] = (
            capo_emr.types.bootstrap_action_config_list.serialize_aws_json_1_1(
                value["bootstrap_actions"]
            )
        )
    if "supported_products" in value:
        import capo_emr.types.supported_products_list

        out["SupportedProducts"] = (
            capo_emr.types.supported_products_list.serialize_aws_json_1_1(
                value["supported_products"]
            )
        )
    if "new_supported_products" in value:
        import capo_emr.types.new_supported_products_list

        out["NewSupportedProducts"] = (
            capo_emr.types.new_supported_products_list.serialize_aws_json_1_1(
                value["new_supported_products"]
            )
        )
    if "applications" in value:
        import capo_emr.types.application_list

        out["Applications"] = capo_emr.types.application_list.serialize_aws_json_1_1(
            value["applications"]
        )
    if "configurations" in value:
        import capo_emr.types.configuration_list

        out["Configurations"] = (
            capo_emr.types.configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "visible_to_all_users" in value:
        out["VisibleToAllUsers"] = value["visible_to_all_users"]
    if "job_flow_role" in value:
        out["JobFlowRole"] = value["job_flow_role"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "tags" in value:
        import capo_emr.types.tag_list

        out["Tags"] = capo_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
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
    if "step_concurrency_level" in value:
        out["StepConcurrencyLevel"] = value["step_concurrency_level"]
    if "managed_scaling_policy" in value:
        import capo_emr.types.managed_scaling_policy

        out["ManagedScalingPolicy"] = (
            capo_emr.types.managed_scaling_policy.serialize_aws_json_1_1(
                value["managed_scaling_policy"]
            )
        )
    if "placement_group_configs" in value:
        import capo_emr.types.placement_group_config_list

        out["PlacementGroupConfigs"] = (
            capo_emr.types.placement_group_config_list.serialize_aws_json_1_1(
                value["placement_group_configs"]
            )
        )
    if "auto_termination_policy" in value:
        import capo_emr.types.auto_termination_policy

        out["AutoTerminationPolicy"] = (
            capo_emr.types.auto_termination_policy.serialize_aws_json_1_1(
                value["auto_termination_policy"]
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


def deserialize_aws_json_1_1(data: dict) -> RunJobFlowInput:
    out: RunJobFlowInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("LogUri") is not None:
        out["log_uri"] = data["LogUri"]
    if data.get("LogEncryptionKmsKeyId") is not None:
        out["log_encryption_kms_key_id"] = data["LogEncryptionKmsKeyId"]
    if data.get("AdditionalInfo") is not None:
        out["additional_info"] = data["AdditionalInfo"]
    if data.get("AmiVersion") is not None:
        out["ami_version"] = data["AmiVersion"]
    if data.get("ReleaseLabel") is not None:
        out["release_label"] = data["ReleaseLabel"]
    if data.get("Instances") is not None:
        import capo_emr.types.job_flow_instances_config

        out["instances"] = (
            capo_emr.types.job_flow_instances_config.deserialize_aws_json_1_1(
                data["Instances"]
            )
        )
    if data.get("Steps") is not None:
        import capo_emr.types.step_config_list

        out["steps"] = capo_emr.types.step_config_list.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if data.get("StepExecutionRoleArn") is not None:
        out["step_execution_role_arn"] = data["StepExecutionRoleArn"]
    if data.get("BootstrapActions") is not None:
        import capo_emr.types.bootstrap_action_config_list

        out["bootstrap_actions"] = (
            capo_emr.types.bootstrap_action_config_list.deserialize_aws_json_1_1(
                data["BootstrapActions"]
            )
        )
    if data.get("SupportedProducts") is not None:
        import capo_emr.types.supported_products_list

        out["supported_products"] = (
            capo_emr.types.supported_products_list.deserialize_aws_json_1_1(
                data["SupportedProducts"]
            )
        )
    if data.get("NewSupportedProducts") is not None:
        import capo_emr.types.new_supported_products_list

        out["new_supported_products"] = (
            capo_emr.types.new_supported_products_list.deserialize_aws_json_1_1(
                data["NewSupportedProducts"]
            )
        )
    if data.get("Applications") is not None:
        import capo_emr.types.application_list

        out["applications"] = capo_emr.types.application_list.deserialize_aws_json_1_1(
            data["Applications"]
        )
    if data.get("Configurations") is not None:
        import capo_emr.types.configuration_list

        out["configurations"] = (
            capo_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if data.get("VisibleToAllUsers") is not None:
        out["visible_to_all_users"] = data["VisibleToAllUsers"]
    if data.get("JobFlowRole") is not None:
        out["job_flow_role"] = data["JobFlowRole"]
    if data.get("ServiceRole") is not None:
        out["service_role"] = data["ServiceRole"]
    if data.get("Tags") is not None:
        import capo_emr.types.tag_list

        out["tags"] = capo_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
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
    if data.get("StepConcurrencyLevel") is not None:
        out["step_concurrency_level"] = data["StepConcurrencyLevel"]
    if data.get("ManagedScalingPolicy") is not None:
        import capo_emr.types.managed_scaling_policy

        out["managed_scaling_policy"] = (
            capo_emr.types.managed_scaling_policy.deserialize_aws_json_1_1(
                data["ManagedScalingPolicy"]
            )
        )
    if data.get("PlacementGroupConfigs") is not None:
        import capo_emr.types.placement_group_config_list

        out["placement_group_configs"] = (
            capo_emr.types.placement_group_config_list.deserialize_aws_json_1_1(
                data["PlacementGroupConfigs"]
            )
        )
    if data.get("AutoTerminationPolicy") is not None:
        import capo_emr.types.auto_termination_policy

        out["auto_termination_policy"] = (
            capo_emr.types.auto_termination_policy.deserialize_aws_json_1_1(
                data["AutoTerminationPolicy"]
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
