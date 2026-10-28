"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.efs_file_system
    import capo_sagemaker.types.f_sx_lustre_file_system
    import capo_sagemaker.types.s3_file_system


class CustomFileSystemEFSFileSystemMember(TypedDict, closed=True):
    EFSFileSystem: "capo_sagemaker.types.efs_file_system.EFSFileSystem"


class CustomFileSystemFSxLustreFileSystemMember(TypedDict, closed=True):
    FSxLustreFileSystem: (
        "capo_sagemaker.types.f_sx_lustre_file_system.FSxLustreFileSystem"
    )


class CustomFileSystemS3FileSystemMember(TypedDict, closed=True):
    S3FileSystem: "capo_sagemaker.types.s3_file_system.S3FileSystem"


CustomFileSystem: TypeAlias = (
    CustomFileSystemEFSFileSystemMember
    | CustomFileSystemFSxLustreFileSystemMember
    | CustomFileSystemS3FileSystemMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystem) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomFileSystem: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "EFSFileSystem" in value:
        import capo_sagemaker.types.efs_file_system

        return {
            "EFSFileSystem": capo_sagemaker.types.efs_file_system.serialize_aws_json_1_1(
                value["EFSFileSystem"]
            )
        }
    elif "FSxLustreFileSystem" in value:
        import capo_sagemaker.types.f_sx_lustre_file_system

        return {
            "FSxLustreFileSystem": capo_sagemaker.types.f_sx_lustre_file_system.serialize_aws_json_1_1(
                value["FSxLustreFileSystem"]
            )
        }
    elif "S3FileSystem" in value:
        import capo_sagemaker.types.s3_file_system

        return {
            "S3FileSystem": capo_sagemaker.types.s3_file_system.serialize_aws_json_1_1(
                value["S3FileSystem"]
            )
        }
    else:
        raise SerializationError("CustomFileSystem: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CustomFileSystem:
    if data.get("EFSFileSystem") is not None:
        import capo_sagemaker.types.efs_file_system

        return {
            "EFSFileSystem": capo_sagemaker.types.efs_file_system.deserialize_aws_json_1_1(
                data["EFSFileSystem"]
            )
        }
    elif data.get("FSxLustreFileSystem") is not None:
        import capo_sagemaker.types.f_sx_lustre_file_system

        return {
            "FSxLustreFileSystem": capo_sagemaker.types.f_sx_lustre_file_system.deserialize_aws_json_1_1(
                data["FSxLustreFileSystem"]
            )
        }
    elif data.get("S3FileSystem") is not None:
        import capo_sagemaker.types.s3_file_system

        return {
            "S3FileSystem": capo_sagemaker.types.s3_file_system.deserialize_aws_json_1_1(
                data["S3FileSystem"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CustomFileSystem: no recognized variant key")
