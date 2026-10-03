"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemOntapConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.admin_password
    import capo_fsx.types.automatic_backup_retention_days
    import capo_fsx.types.daily_time
    import capo_fsx.types.disk_iops_configuration
    import capo_fsx.types.ha_pairs
    import capo_fsx.types.ipv6_address_range
    import capo_fsx.types.megabytes_per_second
    import capo_fsx.types.route_table_ids
    import capo_fsx.types.throughput_capacity_per_ha_pair
    import capo_fsx.types.weekly_time


class UpdateFileSystemOntapConfiguration(TypedDict, closed=True):
    automatic_backup_retention_days: NotRequired[
        "capo_fsx.types.automatic_backup_retention_days.AutomaticBackupRetentionDays"
    ]
    daily_automatic_backup_start_time: NotRequired[
        "capo_fsx.types.daily_time.DailyTime"
    ]
    fsx_admin_password: NotRequired["capo_fsx.types.admin_password.AdminPassword"]
    """<p>Update the password for the <code>fsxadmin</code> user by entering a new password. You use the <code>fsxadmin</code> user to access the NetApp ONTAP CLI and REST API to manage your file system resources. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html">Managing resources using NetApp Application</a>.</p>"""
    weekly_maintenance_start_time: NotRequired["capo_fsx.types.weekly_time.WeeklyTime"]
    disk_iops_configuration: NotRequired[
        "capo_fsx.types.disk_iops_configuration.DiskIopsConfiguration"
    ]
    """<p>The SSD IOPS (input output operations per second) configuration for an Amazon FSx for NetApp ONTAP file system. The default is 3 IOPS per GB of storage capacity, but you can provision additional IOPS per GB of storage. The configuration consists of an IOPS mode (<code>AUTOMATIC</code> or <code>USER_PROVISIONED</code>), and in the case of <code>USER_PROVISIONED</code> IOPS, the total number of SSD IOPS provisioned. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/storage-capacity-and-IOPS.html">File system storage capacity and IOPS</a>.</p>"""
    throughput_capacity: NotRequired[
        "capo_fsx.types.megabytes_per_second.MegabytesPerSecond"
    ]
    """<p>Enter a new value to change the amount of throughput capacity for the file system in megabytes per second (MBps). For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-throughput-capacity.html">Managing throughput capacity</a> in the FSx for ONTAP User Guide.</p> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:</p> <ul> <li> <p>The value of <code>ThroughputCapacity</code> and <code>ThroughputCapacityPerHAPair</code> are not the same value.</p> </li> <li> <p>The value of <code>ThroughputCapacity</code> when divided by the value of <code>HAPairs</code> is outside of the valid range for <code>ThroughputCapacity</code>.</p> </li> </ul>"""
    add_route_table_ids: NotRequired["capo_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) A list of IDs of new virtual private cloud (VPC) route tables to associate (add) with your Amazon FSx for NetApp ONTAP file system.</p>"""
    remove_route_table_ids: NotRequired["capo_fsx.types.route_table_ids.RouteTableIds"]
    """<p>(Multi-AZ only) A list of IDs of existing virtual private cloud (VPC) route tables to disassociate (remove) from your Amazon FSx for NetApp ONTAP file system. You can use the API operation to retrieve the list of VPC route table IDs for a file system.</p>"""
    throughput_capacity_per_ha_pair: NotRequired[
        "capo_fsx.types.throughput_capacity_per_ha_pair.ThroughputCapacityPerHAPair"
    ]
    """<p>Use to choose the throughput capacity per HA pair, rather than the total throughput for the file system. </p> <p>This field and <code>ThroughputCapacity</code> cannot be defined in the same API call, but one is required.</p> <p>This field and <code>ThroughputCapacity</code> are the same for file systems with one HA pair.</p> <ul> <li> <p>For <code>SINGLE_AZ_1</code> and <code>MULTI_AZ_1</code> file systems, valid values are 128, 256, 512, 1024, 2048, or 4096 MBps.</p> </li> <li> <p>For <code>SINGLE_AZ_2</code>, valid values are 1536, 3072, or 6144 MBps.</p> </li> <li> <p>For <code>MULTI_AZ_2</code>, valid values are 384, 768, 1536, 3072, or 6144 MBps.</p> </li> </ul> <p>Amazon FSx responds with an HTTP status code 400 (Bad Request) for the following conditions:</p> <ul> <li> <p>The value of <code>ThroughputCapacity</code> and <code>ThroughputCapacityPerHAPair</code> are not the same value for file systems with one HA pair.</p> </li> <li> <p>The value of deployment type is <code>SINGLE_AZ_2</code> and <code>ThroughputCapacity</code> / <code>ThroughputCapacityPerHAPair</code> is not a valid HA pair (a value between 1 and 12).</p> </li> <li> <p>The value of <code>ThroughputCapacityPerHAPair</code> is not a valid value.</p> </li> </ul>"""
    ha_pairs: NotRequired["capo_fsx.types.ha_pairs.HAPairs"]
    """<p>Use to update the number of high-availability (HA) pairs for a second-generation single-AZ file system. If you increase the number of HA pairs for your file system, you must specify proportional increases for <code>StorageCapacity</code>, <code>Iops</code>, and <code>ThroughputCapacity</code>. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/administering-file-systems.html#HA-pairs">High-availability (HA) pairs</a> in the FSx for ONTAP user guide. Block storage protocol support (iSCSI and NVMe over TCP) is disabled on file systems with more than 6 HA pairs. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/supported-fsx-clients.html#using-block-storage">Using block storage protocols</a>.</p>"""
    endpoint_ipv6_address_range: NotRequired[
        "capo_fsx.types.ipv6_address_range.Ipv6AddressRange"
    ]
    """<p>(Multi-AZ only) Specifies the IPv6 address range in which the endpoints to access your file system will be created. By default in the Amazon FSx API and Amazon FSx console, Amazon FSx selects an available /118 IP address range for you from one of the VPC's CIDR ranges. You can have overlapping endpoint IP addresses for file systems deployed in the same VPC/route tables, as long as they don't overlap with any subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemOntapConfiguration) -> dict:
    out: dict = {}
    if "automatic_backup_retention_days" in value:
        out["AutomaticBackupRetentionDays"] = value["automatic_backup_retention_days"]
    if "daily_automatic_backup_start_time" in value:
        out["DailyAutomaticBackupStartTime"] = value[
            "daily_automatic_backup_start_time"
        ]
    if "fsx_admin_password" in value:
        out["FsxAdminPassword"] = value["fsx_admin_password"]
    if "weekly_maintenance_start_time" in value:
        out["WeeklyMaintenanceStartTime"] = value["weekly_maintenance_start_time"]
    if "disk_iops_configuration" in value:
        import capo_fsx.types.disk_iops_configuration

        out["DiskIopsConfiguration"] = (
            capo_fsx.types.disk_iops_configuration.serialize_aws_json_1_1(
                value["disk_iops_configuration"]
            )
        )
    if "throughput_capacity" in value:
        out["ThroughputCapacity"] = value["throughput_capacity"]
    if "add_route_table_ids" in value:
        import capo_fsx.types.route_table_ids

        out["AddRouteTableIds"] = capo_fsx.types.route_table_ids.serialize_aws_json_1_1(
            value["add_route_table_ids"]
        )
    if "remove_route_table_ids" in value:
        import capo_fsx.types.route_table_ids

        out["RemoveRouteTableIds"] = (
            capo_fsx.types.route_table_ids.serialize_aws_json_1_1(
                value["remove_route_table_ids"]
            )
        )
    if "throughput_capacity_per_ha_pair" in value:
        out["ThroughputCapacityPerHAPair"] = value["throughput_capacity_per_ha_pair"]
    if "ha_pairs" in value:
        out["HAPairs"] = value["ha_pairs"]
    if "endpoint_ipv6_address_range" in value:
        out["EndpointIpv6AddressRange"] = value["endpoint_ipv6_address_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemOntapConfiguration:
    out: UpdateFileSystemOntapConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AutomaticBackupRetentionDays") is not None:
        out["automatic_backup_retention_days"] = data["AutomaticBackupRetentionDays"]
    if data.get("DailyAutomaticBackupStartTime") is not None:
        out["daily_automatic_backup_start_time"] = data["DailyAutomaticBackupStartTime"]
    if data.get("FsxAdminPassword") is not None:
        out["fsx_admin_password"] = data["FsxAdminPassword"]
    if data.get("WeeklyMaintenanceStartTime") is not None:
        out["weekly_maintenance_start_time"] = data["WeeklyMaintenanceStartTime"]
    if data.get("DiskIopsConfiguration") is not None:
        import capo_fsx.types.disk_iops_configuration

        out["disk_iops_configuration"] = (
            capo_fsx.types.disk_iops_configuration.deserialize_aws_json_1_1(
                data["DiskIopsConfiguration"]
            )
        )
    if data.get("ThroughputCapacity") is not None:
        out["throughput_capacity"] = data["ThroughputCapacity"]
    if data.get("AddRouteTableIds") is not None:
        import capo_fsx.types.route_table_ids

        out["add_route_table_ids"] = (
            capo_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["AddRouteTableIds"]
            )
        )
    if data.get("RemoveRouteTableIds") is not None:
        import capo_fsx.types.route_table_ids

        out["remove_route_table_ids"] = (
            capo_fsx.types.route_table_ids.deserialize_aws_json_1_1(
                data["RemoveRouteTableIds"]
            )
        )
    if data.get("ThroughputCapacityPerHAPair") is not None:
        out["throughput_capacity_per_ha_pair"] = data["ThroughputCapacityPerHAPair"]
    if data.get("HAPairs") is not None:
        out["ha_pairs"] = data["HAPairs"]
    if data.get("EndpointIpv6AddressRange") is not None:
        out["endpoint_ipv6_address_range"] = data["EndpointIpv6AddressRange"]
    return out
