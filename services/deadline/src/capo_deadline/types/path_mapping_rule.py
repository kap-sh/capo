"""Generated from Smithy shape ``com.amazonaws.deadline#PathMappingRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.path_format
    import capo_deadline.types.string


class PathMappingRule(TypedDict, closed=True):
    source_path_format: "capo_deadline.types.path_format.PathFormat"
    """<p>The source path format.</p>"""
    source_path: "capo_deadline.types.string.String"
    """<p>The source path.</p>"""
    destination_path: "capo_deadline.types.string.String"
    """<p>The destination path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PathMappingRule) -> dict:
    out: dict = {}
    import capo_deadline.types.path_format

    out["sourcePathFormat"] = capo_deadline.types.path_format.serialize_json(
        value["source_path_format"]
    )
    out["sourcePath"] = value["source_path"]
    out["destinationPath"] = value["destination_path"]
    return out


def deserialize_json(data: dict) -> PathMappingRule:
    out: PathMappingRule = {}  # type: ignore[typeddict-item]
    if data.get("sourcePathFormat") is not None:
        import capo_deadline.types.path_format

        out["source_path_format"] = capo_deadline.types.path_format.deserialize_json(
            data["sourcePathFormat"]
        )
    else:
        import typing

        out["source_path_format"] = typing.cast(
            "capo_deadline.types.path_format.PathFormat", ""
        )
    if data.get("sourcePath") is not None:
        out["source_path"] = data["sourcePath"]
    else:
        out["source_path"] = ""
    if data.get("destinationPath") is not None:
        out["destination_path"] = data["destinationPath"]
    else:
        out["destination_path"] = ""
    return out
