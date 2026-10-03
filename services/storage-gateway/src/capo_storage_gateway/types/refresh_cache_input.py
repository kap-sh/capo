"""Generated from Smithy shape ``com.amazonaws.storagegateway#RefreshCacheInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean
    import capo_storage_gateway.types.file_share_arn
    import capo_storage_gateway.types.folder_list


class RefreshCacheInput(TypedDict, closed=True):
    file_share_arn: "capo_storage_gateway.types.file_share_arn.FileShareARN"
    """<p>The Amazon Resource Name (ARN) of the file share you want to refresh.</p>"""
    folder_list: NotRequired["capo_storage_gateway.types.folder_list.FolderList"]
    """<p>A comma-separated list of the paths of folders to refresh in the cache. The default is [<code>"/"</code>]. The default refreshes objects and folders at the root of the Amazon S3 bucket. If <code>Recursive</code> is set to <code>true</code>, the entire S3 bucket that the file share has access to is refreshed.</p> <p>Do not include <code>/</code> when specifying folder names. For example, you would specify <code>samplefolder</code> rather than <code>samplefolder/</code>.</p>"""
    recursive: NotRequired["capo_storage_gateway.types.boolean.Boolean"]
    """<p>A value that specifies whether to recursively refresh folders in the cache. The refresh includes folders that were in the cache the last time the gateway listed the folder's contents. If this value set to <code>true</code>, each folder that is listed in <code>FolderList</code> is recursively updated. Otherwise, subfolders listed in <code>FolderList</code> are not refreshed. Only objects that are in folders listed directly under <code>FolderList</code> are found and used for the update. The default is <code>true</code>.</p> <p>Valid Values: <code>true</code> | <code>false</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshCacheInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    if "folder_list" in value:
        import capo_storage_gateway.types.folder_list

        out["FolderList"] = (
            capo_storage_gateway.types.folder_list.serialize_aws_json_1_1(
                value["folder_list"]
            )
        )
    if "recursive" in value:
        out["Recursive"] = value["recursive"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshCacheInput:
    out: RefreshCacheInput = {}  # type: ignore[typeddict-item]
    if data.get("FileShareARN") is not None:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        raise DeserializationError("RefreshCacheInput.file_share_arn required")
    if data.get("FolderList") is not None:
        import capo_storage_gateway.types.folder_list

        out["folder_list"] = (
            capo_storage_gateway.types.folder_list.deserialize_aws_json_1_1(
                data["FolderList"]
            )
        )
    if data.get("Recursive") is not None:
        out["recursive"] = data["Recursive"]
    return out
