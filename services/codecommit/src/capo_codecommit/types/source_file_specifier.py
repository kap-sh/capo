"""Generated from Smithy shape ``com.amazonaws.codecommit#SourceFileSpecifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.is_move
    import capo_codecommit.types.path


class SourceFileSpecifier(TypedDict, closed=True):
    file_path: "capo_codecommit.types.path.Path"
    """<p>The full path to the file, including the name of the file.</p>"""
    is_move: "capo_codecommit.types.is_move.IsMove"
    """<p>Whether to remove the source file from the parent commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceFileSpecifier) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    out["isMove"] = value.get("is_move", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceFileSpecifier:
    out: SourceFileSpecifier = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    else:
        out["file_path"] = ""
    if data.get("isMove") is not None:
        out["is_move"] = data["isMove"]
    else:
        out["is_move"] = False
    return out
