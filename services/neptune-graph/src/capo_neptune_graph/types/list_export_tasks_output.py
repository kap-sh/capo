"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListExportTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.export_task_summary_list
    import capo_neptune_graph.types.pagination_token


class ListExportTasksOutput(TypedDict, closed=True):
    tasks: "capo_neptune_graph.types.export_task_summary_list.ExportTaskSummaryList"
    """<p>The requested list of export tasks.</p>"""
    next_token: NotRequired["capo_neptune_graph.types.pagination_token.PaginationToken"]
    """<p>Pagination token used to paginate output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportTasksOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.export_task_summary_list

    out["tasks"] = capo_neptune_graph.types.export_task_summary_list.serialize_json(
        value["tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportTasksOutput:
    out: ListExportTasksOutput = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_neptune_graph.types.export_task_summary_list

        out["tasks"] = (
            capo_neptune_graph.types.export_task_summary_list.deserialize_json(
                data["tasks"]
            )
        )
    else:
        out["tasks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
