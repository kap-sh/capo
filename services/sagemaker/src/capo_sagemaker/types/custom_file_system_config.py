"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystemConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.efs_file_system_config
    import capo_sagemaker.types.f_sx_lustre_file_system_config
    import capo_sagemaker.types.s3_file_system_config


class _CustomFileSystemConfig_EFSFileSystemConfig(TypedDict, closed=True):
    EFSFileSystemConfig: (
        "capo_sagemaker.types.efs_file_system_config.EFSFileSystemConfig"
    )


class _CustomFileSystemConfig_FSxLustreFileSystemConfig(TypedDict, closed=True):
    FSxLustreFileSystemConfig: (
        "capo_sagemaker.types.f_sx_lustre_file_system_config.FSxLustreFileSystemConfig"
    )


class _CustomFileSystemConfig_S3FileSystemConfig(TypedDict, closed=True):
    S3FileSystemConfig: "capo_sagemaker.types.s3_file_system_config.S3FileSystemConfig"


CustomFileSystemConfig: TypeAlias = (
    _CustomFileSystemConfig_EFSFileSystemConfig
    | _CustomFileSystemConfig_FSxLustreFileSystemConfig
    | _CustomFileSystemConfig_S3FileSystemConfig
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
