"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstanceLaunchSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.architecture_values
    import capo_ec2.types.boolean
    import capo_ec2.types.instance_type
    import capo_ec2.types.placement
    import capo_ec2.types.security_group_id_string_list
    import capo_ec2.types.security_group_string_list
    import capo_ec2.types.shutdown_behavior
    import capo_ec2.types.string
    import capo_ec2.types.subnet_id
    import capo_ec2.types.user_data


class ImportInstanceLaunchSpecification(TypedDict, closed=True):
    architecture: NotRequired["capo_ec2.types.architecture_values.ArchitectureValues"]
    """<p>The architecture of the instance.</p>"""
    group_names: NotRequired[
        "capo_ec2.types.security_group_string_list.SecurityGroupStringList"
    ]
    """<p>The security group names.</p>"""
    group_ids: NotRequired[
        "capo_ec2.types.security_group_id_string_list.SecurityGroupIdStringList"
    ]
    """<p>The security group IDs.</p>"""
    additional_info: NotRequired["capo_ec2.types.string.String"]
    """<p>Reserved.</p>"""
    user_data: NotRequired["capo_ec2.types.user_data.UserData"]
    """<p>The Base64-encoded user data to make available to the instance.</p>"""
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information about the instance types that you can import, see <a href="https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-instance-types">Instance Types</a> in the VM Import/Export User Guide.</p>"""
    placement: NotRequired["capo_ec2.types.placement.Placement"]
    """<p>The placement information for the instance.</p>"""
    monitoring: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether monitoring is enabled.</p>"""
    subnet_id: NotRequired["capo_ec2.types.subnet_id.SubnetId"]
    """<p>[EC2-VPC] The ID of the subnet in which to launch the instance.</p>"""
    instance_initiated_shutdown_behavior: NotRequired[
        "capo_ec2.types.shutdown_behavior.ShutdownBehavior"
    ]
    """<p>Indicates whether an instance stops or terminates when you initiate shutdown from the instance (using the operating system command for system shutdown).</p>"""
    private_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>[EC2-VPC] An available IP address from the IP address range of the subnet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportInstanceLaunchSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "architecture" in value:
        import capo_ec2.types.architecture_values

        capo_ec2.types.architecture_values.serialize_ec2_query(
            value["architecture"], pairs, f"{key_prefix}Architecture"
        )
    if "group_names" in value:
        import capo_ec2.types.security_group_string_list

        capo_ec2.types.security_group_string_list.serialize_ec2_query(
            value["group_names"], pairs, f"{key_prefix}GroupName"
        )
    if "group_ids" in value:
        import capo_ec2.types.security_group_id_string_list

        capo_ec2.types.security_group_id_string_list.serialize_ec2_query(
            value["group_ids"], pairs, f"{key_prefix}GroupId"
        )
    if "additional_info" in value:
        pairs.append((f"{key_prefix}AdditionalInfo", str(value["additional_info"])))
    if "user_data" in value:
        import capo_ec2.types.user_data

        capo_ec2.types.user_data.serialize_ec2_query(
            value["user_data"], pairs, f"{key_prefix}UserData"
        )
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "placement" in value:
        import capo_ec2.types.placement

        capo_ec2.types.placement.serialize_ec2_query(
            value["placement"], pairs, f"{key_prefix}Placement"
        )
    if "monitoring" in value:
        pairs.append(
            (f"{key_prefix}Monitoring", "true" if value["monitoring"] else "false")
        )
    if "subnet_id" in value:
        pairs.append((f"{key_prefix}SubnetId", str(value["subnet_id"])))
    if "instance_initiated_shutdown_behavior" in value:
        import capo_ec2.types.shutdown_behavior

        capo_ec2.types.shutdown_behavior.serialize_ec2_query(
            value["instance_initiated_shutdown_behavior"],
            pairs,
            f"{key_prefix}InstanceInitiatedShutdownBehavior",
        )
    if "private_ip_address" in value:
        pairs.append(
            (f"{key_prefix}PrivateIpAddress", str(value["private_ip_address"]))
        )


def deserialize_ec2_query(el: Element) -> ImportInstanceLaunchSpecification:
    out: ImportInstanceLaunchSpecification = {}  # type: ignore[typeddict-item]
    child_architecture = el.find("architecture")
    if child_architecture is not None:
        import capo_ec2.types.architecture_values

        out["architecture"] = capo_ec2.types.architecture_values.deserialize_ec2_query(
            child_architecture
        )
    child_group_names = el.find("GroupName")
    if child_group_names is not None:
        import capo_ec2.types.security_group_string_list

        out["group_names"] = (
            capo_ec2.types.security_group_string_list.deserialize_ec2_query(
                child_group_names
            )
        )
    child_group_ids = el.find("GroupId")
    if child_group_ids is not None:
        import capo_ec2.types.security_group_id_string_list

        out["group_ids"] = (
            capo_ec2.types.security_group_id_string_list.deserialize_ec2_query(
                child_group_ids
            )
        )
    child_additional_info = el.find("additionalInfo")
    if child_additional_info is not None:
        out["additional_info"] = str(child_additional_info.text or "")
    child_user_data = el.find("userData")
    if child_user_data is not None:
        import capo_ec2.types.user_data

        out["user_data"] = capo_ec2.types.user_data.deserialize_ec2_query(
            child_user_data
        )
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_placement = el.find("placement")
    if child_placement is not None:
        import capo_ec2.types.placement

        out["placement"] = capo_ec2.types.placement.deserialize_ec2_query(
            child_placement
        )
    child_monitoring = el.find("monitoring")
    if child_monitoring is not None:
        out["monitoring"] = (child_monitoring.text or "").lower() == "true"
    child_subnet_id = el.find("subnetId")
    if child_subnet_id is not None:
        out["subnet_id"] = str(child_subnet_id.text or "")
    child_instance_initiated_shutdown_behavior = el.find(
        "instanceInitiatedShutdownBehavior"
    )
    if child_instance_initiated_shutdown_behavior is not None:
        import capo_ec2.types.shutdown_behavior

        out["instance_initiated_shutdown_behavior"] = (
            capo_ec2.types.shutdown_behavior.deserialize_ec2_query(
                child_instance_initiated_shutdown_behavior
            )
        )
    child_private_ip_address = el.find("privateIpAddress")
    if child_private_ip_address is not None:
        out["private_ip_address"] = str(child_private_ip_address.text or "")
    return out
