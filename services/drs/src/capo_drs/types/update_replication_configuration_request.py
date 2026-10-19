"""Generated from Smithy shape ``com.amazonaws.drs#UpdateReplicationConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.arn
    import capo_drs.types.ec2_instance_type
    import capo_drs.types.internet_protocol
    import capo_drs.types.pit_policy
    import capo_drs.types.positive_integer
    import capo_drs.types.replication_configuration_data_plane_routing
    import capo_drs.types.replication_configuration_default_large_staging_disk_type
    import capo_drs.types.replication_configuration_ebs_encryption
    import capo_drs.types.replication_configuration_replicated_disks
    import capo_drs.types.replication_servers_security_groups_i_ds
    import capo_drs.types.small_bounded_string
    import capo_drs.types.source_server_id
    import capo_drs.types.subnet_id
    import capo_drs.types.tags_map


class UpdateReplicationConfigurationRequest(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>The ID of the Source Server for this Replication Configuration.</p>"""
    name: NotRequired["capo_drs.types.small_bounded_string.SmallBoundedString"]
    """<p>The name of the Replication Configuration.</p>"""
    staging_area_subnet_id: NotRequired["capo_drs.types.subnet_id.SubnetID"]
    """<p>The subnet to be used by the replication staging area.</p>"""
    associate_default_security_group: NotRequired["bool"]
    """<p>Whether to associate the default Elastic Disaster Recovery Security group with the Replication Configuration.</p>"""
    replication_servers_security_groups_i_ds: NotRequired[
        "capo_drs.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    ]
    """<p>The security group IDs that will be used by the replication server.</p>"""
    replication_server_instance_type: NotRequired[
        "capo_drs.types.ec2_instance_type.EC2InstanceType"
    ]
    """<p>The instance type to be used for the replication server.</p>"""
    use_dedicated_replication_server: NotRequired["bool"]
    """<p>Whether to use a dedicated Replication Server in the replication staging area.</p>"""
    default_large_staging_disk_type: NotRequired[
        "capo_drs.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    ]
    """<p>The Staging Disk EBS volume type to be used during replication.</p>"""
    replicated_disks: NotRequired[
        "capo_drs.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
    ]
    """<p>The configuration of the disks of the Source Server to be replicated.</p>"""
    ebs_encryption: NotRequired[
        "capo_drs.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    ]
    """<p>The type of EBS encryption to be used during replication.</p>"""
    ebs_encryption_key_arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>The ARN of the EBS encryption key to be used during replication.</p>"""
    bandwidth_throttling: "capo_drs.types.positive_integer.PositiveInteger"
    """<p>Configure bandwidth throttling for the outbound data transfer rate of the Source Server in Mbps.</p>"""
    data_plane_routing: NotRequired[
        "capo_drs.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    ]
    """<p>The data plane routing mechanism that will be used for replication.</p>"""
    create_public_ip: NotRequired["bool"]
    """<p>Whether to create a Public IP for the Recovery Instance by default.</p>"""
    staging_area_tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A set of tags to be associated with all resources created in the replication staging area: EC2 replication server, EBS volumes, EBS snapshots, etc.</p>"""
    pit_policy: NotRequired["capo_drs.types.pit_policy.PITPolicy"]
    """<p>The Point in time (PIT) policy to manage snapshots taken during replication.</p>"""
    auto_replicate_new_disks: NotRequired["bool"]
    """<p>Whether to allow the AWS replication agent to automatically replicate newly added disks.</p>"""
    internet_protocol: NotRequired["capo_drs.types.internet_protocol.InternetProtocol"]
    """<p>Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReplicationConfigurationRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "staging_area_subnet_id" in value:
        out["stagingAreaSubnetId"] = value["staging_area_subnet_id"]
    if "associate_default_security_group" in value:
        out["associateDefaultSecurityGroup"] = value["associate_default_security_group"]
    if "replication_servers_security_groups_i_ds" in value:
        import capo_drs.types.replication_servers_security_groups_i_ds

        out["replicationServersSecurityGroupsIDs"] = (
            capo_drs.types.replication_servers_security_groups_i_ds.serialize_json(
                value["replication_servers_security_groups_i_ds"]
            )
        )
    if "replication_server_instance_type" in value:
        out["replicationServerInstanceType"] = value["replication_server_instance_type"]
    if "use_dedicated_replication_server" in value:
        out["useDedicatedReplicationServer"] = value["use_dedicated_replication_server"]
    if "default_large_staging_disk_type" in value:
        out["defaultLargeStagingDiskType"] = value["default_large_staging_disk_type"]
    if "replicated_disks" in value:
        import capo_drs.types.replication_configuration_replicated_disks

        out["replicatedDisks"] = (
            capo_drs.types.replication_configuration_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
    if "ebs_encryption" in value:
        out["ebsEncryption"] = value["ebs_encryption"]
    if "ebs_encryption_key_arn" in value:
        out["ebsEncryptionKeyArn"] = value["ebs_encryption_key_arn"]
    out["bandwidthThrottling"] = value.get("bandwidth_throttling", 0)
    if "data_plane_routing" in value:
        out["dataPlaneRouting"] = value["data_plane_routing"]
    if "create_public_ip" in value:
        out["createPublicIP"] = value["create_public_ip"]
    if "staging_area_tags" in value:
        import capo_drs.types.tags_map

        out["stagingAreaTags"] = capo_drs.types.tags_map.serialize_json(
            value["staging_area_tags"]
        )
    if "pit_policy" in value:
        import capo_drs.types.pit_policy

        out["pitPolicy"] = capo_drs.types.pit_policy.serialize_json(value["pit_policy"])
    if "auto_replicate_new_disks" in value:
        out["autoReplicateNewDisks"] = value["auto_replicate_new_disks"]
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
    return out


def deserialize_json(data: dict) -> UpdateReplicationConfigurationRequest:
    out: UpdateReplicationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("stagingAreaSubnetId") is not None:
        out["staging_area_subnet_id"] = data["stagingAreaSubnetId"]
    if data.get("associateDefaultSecurityGroup") is not None:
        out["associate_default_security_group"] = data["associateDefaultSecurityGroup"]
    if data.get("replicationServersSecurityGroupsIDs") is not None:
        import capo_drs.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            capo_drs.types.replication_servers_security_groups_i_ds.deserialize_json(
                data["replicationServersSecurityGroupsIDs"]
            )
        )
    if data.get("replicationServerInstanceType") is not None:
        out["replication_server_instance_type"] = data["replicationServerInstanceType"]
    if data.get("useDedicatedReplicationServer") is not None:
        out["use_dedicated_replication_server"] = data["useDedicatedReplicationServer"]
    if data.get("defaultLargeStagingDiskType") is not None:
        out["default_large_staging_disk_type"] = data["defaultLargeStagingDiskType"]
    if data.get("replicatedDisks") is not None:
        import capo_drs.types.replication_configuration_replicated_disks

        out["replicated_disks"] = (
            capo_drs.types.replication_configuration_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
    if data.get("ebsEncryption") is not None:
        out["ebs_encryption"] = data["ebsEncryption"]
    if data.get("ebsEncryptionKeyArn") is not None:
        out["ebs_encryption_key_arn"] = data["ebsEncryptionKeyArn"]
    if data.get("bandwidthThrottling") is not None:
        out["bandwidth_throttling"] = data["bandwidthThrottling"]
    else:
        out["bandwidth_throttling"] = 0
    if data.get("dataPlaneRouting") is not None:
        out["data_plane_routing"] = data["dataPlaneRouting"]
    if data.get("createPublicIP") is not None:
        out["create_public_ip"] = data["createPublicIP"]
    if data.get("stagingAreaTags") is not None:
        import capo_drs.types.tags_map

        out["staging_area_tags"] = capo_drs.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
        )
    if data.get("pitPolicy") is not None:
        import capo_drs.types.pit_policy

        out["pit_policy"] = capo_drs.types.pit_policy.deserialize_json(
            data["pitPolicy"]
        )
    if data.get("autoReplicateNewDisks") is not None:
        out["auto_replicate_new_disks"] = data["autoReplicateNewDisks"]
    if data.get("internetProtocol") is not None:
        out["internet_protocol"] = data["internetProtocol"]
    return out


def redact_sensitive(value: UpdateReplicationConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "staging_area_tags" in value:
        out["staging_area_tags"] = "*** Sensitive Data Redacted ***"
    return out
