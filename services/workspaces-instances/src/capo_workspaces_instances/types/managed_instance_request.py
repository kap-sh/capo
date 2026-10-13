"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ManagedInstanceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.block_device_mappings
    import capo_workspaces_instances.types.capacity_reservation_specification
    import capo_workspaces_instances.types.cpu_options_request
    import capo_workspaces_instances.types.credit_specification_request
    import capo_workspaces_instances.types.enclave_options_request
    import capo_workspaces_instances.types.hibernation_options_request
    import capo_workspaces_instances.types.iam_instance_profile_specification
    import capo_workspaces_instances.types.image_id
    import capo_workspaces_instances.types.instance_maintenance_options_request
    import capo_workspaces_instances.types.instance_market_options_request
    import capo_workspaces_instances.types.instance_metadata_options_request
    import capo_workspaces_instances.types.instance_network_performance_options_request
    import capo_workspaces_instances.types.instance_type
    import capo_workspaces_instances.types.ipv4_address
    import capo_workspaces_instances.types.ipv6_addresses
    import capo_workspaces_instances.types.license_specifications
    import capo_workspaces_instances.types.network_interfaces
    import capo_workspaces_instances.types.non_negative_integer
    import capo_workspaces_instances.types.placement
    import capo_workspaces_instances.types.private_dns_name_options_request
    import capo_workspaces_instances.types.run_instances_monitoring_enabled
    import capo_workspaces_instances.types.security_group_ids
    import capo_workspaces_instances.types.security_group_names
    import capo_workspaces_instances.types.string64
    import capo_workspaces_instances.types.string128
    import capo_workspaces_instances.types.subnet_id
    import capo_workspaces_instances.types.tag_specifications
    import capo_workspaces_instances.types.user_data


