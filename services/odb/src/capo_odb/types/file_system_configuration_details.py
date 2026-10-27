"""Generated from Smithy shape ``com.amazonaws.odb#FileSystemConfigurationDetails``."""

from typing_extensions import NotRequired, TypedDict


class FileSystemConfigurationDetails(TypedDict, closed=True):
    mount_point: NotRequired["str"]
    """<p>The mount point of the file system.</p>"""
    file_system_size_in_g_bs: NotRequired["int"]
    """<p>The size of the file system, in gigabytes (GB).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileSystemConfigurationDetails) -> dict:
    out: dict = {}
    if "mount_point" in value:
        out["mountPoint"] = value["mount_point"]
    if "file_system_size_in_g_bs" in value:
        out["fileSystemSizeInGBs"] = value["file_system_size_in_g_bs"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FileSystemConfigurationDetails:
    out: FileSystemConfigurationDetails = {}  # type: ignore[typeddict-item]
    if data.get("mountPoint") is not None:
        out["mount_point"] = data["mountPoint"]
    if data.get("fileSystemSizeInGBs") is not None:
        out["file_system_size_in_g_bs"] = data["fileSystemSizeInGBs"]
    return out
