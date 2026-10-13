"""Generated from Smithy shape ``com.amazonaws.mgn#StartImportResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.import_task


class StartImportResponse(TypedDict, closed=True):
    import_task: NotRequired["capo_mgn.types.import_task.ImportTask"]
    """<p>Start import response import task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportResponse) -> dict:
    out: dict = {}
    if "import_task" in value:
        import capo_mgn.types.import_task

        out["importTask"] = capo_mgn.types.import_task.serialize_json(
            value["import_task"]
        )
    return out


def deserialize_json(data: dict) -> StartImportResponse:
    out: StartImportResponse = {}  # type: ignore[typeddict-item]
    if data.get("importTask") is not None:
        import capo_mgn.types.import_task

        out["import_task"] = capo_mgn.types.import_task.deserialize_json(
            data["importTask"]
        )
    return out


def redact_sensitive(value: StartImportResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "import_task" in value:
        import capo_mgn.types.import_task

        out["import_task"] = capo_mgn.types.import_task.redact_sensitive(
            value["import_task"]
        )
    return out
