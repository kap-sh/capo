"""Generated from Smithy shape ``com.amazonaws.backupgateway#VirtualMachineDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.path
    import capo_backup_gateway.types.resource_arn
    import capo_backup_gateway.types.string
    import capo_backup_gateway.types.time
    import capo_backup_gateway.types.vmware_tags


class VirtualMachineDetails(TypedDict, closed=True):
    host_name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The host name of the virtual machine.</p>"""
    hypervisor_id: NotRequired["capo_backup_gateway.types.string.string"]
    """<p>The ID of the virtual machine's hypervisor.</p>"""
    name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The name of the virtual machine.</p>"""
    path: NotRequired["capo_backup_gateway.types.path.Path"]
    """<p>The path of the virtual machine.</p>"""
    resource_arn: NotRequired["capo_backup_gateway.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the virtual machine. For example, <code>arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL</code>.</p>"""
    last_backup_date: NotRequired["capo_backup_gateway.types.time.Time"]
    """<p>The most recent date a virtual machine was backed up, in Unix format and UTC time.</p>"""
    vmware_tags: NotRequired["capo_backup_gateway.types.vmware_tags.VmwareTags"]
    """<p>These are the details of the VMware tags associated with the specified virtual machine.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VirtualMachineDetails) -> dict:
    out: dict = {}
    if "host_name" in value:
        out["HostName"] = value["host_name"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "last_backup_date" in value:
        import capo_backup_gateway.types.time

        out["LastBackupDate"] = capo_backup_gateway.types.time.serialize_aws_json_1_0(
            value["last_backup_date"]
        )
    if "vmware_tags" in value:
        import capo_backup_gateway.types.vmware_tags

        out["VmwareTags"] = (
            capo_backup_gateway.types.vmware_tags.serialize_aws_json_1_0(
                value["vmware_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VirtualMachineDetails:
    out: VirtualMachineDetails = {}  # type: ignore[typeddict-item]
    if data.get("HostName") is not None:
        out["host_name"] = data["HostName"]
    if data.get("HypervisorId") is not None:
        out["hypervisor_id"] = data["HypervisorId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("LastBackupDate") is not None:
        import capo_backup_gateway.types.time

        out["last_backup_date"] = (
            capo_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["LastBackupDate"]
            )
        )
    if data.get("VmwareTags") is not None:
        import capo_backup_gateway.types.vmware_tags

        out["vmware_tags"] = (
            capo_backup_gateway.types.vmware_tags.deserialize_aws_json_1_0(
                data["VmwareTags"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VirtualMachineDetails) -> dict:
    out: dict = {}
    if "host_name" in value:
        out["HostName"] = value["host_name"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "path" in value:
        out["Path"] = value["path"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "last_backup_date" in value:
        import capo_backup_gateway.types.time

        out["LastBackupDate"] = capo_backup_gateway.types.time.serialize_cbor(
            value["last_backup_date"]
        )
    if "vmware_tags" in value:
        import capo_backup_gateway.types.vmware_tags

        out["VmwareTags"] = capo_backup_gateway.types.vmware_tags.serialize_cbor(
            value["vmware_tags"]
        )
    return out


def deserialize_cbor(data: dict) -> VirtualMachineDetails:
    out: VirtualMachineDetails = {}  # type: ignore[typeddict-item]
    if data.get("HostName") is not None:
        out["host_name"] = data["HostName"]
    if data.get("HypervisorId") is not None:
        out["hypervisor_id"] = data["HypervisorId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("LastBackupDate") is not None:
        import capo_backup_gateway.types.time

        out["last_backup_date"] = capo_backup_gateway.types.time.deserialize_cbor(
            data["LastBackupDate"]
        )
    if data.get("VmwareTags") is not None:
        import capo_backup_gateway.types.vmware_tags

        out["vmware_tags"] = capo_backup_gateway.types.vmware_tags.deserialize_cbor(
            data["VmwareTags"]
        )
    return out
