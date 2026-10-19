"""Generated from Smithy shape ``com.amazonaws.lambda#FileSystemConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.file_system_arn
    import capo_lambda.types.local_mount_path
    import capo_lambda.types.s3_files_config


class FileSystemConfig(TypedDict, closed=True):
    arn: "capo_lambda.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon EFS or Amazon S3 Files access point that provides access to the file system.</p>"""
    local_mount_path: "capo_lambda.types.local_mount_path.LocalMountPath"
    """<p>The path where the function can access the file system, starting with <code>/mnt/</code>.</p>"""
    s3_files_config: NotRequired["capo_lambda.types.s3_files_config.S3FilesConfig"]
    """<p>The configuration for how your function accesses data on an Amazon S3 file system. Valid only when the file system access point ARN is an Amazon S3 Files access point. If you specify a different access point type (for example, Amazon Elastic File System), the operation returns an <code>InvalidParameterException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemConfig) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["LocalMountPath"] = value["local_mount_path"]
    if "s3_files_config" in value:
        import capo_lambda.types.s3_files_config

        out["S3FilesConfig"] = capo_lambda.types.s3_files_config.serialize_json(
            value["s3_files_config"]
        )
    return out


def deserialize_json(data: dict) -> FileSystemConfig:
    out: FileSystemConfig = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("LocalMountPath") is not None:
        out["local_mount_path"] = data["LocalMountPath"]
    else:
        out["local_mount_path"] = ""
    if data.get("S3FilesConfig") is not None:
        import capo_lambda.types.s3_files_config

        out["s3_files_config"] = capo_lambda.types.s3_files_config.deserialize_json(
            data["S3FilesConfig"]
        )
    return out
