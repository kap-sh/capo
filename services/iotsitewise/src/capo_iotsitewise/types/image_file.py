"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageFile``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.image_file_data
    import capo_iotsitewise.types.image_file_type


class ImageFile(TypedDict, closed=True):
    data: "capo_iotsitewise.types.image_file_data.ImageFileData"
    """<p>The image file contents, represented as a base64-encoded string. The file size must be less than 1 MB.</p>"""
    type: "capo_iotsitewise.types.image_file_type.ImageFileType"
    """<p>The file type of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageFile) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.image_file_data

    out["data"] = capo_iotsitewise.types.image_file_data.serialize_json(value["data"])
    import capo_iotsitewise.types.image_file_type

    out["type"] = capo_iotsitewise.types.image_file_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> ImageFile:
    out: ImageFile = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_iotsitewise.types.image_file_data

        out["data"] = capo_iotsitewise.types.image_file_data.deserialize_json(
            data["data"]
        )
    else:
        out["data"] = b""
    if data.get("type") is not None:
        import capo_iotsitewise.types.image_file_type

        out["type"] = capo_iotsitewise.types.image_file_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_iotsitewise.types.image_file_type.ImageFileType", ""
        )
    return out
