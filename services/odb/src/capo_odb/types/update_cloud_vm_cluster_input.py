"""Generated from Smithy shape ``com.amazonaws.odb#UpdateCloudVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.data_collection_options
    import capo_odb.types.license_model
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id
    import capo_odb.types.string_list


class UpdateCloudVmClusterInput(TypedDict, closed=True):
    cloud_vm_cluster_id: "capo_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster to update.</p>"""
    cpu_core_count: NotRequired["int"]
    """<p>The number of CPU cores to enable on the VM cluster. If you don't specify a value, the existing number of CPU cores is retained.</p>"""
    data_collection_options: NotRequired[
        "capo_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of preferences for the diagnostic collection options for the VM cluster.</p>"""
    data_storage_size_in_t_bs: NotRequired["float"]
    """<p>The size of the data disk group, in terabytes (TB), to allocate for the VM cluster.</p>"""
    db_node_storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), to allocate for the VM cluster.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new user-friendly name for the VM cluster.</p>"""
    ssh_public_keys: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The public key portion of one or more key pairs used for SSH access to the VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the VM cluster.</p>"""
    memory_size_in_g_bs: NotRequired["int"]
    """<p>The amount of memory, in gigabytes (GB), to allocate for the VM cluster.</p>"""
    storage_size_in_g_bs: NotRequired["int"]
    """<p>The amount of local node storage, in gigabytes (GB), to allocate to the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateCloudVmClusterInput) -> dict:
    out: dict = {}
    out["cloudVmClusterId"] = value["cloud_vm_cluster_id"]
    if "cpu_core_count" in value:
        out["cpuCoreCount"] = value["cpu_core_count"]
    if "data_collection_options" in value:
        import capo_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            capo_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
        )
    if "data_storage_size_in_t_bs" in value:
        out["dataStorageSizeInTBs"] = (
            "NaN"
            if value["data_storage_size_in_t_bs"] != value["data_storage_size_in_t_bs"]
            else "Infinity"
            if value["data_storage_size_in_t_bs"] == float("inf")
            else "-Infinity"
            if value["data_storage_size_in_t_bs"] == float("-inf")
            else value["data_storage_size_in_t_bs"]
        )
    if "db_node_storage_size_in_g_bs" in value:
        out["dbNodeStorageSizeInGBs"] = value["db_node_storage_size_in_g_bs"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "ssh_public_keys" in value:
        import capo_odb.types.string_list

        out["sshPublicKeys"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["ssh_public_keys"]
        )
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "memory_size_in_g_bs" in value:
        out["memorySizeInGBs"] = value["memory_size_in_g_bs"]
    if "storage_size_in_g_bs" in value:
        out["storageSizeInGBs"] = value["storage_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateCloudVmClusterInput:
    out: UpdateCloudVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("cloudVmClusterId") is not None:
        out["cloud_vm_cluster_id"] = data["cloudVmClusterId"]
    else:
        out["cloud_vm_cluster_id"] = ""
    if data.get("cpuCoreCount") is not None:
        out["cpu_core_count"] = data["cpuCoreCount"]
    if data.get("dataCollectionOptions") is not None:
        import capo_odb.types.data_collection_options

        out["data_collection_options"] = (
            capo_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if data.get("dataStorageSizeInTBs") is not None:
        out["data_storage_size_in_t_bs"] = float(data["dataStorageSizeInTBs"])
    if data.get("dbNodeStorageSizeInGBs") is not None:
        out["db_node_storage_size_in_g_bs"] = data["dbNodeStorageSizeInGBs"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("sshPublicKeys") is not None:
        import capo_odb.types.string_list

        out["ssh_public_keys"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["sshPublicKeys"]
        )
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("memorySizeInGBs") is not None:
        out["memory_size_in_g_bs"] = data["memorySizeInGBs"]
    if data.get("storageSizeInGBs") is not None:
        out["storage_size_in_g_bs"] = data["storageSizeInGBs"]
    return out
