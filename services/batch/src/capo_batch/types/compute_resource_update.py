"""Generated from Smithy shape ``com.amazonaws.batch#ComputeResourceUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.boolean
    import capo_batch.types.compute_scaling_policy
    import capo_batch.types.cr_type
    import capo_batch.types.cr_update_allocation_strategy
    import capo_batch.types.ec2_configuration_list
    import capo_batch.types.integer
    import capo_batch.types.launch_template_specification
    import capo_batch.types.string
    import capo_batch.types.string_list
    import capo_batch.types.tagris_tags_map
    import capo_batch.types.tags_map
    import capo_batch.types.update_managed_instances_provider_configuration


class ComputeResourceUpdate(TypedDict, closed=True):
    minv_cpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The minimum number of vCPUs that an environment should maintain (even if the compute environment is <code>DISABLED</code>).</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    maxv_cpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum number of Amazon EC2 vCPUs that an environment can reach.</p> <note> <p>With any allocation strategy except <code>BEST_FIT</code> using On-Demand (<code>EC2</code>) compute resources, Batch might need to exceed <code>maxvCpus</code> to meet your capacity requirements. In this event, Batch never exceeds <code>maxvCpus</code> by more than a single instance.</p> </note>"""
    desiredv_cpus: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The desired number of vCPUS in the compute environment. Batch modifies this value between the minimum and maximum values based on job queue demand.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>Batch doesn't support changing the desired number of vCPUs of an existing compute environment. Don't specify this parameter for compute environments using Amazon EKS clusters.</p> </note> <note> <p>When you update the <code>desiredvCpus</code> setting, the value must be between the <code>minvCpus</code> and <code>maxvCpus</code> values. </p> <p>Additionally, the updated <code>desiredvCpus</code> value must be greater than or equal to the current <code>desiredvCpus</code> value. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#error-desired-vcpus-update">Troubleshooting Batch</a> in the <i>Batch User Guide</i>.</p> </note>"""
    subnets: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The VPC subnets where the compute resources are launched. Fargate compute resources can contain up to 16 subnets. For Fargate compute resources, providing an empty list will be handled as if this parameter wasn't specified and no change is made. For Amazon EC2 compute resources, providing an empty list removes the VPC subnets from the compute resource. For more information, see <a href="https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html">VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p> <p>When updating a compute environment, changing the VPC subnets requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>Batch on Amazon EC2 and Batch on Amazon EKS support Local Zones. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones"> Local Zones</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>, <a href="https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html">Amazon EKS and Amazon Web Services Local Zones</a> in the <i>Amazon EKS User Guide</i> and <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones"> Amazon ECS clusters in Local Zones, Wavelength Zones, and Amazon Web Services Outposts</a> in the <i>Amazon ECS Developer Guide</i>.</p> <p>Batch on Fargate doesn't currently support Local Zones.</p> </note>"""
    security_group_ids: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The Amazon EC2 security groups that are associated with instances launched in the compute environment. This parameter is required for Fargate compute resources, where it can contain up to 5 security groups. For Fargate compute resources, providing an empty list is handled as if this parameter wasn't specified and no change is made. For Amazon EC2 compute resources, providing an empty list removes the security groups from the compute resource.</p> <p>When updating a compute environment, changing the Amazon EC2 security groups requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    allocation_strategy: NotRequired[
        "capo_batch.types.cr_update_allocation_strategy.CRUpdateAllocationStrategy"
    ]
    """<p>The allocation strategy to use for the compute resource if there's not enough instances of the best fitting instance type that can be allocated. This might be because of availability of the instance type in the Region or <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html">Amazon EC2 service limits</a>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html">Allocation strategies</a> in the <i>Batch User Guide</i>.</p> <p>When updating a compute environment, changing the allocation strategy requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>. <code>BEST_FIT</code> isn't supported when updating a compute environment.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <dl> <dt>BEST_FIT_PROGRESSIVE</dt> <dd> <p>Batch selects additional instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types with lower cost vCPUs. If additional instances of the previously selected instance types aren't available, Batch selects new instance types.</p> </dd> <dt>BEST_FIT_PROGRESSIVE_ORDERED</dt> <dd> <important> <p>This is an advanced allocation strategy only for customers who want to control which instance types are preferred during scaling.</p> <p>Placing large instance types at the top of the list may result in <b>over-provisioning</b> for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching <code>maxvCpus</code>.</p> </important> <p>Batch selects instance types in the order they appear in the <code>instanceTypes</code> list. When an instance family is specified, sizes within that family are expanded using <code>BEST_FIT_PROGRESSIVE</code> logic—preferring sizes that best fit the jobs, with larger sizes as fallback. Instance types that cannot meet the resource requirements of the jobs are skipped. This strategy is only available for On-Demand Instance (<code>EC2</code>) compute resources.</p> <p>If an instance family and an explicit instance type from that family both appear in <code>instanceTypes</code>, the explicit type takes its listed position and is excluded from the family expansion. For example, in <code>["m7a.4xlarge", "m7a", "m6a"]</code>, <code>m7a.4xlarge</code> is always placed first and is excluded from the <code>m7a</code> family expansion.</p> </dd> <dt>SPOT_CAPACITY_OPTIMIZED</dt> <dd> <p>Batch selects one or more instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.</p> </dd> <dt>SPOT_PRICE_CAPACITY_OPTIMIZED</dt> <dd> <p>The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price. This allocation strategy is only available for Spot Instance compute resources.</p> </dd> <dt>SPOT_CAPACITY_OPTIMIZED_PRIORITIZED</dt> <dd> <important> <p>This is an advanced allocation strategy for customers who want to influence instance type selection during scaling. This strategy optimizes for <b>capacity first</b>, and honors instance type priorities on a best-effort basis (priorities are honored when they do not significantly reduce available Spot capacity).</p> <p>Placing large instance types at the top of the list may result in <b>over-provisioning</b> for small jobs. Placing small instance types at the top may cause the compute environment to reach Amazon EC2 instance count limits before reaching <code>maxvCpus</code>.</p> </important> <p>Batch selects instance types in the order they appear in the <code>instanceTypes</code> list, but <b>optimizes for capacity first</b>. The customer-defined priority is honored on a best-effort basis. When Spot Instance capacity pools are similarly available, priority order is respected. When capacity is constrained, Batch selects from the most available pools regardless of priority to minimize the likelihood of Spot Instance interruptions. This strategy is only available for Spot Instance compute resources.</p> </dd> </dl> <p>With any allocation strategy except <code>BEST_FIT</code> using On-Demand (<code>EC2</code>) compute resources, Batch might need to exceed <code>maxvCpus</code> to meet your capacity requirements. In this event, Batch never exceeds <code>maxvCpus</code> by more than a single instance.</p>"""
    instance_types: NotRequired["capo_batch.types.string_list.StringList"]
    """<p>The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, <code>c5</code> or <code>p3</code>), or you can specify specific sizes within a family (such as <code>c5.8xlarge</code>). </p> <p>Batch can select the instance type for you if you choose one of the following:</p> <ul> <li> <p> <code>optimal</code> to select instance types (from the <code>c4</code>, <code>m4</code>, <code>r4</code>, <code>c5</code>, <code>m5</code>, and <code>r5</code> instance families) that match the demand of your job queues. </p> </li> <li> <p> <code>default_x86_64</code> to choose x86 based instance types (from the <code>m6i</code>, <code>c6i</code>, <code>r6i</code>, and <code>c7i</code> instance families) that matches the resource demands of the job queue.</p> </li> <li> <p> <code>default_arm64</code> to choose x86 based instance types (from the <code>m6g</code>, <code>c6g</code>, <code>r6g</code>, and <code>c7g</code> instance families) that matches the resource demands of the job queue.</p> </li> </ul> <note> <p>Starting on 11/01/2025 the behavior of <code>optimal</code> is going to be changed to match <code>default_x86_64</code>. During the change your instance families could be updated to a newer generation. You do not need to perform any actions for the upgrade to happen. For more information about change, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/optimal-default-instance-troubleshooting.html">Optimal instance type configuration to receive automatic instance family updates</a>.</p> </note> <note> <p>Instance family availability varies by Amazon Web Services Region. For example, some Amazon Web Services Regions may not have any fourth generation instance families but have fifth and sixth generation instance families.</p> <p>When using <code>default_x86_64</code> or <code>default_arm64</code> instance bundles, Batch selects instance families based on a balance of cost-effectiveness and performance. While newer generation instances often provide better price-performance, Batch may choose an earlier generation instance family if it provides the optimal combination of availability, cost, and performance for your workload. For example, in an Amazon Web Services Region where both c6i and c7i instances are available, Batch might select c6i instances if they offer better cost-effectiveness for your specific job requirements. For more information on Batch instance types and Amazon Web Services Region availability, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/instance-type-compute-table.html">Instance type compute table</a> in the <i>Batch User Guide</i>.</p> <p>Batch periodically updates your instances in default bundles to newer, more cost-effective options. Updates happen automatically without requiring any action from you. Your workloads continue running during updates with no interruption </p> </note> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment.</p> </note>"""
    ec2_key_pair: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon EC2 key pair that's used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH. To remove the Amazon EC2 key pair, set this value to an empty string.</p> <p>When updating a compute environment, changing the Amazon EC2 key pair requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    instance_role: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. Required for Amazon EC2 instances. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, <code> <i>ecsInstanceRole</i> </code> or <code>arn:aws:iam::<i><aws_account_id></i>:instance-profile/<i>ecsInstanceRole</i> </code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html">Amazon ECS instance role</a> in the <i>Batch User Guide</i>.</p> <p>When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    tags: NotRequired["capo_batch.types.tags_map.TagsMap"]
    """<p>Key-value pair tags to be applied to Amazon EC2 resources that are launched in the compute environment. For Batch, these take the form of <code>"String1": "String2"</code>, where <code>String1</code> is the tag key and <code>String2</code> is the tag value (for example, <code>{ "Name": "Batch Instance - C4OnDemand" }</code>). This is helpful for recognizing your Batch instances in the Amazon EC2 console. These tags aren't seen when using the Batch <code>ListTagsForResource</code> API operation.</p> <p>When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    placement_group: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html">Placement groups</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p> <p>When updating a compute environment, changing the placement group requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    bid_percentage: NotRequired["capo_batch.types.integer.Integer"]
    """<p>The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. For most use cases, we recommend leaving this field empty.</p> <p>When updating a compute environment, changing the bid percentage requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    launch_template: NotRequired[
        "capo_batch.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    """<p>The updated launch template to use for your compute resources. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html">Launch template support</a> in the <i>Batch User Guide</i>. To remove the custom launch template and use the default launch template, set <code>launchTemplateId</code> or <code>launchTemplateName</code> member of the launch template specification to an empty string. Removing the launch template from a compute environment will not remove the AMI specified in the launch template. In order to update the AMI specified in a launch template, the <code>updateToLatestImageVersion</code> parameter must be set to <code>true</code>.</p> <p>When updating a compute environment, changing the launch template requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    ec2_configuration: NotRequired[
        "capo_batch.types.ec2_configuration_list.Ec2ConfigurationList"
    ]
    """<p>Provides information used to select Amazon Machine Images (AMIs) for Amazon EC2 instances in the compute environment. If <code>Ec2Configuration</code> isn't specified, the default is <code>ECS_AL2023</code> for EC2 (ECS) compute environments and <code>EKS_AL2023</code> for EKS compute environments.</p> <p>When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>. To remove the Amazon EC2 configuration and any custom AMI ID specified in <code>imageIdOverride</code>, set this value to an empty string.</p> <p>One or two values can be provided.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    update_to_latest_image_version: NotRequired["capo_batch.types.boolean.Boolean"]
    """<p>Specifies whether the AMI ID is updated to the latest one that's supported by Batch when the compute environment has an infrastructure update. The default value is <code>false</code>.</p> <note> <p>An AMI ID can either be specified in the <code>imageId</code> or <code>imageIdOverride</code> parameters or be determined by the launch template that's specified in the <code>launchTemplate</code> parameter. If an AMI ID is specified any of these ways, this parameter is ignored. For more information about to update AMI IDs during an infrastructure update, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html#updating-compute-environments-ami">Updating the AMI ID</a> in the <i>Batch User Guide</i>.</p> </note> <p>When updating a compute environment, changing this setting requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p>"""
    type: NotRequired["capo_batch.types.cr_type.CRType"]
    """<p>The type of compute environment: <code>EC2</code>, <code>SPOT</code>, <code>FARGATE</code>, <code>FARGATE_SPOT</code>, or <code>ECS_MANAGED_INSTANCES</code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html">Compute environments</a> in the <i>Batch User Guide</i>.</p> <p> If you choose <code>SPOT</code>, you must also specify an Amazon EC2 Spot Fleet role with the <code>spotIamFleetRole</code> parameter. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html">Amazon EC2 spot fleet role</a> in the <i>Batch User Guide</i>.</p> <p>When updating a compute environment, changing the type of a compute environment requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <p>You cannot change the type to or from <code>ECS_MANAGED_INSTANCES</code>.</p>"""
    image_id: NotRequired["capo_batch.types.string.String"]
    """<p>The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the <code>imageIdOverride</code> member of the <code>Ec2Configuration</code> structure. To remove the custom AMI ID and use the default AMI ID, set this value to an empty string.</p> <p>When updating a compute environment, changing the AMI ID requires an infrastructure update of the compute environment. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2023 AMI. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html">Amazon ECS-optimized Amazon Linux 2023 AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    scaling_policy: NotRequired[
        "capo_batch.types.compute_scaling_policy.ComputeScalingPolicy"
    ]
    """<p>The scaling policy configuration for the compute environment.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    managed_instances_provider: NotRequired[
        "capo_batch.types.update_managed_instances_provider_configuration.UpdateManagedInstancesProviderConfiguration"
    ]
    """<p>The updated configuration for the Amazon ECS Managed Instances capacity provider. This parameter is only valid when the compute environment type is <code>ECS_MANAGED_INSTANCES</code>. You cannot change <code>capacityOptionType</code> or <code>fipsEnabled</code> on update.</p>"""
    capacity_tags: NotRequired["capo_batch.types.tagris_tags_map.TagrisTagsMap"]
    """<p>The updated tags to apply to the Amazon ECS capacity provider and Amazon EC2 instances. This parameter is only valid for <code>ECS_MANAGED_INSTANCES</code> compute environments. You must have the <code>batch:SetCapacityTags</code> permission on the compute environment resource to use this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeResourceUpdate) -> dict:
    out: dict = {}
    if "minv_cpus" in value:
        out["minvCpus"] = value["minv_cpus"]
    if "maxv_cpus" in value:
        out["maxvCpus"] = value["maxv_cpus"]
    if "desiredv_cpus" in value:
        out["desiredvCpus"] = value["desiredv_cpus"]
    if "subnets" in value:
        import capo_batch.types.string_list

        out["subnets"] = capo_batch.types.string_list.serialize_json(value["subnets"])
    if "security_group_ids" in value:
        import capo_batch.types.string_list

        out["securityGroupIds"] = capo_batch.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "allocation_strategy" in value:
        import capo_batch.types.cr_update_allocation_strategy

        out["allocationStrategy"] = (
            capo_batch.types.cr_update_allocation_strategy.serialize_json(
                value["allocation_strategy"]
            )
        )
    if "instance_types" in value:
        import capo_batch.types.string_list

        out["instanceTypes"] = capo_batch.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "ec2_key_pair" in value:
        out["ec2KeyPair"] = value["ec2_key_pair"]
    if "instance_role" in value:
        out["instanceRole"] = value["instance_role"]
    if "tags" in value:
        import capo_batch.types.tags_map

        out["tags"] = capo_batch.types.tags_map.serialize_json(value["tags"])
    if "placement_group" in value:
        out["placementGroup"] = value["placement_group"]
    if "bid_percentage" in value:
        out["bidPercentage"] = value["bid_percentage"]
    if "launch_template" in value:
        import capo_batch.types.launch_template_specification

        out["launchTemplate"] = (
            capo_batch.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "ec2_configuration" in value:
        import capo_batch.types.ec2_configuration_list

        out["ec2Configuration"] = (
            capo_batch.types.ec2_configuration_list.serialize_json(
                value["ec2_configuration"]
            )
        )
    if "update_to_latest_image_version" in value:
        out["updateToLatestImageVersion"] = value["update_to_latest_image_version"]
    if "type" in value:
        import capo_batch.types.cr_type

        out["type"] = capo_batch.types.cr_type.serialize_json(value["type"])
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "scaling_policy" in value:
        import capo_batch.types.compute_scaling_policy

        out["scalingPolicy"] = capo_batch.types.compute_scaling_policy.serialize_json(
            value["scaling_policy"]
        )
    if "managed_instances_provider" in value:
        import capo_batch.types.update_managed_instances_provider_configuration

        out["managedInstancesProvider"] = (
            capo_batch.types.update_managed_instances_provider_configuration.serialize_json(
                value["managed_instances_provider"]
            )
        )
    if "capacity_tags" in value:
        import capo_batch.types.tagris_tags_map

        out["capacityTags"] = capo_batch.types.tagris_tags_map.serialize_json(
            value["capacity_tags"]
        )
    return out


def deserialize_json(data: dict) -> ComputeResourceUpdate:
    out: ComputeResourceUpdate = {}  # type: ignore[typeddict-item]
    if data.get("minvCpus") is not None:
        out["minv_cpus"] = data["minvCpus"]
    if data.get("maxvCpus") is not None:
        out["maxv_cpus"] = data["maxvCpus"]
    if data.get("desiredvCpus") is not None:
        out["desiredv_cpus"] = data["desiredvCpus"]
    if data.get("subnets") is not None:
        import capo_batch.types.string_list

        out["subnets"] = capo_batch.types.string_list.deserialize_json(data["subnets"])
    if data.get("securityGroupIds") is not None:
        import capo_batch.types.string_list

        out["security_group_ids"] = capo_batch.types.string_list.deserialize_json(
            data["securityGroupIds"]
        )
    if data.get("allocationStrategy") is not None:
        import capo_batch.types.cr_update_allocation_strategy

        out["allocation_strategy"] = (
            capo_batch.types.cr_update_allocation_strategy.deserialize_json(
                data["allocationStrategy"]
            )
        )
    if data.get("instanceTypes") is not None:
        import capo_batch.types.string_list

        out["instance_types"] = capo_batch.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if data.get("ec2KeyPair") is not None:
        out["ec2_key_pair"] = data["ec2KeyPair"]
    if data.get("instanceRole") is not None:
        out["instance_role"] = data["instanceRole"]
    if data.get("tags") is not None:
        import capo_batch.types.tags_map

        out["tags"] = capo_batch.types.tags_map.deserialize_json(data["tags"])
    if data.get("placementGroup") is not None:
        out["placement_group"] = data["placementGroup"]
    if data.get("bidPercentage") is not None:
        out["bid_percentage"] = data["bidPercentage"]
    if data.get("launchTemplate") is not None:
        import capo_batch.types.launch_template_specification

        out["launch_template"] = (
            capo_batch.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if data.get("ec2Configuration") is not None:
        import capo_batch.types.ec2_configuration_list

        out["ec2_configuration"] = (
            capo_batch.types.ec2_configuration_list.deserialize_json(
                data["ec2Configuration"]
            )
        )
    if data.get("updateToLatestImageVersion") is not None:
        out["update_to_latest_image_version"] = data["updateToLatestImageVersion"]
    if data.get("type") is not None:
        import capo_batch.types.cr_type

        out["type"] = capo_batch.types.cr_type.deserialize_json(data["type"])
    if data.get("imageId") is not None:
        out["image_id"] = data["imageId"]
    if data.get("scalingPolicy") is not None:
        import capo_batch.types.compute_scaling_policy

        out["scaling_policy"] = (
            capo_batch.types.compute_scaling_policy.deserialize_json(
                data["scalingPolicy"]
            )
        )
    if data.get("managedInstancesProvider") is not None:
        import capo_batch.types.update_managed_instances_provider_configuration

        out["managed_instances_provider"] = (
            capo_batch.types.update_managed_instances_provider_configuration.deserialize_json(
                data["managedInstancesProvider"]
            )
        )
    if data.get("capacityTags") is not None:
        import capo_batch.types.tagris_tags_map

        out["capacity_tags"] = capo_batch.types.tagris_tags_map.deserialize_json(
            data["capacityTags"]
        )
    return out
