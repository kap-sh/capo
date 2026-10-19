"""Generated from Smithy shape ``com.amazonaws.s3files#ListFileSystemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.file_systems


class ListFileSystemsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A pagination token to use in a subsequent request if more results are available.</p>"""
    file_systems: "capo_s3files.types.file_systems.FileSystems"
    """<p>An array of file system descriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFileSystemsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_s3files.types.file_systems

    out["fileSystems"] = capo_s3files.types.file_systems.serialize_json(
        value["file_systems"]
    )
    return out


def deserialize_json(data: dict) -> ListFileSystemsResponse:
    out: ListFileSystemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("fileSystems") is not None:
        import capo_s3files.types.file_systems

        out["file_systems"] = capo_s3files.types.file_systems.deserialize_json(
            data["fileSystems"]
        )
    else:
        out["file_systems"] = []
    return out
