"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IconImageInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_workspaces_web.errors import DeserializationError, SerializationError
from capo_workspaces_web.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_workspaces_web.types.icon_image
    import capo_workspaces_web.types.s3_uri


class _IconImageInput_blob(TypedDict, closed=True):
    blob: "capo_workspaces_web.types.icon_image.IconImage"


class _IconImageInput_s3Uri(TypedDict, closed=True):
    s3Uri: "capo_workspaces_web.types.s3_uri.S3Uri"


IconImageInput: TypeAlias = (
    _IconImageInput_blob | _IconImageInput_s3Uri | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IconImageInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IconImageInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "blob" in value:
        import capo_workspaces_web.types.icon_image

        return {
            "blob": capo_workspaces_web.types.icon_image.serialize_json(value["blob"])
        }
    elif "s3Uri" in value:
        return {"s3Uri": value["s3Uri"]}
    else:
        raise SerializationError("IconImageInput: no variant present")


def deserialize_json(data: dict) -> IconImageInput:
    if data.get("blob") is not None:
        import capo_workspaces_web.types.icon_image

        return {
            "blob": capo_workspaces_web.types.icon_image.deserialize_json(data["blob"])
        }
    elif data.get("s3Uri") is not None:
        return {"s3Uri": data["s3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IconImageInput: no recognized variant key")
