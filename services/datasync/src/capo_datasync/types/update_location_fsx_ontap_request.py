"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxOntapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.fsx_ontap_subdirectory
    import capo_datasync.types.fsx_update_protocol
    import capo_datasync.types.location_arn


class UpdateLocationFsxOntapRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP transfer location that you're updating.</p>"""
    protocol: NotRequired["capo_datasync.types.fsx_update_protocol.FsxUpdateProtocol"]
    """<p>Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.</p>"""
    subdirectory: NotRequired[
        "capo_datasync.types.fsx_ontap_subdirectory.FsxOntapSubdirectory"
    ]
    """<p>Specifies a path to the file share in the storage virtual machine (SVM) where you want to transfer data to or from.</p> <p>You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be <code>/vol1</code>, <code>/vol1/tree1</code>, or <code>/share1</code>.</p> <note> <p>Don't specify a junction path in the SVM's root volume. For more information, see <a href="https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html">Managing FSx for ONTAP storage virtual machines</a> in the <i>Amazon FSx for NetApp ONTAP User Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxOntapRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "protocol" in value:
        import capo_datasync.types.fsx_update_protocol

        out["Protocol"] = (
            capo_datasync.types.fsx_update_protocol.serialize_aws_json_1_1(
                value["protocol"]
            )
        )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxOntapRequest:
    out: UpdateLocationFsxOntapRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError(
            "UpdateLocationFsxOntapRequest.location_arn required"
        )
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_update_protocol

        out["protocol"] = (
            capo_datasync.types.fsx_update_protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    return out
