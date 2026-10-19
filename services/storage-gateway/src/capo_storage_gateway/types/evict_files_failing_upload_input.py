"""Generated from Smithy shape ``com.amazonaws.storagegateway#EvictFilesFailingUploadInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.file_share_arn


class EvictFilesFailingUploadInput(TypedDict, closed=True):
    file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN"
    """<p>The Amazon Resource Name (ARN) of the file share for which you want to start the cache clean operation.</p>"""
    force_remove: NotRequired["capo_storage_gateway.types.boolean2.Boolean2"]
    """<p>Specifies whether cache entries with full or partial file data currently stored on the gateway will be forcibly removed by the cache clean operation.</p> <p>Valid arguments:</p> <ul> <li> <p> <code>False</code> - The cache clean operation skips cache entries failing upload if they are associated with data currently stored on the gateway. This preserves the cached data.</p> </li> <li> <p> <code>True</code> - The cache clean operation removes cache entries failing upload even if they are associated with data currently stored on the gateway. This deletes the cached data.</p> <important> <p>If <code>ForceRemove</code> is set to <code>True</code>, the cache clean operation will delete file data from the gateway which might otherwise be recoverable.</p> </important> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvictFilesFailingUploadInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    if "force_remove" in value:
        out["ForceRemove"] = value["force_remove"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvictFilesFailingUploadInput:
    out: EvictFilesFailingUploadInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        raise DeserializationError(
            "EvictFilesFailingUploadInput.file_share_arn required"
        )
    if data.get("ForceRemove") is not None:
        out["force_remove"] = data["ForceRemove"]
    return out
