"""Generated from Smithy shape ``com.amazonaws.storagegateway#DisassociateFileSystemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.file_system_association_arn


class DisassociateFileSystemInput(TypedDict, closed=True):
    file_system_association_arn: "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    """<p>The Amazon Resource Name (ARN) of the file system association to be deleted.</p>"""
    force_delete: NotRequired["capo_storage_gateway.types.boolean2.Boolean2"]
    """<p>If this value is set to true, the operation disassociates an Amazon FSx file system immediately. It ends all data uploads to the file system, and the file system association enters the <code>FORCE_DELETING</code> status. If this value is set to false, the Amazon FSx file system does not disassociate until all data is uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFileSystemInput) -> dict:
    out: dict = {}
    out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    if "force_delete" in value:
        out["ForceDelete"] = value["force_delete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFileSystemInput:
    out: DisassociateFileSystemInput = {}  # type: ignore[typeddict-item]
    if data.get("FileSystemAssociationARN") is not None:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    else:
        raise DeserializationError(
            "DisassociateFileSystemInput.file_system_association_arn required"
        )
    if data.get("ForceDelete") is not None:
        out["force_delete"] = data["ForceDelete"]
    return out
