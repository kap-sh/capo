"""Generated from Smithy shape ``com.amazonaws.m2#StorageConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_m2.errors import DeserializationError, SerializationError
from capo_m2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_m2.types.efs_storage_configuration
    import capo_m2.types.fsx_storage_configuration


class StorageConfigurationEfsMember(TypedDict, closed=True):
    efs: "capo_m2.types.efs_storage_configuration.EfsStorageConfiguration"


class StorageConfigurationFsxMember(TypedDict, closed=True):
    fsx: "capo_m2.types.fsx_storage_configuration.FsxStorageConfiguration"


StorageConfiguration: TypeAlias = (
    StorageConfigurationEfsMember | StorageConfigurationFsxMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: StorageConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"StorageConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "efs" in value:
        import capo_m2.types.efs_storage_configuration

        return {
            "efs": capo_m2.types.efs_storage_configuration.serialize_json(value["efs"])
        }
    elif "fsx" in value:
        import capo_m2.types.fsx_storage_configuration

        return {
            "fsx": capo_m2.types.fsx_storage_configuration.serialize_json(value["fsx"])
        }
    else:
        raise SerializationError("StorageConfiguration: no variant present")


def deserialize_json(data: dict) -> StorageConfiguration:
    if data.get("efs") is not None:
        import capo_m2.types.efs_storage_configuration

        return {
            "efs": capo_m2.types.efs_storage_configuration.deserialize_json(data["efs"])
        }
    elif data.get("fsx") is not None:
        import capo_m2.types.fsx_storage_configuration

        return {
            "fsx": capo_m2.types.fsx_storage_configuration.deserialize_json(data["fsx"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("StorageConfiguration: no recognized variant key")
