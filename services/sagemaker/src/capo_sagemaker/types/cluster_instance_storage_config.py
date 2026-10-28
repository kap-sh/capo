"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterInstanceStorageConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker.errors import DeserializationError, SerializationError
from capo_sagemaker.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_ebs_volume_config
    import capo_sagemaker.types.cluster_fsx_lustre_config
    import capo_sagemaker.types.cluster_fsx_open_zfs_config


class ClusterInstanceStorageConfigEbsVolumeConfigMember(TypedDict, closed=True):
    EbsVolumeConfig: (
        "capo_sagemaker.types.cluster_ebs_volume_config.ClusterEbsVolumeConfig"
    )


class ClusterInstanceStorageConfigFsxLustreConfigMember(TypedDict, closed=True):
    FsxLustreConfig: (
        "capo_sagemaker.types.cluster_fsx_lustre_config.ClusterFsxLustreConfig"
    )


class ClusterInstanceStorageConfigFsxOpenZfsConfigMember(TypedDict, closed=True):
    FsxOpenZfsConfig: (
        "capo_sagemaker.types.cluster_fsx_open_zfs_config.ClusterFsxOpenZfsConfig"
    )


ClusterInstanceStorageConfig: TypeAlias = (
    ClusterInstanceStorageConfigEbsVolumeConfigMember
    | ClusterInstanceStorageConfigFsxLustreConfigMember
    | ClusterInstanceStorageConfigFsxOpenZfsConfigMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterInstanceStorageConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ClusterInstanceStorageConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "EbsVolumeConfig" in value:
        import capo_sagemaker.types.cluster_ebs_volume_config

        return {
            "EbsVolumeConfig": capo_sagemaker.types.cluster_ebs_volume_config.serialize_aws_json_1_1(
                value["EbsVolumeConfig"]
            )
        }
    elif "FsxLustreConfig" in value:
        import capo_sagemaker.types.cluster_fsx_lustre_config

        return {
            "FsxLustreConfig": capo_sagemaker.types.cluster_fsx_lustre_config.serialize_aws_json_1_1(
                value["FsxLustreConfig"]
            )
        }
    elif "FsxOpenZfsConfig" in value:
        import capo_sagemaker.types.cluster_fsx_open_zfs_config

        return {
            "FsxOpenZfsConfig": capo_sagemaker.types.cluster_fsx_open_zfs_config.serialize_aws_json_1_1(
                value["FsxOpenZfsConfig"]
            )
        }
    else:
        raise SerializationError("ClusterInstanceStorageConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> ClusterInstanceStorageConfig:
    if data.get("EbsVolumeConfig") is not None:
        import capo_sagemaker.types.cluster_ebs_volume_config

        return {
            "EbsVolumeConfig": capo_sagemaker.types.cluster_ebs_volume_config.deserialize_aws_json_1_1(
                data["EbsVolumeConfig"]
            )
        }
    elif data.get("FsxLustreConfig") is not None:
        import capo_sagemaker.types.cluster_fsx_lustre_config

        return {
            "FsxLustreConfig": capo_sagemaker.types.cluster_fsx_lustre_config.deserialize_aws_json_1_1(
                data["FsxLustreConfig"]
            )
        }
    elif data.get("FsxOpenZfsConfig") is not None:
        import capo_sagemaker.types.cluster_fsx_open_zfs_config

        return {
            "FsxOpenZfsConfig": capo_sagemaker.types.cluster_fsx_open_zfs_config.deserialize_aws_json_1_1(
                data["FsxOpenZfsConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ClusterInstanceStorageConfig: no recognized variant key"
        )
