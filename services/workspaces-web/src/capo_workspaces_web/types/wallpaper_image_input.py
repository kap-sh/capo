"""Generated from Smithy shape ``com.amazonaws.workspacesweb#WallpaperImageInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError, SerializationError
from capo_workspaces_web.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_workspaces_web.types.s3_uri
    import capo_workspaces_web.types.wallpaper_image


class WallpaperImageInputBlobMember(TypedDict, closed=True):
    blob: "capo_workspaces_web.types.wallpaper_image.WallpaperImage"


class WallpaperImageInputS3UriMember(TypedDict, closed=True):
    s3Uri: "capo_workspaces_web.types.s3_uri.S3Uri"


WallpaperImageInput: TypeAlias = (
    WallpaperImageInputBlobMember | WallpaperImageInputS3UriMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: WallpaperImageInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WallpaperImageInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "blob" in value:
        import capo_workspaces_web.types.wallpaper_image

        return {
            "blob": capo_workspaces_web.types.wallpaper_image.serialize_json(
                value["blob"]
            )
        }
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("WallpaperImageInput: no variant present")


def deserialize_json(data: dict) -> WallpaperImageInput:
    if data.get("blob") is not None:
        import capo_workspaces_web.types.wallpaper_image

        return {
            "blob": capo_workspaces_web.types.wallpaper_image.deserialize_json(
                data["blob"]
            )
        }
    elif data.get("s3Uri") is not None:
        return {"s3Uri": data["s3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("WallpaperImageInput: no recognized variant key")
