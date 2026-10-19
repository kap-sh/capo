"""Generated from Smithy shape ``com.amazonaws.odb#UpdateExadbVmClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.data_collection_options
    import capo_odb.types.license_model
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.string_list
    import capo_odb.types.update_action


class UpdateExadbVmClusterInput(TypedDict, closed=True):
    exadb_vm_cluster_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the Exascale VM cluster to update.</p>"""
    data_collection_options: NotRequired[
        "capo_odb.types.data_collection_options.DataCollectionOptions"
    ]
    """<p>The set of preferences for the various diagnostic collection options for the Exascale VM cluster.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>A new user-friendly name for the Exascale VM cluster.</p>"""
    enabled_ecpu_count: NotRequired["int"]
    """<p>The number of ECPUs to enable for the Exascale VM cluster.</p>"""
    grid_image_id: NotRequired["str"]
    """<p>The Grid Infrastructure software image ID for the Exascale VM cluster.</p>"""
    license_model: NotRequired["capo_odb.types.license_model.LicenseModel"]
    """<p>The Oracle license model to apply to the Exascale VM cluster.</p>"""
    ssh_public_keys: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The public key portion of one or more key pairs used for SSH access to the Exascale VM cluster.</p>"""
    system_version: NotRequired["str"]
    """<p>The version of the operating system of the image for the Exascale VM cluster.</p>"""
    total_ecpu_count: NotRequired["int"]
    """<p>The total number of ECPUs for the Exascale VM cluster.</p>"""
    update_action: NotRequired["capo_odb.types.update_action.UpdateAction"]
    """<p>The update action to perform on the Exascale VM cluster.</p>"""
    vm_file_system_storage_total_size_in_g_bs: NotRequired["int"]
    """<p>The total amount of file system storage, in gigabytes (GB), for the Exascale VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateExadbVmClusterInput) -> dict:
    out: dict = {}
    out["exadbVmClusterId"] = value["exadb_vm_cluster_id"]
    if "data_collection_options" in value:
        import capo_odb.types.data_collection_options

        out["dataCollectionOptions"] = (
            capo_odb.types.data_collection_options.serialize_aws_json_1_0(
                value["data_collection_options"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "enabled_ecpu_count" in value:
        out["enabledEcpuCount"] = value["enabled_ecpu_count"]
    if "grid_image_id" in value:
        out["gridImageId"] = value["grid_image_id"]
    if "license_model" in value:
        import capo_odb.types.license_model

        out["licenseModel"] = capo_odb.types.license_model.serialize_aws_json_1_0(
            value["license_model"]
        )
    if "ssh_public_keys" in value:
        import capo_odb.types.string_list

        out["sshPublicKeys"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["ssh_public_keys"]
        )
    if "system_version" in value:
        out["systemVersion"] = value["system_version"]
    if "total_ecpu_count" in value:
        out["totalEcpuCount"] = value["total_ecpu_count"]
    if "update_action" in value:
        import capo_odb.types.update_action

        out["updateAction"] = capo_odb.types.update_action.serialize_aws_json_1_0(
            value["update_action"]
        )
    if "vm_file_system_storage_total_size_in_g_bs" in value:
        out["vmFileSystemStorageTotalSizeInGBs"] = value[
            "vm_file_system_storage_total_size_in_g_bs"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateExadbVmClusterInput:
    out: UpdateExadbVmClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("exadbVmClusterId") is not None:
        out["exadb_vm_cluster_id"] = data["exadbVmClusterId"]
    else:
        out["exadb_vm_cluster_id"] = ""
    if data.get("dataCollectionOptions") is not None:
        import capo_odb.types.data_collection_options

        out["data_collection_options"] = (
            capo_odb.types.data_collection_options.deserialize_aws_json_1_0(
                data["dataCollectionOptions"]
            )
        )
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("enabledEcpuCount") is not None:
        out["enabled_ecpu_count"] = data["enabledEcpuCount"]
    if data.get("gridImageId") is not None:
        out["grid_image_id"] = data["gridImageId"]
    if data.get("licenseModel") is not None:
        import capo_odb.types.license_model

        out["license_model"] = capo_odb.types.license_model.deserialize_aws_json_1_0(
            data["licenseModel"]
        )
    if data.get("sshPublicKeys") is not None:
        import capo_odb.types.string_list

        out["ssh_public_keys"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["sshPublicKeys"]
        )
    if data.get("systemVersion") is not None:
        out["system_version"] = data["systemVersion"]
    if data.get("totalEcpuCount") is not None:
        out["total_ecpu_count"] = data["totalEcpuCount"]
    if data.get("updateAction") is not None:
        import capo_odb.types.update_action

        out["update_action"] = capo_odb.types.update_action.deserialize_aws_json_1_0(
            data["updateAction"]
        )
    if data.get("vmFileSystemStorageTotalSizeInGBs") is not None:
        out["vm_file_system_storage_total_size_in_g_bs"] = data[
            "vmFileSystemStorageTotalSizeInGBs"
        ]
    return out
