"""Generated from Smithy shape ``com.amazonaws.deadline#FileSystemLocationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.file_system_location

FileSystemLocationsList: TypeAlias = list[
    "capo_deadline.types.file_system_location.FileSystemLocation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemLocationsList) -> list:
    import capo_deadline.types.file_system_location

    out: list = []
    for item in value:
        out.append(capo_deadline.types.file_system_location.serialize_json(item))
    return out


def deserialize_json(data: list) -> FileSystemLocationsList:
    import capo_deadline.types.file_system_location

    out: FileSystemLocationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.file_system_location.deserialize_json(item))
    return out


def redact_sensitive(value: FileSystemLocationsList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
