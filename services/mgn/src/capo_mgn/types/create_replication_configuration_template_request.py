"""Generated from Smithy shape ``com.amazonaws.mgn#CreateReplicationConfigurationTemplateRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.arn
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.storage_configuration
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tags_map


class CreateReplicationConfigurationTemplateRequest(TypedDict, closed=True):
    staging_area_subnet_id: "capo_mgn.types.subnet_id.SubnetID"
    """<p>Request to configure the Staging Area subnet ID during Replication Settings template creation.</p>"""
    associate_default_security_group: "bool"
    """<p>Request to associate the default Application Migration Service Security group with the Replication Settings template.</p>"""
    replication_servers_security_groups_i_ds: "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
    """<p>Request to configure the Replication Server Security group ID during Replication Settings template creation.</p>"""
    replication_server_instance_type: "capo_mgn.types.ec2_instance_type.EC2InstanceType"
    """<p>Request to configure the Replication Server instance type during Replication Settings template creation.</p>"""
    use_dedicated_replication_server: "bool"
    """<p>Request to use Dedicated Replication Servers during Replication Settings template creation.</p>"""
    default_large_staging_disk_type: "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
    """<p>Request to configure the default large staging disk EBS volume type during Replication Settings template creation.</p>"""
    ebs_encryption: "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
    """<p>Request to configure EBS encryption during Replication Settings template creation.</p>"""
    ebs_encryption_key_arn: NotRequired["capo_mgn.types.arn.ARN"]
    """<p>Request to configure an EBS encryption key during Replication Settings template creation.</p>"""
    bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
    """<p>Request to configure bandwidth throttling during Replication Settings template creation.</p>"""
    data_plane_routing: "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
    """<p>Request to configure data plane routing during Replication Settings template creation.</p>"""
    create_public_ip: "bool"
    """<p>Request to create Public IP during Replication Settings template creation.</p>"""
    staging_area_tags: "capo_mgn.types.tags_map.TagsMap"
    """<p>Request to configure Staging Area tags during Replication Settings template creation.</p>"""
    use_fips_endpoint: NotRequired["bool"]
    """<p>Request to use Fips Endpoint during Replication Settings template creation.</p>"""
    tags: NotRequired["capo_mgn.types.tags_map.TagsMap"]
    """<p>Request to configure tags during Replication Settings template creation.</p>"""
    internet_protocol: NotRequired["capo_mgn.types.internet_protocol.InternetProtocol"]
    """<p>Request to configure the internet protocol to IPv4 or IPv6.</p>"""
    store_snapshot_on_local_zone: NotRequired["bool"]
    """<p>Request to store snapshot on local zone during Replication Settings template creation.</p>"""
    storage_configuration: NotRequired[
        "capo_mgn.types.storage_configuration.StorageConfiguration"
    ]
    """<p>Request to configure storage during Replication Settings template creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationConfigurationTemplateRequest) -> dict:
    out: dict = {}
    out["stagingAreaSubnetId"] = value["staging_area_subnet_id"]
    out["associateDefaultSecurityGroup"] = value["associate_default_security_group"]
    import capo_mgn.types.replication_servers_security_groups_i_ds

    out["replicationServersSecurityGroupsIDs"] = (
        capo_mgn.types.replication_servers_security_groups_i_ds.serialize_json(
            value["replication_servers_security_groups_i_ds"]
        )
    )
    out["replicationServerInstanceType"] = value["replication_server_instance_type"]
    out["useDedicatedReplicationServer"] = value["use_dedicated_replication_server"]
    out["defaultLargeStagingDiskType"] = value["default_large_staging_disk_type"]
    out["ebsEncryption"] = value["ebs_encryption"]
    if "ebs_encryption_key_arn" in value:
        out["ebsEncryptionKeyArn"] = value["ebs_encryption_key_arn"]
    out["bandwidthThrottling"] = value.get("bandwidth_throttling", 0)
    out["dataPlaneRouting"] = value["data_plane_routing"]
    out["createPublicIP"] = value["create_public_ip"]
    import capo_mgn.types.tags_map

    out["stagingAreaTags"] = capo_mgn.types.tags_map.serialize_json(
        value["staging_area_tags"]
    )
    if "use_fips_endpoint" in value:
        out["useFipsEndpoint"] = value["use_fips_endpoint"]
    if "tags" in value:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.serialize_json(value["tags"])
    if "internet_protocol" in value:
        out["internetProtocol"] = value["internet_protocol"]
    if "store_snapshot_on_local_zone" in value:
        out["storeSnapshotOnLocalZone"] = value["store_snapshot_on_local_zone"]
    if "storage_configuration" in value:
        import capo_mgn.types.storage_configuration

        out["storageConfiguration"] = (
            capo_mgn.types.storage_configuration.serialize_json(
                value["storage_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateReplicationConfigurationTemplateRequest:
    out: CreateReplicationConfigurationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("stagingAreaSubnetId") is not None:
        out["staging_area_subnet_id"] = data["stagingAreaSubnetId"]
    else:
        out["staging_area_subnet_id"] = ""
    if data.get("associateDefaultSecurityGroup") is not None:
        out["associate_default_security_group"] = data["associateDefaultSecurityGroup"]
    else:
        out["associate_default_security_group"] = False
    if data.get("replicationServersSecurityGroupsIDs") is not None:
        import capo_mgn.types.replication_servers_security_groups_i_ds

        out["replication_servers_security_groups_i_ds"] = (
            capo_mgn.types.replication_servers_security_groups_i_ds.deserialize_json(
                data["replicationServersSecurityGroupsIDs"]
            )
        )
    else:
        out["replication_servers_security_groups_i_ds"] = []
    if data.get("replicationServerInstanceType") is not None:
        out["replication_server_instance_type"] = data["replicationServerInstanceType"]
    else:
        out["replication_server_instance_type"] = ""
    if data.get("useDedicatedReplicationServer") is not None:
        out["use_dedicated_replication_server"] = data["useDedicatedReplicationServer"]
    else:
        out["use_dedicated_replication_server"] = False
    if data.get("defaultLargeStagingDiskType") is not None:
        out["default_large_staging_disk_type"] = data["defaultLargeStagingDiskType"]
    else:
        out["default_large_staging_disk_type"] = ""
    if data.get("ebsEncryption") is not None:
        out["ebs_encryption"] = data["ebsEncryption"]
    else:
        out["ebs_encryption"] = ""
    if data.get("ebsEncryptionKeyArn") is not None:
        out["ebs_encryption_key_arn"] = data["ebsEncryptionKeyArn"]
    if data.get("bandwidthThrottling") is not None:
        out["bandwidth_throttling"] = data["bandwidthThrottling"]
    else:
        out["bandwidth_throttling"] = 0
    if data.get("dataPlaneRouting") is not None:
        out["data_plane_routing"] = data["dataPlaneRouting"]
    else:
        out["data_plane_routing"] = ""
    if data.get("createPublicIP") is not None:
        out["create_public_ip"] = data["createPublicIP"]
    else:
        out["create_public_ip"] = False
    if data.get("stagingAreaTags") is not None:
        import capo_mgn.types.tags_map

        out["staging_area_tags"] = capo_mgn.types.tags_map.deserialize_json(
            data["stagingAreaTags"]
        )
    else:
        out["staging_area_tags"] = {}
    if data.get("useFipsEndpoint") is not None:
        out["use_fips_endpoint"] = data["useFipsEndpoint"]
    if data.get("tags") is not None:
        import capo_mgn.types.tags_map

        out["tags"] = capo_mgn.types.tags_map.deserialize_json(data["tags"])
    if data.get("internetProtocol") is not None:
        out["internet_protocol"] = data["internetProtocol"]
    if data.get("storeSnapshotOnLocalZone") is not None:
        out["store_snapshot_on_local_zone"] = data["storeSnapshotOnLocalZone"]
    if data.get("storageConfiguration") is not None:
        import capo_mgn.types.storage_configuration

        out["storage_configuration"] = (
            capo_mgn.types.storage_configuration.deserialize_json(
                data["storageConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: CreateReplicationConfigurationTemplateRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "staging_area_tags" in value:
        out["staging_area_tags"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
