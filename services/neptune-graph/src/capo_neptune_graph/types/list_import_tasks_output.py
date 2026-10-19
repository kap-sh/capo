"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListImportTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.import_task_summary_list
    import capo_neptune_graph.types.pagination_token


class ListImportTasksOutput(TypedDict, closed=True):
    tasks: "capo_neptune_graph.types.import_task_summary_list.ImportTaskSummaryList"
    """<p>The requested list of import tasks.</p>"""
    next_token: NotRequired["capo_neptune_graph.types.pagination_token.PaginationToken"]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportTasksOutput) -> dict:
    out: dict = {}
    import capo_neptune_graph.types.import_task_summary_list

    out["tasks"] = capo_neptune_graph.types.import_task_summary_list.serialize_json(
        value["tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportTasksOutput:
    out: ListImportTasksOutput = {}  # type: ignore[typeddict-item]
    if data.get("tasks") is not None:
        import capo_neptune_graph.types.import_task_summary_list

        out["tasks"] = (
            capo_neptune_graph.types.import_task_summary_list.deserialize_json(
                data["tasks"]
            )
        )
    else:
        out["tasks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
