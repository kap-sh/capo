"""Generated from Smithy shape ``com.amazonaws.emr#JobFlowInstancesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.boolean
    import capo_emr.types.boolean_object
    import capo_emr.types.instance_fleet_config_list
    import capo_emr.types.instance_group_config_list
    import capo_emr.types.instance_type
    import capo_emr.types.integer
    import capo_emr.types.placement_type
    import capo_emr.types.security_groups_list
    import capo_emr.types.xml_string_max_len256
    import capo_emr.types.xml_string_max_len256_list


class JobFlowInstancesConfig(TypedDict, closed=True):
    master_instance_type: NotRequired["capo_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type of the master node.</p>"""
    slave_instance_type: NotRequired["capo_emr.types.instance_type.InstanceType"]
    """<p>The Amazon EC2 instance type of the core and task nodes.</p>"""
    instance_count: NotRequired["capo_emr.types.integer.Integer"]
    """<p>The number of Amazon EC2 instances in the cluster.</p>"""
    instance_groups: NotRequired[
        "capo_emr.types.instance_group_config_list.InstanceGroupConfigList"
    ]
    """<p>Configuration for the instance groups in a cluster.</p>"""
    instance_fleets: NotRequired[
        "capo_emr.types.instance_fleet_config_list.InstanceFleetConfigList"
    ]
    """<note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note> <p>Describes the Amazon EC2 instances and instance configurations for clusters that use the instance fleet configuration.</p>"""
    ec2_key_name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the Amazon EC2 key pair that can be used to connect to the master node using SSH as the user called "hadoop."</p>"""
    placement: NotRequired["capo_emr.types.placement_type.PlacementType"]
    """<p>The Availability Zone in which the cluster runs.</p>"""
    keep_job_flow_alive_when_no_steps: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Specifies whether the cluster should remain available after completing all steps. Defaults to <code>false</code>. For more information about configuring cluster termination, see <a href="https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html">Control Cluster Termination</a> in the <i>EMR Management Guide</i>.</p>"""
    termination_protected: NotRequired["capo_emr.types.boolean.Boolean"]
    """<p>Specifies whether to lock the cluster to prevent the Amazon EC2 instances from being terminated by API call, user intervention, or in the event of a job-flow error.</p>"""
    unhealthy_node_replacement: NotRequired[
        "capo_emr.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether Amazon EMR should gracefully replace core nodes that have degraded within the cluster.</p>"""
    hadoop_version: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Applies only to Amazon EMR release versions earlier than 4.0. The Hadoop version for the cluster. Valid inputs are "0.18" (no longer maintained), "0.20" (no longer maintained), "0.20.205" (no longer maintained), "1.0.3", "2.2.0", or "2.4.0". If you do not set this value, the default of 0.18 is used, unless the <code>AmiVersion</code> parameter is set in the RunJobFlow call, in which case the default version of Hadoop for that AMI version is used.</p>"""
    ec2_subnet_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>Applies to clusters that use the uniform instance group configuration. To launch the cluster in Amazon Virtual Private Cloud (Amazon VPC), set this parameter to the identifier of the Amazon VPC subnet where you want the cluster to launch. If you do not specify this value and your account supports EC2-Classic, the cluster launches in EC2-Classic.</p>"""
    ec2_subnet_ids: NotRequired[
        "capo_emr.types.xml_string_max_len256_list.XmlStringMaxLen256List"
    ]
    """<p>Applies to clusters that use the instance fleet configuration. When multiple Amazon EC2 subnet IDs are specified, Amazon EMR evaluates them and launches instances in the optimal subnet.</p> <note> <p>The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.</p> </note>"""
    emr_managed_master_security_group: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the master node. If you specify <code>EmrManagedMasterSecurityGroup</code>, you must also specify <code>EmrManagedSlaveSecurityGroup</code>.</p>"""
    emr_managed_slave_security_group: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the core and task nodes. If you specify <code>EmrManagedSlaveSecurityGroup</code>, you must also specify <code>EmrManagedMasterSecurityGroup</code>.</p>"""
    service_access_security_group: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The identifier of the Amazon EC2 security group for the Amazon EMR service to access clusters in VPC private subnets.</p>"""
    additional_master_security_groups: NotRequired[
        "capo_emr.types.security_groups_list.SecurityGroupsList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the master node.</p>"""
    additional_slave_security_groups: NotRequired[
        "capo_emr.types.security_groups_list.SecurityGroupsList"
    ]
    """<p>A list of additional Amazon EC2 security group IDs for the core and task nodes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobFlowInstancesConfig) -> dict:
    out: dict = {}
    if "master_instance_type" in value:
        out["MasterInstanceType"] = value["master_instance_type"]
    if "slave_instance_type" in value:
        out["SlaveInstanceType"] = value["slave_instance_type"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "instance_groups" in value:
        import capo_emr.types.instance_group_config_list

        out["InstanceGroups"] = (
            capo_emr.types.instance_group_config_list.serialize_aws_json_1_1(
                value["instance_groups"]
            )
        )
    if "instance_fleets" in value:
        import capo_emr.types.instance_fleet_config_list

        out["InstanceFleets"] = (
            capo_emr.types.instance_fleet_config_list.serialize_aws_json_1_1(
                value["instance_fleets"]
            )
        )
    if "ec2_key_name" in value:
        out["Ec2KeyName"] = value["ec2_key_name"]
    if "placement" in value:
        import capo_emr.types.placement_type

        out["Placement"] = capo_emr.types.placement_type.serialize_aws_json_1_1(
            value["placement"]
        )
    if "keep_job_flow_alive_when_no_steps" in value:
        out["KeepJobFlowAliveWhenNoSteps"] = value["keep_job_flow_alive_when_no_steps"]
    if "termination_protected" in value:
        out["TerminationProtected"] = value["termination_protected"]
    if "unhealthy_node_replacement" in value:
        out["UnhealthyNodeReplacement"] = value["unhealthy_node_replacement"]
    if "hadoop_version" in value:
        out["HadoopVersion"] = value["hadoop_version"]
    if "ec2_subnet_id" in value:
        out["Ec2SubnetId"] = value["ec2_subnet_id"]
    if "ec2_subnet_ids" in value:
        import capo_emr.types.xml_string_max_len256_list

        out["Ec2SubnetIds"] = (
            capo_emr.types.xml_string_max_len256_list.serialize_aws_json_1_1(
                value["ec2_subnet_ids"]
            )
        )
    if "emr_managed_master_security_group" in value:
        out["EmrManagedMasterSecurityGroup"] = value[
            "emr_managed_master_security_group"
        ]
    if "emr_managed_slave_security_group" in value:
        out["EmrManagedSlaveSecurityGroup"] = value["emr_managed_slave_security_group"]
    if "service_access_security_group" in value:
        out["ServiceAccessSecurityGroup"] = value["service_access_security_group"]
    if "additional_master_security_groups" in value:
        import capo_emr.types.security_groups_list

        out["AdditionalMasterSecurityGroups"] = (
            capo_emr.types.security_groups_list.serialize_aws_json_1_1(
                value["additional_master_security_groups"]
            )
        )
    if "additional_slave_security_groups" in value:
        import capo_emr.types.security_groups_list

        out["AdditionalSlaveSecurityGroups"] = (
            capo_emr.types.security_groups_list.serialize_aws_json_1_1(
                value["additional_slave_security_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JobFlowInstancesConfig:
    out: JobFlowInstancesConfig = {}  # type: ignore[typeddict-item]
    if data.get("MasterInstanceType") is not None:
        out["master_instance_type"] = data["MasterInstanceType"]
    if data.get("SlaveInstanceType") is not None:
        out["slave_instance_type"] = data["SlaveInstanceType"]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("InstanceGroups") is not None:
        import capo_emr.types.instance_group_config_list

        out["instance_groups"] = (
            capo_emr.types.instance_group_config_list.deserialize_aws_json_1_1(
                data["InstanceGroups"]
            )
        )
    if data.get("InstanceFleets") is not None:
        import capo_emr.types.instance_fleet_config_list

        out["instance_fleets"] = (
            capo_emr.types.instance_fleet_config_list.deserialize_aws_json_1_1(
                data["InstanceFleets"]
            )
        )
    if data.get("Ec2KeyName") is not None:
        out["ec2_key_name"] = data["Ec2KeyName"]
    if data.get("Placement") is not None:
        import capo_emr.types.placement_type

        out["placement"] = capo_emr.types.placement_type.deserialize_aws_json_1_1(
            data["Placement"]
        )
    if data.get("KeepJobFlowAliveWhenNoSteps") is not None:
        out["keep_job_flow_alive_when_no_steps"] = data["KeepJobFlowAliveWhenNoSteps"]
    if data.get("TerminationProtected") is not None:
        out["termination_protected"] = data["TerminationProtected"]
    if data.get("UnhealthyNodeReplacement") is not None:
        out["unhealthy_node_replacement"] = data["UnhealthyNodeReplacement"]
    if data.get("HadoopVersion") is not None:
        out["hadoop_version"] = data["HadoopVersion"]
    if data.get("Ec2SubnetId") is not None:
        out["ec2_subnet_id"] = data["Ec2SubnetId"]
    if data.get("Ec2SubnetIds") is not None:
        import capo_emr.types.xml_string_max_len256_list

        out["ec2_subnet_ids"] = (
            capo_emr.types.xml_string_max_len256_list.deserialize_aws_json_1_1(
                data["Ec2SubnetIds"]
            )
        )
    if data.get("EmrManagedMasterSecurityGroup") is not None:
        out["emr_managed_master_security_group"] = data["EmrManagedMasterSecurityGroup"]
    if data.get("EmrManagedSlaveSecurityGroup") is not None:
        out["emr_managed_slave_security_group"] = data["EmrManagedSlaveSecurityGroup"]
    if data.get("ServiceAccessSecurityGroup") is not None:
        out["service_access_security_group"] = data["ServiceAccessSecurityGroup"]
    if data.get("AdditionalMasterSecurityGroups") is not None:
        import capo_emr.types.security_groups_list

        out["additional_master_security_groups"] = (
            capo_emr.types.security_groups_list.deserialize_aws_json_1_1(
                data["AdditionalMasterSecurityGroups"]
            )
        )
    if data.get("AdditionalSlaveSecurityGroups") is not None:
        import capo_emr.types.security_groups_list

        out["additional_slave_security_groups"] = (
            capo_emr.types.security_groups_list.deserialize_aws_json_1_1(
                data["AdditionalSlaveSecurityGroups"]
            )
        )
    return out
