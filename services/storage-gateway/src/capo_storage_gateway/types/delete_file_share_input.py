"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteFileShareInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.file_share_arn


class DeleteFileShareInput(TypedDict, closed=True):
    file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN"
    """<p>The Amazon Resource Name (ARN) of the file share to be deleted.</p>"""
    force_delete: NotRequired["capo_storage_gateway.types.boolean2.Boolean2"]
    """<p>If this value is set to <code>true</code>, the operation deletes a file share immediately and aborts all data uploads to Amazon Web Services. Otherwise, the file share is not deleted until all data is uploaded to Amazon Web Services. This process aborts the data upload process, and the file share enters the <code>FORCE_DELETING</code> status.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileShareInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    if "force_delete" in value:
        out["ForceDelete"] = value["force_delete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileShareInput:
    out: DeleteFileShareInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        out["file_share_arn"] = ""
    if data.get("ForceDelete") is not None:
        out["force_delete"] = data["ForceDelete"]
    return out
