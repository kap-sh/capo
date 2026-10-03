"""Generated from Smithy shape ``com.amazonaws.fsx#CreateFileSystemOpenZFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.disk_iops_configuration
    import capo_fsx.types.flag
    import capo_fsx.types.ip_address_range
    import capo_fsx.types.ipv6_address_range
    import capo_fsx.types.megabytes_per_second
    import capo_fsx.types.open_zfs_create_root_volume_configuration
    import capo_fsx.types.open_zfs_deployment_type
    import capo_fsx.types.open_zfs_read_cache_configuration
    import capo_fsx.types.route_table_ids
    import capo_fsx.types.subnet_id
    import capo_fsx.types.weekly_time


class CreateFileSystemOpenZFSConfiguration(TypedDict, closed=True):
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    copy_tags_to_backups: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the file system should be copied to backups. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the file system are copied to all automatic and user-initiated backups where the user doesn't specify tags. If this value is <code>true</code>, and you specify one or more tags, only the specified tags are copied to backups. If you specify one or more tags when creating a user-initiated backup, no tags are copied from the file system, regardless of this value.</p>"""
    copy_tags_to_volumes: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>A Boolean value indicating whether tags for the file system should be copied to volumes. This value defaults to <code>false</code>. If it's set to <code>true</code>, all tags for the file system are copied to volumes where the user doesn't specify tags. If this value is <code>true</code>, and you specify one or more tags, only the specified tags are copied to volumes. If you specify one or more tags when creating the volume, no tags are copied from the file system, regardless of this value.</p>"""
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    deployment_type: NotRequired[
        "capo_fsx.types.open_zfs_deployment_type.OpenZFSDeploymentType"
    ]
    """<p>Specifies the file system deployment type. Valid values are the following:</p> <ul> <li> <p> <code>MULTI_AZ_1</code>- Creates file systems with high availability and durability by replicating your data and supporting failover across multiple Availability Zones in the same Amazon Web Services Region.</p> </li> <li> <p> <code>SINGLE_AZ_HA_2</code>- Creates file systems with high availability and throughput capacities of 160 - 10,240 MB/s using an NVMe L2ARC cache by deploying a primary and standby file system within the same Availability Zone.</p> </li> <li> <p> <code>SINGLE_AZ_HA_1</code>- Creates file systems with high availability and throughput capacities of 64 - 4,096 MB/s by deploying a primary and standby file system within the same Availability Zone.</p> </li> <li> <p> <code>SINGLE_AZ_2</code>- Creates file systems with throughput capacities of 160 - 10,240 MB/s using an NVMe L2ARC cache that automatically recover within a single Availability Zone.</p> </li> <li> <p> <code>SINGLE_AZ_1</code>- Creates file systems with throughput capacities of 64 - 4,096 MBs that automatically recover within a single Availability Zone.</p> </li> </ul> <p>For a list of which Amazon Web Services Regions each deployment type is available in, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/availability-durability.html#available-aws-regions">Deployment type availability</a>. For more information on the differences in performance between deployment types, see <a href="https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#zfs-fs-performance">File system performance</a> in the <i>Amazon FSx for OpenZFS User Guide</i>.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>Specifies the throughput of an Amazon FSx for OpenZFS file system, measured in megabytes per second (MBps). Valid values depend on the <code>DeploymentType</code> that you choose, as follows:</p> <ul> <li> <p>For <code>MULTI_AZ_1</code> and <code>SINGLE_AZ_2</code>, valid values are 160, 320, 640, 1280, 2560, 3840, 5120, 7680, or 10240 MBps.</p> </li> <li> <p>For <code>SINGLE_AZ_1</code>, valid values are 64, 128, 256, 512, 1024, 2048, 3072, or 4096 MBps.</p> </li> </ul> <p>You pay for additional throughput capacity that you provision.</p>"""
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    disk_iops_configuration: NotRequired[
        "capo_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    root_volume_configuration: NotRequired[
        "capo_fsx.types.open_zfs_create_root_volume_configuration.OpenZFSCreateRootVolumeConfiguration"
    ]
    """<p>The configuration Amazon FSx uses when creating the root value of the Amazon FSx for OpenZFS file system. All volumes are children of the root volume. </p>"""
    preferred_subnet_id: NotRequired["capo_fsx.types.subnet_id.SubnetId"]
    """<p>Required when <code>DeploymentType</code> is set to <code>MULTI_AZ_1</code>. This specifies the subnet in which you want the preferred file server to be located.</p>"""
    endpoint_ip_address_range: NotRequired[
        "capo_fsx.types.ip_address_range.IpAddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv4 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /28 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""
    endpoint_ipv6_address_range: NotRequired[
        "capo_fsx.types.ipv6_address_range.Ipv6AddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""
    route_table_ids: NotRequired["capo_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) Specifies the route tables in which Amazon FSx creates the rules for routing traffic to the correct file server. You should specify all virtual private cloud (VPC) route tables associated with the subnets in which your clients are located. By default, Amazon FSx selects your VPC's default route table.</p>"""
    read_cache_configuration: NotRequired[
        "capo_fsx.types.open_zfs_read_cache_configuration.OpenZFSReadCacheConfiguration"
    ]
    """<p> Specifies the optional provisioned SSD read cache on file systems that use the Intelligent-Tiering storage class. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFileSystemOpenZFSConfiguration) -> dict:
    out: dict = {}
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "copy_tags_to_backups" in value:
        out["CopyTagsToBackups"] = value["copy_tags_to_backups"]
    if "copy_tags_to_volumes" in value:
        out["CopyTagsToVolumes"] = value["copy_tags_to_volumes"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "deployment_type" in value:
        import capo_fsx.types.open_zfs_deployment_type

        out["DeploymentType"] = (
            capo_fsx.types.open_zfs_deployment_type.serialize_aws_json_1_1(
                value["deployment_type"]
            )
        )
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "disk_iops_configuration" in value:
        import capo_fsx.types.disk_iops_configuration

        out["DiskIopsConfiguration"] = (
            capo_fsx.types.disk_iops_configuration.serialize_aws_json_1_1(
                value["disk_iops_configuration"]
            )
        )
    if "root_volume_configuration" in value:
        import capo_fsx.types.open_zfs_create_root_volume_configuration

        out["RootVolumeConfiguration"] = (
            capo_fsx.types.open_zfs_create_root_volume_configuration.serialize_aws_json_1_1(
                value["root_volume_configuration"]
            )
        )
    if "preferred_subnet_id" in value:
        out["PreferredSubnetId"] = value["preferred_subnet_id"]
    if "endpoint_ip_address_range" in value:
        out["EndpointIpAddressRange"] = value["endpoint_ip_address_range"]
    if "endpoint_ipv6_address_range" in value:
        out["EndpointIpv6AddressRange"] = value["endpoint_ipv6_address_range"]
    if "route_table_ids" in value:
        import capo_fsx.types.route_table_ids

        out["RouteTableIds"] = capo_fsx.types.route_table_ids.serialize_aws_json_1_1(
            value["route_table_ids"]
        )
    if "read_cache_configuration" in value:
        import capo_fsx.types.open_zfs_read_cache_configuration

        out["ReadCacheConfiguration"] = (
            capo_fsx.types.open_zfs_read_cache_configuration.serialize_aws_json_1_1(
                value["read_cache_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFileSystemOpenZFSConfiguration:
    out: CreateFileSystemOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("CopyTagsToBackups") is not None:
        out["copy_tags_to_backups"] = data["CopyTagsToBackups"]
    if data.get("CopyTagsToVolumes") is not None:
        out["copy_tags_to_volumes"] = data["CopyTagsToVolumes"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("DeploymentType") is not None:
        import capo_fsx.types.open_zfs_deployment_type

        out["deployment_type"] = (
            capo_fsx.types.open_zfs_deployment_type.deserialize_aws_json_1_1(
                data["DeploymentType"]
            )
        )
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DiskIopsConfiguration") is not None:
        import capo_fsx.types.disk_iops_configuration

        out["disk_iops_configuration"] = (
            capo_fsx.types.disk_iops_configuration.deserialize_aws_json_1_1(
                data["DiskIopsConfiguration"]
            )
        )
    if data.get("RootVolumeConfiguration") is not None:
        import capo_fsx.types.open_zfs_create_root_volume_configuration

        out["root_volume_configuration"] = (
            capo_fsx.types.open_zfs_create_root_volume_configuration.deserialize_aws_json_1_1(
                data["RootVolumeConfiguration"]
            )
        )
    if data.get("PreferredSubnetId") is not None:
        out["preferred_subnet_id"] = data["PreferredSubnetId"]
    if data.get("EndpointIpAddressRange") is not None:
        out["endpoint_ip_address_range"] = data["EndpointIpAddressRange"]
    if data.get("EndpointIpv6AddressRange") is not None:
        out["endpoint_ipv6_address_range"] = data["EndpointIpv6AddressRange"]
    if data.get("RouteTableIds") is not None:
        import capo_fsx.types.route_table_ids

        out["route_table_ids"] = (
            capo_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["RouteTableIds"]
            )
        )
    if data.get("ReadCacheConfiguration") is not None:
        import capo_fsx.types.open_zfs_read_cache_configuration

        out["read_cache_configuration"] = (
            capo_fsx.types.open_zfs_read_cache_configuration.deserialize_aws_json_1_1(
                data["ReadCacheConfiguration"]
            )
        )
    return out
