"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.file_system_location_name
    import capo_deadline.types.file_system_location_type
    import capo_deadline.types.path_string


class FileSystemLocation(TypedDict, closed=True):
    name: "capo_deadline.types.file_system_location_name.FileSystemLocationName"
    """<p>The location name.</p>"""
    path: "capo_deadline.types.path_string.PathString"
    """<p>The file path.</p>"""
    type: "capo_deadline.types.file_system_location_type.FileSystemLocationType"
    """<p>The type of file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemLocation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["path"] = value["path"]
    import capo_deadline.types.file_system_location_type

    out["type"] = capo_deadline.types.file_system_location_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> FileSystemLocation:
    out: FileSystemLocation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("path") is not None:
        out["path"] = data["path"]
    else:
        out["path"] = ""
    if data.get("type") is not None:
        import capo_deadline.types.file_system_location_type

        out["type"] = capo_deadline.types.file_system_location_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_deadline.types.file_system_location_type.FileSystemLocationType", ""
        )
    return out
