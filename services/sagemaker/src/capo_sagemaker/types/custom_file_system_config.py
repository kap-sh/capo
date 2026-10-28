"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystemConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.efs_file_system_config
    import capo_sagemaker.types.f_sx_lustre_file_system_config
    import capo_sagemaker.types.s3_file_system_config


class CustomFileSystemConfigEFSFileSystemConfigMember(TypedDict, closed=True):
    EFSFileSystemConfig: (
        "capo_sagemaker.types.efs_file_system_config.EFSFileSystemConfig"
    )


class CustomFileSystemConfigFSxLustreFileSystemConfigMember(TypedDict, closed=True):
    FSxLustreFileSystemConfig: (
        "capo_sagemaker.types.f_sx_lustre_file_system_config.FSxLustreFileSystemConfig"
    )


class CustomFileSystemConfigS3FileSystemConfigMember(TypedDict, closed=True):
    S3FileSystemConfig: "capo_sagemaker.types.s3_file_system_config.S3FileSystemConfig"


CustomFileSystemConfig: TypeAlias = (
    CustomFileSystemConfigEFSFileSystemConfigMember
    | CustomFileSystemConfigFSxLustreFileSystemConfigMember
    | CustomFileSystemConfigS3FileSystemConfigMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystemConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CustomFileSystemConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "EFSFileSystemConfig" in value:
        import capo_sagemaker.types.efs_file_system_config

        return {
            "EFSFileSystemConfig": capo_sagemaker.types.efs_file_system_config.serialize_aws_json_1_1(
                value["EFSFileSystemConfig"]
            )
        }
    elif "FSxLustreFileSystemConfig" in value:
        import capo_sagemaker.types.f_sx_lustre_file_system_config

        return {
            "FSxLustreFileSystemConfig": capo_sagemaker.types.f_sx_lustre_file_system_config.serialize_aws_json_1_1(
                value["FSxLustreFileSystemConfig"]
            )
        }
    elif "S3FileSystemConfig" in value:
        import capo_sagemaker.types.s3_file_system_config

        return {
            "S3FileSystemConfig": capo_sagemaker.types.s3_file_system_config.serialize_aws_json_1_1(
                value["S3FileSystemConfig"]
            )
        }
    else:
        raise SerializationError("CustomFileSystemConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CustomFileSystemConfig:
    if data.get("EFSFileSystemConfig") is not None:
        import capo_sagemaker.types.efs_file_system_config

        return {
            "EFSFileSystemConfig": capo_sagemaker.types.efs_file_system_config.deserialize_aws_json_1_1(
                data["EFSFileSystemConfig"]
            )
        }
    elif data.get("FSxLustreFileSystemConfig") is not None:
        import capo_sagemaker.types.f_sx_lustre_file_system_config

        return {
            "FSxLustreFileSystemConfig": capo_sagemaker.types.f_sx_lustre_file_system_config.deserialize_aws_json_1_1(
                data["FSxLustreFileSystemConfig"]
            )
        }
    elif data.get("S3FileSystemConfig") is not None:
        import capo_sagemaker.types.s3_file_system_config

        return {
            "S3FileSystemConfig": capo_sagemaker.types.s3_file_system_config.deserialize_aws_json_1_1(
                data["S3FileSystemConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CustomFileSystemConfig: no recognized variant key")
