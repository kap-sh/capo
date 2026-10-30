"""Generated from Smithy shape ``com.amazonaws.continuum#FindingLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_file_path


class FindingLocation(TypedDict, closed=True):
    file_path: NotRequired["capo_continuum.types.finding_file_path.FindingFilePath"]
    """Repository-relative path."""
    start_line: NotRequired["int"]
    """1-indexed first line of the affected range."""
    end_line: NotRequired["int"]
    """1-indexed last line, when the producer reported a range."""


# --- restJson1 ser/de ---
def serialize_json(value: FindingLocation) -> dict:
    out: dict = {}
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "start_line" in value:
        out["startLine"] = value["start_line"]
    if "end_line" in value:
        out["endLine"] = value["end_line"]
    return out


def deserialize_json(data: dict) -> FindingLocation:
    out: FindingLocation = {}  # type: ignore[typeddict-item]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("startLine") is not None:
        out["start_line"] = data["startLine"]
    if data.get("endLine") is not None:
        out["end_line"] = data["endLine"]
    return out
