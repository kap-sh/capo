"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxOntapResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.fsx_filesystem_arn
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.storage_virtual_machine_arn
    import capo_datasync.types.time


class DescribeLocationFsxOntapResponse(TypedDict, closed=True):
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the location was created.</p>"""
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the FSx for ONTAP file system location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The uniform resource identifier (URI) of the FSx for ONTAP file system location.</p>"""
    protocol: NotRequired["capo_datasync.types.fsx_protocol.FsxProtocol"]
    security_group_arns: NotRequired[
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    ]
    """<p>The security groups that DataSync uses to access your FSx for ONTAP file system.</p>"""
    storage_virtual_machine_arn: NotRequired[
        "capo_datasync.types.storage_virtual_machine_arn.StorageVirtualMachineArn"
    ]
    """<p>The ARN of the storage virtual machine (SVM) on your FSx for ONTAP file system where you're copying data to or from.</p>"""
    fsx_filesystem_arn: NotRequired[
        "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn"
    ]
    """<p>The ARN of the FSx for ONTAP file system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxOntapResponse) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "security_group_arns" in value:
        import capo_datasync.types.ec2_security_group_arn_list

        out["SecurityGroupArns"] = (
            capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    if "storage_virtual_machine_arn" in value:
        out["StorageVirtualMachineArn"] = value["storage_virtual_machine_arn"]
    if "fsx_filesystem_arn" in value:
        out["FsxFilesystemArn"] = value["fsx_filesystem_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxOntapResponse:
    out: DescribeLocationFsxOntapResponse = {}  # type: ignore[typeddict-item]
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    if data.get("StorageVirtualMachineArn") is not None:
        out["storage_virtual_machine_arn"] = data["StorageVirtualMachineArn"]
    if data.get("FsxFilesystemArn") is not None:
        out["fsx_filesystem_arn"] = data["FsxFilesystemArn"]
    return out


def redact_sensitive(value: DescribeLocationFsxOntapResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.redact_sensitive(
            value["protocol"]
        )
    return out
