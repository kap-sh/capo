"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilesystemConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration
    import capo_bedrock_agentcore_control.types.efs_access_point_configuration
    import capo_bedrock_agentcore_control.types.s3_files_access_point_configuration
    import capo_bedrock_agentcore_control.types.session_storage_configuration


class _FilesystemConfiguration_sessionStorage(TypedDict, closed=True):
    sessionStorage: "capo_bedrock_agentcore_control.types.session_storage_configuration.SessionStorageConfiguration"


class _FilesystemConfiguration_s3FilesAccessPoint(TypedDict, closed=True):
    s3FilesAccessPoint: "capo_bedrock_agentcore_control.types.s3_files_access_point_configuration.S3FilesAccessPointConfiguration"


class _FilesystemConfiguration_efsAccessPoint(TypedDict, closed=True):
    efsAccessPoint: "capo_bedrock_agentcore_control.types.efs_access_point_configuration.EfsAccessPointConfiguration"


class _FilesystemConfiguration_capacityProviderVolume(TypedDict, closed=True):
    capacityProviderVolume: "capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration.CapacityProviderVolumeConfiguration"


FilesystemConfiguration: TypeAlias = (
    _FilesystemConfiguration_sessionStorage
    | _FilesystemConfiguration_s3FilesAccessPoint
    | _FilesystemConfiguration_efsAccessPoint
    | _FilesystemConfiguration_capacityProviderVolume
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FilesystemConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FilesystemConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "sessionStorage" in value:
        import capo_bedrock_agentcore_control.types.session_storage_configuration

        return {
            "sessionStorage": capo_bedrock_agentcore_control.types.session_storage_configuration.serialize_json(
                value["sessionStorage"]
            )
        }
    elif "s3FilesAccessPoint" in value:
        import capo_bedrock_agentcore_control.types.s3_files_access_point_configuration

        return {
            "s3FilesAccessPoint": capo_bedrock_agentcore_control.types.s3_files_access_point_configuration.serialize_json(
                value["s3FilesAccessPoint"]
            )
        }
    elif "efsAccessPoint" in value:
        import capo_bedrock_agentcore_control.types.efs_access_point_configuration

        return {
            "efsAccessPoint": capo_bedrock_agentcore_control.types.efs_access_point_configuration.serialize_json(
                value["efsAccessPoint"]
            )
        }
    elif "capacityProviderVolume" in value:
        import capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration

        return {
            "capacityProviderVolume": capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration.serialize_json(
                value["capacityProviderVolume"]
            )
        }
    else:
        raise SerializationError("FilesystemConfiguration: no variant present")


def deserialize_json(data: dict) -> FilesystemConfiguration:
    if data.get("sessionStorage") is not None:
        import capo_bedrock_agentcore_control.types.session_storage_configuration

        return {
            "sessionStorage": capo_bedrock_agentcore_control.types.session_storage_configuration.deserialize_json(
                data["sessionStorage"]
            )
        }
    elif data.get("s3FilesAccessPoint") is not None:
        import capo_bedrock_agentcore_control.types.s3_files_access_point_configuration

        return {
            "s3FilesAccessPoint": capo_bedrock_agentcore_control.types.s3_files_access_point_configuration.deserialize_json(
                data["s3FilesAccessPoint"]
            )
        }
    elif data.get("efsAccessPoint") is not None:
        import capo_bedrock_agentcore_control.types.efs_access_point_configuration

        return {
            "efsAccessPoint": capo_bedrock_agentcore_control.types.efs_access_point_configuration.deserialize_json(
                data["efsAccessPoint"]
            )
        }
    elif data.get("capacityProviderVolume") is not None:
        import capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration

        return {
            "capacityProviderVolume": capo_bedrock_agentcore_control.types.capacity_provider_volume_configuration.deserialize_json(
                data["capacityProviderVolume"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FilesystemConfiguration: no recognized variant key")
