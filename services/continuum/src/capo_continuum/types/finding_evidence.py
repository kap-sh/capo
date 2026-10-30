"""Generated from Smithy shape ``com.amazonaws.continuum#FindingEvidence``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.finding_code_snippet
    import capo_continuum.types.finding_file_path


class FindingEvidence(TypedDict, closed=True):
    file: NotRequired["capo_continuum.types.finding_file_path.FindingFilePath"]
    """The file the evidence was found in."""
    line: NotRequired["int"]
    """The 1-indexed line, when known."""
    snippet: NotRequired["capo_continuum.types.finding_code_snippet.FindingCodeSnippet"]
    """The cited excerpt."""


# --- restJson1 ser/de ---
def serialize_json(value: FindingEvidence) -> dict:
    out: dict = {}
    if "file" in value:
        out["file"] = value["file"]
    if "line" in value:
        out["line"] = value["line"]
    if "snippet" in value:
        out["snippet"] = value["snippet"]
    return out


def deserialize_json(data: dict) -> FindingEvidence:
    out: FindingEvidence = {}  # type: ignore[typeddict-item]
    if data.get("file") is not None:
        out["file"] = data["file"]
    if data.get("line") is not None:
        out["line"] = data["line"]
    if data.get("snippet") is not None:
        out["snippet"] = data["snippet"]
    return out