class ManagedInstanceRequest(TypedDict, closed=True):
    block_device_mappings: NotRequired[
        "capo_workspaces_instances.types.block_device_mappings.BlockDeviceMappings"
    ]
    """<p>Configures block device mappings for storage.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_workspaces_instances.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>Specifies capacity reservation preferences.</p>"""
    cpu_options: NotRequired[
        "capo_workspaces_instances.types.cpu_options_request.CpuOptionsRequest"
    ]
    """<p>Configures CPU-specific settings.</p>"""
    credit_specification: NotRequired[
        "capo_workspaces_instances.types.credit_specification_request.CreditSpecificationRequest"
    ]
    """<p>Defines CPU credit configuration for burstable instances.</p>"""
    disable_api_stop: NotRequired["bool"]
    """<p>Prevents API-initiated instance stop.</p>"""
    ebs_optimized: NotRequired["bool"]
    """<p>Enables optimized EBS performance.</p>"""
    enable_primary_ipv6: NotRequired["bool"]
    """<p>Enables primary IPv6 address configuration.</p>"""
    enclave_options: NotRequired[
        "capo_workspaces_instances.types.enclave_options_request.EnclaveOptionsRequest"
    ]
    """<p>Configures AWS Nitro Enclave settings.</p>"""
    hibernation_options: NotRequired[
        "capo_workspaces_instances.types.hibernation_options_request.HibernationOptionsRequest"
    ]
    """<p>Configures instance hibernation capabilities.</p>"""
    iam_instance_profile: NotRequired[
        "capo_workspaces_instances.types.iam_instance_profile_specification.IamInstanceProfileSpecification"
    ]
    """<p>Specifies IAM instance profile configuration.</p>"""
    image_id: NotRequired["capo_workspaces_instances.types.image_id.ImageId"]
    """<p>Identifies the Amazon Machine Image (AMI) for the instance.</p>"""
    instance_market_options: NotRequired[
        "capo_workspaces_instances.types.instance_market_options_request.InstanceMarketOptionsRequest"
    ]
    """<p>Configures marketplace-specific deployment options.</p>"""
    instance_type: NotRequired[
        "capo_workspaces_instances.types.instance_type.InstanceType"
    ]
    """<p>Specifies the WorkSpace Instance type.</p>"""
    ipv6_addresses: NotRequired[
        "capo_workspaces_instances.types.ipv6_addresses.Ipv6Addresses"
    ]
    """<p>Configures specific IPv6 addresses.</p>"""
    ipv6_address_count: NotRequired[
        "capo_workspaces_instances.types.non_negative_integer.NonNegativeInteger"
    ]
    """<p>Specifies number of IPv6 addresses to assign.</p>"""
    kernel_id: NotRequired["capo_workspaces_instances.types.string128.String128"]
    """<p>Identifies the kernel for the instance.</p>"""
    key_name: NotRequired["capo_workspaces_instances.types.string64.String64"]
    """<p>Specifies the key pair for instance access.</p>"""
    license_specifications: NotRequired[
        "capo_workspaces_instances.types.license_specifications.LicenseSpecifications"
    ]
    """<p>Configures license-related settings.</p>"""
    maintenance_options: NotRequired[
        "capo_workspaces_instances.types.instance_maintenance_options_request.InstanceMaintenanceOptionsRequest"
    ]
    """<p>Defines automatic maintenance settings.</p>"""
    metadata_options: NotRequired[
        "capo_workspaces_instances.types.instance_metadata_options_request.InstanceMetadataOptionsRequest"
    ]
    """<p>Configures instance metadata service settings.</p>"""
    monitoring: NotRequired[
        "capo_workspaces_instances.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"
    ]
    """<p>Enables or disables detailed instance monitoring.</p>"""
    network_interfaces: NotRequired[
        "capo_workspaces_instances.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>Configures network interface settings.</p>"""
    network_performance_options: NotRequired[
        "capo_workspaces_instances.types.instance_network_performance_options_request.InstanceNetworkPerformanceOptionsRequest"
    ]
    """<p>Defines network performance configuration.</p>"""
    placement: NotRequired["capo_workspaces_instances.types.placement.Placement"]
    """<p>Specifies instance placement preferences.</p>"""
    private_dns_name_options: NotRequired[
        "capo_workspaces_instances.types.private_dns_name_options_request.PrivateDnsNameOptionsRequest"
    ]
    """<p>Configures private DNS name settings.</p>"""
    private_ip_address: NotRequired[
        "capo_workspaces_instances.types.ipv4_address.Ipv4Address"
    ]
    """<p>Specifies the primary private IP address.</p>"""
    ramdisk_id: NotRequired["capo_workspaces_instances.types.string128.String128"]
    """<p>Identifies the ramdisk for the instance.</p>"""
    security_group_ids: NotRequired[
        "capo_workspaces_instances.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>Specifies security group identifiers.</p>"""
    security_groups: NotRequired[
        "capo_workspaces_instances.types.security_group_names.SecurityGroupNames"
    ]
    """<p>Configures security group settings.</p>"""
    subnet_id: NotRequired["capo_workspaces_instances.types.subnet_id.SubnetId"]
    """<p>Identifies the subnet for the instance.</p>"""
    tag_specifications: NotRequired[
        "capo_workspaces_instances.types.tag_specifications.TagSpecifications"
    ]
    """<p>Configures resource tagging specifications.</p>"""
    user_data: NotRequired["capo_workspaces_instances.types.user_data.UserData"]
    """<p>Provides custom initialization data for the instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedInstanceRequest) -> dict:
    out: dict = {}
    if "block_device_mappings" in value:
        import capo_workspaces_instances.types.block_device_mappings

        out["BlockDeviceMappings"] = (
            capo_workspaces_instances.types.block_device_mappings.serialize_aws_json_1_0(
                value["block_device_mappings"]
            )
        )
    if "capacity_reservation_specification" in value:
        import capo_workspaces_instances.types.capacity_reservation_specification

        out["CapacityReservationSpecification"] = (
            capo_workspaces_instances.types.capacity_reservation_specification.serialize_aws_json_1_0(
                value["capacity_reservation_specification"]
            )
        )
    if "cpu_options" in value:
        import capo_workspaces_instances.types.cpu_options_request

        out["CpuOptions"] = (
            capo_workspaces_instances.types.cpu_options_request.serialize_aws_json_1_0(
                value["cpu_options"]
            )
        )
    if "credit_specification" in value:
        import capo_workspaces_instances.types.credit_specification_request

        out["CreditSpecification"] = (
            capo_workspaces_instances.types.credit_specification_request.serialize_aws_json_1_0(
                value["credit_specification"]
            )
        )
    if "disable_api_stop" in value:
        out["DisableApiStop"] = value["disable_api_stop"]
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "enable_primary_ipv6" in value:
        out["EnablePrimaryIpv6"] = value["enable_primary_ipv6"]
    if "enclave_options" in value:
        import capo_workspaces_instances.types.enclave_options_request

        out["EnclaveOptions"] = (
            capo_workspaces_instances.types.enclave_options_request.serialize_aws_json_1_0(
                value["enclave_options"]
            )
        )
    if "hibernation_options" in value:
        import capo_workspaces_instances.types.hibernation_options_request

        out["HibernationOptions"] = (
            capo_workspaces_instances.types.hibernation_options_request.serialize_aws_json_1_0(
                value["hibernation_options"]
            )
        )
    if "iam_instance_profile" in value:
        import capo_workspaces_instances.types.iam_instance_profile_specification

        out["IamInstanceProfile"] = (
            capo_workspaces_instances.types.iam_instance_profile_specification.serialize_aws_json_1_0(
                value["iam_instance_profile"]
            )
        )
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "instance_market_options" in value:
        import capo_workspaces_instances.types.instance_market_options_request

        out["InstanceMarketOptions"] = (
            capo_workspaces_instances.types.instance_market_options_request.serialize_aws_json_1_0(
                value["instance_market_options"]
            )
        )
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "ipv6_addresses" in value:
        import capo_workspaces_instances.types.ipv6_addresses

        out["Ipv6Addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.serialize_aws_json_1_0(
                value["ipv6_addresses"]
            )
        )
    if "ipv6_address_count" in value:
        out["Ipv6AddressCount"] = value["ipv6_address_count"]
    if "kernel_id" in value:
        out["KernelId"] = value["kernel_id"]
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "license_specifications" in value:
        import capo_workspaces_instances.types.license_specifications

        out["LicenseSpecifications"] = (
            capo_workspaces_instances.types.license_specifications.serialize_aws_json_1_0(
                value["license_specifications"]
            )
        )
    if "maintenance_options" in value:
        import capo_workspaces_instances.types.instance_maintenance_options_request

        out["MaintenanceOptions"] = (
            capo_workspaces_instances.types.instance_maintenance_options_request.serialize_aws_json_1_0(
                value["maintenance_options"]
            )
        )
    if "metadata_options" in value:
        import capo_workspaces_instances.types.instance_metadata_options_request

        out["MetadataOptions"] = (
            capo_workspaces_instances.types.instance_metadata_options_request.serialize_aws_json_1_0(
                value["metadata_options"]
            )
        )
    if "monitoring" in value:
        import capo_workspaces_instances.types.run_instances_monitoring_enabled

        out["Monitoring"] = (
            capo_workspaces_instances.types.run_instances_monitoring_enabled.serialize_aws_json_1_0(
                value["monitoring"]
            )
        )
    if "network_interfaces" in value:
        import capo_workspaces_instances.types.network_interfaces

        out["NetworkInterfaces"] = (
            capo_workspaces_instances.types.network_interfaces.serialize_aws_json_1_0(
                value["network_interfaces"]
            )
        )
    if "network_performance_options" in value:
        import capo_workspaces_instances.types.instance_network_performance_options_request

        out["NetworkPerformanceOptions"] = (
            capo_workspaces_instances.types.instance_network_performance_options_request.serialize_aws_json_1_0(
                value["network_performance_options"]
            )
        )
    if "placement" in value:
        import capo_workspaces_instances.types.placement

        out["Placement"] = (
            capo_workspaces_instances.types.placement.serialize_aws_json_1_0(
                value["placement"]
            )
        )
    if "private_dns_name_options" in value:
        import capo_workspaces_instances.types.private_dns_name_options_request

        out["PrivateDnsNameOptions"] = (
            capo_workspaces_instances.types.private_dns_name_options_request.serialize_aws_json_1_0(
                value["private_dns_name_options"]
            )
        )
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "ramdisk_id" in value:
        out["RamdiskId"] = value["ramdisk_id"]
    if "security_group_ids" in value:
        import capo_workspaces_instances.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_workspaces_instances.types.security_group_ids.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "security_groups" in value:
        import capo_workspaces_instances.types.security_group_names

        out["SecurityGroups"] = (
            capo_workspaces_instances.types.security_group_names.serialize_aws_json_1_0(
                value["security_groups"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "tag_specifications" in value:
        import capo_workspaces_instances.types.tag_specifications

        out["TagSpecifications"] = (
            capo_workspaces_instances.types.tag_specifications.serialize_aws_json_1_0(
                value["tag_specifications"]
            )
        )
    if "user_data" in value:
        out["UserData"] = value["user_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedInstanceRequest:
    out: ManagedInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("BlockDeviceMappings") is not None:
        import capo_workspaces_instances.types.block_device_mappings

        out["block_device_mappings"] = (
            capo_workspaces_instances.types.block_device_mappings.deserialize_aws_json_1_0(
                data["BlockDeviceMappings"]
            )
        )
    if data.get("CapacityReservationSpecification") is not None:
        import capo_workspaces_instances.types.capacity_reservation_specification

        out["capacity_reservation_specification"] = (
            capo_workspaces_instances.types.capacity_reservation_specification.deserialize_aws_json_1_0(
                data["CapacityReservationSpecification"]
            )
        )
    if data.get("CpuOptions") is not None:
        import capo_workspaces_instances.types.cpu_options_request

        out["cpu_options"] = (
            capo_workspaces_instances.types.cpu_options_request.deserialize_aws_json_1_0(
                data["CpuOptions"]
            )
        )
    if data.get("CreditSpecification") is not None:
        import capo_workspaces_instances.types.credit_specification_request

        out["credit_specification"] = (
            capo_workspaces_instances.types.credit_specification_request.deserialize_aws_json_1_0(
                data["CreditSpecification"]
            )
        )
    if data.get("DisableApiStop") is not None:
        out["disable_api_stop"] = data["DisableApiStop"]
    if data.get("EbsOptimized") is not None:
        out["ebs_optimized"] = data["EbsOptimized"]
    if data.get("EnablePrimaryIpv6") is not None:
        out["enable_primary_ipv6"] = data["EnablePrimaryIpv6"]
    if data.get("EnclaveOptions") is not None:
        import capo_workspaces_instances.types.enclave_options_request

        out["enclave_options"] = (
            capo_workspaces_instances.types.enclave_options_request.deserialize_aws_json_1_0(
                data["EnclaveOptions"]
            )
        )
    if data.get("HibernationOptions") is not None:
        import capo_workspaces_instances.types.hibernation_options_request

        out["hibernation_options"] = (
            capo_workspaces_instances.types.hibernation_options_request.deserialize_aws_json_1_0(
                data["HibernationOptions"]
            )
        )
    if data.get("IamInstanceProfile") is not None:
        import capo_workspaces_instances.types.iam_instance_profile_specification

        out["iam_instance_profile"] = (
            capo_workspaces_instances.types.iam_instance_profile_specification.deserialize_aws_json_1_0(
                data["IamInstanceProfile"]
            )
        )
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("InstanceMarketOptions") is not None:
        import capo_workspaces_instances.types.instance_market_options_request

        out["instance_market_options"] = (
            capo_workspaces_instances.types.instance_market_options_request.deserialize_aws_json_1_0(
                data["InstanceMarketOptions"]
            )
        )
    if data.get("InstanceType") is not None:
        out["instance_type"] = data["InstanceType"]
    if data.get("Ipv6Addresses") is not None:
        import capo_workspaces_instances.types.ipv6_addresses

        out["ipv6_addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.deserialize_aws_json_1_0(
                data["Ipv6Addresses"]
            )
        )
    if data.get("Ipv6AddressCount") is not None:
        out["ipv6_address_count"] = data["Ipv6AddressCount"]
    if data.get("KernelId") is not None:
        out["kernel_id"] = data["KernelId"]
    if data.get("KeyName") is not None:
        out["key_name"] = data["KeyName"]
    if data.get("LicenseSpecifications") is not None:
        import capo_workspaces_instances.types.license_specifications

        out["license_specifications"] = (
            capo_workspaces_instances.types.license_specifications.deserialize_aws_json_1_0(
                data["LicenseSpecifications"]
            )
        )
    if data.get("MaintenanceOptions") is not None:
        import capo_workspaces_instances.types.instance_maintenance_options_request

        out["maintenance_options"] = (
            capo_workspaces_instances.types.instance_maintenance_options_request.deserialize_aws_json_1_0(
                data["MaintenanceOptions"]
            )
        )
    if data.get("MetadataOptions") is not None:
        import capo_workspaces_instances.types.instance_metadata_options_request

        out["metadata_options"] = (
            capo_workspaces_instances.types.instance_metadata_options_request.deserialize_aws_json_1_0(
                data["MetadataOptions"]
            )
        )
    if data.get("Monitoring") is not None:
        import capo_workspaces_instances.types.run_instances_monitoring_enabled

        out["monitoring"] = (
            capo_workspaces_instances.types.run_instances_monitoring_enabled.deserialize_aws_json_1_0(
                data["Monitoring"]
            )
        )
    if data.get("NetworkInterfaces") is not None:
        import capo_workspaces_instances.types.network_interfaces

        out["network_interfaces"] = (
            capo_workspaces_instances.types.network_interfaces.deserialize_aws_json_1_0(
                data["NetworkInterfaces"]
            )
        )
    if data.get("NetworkPerformanceOptions") is not None:
        import capo_workspaces_instances.types.instance_network_performance_options_request

        out["network_performance_options"] = (
            capo_workspaces_instances.types.instance_network_performance_options_request.deserialize_aws_json_1_0(
                data["NetworkPerformanceOptions"]
            )
        )
    if data.get("Placement") is not None:
        import capo_workspaces_instances.types.placement

        out["placement"] = (
            capo_workspaces_instances.types.placement.deserialize_aws_json_1_0(
                data["Placement"]
            )
        )
    if data.get("PrivateDnsNameOptions") is not None:
        import capo_workspaces_instances.types.private_dns_name_options_request

        out["private_dns_name_options"] = (
            capo_workspaces_instances.types.private_dns_name_options_request.deserialize_aws_json_1_0(
                data["PrivateDnsNameOptions"]
            )
        )
    if data.get("PrivateIpAddress") is not None:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if data.get("RamdiskId") is not None:
        out["ramdisk_id"] = data["RamdiskId"]
    if data.get("SecurityGroupIds") is not None:
        import capo_workspaces_instances.types.security_group_ids

        out["security_group_ids"] = (
            capo_workspaces_instances.types.security_group_ids.deserialize_aws_json_1_0(
                data["SecurityGroupIds"]
            )
        )
    if data.get("SecurityGroups") is not None:
        import capo_workspaces_instances.types.security_group_names

        out["security_groups"] = (
            capo_workspaces_instances.types.security_group_names.deserialize_aws_json_1_0(
                data["SecurityGroups"]
            )
        )
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("TagSpecifications") is not None:
        import capo_workspaces_instances.types.tag_specifications

        out["tag_specifications"] = (
            capo_workspaces_instances.types.tag_specifications.deserialize_aws_json_1_0(
                data["TagSpecifications"]
            )
        )
    if data.get("UserData") is not None:
        out["user_data"] = data["UserData"]
    return out


def redact_sensitive(value: ManagedInstanceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "block_device_mappings" in value:
        import capo_workspaces_instances.types.block_device_mappings

        out["block_device_mappings"] = (
            capo_workspaces_instances.types.block_device_mappings.redact_sensitive(
                value["block_device_mappings"]
            )
        )
    if "ipv6_addresses" in value:
        import capo_workspaces_instances.types.ipv6_addresses

        out["ipv6_addresses"] = (
            capo_workspaces_instances.types.ipv6_addresses.redact_sensitive(
                value["ipv6_addresses"]
            )
        )
    if "network_interfaces" in value:
        import capo_workspaces_instances.types.network_interfaces

        out["network_interfaces"] = (
            capo_workspaces_instances.types.network_interfaces.redact_sensitive(
                value["network_interfaces"]
            )
        )
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    if "user_data" in value:
        out["user_data"] = "*** Sensitive Data Redacted ***"
    return out
