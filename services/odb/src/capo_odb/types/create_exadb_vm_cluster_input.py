"""Generated from Smithy shape ``com.amazonaws.odb#CreateExadbVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cluster_name
    import capo_odb.types.data_collection_options
    import capo_odb.types.general_input_string
    import capo_odb.types.hostname
    import capo_odb.types.license_model
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.shape_attribute
    import capo_odb.types.string_list


class CreateExadbVmClusterInput(TypedDict, closed=True):
    display_name: "capo_odb.types.resource_display_name.ResourceDisplayName"
    """<p>A user-friendly name for the Exascale VM cluster.</p>"""
    enabled_ecpu_count: "int"
    """<p>The number of ECPUs to enable for the Exascale VM cluster.</p>"""
    exascale_db_storage_vault_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale storage vault for this Exascale VM cluster.</p>"""
    grid_image_id: "str"
    """<p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>"""
    hostname: "capo_odb.types.hostname.Hostname"
    """<p>The host name for the Exascale VM cluster.</p>"""
    node_count: "int"
    """<p>The number of nodes in the Exascale VM cluster.</p>"""
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network for the Exascale VM cluster.</p>"""
    shape: "str"
    """<p>The shape of the Exascale VM cluster.</p>"""
    ssh_public_keys: "capo_odb.types.string_list.StringList"
    """<p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>"""
    total_ecpu_count: "int"
    """<p>The total number of ECPUs for the Exascale VM cluster.</p>"""
    vm_file_system_storage_total_size_in_g_bs: "int"
    """<p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>"""
    cluster_name: NotRequired["capo_odb.types.cluster_name.ClusterName"]
    """<p>A name for the Grid Infrastructure cluster. The name isn't case sensitive.</p>"""
    data_collection_options: NotRequired[
        "capo_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Exascale VM cluster.</p>"""
    scan_listener_port_tcp: NotRequired["int"]
    """<p>The port number for TCP connections to the Single Client Access Name (SCAN) listener.</p>"""
    scan_listener_port_tcp_ssl: NotRequired["int"]
    """<p>Reserved for future use.</p>"""
    shape_attribute: NotRequired["capo_odb.types.shape_attribute.ShapeAttribute"]
    """<p>The shape attribute for the Exascale VM cluster.</p>"""
    system_version: NotRequired["str"]
    """<p>The version of the operating system of the image for the Exascale VM cluster.</p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the Exascale VM cluster.</p>"""
    time_zone: NotRequired["str"]
    """<p>The time zone for the Exascale VM cluster.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you submit the same request twice with the same client token, the service ignores the second request and returns the result of the first. If you don't specify a client token, the AWS SDK automatically generates one. The client token is valid for up to 24 hours after it's first used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateExadbVmClusterInput) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    out["enabledEcpuCount"] = value["enabled_ecpu_count"]
    out["exascaleDbStorageVaultId"] = value["exascale_db_storage_vault_id"]
    out["gridImageId"] = value["grid_image_id"]
    out["hostname"] = value["hostname"]
    out["nodeCount"] = value["node_count"]
    out["odbNetworkId"] = value["odb_network_id"]
    out["shape"] = value["shape"]
    import capo_odb.types.string_list

    out["sshPublicKeys"] = capo_odb.types.string_list.serialize_aws_json_1_0(
        value["ssh_public_keys"]
    )
    out["totalEcpuCount"] = value["total_ecpu_count"]
    out["vmFileSystemStorageTotalSizeInGBs"] = value[
        "vm_file_system_storage_total_size_in_g_bs"
    ]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "data_collection_options" in value:
        import capo_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            capo_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
        )
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "scan_listener_port_tcp" in value:
        out["scanListenerPortTcp"] = value["scan_listener_port_tcp"]
    if "scan_listener_port_tcp_ssl" in value:
        out["scanListenerPortTcpSsl"] = value["scan_listener_port_tcp_ssl"]
    if "shape_attribute" in value:
        import capo_odb.types.shape_attribute

        out["shapeAttribute"] = capo_odb.types.shape_attribute.serialize_aws_json_1_0(
            value["shape_attribute"]
        )
    if "system_version" in value:
        out["systemVersion"] = value["system_version"]
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "time_zone" in value:
        out["timeZone"] = value["time_zone"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateExadbVmClusterInput:
    out: CreateExadbVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("enabledEcpuCount") is not None:
        out["enabled_ecpu_count"] = data["enabledEcpuCount"]
    else:
        out["enabled_ecpu_count"] = 0
    if data.get("exascaleDbStorageVaultId") is not None:
        out["exascale_db_storage_vault_id"] = data["exascaleDbStorageVaultId"]
    else:
        out["exascale_db_storage_vault_id"] = ""
    if data.get("gridImageId") is not None:
        out["grid_image_id"] = data["gridImageId"]
    else:
        out["grid_image_id"] = ""
    if data.get("hostname") is not None:
        out["hostname"] = data["hostname"]
    else:
        out["hostname"] = ""
    if data.get("nodeCount") is not None:
        out["node_count"] = data["nodeCount"]
    else:
        out["node_count"] = 0
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    if data.get("shape") is not None:
        out["shape"] = data["shape"]
    else:
        out["shape"] = ""
    if data.get("sshPublicKeys") is not None:
        import capo_odb.types.string_list

        out["ssh_public_keys"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["sshPublicKeys"]
        )
    else:
        out["ssh_public_keys"] = []
    if data.get("totalEcpuCount") is not None:
        out["total_ecpu_count"] = data["totalEcpuCount"]
    else:
        out["total_ecpu_count"] = 0
    if data.get("vmFileSystemStorageTotalSizeInGBs") is not None:
        out["vm_file_system_storage_total_size_in_g_bs"] = data[
            "vmFileSystemStorageTotalSizeInGBs"
        ]
    else:
        out["vm_file_system_storage_total_size_in_g_bs"] = 0
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    if data.get("dataCollectionOptions") is not None:
        import capo_odb.types.data_collection_options

        out["data_collection_options"] = (
            capo_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("scanListenerPortTcp") is not None:
        out["scan_listener_port_tcp"] = data["scanListenerPortTcp"]
    if data.get("scanListenerPortTcpSsl") is not None:
        out["scan_listener_port_tcp_ssl"] = data["scanListenerPortTcpSsl"]
    if data.get("shapeAttribute") is not None:
        import capo_odb.types.shape_attribute

        out["shape_attribute"] = (
            capo_odb.types.shape_attribute.deserialize_aws_json_1_0(
                data["shapeAttribute"]
            )
        )
    if data.get("systemVersion") is not None:
        out["system_version"] = data["systemVersion"]
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("timeZone") is not None:
        out["time_zone"] = data["timeZone"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
