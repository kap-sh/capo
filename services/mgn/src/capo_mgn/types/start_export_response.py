"""Generated from Smithy shape ``com.amazonaws.mgn#StartExportResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.export_task


class StartExportResponse(TypedDict, closed=True):
    export_task: NotRequired["capo_mgn.types.export_task.ExportTask"]
    """<p>Start export response export task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExportResponse) -> dict:
    out: dict = {}
    if "export_task" in value:
        import capo_mgn.types.export_task

        out["exportTask"] = capo_mgn.types.export_task.serialize_json(
            value["export_task"]
        )
    return out


def deserialize_json(data: dict) -> StartExportResponse:
    out: StartExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("exportTask") is not None:
        import capo_mgn.types.export_task

        out["export_task"] = capo_mgn.types.export_task.deserialize_json(
            data["exportTask"]
        )
    return out


def redact_sensitive(value: StartExportResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "export_task" in value:
        import capo_mgn.types.export_task

        out["export_task"] = capo_mgn.types.export_task.redact_sensitive(
            value["export_task"]
        )
    return out
