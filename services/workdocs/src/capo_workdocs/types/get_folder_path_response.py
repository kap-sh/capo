"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderPathResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.resource_path


class GetFolderPathResponse(TypedDict, closed=True):
    path: NotRequired["capo_workdocs.types.resource_path.ResourcePath"]
    """<p>The path information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderPathResponse) -> dict:
    out: dict = {}
    if "path" in value:
        import capo_workdocs.types.resource_path

        out["Path"] = capo_workdocs.types.resource_path.serialize_json(value["path"])
    return out


def deserialize_json(data: dict) -> GetFolderPathResponse:
    out: GetFolderPathResponse = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        import capo_workdocs.types.resource_path

        out["path"] = capo_workdocs.types.resource_path.deserialize_json(data["Path"])
    return out


def redact_sensitive(value: GetFolderPathResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "path" in value:
        import capo_workdocs.types.resource_path

        out["path"] = capo_workdocs.types.resource_path.redact_sensitive(value["path"])
    return out
