"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Mount``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.mount_relative_path
    import capo_iotsitewise.types.mount_source
    import capo_iotsitewise.types.mount_storage_type
    import capo_iotsitewise.types.resource_name


class Mount(TypedDict, closed=True):
    name: "capo_iotsitewise.types.resource_name.ResourceName"
    """<p>A unique name for the mount within the task.</p>"""
    relative_path: "capo_iotsitewise.types.mount_relative_path.MountRelativePath"
    """<p>The relative path under the service-owned mount root where this mount is attached inside the container.</p>"""
    source: "capo_iotsitewise.types.mount_source.MountSource"
    """<p>The data source for the mount.</p>"""
    storage_type: "capo_iotsitewise.types.mount_storage_type.MountStorageType"
    """<p>The type of storage used for the mount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Mount) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["relativePath"] = value["relative_path"]
    import capo_iotsitewise.types.mount_source

    out["source"] = capo_iotsitewise.types.mount_source.serialize_json(value["source"])
    import capo_iotsitewise.types.mount_storage_type

    out["storageType"] = capo_iotsitewise.types.mount_storage_type.serialize_json(
        value["storage_type"]
    )
    return out


def deserialize_json(data: dict) -> Mount:
    out: Mount = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("relativePath") is not None:
        out["relative_path"] = data["relativePath"]
    else:
        out["relative_path"] = ""
    if data.get("source") is not None:
        import capo_iotsitewise.types.mount_source

        out["source"] = capo_iotsitewise.types.mount_source.deserialize_json(
            data["source"]
        )
    else:
        import capo_iotsitewise.types._unknown

        out["source"] = capo_iotsitewise.types._unknown.UnknownUnionMember("")
    if data.get("storageType") is not None:
        import capo_iotsitewise.types.mount_storage_type

        out["storage_type"] = (
            capo_iotsitewise.types.mount_storage_type.deserialize_json(
                data["storageType"]
            )
        )
    else:
        import typing

        out["storage_type"] = typing.cast(
            "capo_iotsitewise.types.mount_storage_type.MountStorageType", ""
        )
    return out
