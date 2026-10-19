"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteFileEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.path


class DeleteFileEntry(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The full path of the file to be deleted, including the name of the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileEntry:
    out: DeleteFileEntry = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    return out
