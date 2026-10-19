"""Generated from Smithy shape ``com.amazonaws.connectcases#FileContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.file_arn


class FileContent(TypedDict, closed=True):
    file_arn: "capo_connectcases.types.file_arn.FileArn"
    """<p>The Amazon Resource Name (ARN) of a File in Amazon Connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileContent) -> dict:
    out: dict = {}
    out["fileArn"] = value["file_arn"]
    return out


def deserialize_json(data: dict) -> FileContent:
    out: FileContent = {}  # type: ignore[typeddict-item]
    if data.get("fileArn") is not None:
        out["file_arn"] = data["fileArn"]
    else:
        out["file_arn"] = ""
    return out
