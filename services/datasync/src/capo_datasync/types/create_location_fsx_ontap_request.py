"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationFsxOntapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.fsx_ontap_subdirectory
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.input_tag_list
    import capo_datasync.types.storage_virtual_machine_arn


class CreateLocationFsxOntapRequest(TypedDict, closed=True):
    protocol: "capo_datasync.types.fsx_protocol.FsxProtocol"
    security_group_arns: (
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    )
    """<p>Specifies the Amazon EC2 security groups that provide access to your file system's preferred subnet.</p> <p>The security groups must allow outbound traffic on the following ports (depending on the protocol you use):</p> <ul> <li> <p> <b>Network File System (NFS)</b>: TCP ports 111, 635, and 2049</p> </li> <li> <p> <b>Server Message Block (SMB)</b>: TCP port 445</p> </li> </ul> <p>Your file system's security groups must also allow inbound traffic on the same ports.</p>"""
    storage_virtual_machine_arn: (
        "capo_datasync.types.storage_virtual_machine_arn.StorageVirtualMachineArn"
    )
    """<p>Specifies the ARN of the storage virtual machine (SVM) in your file system where you want to copy data to or from.</p>"""
    subdirectory: NotRequired[
        "capo_datasync.types.fsx_ontap_subdirectory.FsxOntapSubdirectory"
    ]
    """<p>Specifies a path to the file share in the SVM where you want to transfer data to or from.</p> <p>You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be <code>/vol1</code>, <code>/vol1/tree1</code>, or <code>/share1</code>.</p> <note> <p>Don't specify a junction path in the SVM's root volume. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html">Managing FSx for ONTAP storage virtual machines</a> in the <i>Amazon FSx for NetApp ONTAP User Guide</i>.</p> </note>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationFsxOntapRequest) -> dict:
    out: dict = {}
    import capo_datasync.types.fsx_protocol

    out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
        value["protocol"]
    )
    import capo_datasync.types.ec2_security_group_arn_list

    out["SecurityGroupArns"] = (
        capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
            value["security_group_arns"]
        )
    )
    out["StorageVirtualMachineArn"] = value["storage_virtual_machine_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationFsxOntapRequest:
    out: CreateLocationFsxOntapRequest = {}  # type: ignore[typeddict-item]
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    else:
        raise DeserializationError("CreateLocationFsxOntapRequest.protocol required")
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLocationFsxOntapRequest.security_group_arns required"
        )
    if data.get("StorageVirtualMachineArn") is not None:
        out["storage_virtual_machine_arn"] = data["StorageVirtualMachineArn"]
    else:
        raise DeserializationError(
            "CreateLocationFsxOntapRequest.storage_virtual_machine_arn required"
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
