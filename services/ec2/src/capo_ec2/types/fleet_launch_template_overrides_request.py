"""Generated from Smithy shape ``com.amazonaws.ec2#FleetLaunchTemplateOverridesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.double
    import capo_ec2.types.fleet_block_device_mapping_request_list
    import capo_ec2.types.fleet_iam_instance_profile_specification_request
    import capo_ec2.types.fleet_instance_metadata_options_request
    import capo_ec2.types.instance_requirements_request
    import capo_ec2.types.instance_type
    import capo_ec2.types.placement
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id


class FleetLaunchTemplateOverridesRequest(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type.</p> <p> <code>mac1.metal</code> is not supported as a launch template override.</p> <note> <p>If you specify <code>InstanceType</code>, you can't specify <code>InstanceRequirements</code>.</p> </note>"""
    max_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price. </p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> <p>If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message.</p> </important>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>The IDs of the subnets in which to launch the instances. Separate multiple subnet IDs using commas (for example, <code>subnet-1234abcdeexample1, subnet-0987cdef6example2</code>). A request of type <code>instant</code> can have only one subnet ID.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone in which to launch the instances. For example, <code>us-east-2a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    weighted_capacity: NotRequired["capo_ec2.types.double.Double"]
    """<p>The number of units provided by the specified instance type. These are the same units that you chose to set the target capacity in terms of instances, or a performance characteristic such as vCPUs, memory, or I/O.</p> <p>If the target capacity divided by this value is not a whole number, Amazon EC2 rounds the number of instances to the next whole number. If this value is not specified, the default is 1.</p> <note> <p>When specifying weights, the price used in the <code>lowest-price</code> and <code>price-capacity-optimized</code> allocation strategies is per <i>unit</i> hour (where the instance price is divided by the specified weight). However, if all the specified weights are above the requested <code>TargetCapacity</code>, resulting in only 1 instance being launched, the price used is per <i>instance</i> hour.</p> </note>"""
    priority: NotRequired["capo_ec2.types.double.Double"]
    """<p>The priority for the launch template override. The highest priority is launched first.</p> <p>If the On-Demand <code>AllocationStrategy</code> is set to <code>prioritized</code>, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity.</p> <p>If the Spot <code>AllocationStrategy</code> is set to <code>capacity-optimized-prioritized</code>, EC2 Fleet uses priority on a best-effort basis to determine which launch template override to use in fulfilling Spot capacity, but optimizes for capacity first.</p> <p>Valid values are whole numbers starting at <code>0</code>. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. You can set the same priority for different launch template overrides.</p>"""
    placement: NotRequired["capo_ec2.types.placement.Placement"]
    """<p>The location where the instance launched, if applicable.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the key pair to use for the instances.</p> <p>Supported only for fleets of type <code>instant</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html">Amazon EC2 key pairs</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    block_device_mappings: NotRequired[
        "capo_ec2.types.fleet_block_device_mapping_request_list.FleetBlockDeviceMappingRequestList"
    ]
    """<p>The block device mappings, which define the EBS volumes and instance store volumes to attach to the instance at launch.</p> <p>Supported only for fleets of type <code>instant</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html">Block device mappings for volumes on Amazon EC2 instances</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    iam_instance_profile: NotRequired[
        "capo_ec2.types.fleet_iam_instance_profile_specification_request.FleetIamInstanceProfileSpecificationRequest"
    ]
    """<p>The IAM instance profile to associate with the instances.</p> <p>Supported only for fleets of type <code>instant</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html">IAM roles for Amazon EC2</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    metadata_options: NotRequired[
        "capo_ec2.types.fleet_instance_metadata_options_request.FleetInstanceMetadataOptionsRequest"
    ]
    """<p>The metadata options for the instances.</p> <p>Supported only for fleets of type <code>instant</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html">Configure the instance metadata service</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_requirements: NotRequired[
        "capo_ec2.types.instance_requirements_request.InstanceRequirementsRequest"
    ]
    """<p>The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.</p> <note> <p>If you specify <code>InstanceRequirements</code>, you can't specify <code>InstanceType</code>.</p> </note>"""
    image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the AMI in the format <code>ami-17characters00000</code>.</p> <p>Alternatively, you can specify a Systems Manager parameter, using one of the following formats. The Systems Manager parameter will resolve to an AMI ID on launch.</p> <p>To reference a public parameter:</p> <ul> <li> <p> <code>resolve:ssm:<i>public-parameter</i> </code> </p> </li> </ul> <p>To reference a parameter stored in the same account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-name</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-name:label</i> </code> </p> </li> </ul> <p>To reference a parameter shared from another Amazon Web Services account:</p> <ul> <li> <p> <code>resolve:ssm:<i>parameter-ARN</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:version-number</i> </code> </p> </li> <li> <p> <code>resolve:ssm:<i>parameter-ARN:label</i> </code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-launch-template.html#use-an-ssm-parameter-instead-of-an-ami-id">Use a Systems Manager parameter instead of an AMI ID</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>This parameter is only available for fleets of type <code>instant</code>. For fleets of type <code>maintain</code> and <code>request</code>, you must specify the AMI ID in the launch template.</p> </note>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone in which to launch the instances. For example, <code>use2-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetLaunchTemplateOverridesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "max_price" in value:
        pairs.append((f"{key_prefix}MaxPrice", str(value["max_price"])))
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "weighted_capacity" in value:
        pairs.append(
            (
                f"{key_prefix}WeightedCapacity",
                (
                    "NaN"
                    if value["weighted_capacity"] != value["weighted_capacity"]
                    else "Infinity"
                    if value["weighted_capacity"] == float("inf")
                    else "-Infinity"
                    if value["weighted_capacity"] == float("-inf")
                    else str(value["weighted_capacity"])
                ),
            )
        )
    if "priority" in value:
        pairs.append(
            (
                f"{key_prefix}Priority",
                (
                    "NaN"
                    if value["priority"] != value["priority"]
                    else "Infinity"
                    if value["priority"] == float("inf")
                    else "-Infinity"
                    if value["priority"] == float("-inf")
                    else str(value["priority"])
                ),
            )
        )
    if "placement" in value:
        import capo_ec2.types.placement

        capo_ec2.types.placement.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "block_device_mappings" in value:
        import capo_ec2.types.fleet_block_device_mapping_request_list

        capo_ec2.types.fleet_block_device_mapping_request_list.serialize_ec2_query(
            value["block_device_mappings"], pairs, f"{key_prefix}BlockDeviceMapping"
        )
    if "iam_instance_profile" in value:
        import capo_ec2.types.fleet_iam_instance_profile_specification_request

        capo_ec2.types.fleet_iam_instance_profile_specification_request.serialize_ec2_query(
            value["iam_instance_profile"], pairs, f"{key_prefix}IamInstanceProfile"
        )
    if "metadata_options" in value:
        import capo_ec2.types.fleet_instance_metadata_options_request

        capo_ec2.types.fleet_instance_metadata_options_request.serialize_ec2_query(
            value["metadata_options"], pairs, f"{key_prefix}MetadataOptions"
        )
    if "instance_requirements" in value:
        import capo_ec2.types.instance_requirements_request

        capo_ec2.types.instance_requirements_request.serialize_ec2_query(
            value["instance_requirements"], pairs, f"{key_prefix}InstanceRequirements"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> FleetLaunchTemplateOverridesRequest:
    out: FleetLaunchTemplateOverridesRequest = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_max_price = el.find("MaxPrice")
    if child_max_price is not None:
        out["max_price"] = str(child_max_price.text or "")
    child_subnet_id = el.find("SubnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_weighted_capacity = el.find("WeightedCapacity")
    if child_weighted_capacity is not None:
        out["weighted_capacity"] = float(child_weighted_capacity.text or "")
    child_priority = el.find("Priority")
    if child_priority is not None:
        out["priority"] = float(child_priority.text or "")
    child_placement = el.find("Placement")
    if child_placement is not None:
        import capo_ec2.types.placement

        out["placement"] = capo_ec2.types.placement.deserialize_ec2_query(
            child_placement
        )
    child_key_name = el.find("KeyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_block_device_mappings = el.find("BlockDeviceMapping")
    if child_block_device_mappings is not None:
        import capo_ec2.types.fleet_block_device_mapping_request_list

        out["block_device_mappings"] = (
            capo_ec2.types.fleet_block_device_mapping_request_list.deserialize_ec2_query(
                child_block_device_mappings
            )
        )
    child_iam_instance_profile = el.find("IamInstanceProfile")
    if child_iam_instance_profile is not None:
        import capo_ec2.types.fleet_iam_instance_profile_specification_request

        out["iam_instance_profile"] = (
            capo_ec2.types.fleet_iam_instance_profile_specification_request.deserialize_ec2_query(
                child_iam_instance_profile
            )
        )
    child_metadata_options = el.find("MetadataOptions")
    if child_metadata_options is not None:
        import capo_ec2.types.fleet_instance_metadata_options_request

        out["metadata_options"] = (
            capo_ec2.types.fleet_instance_metadata_options_request.deserialize_ec2_query(
                child_metadata_options
            )
        )
    child_instance_requirements = el.find("InstanceRequirements")
    if child_instance_requirements is not None:
        import capo_ec2.types.instance_requirements_request

        out["instance_requirements"] = (
            capo_ec2.types.instance_requirements_request.deserialize_ec2_query(
                child_instance_requirements
            )
        )
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
