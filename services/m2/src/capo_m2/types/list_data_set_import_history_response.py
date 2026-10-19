"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetImportHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_task_list
    import capo_m2.types.next_token


class ListDataSetImportHistoryResponse(TypedDict, closed=True):
    data_set_import_tasks: (
        "capo_m2.types.data_set_import_task_list.DataSetImportTaskList"
    )
    """<p>The data set import tasks.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetImportHistoryResponse) -> dict:
    out: dict = {}
    import capo_m2.types.data_set_import_task_list

    out["dataSetImportTasks"] = capo_m2.types.data_set_import_task_list.serialize_json(
        value["data_set_import_tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetImportHistoryResponse:
    out: ListDataSetImportHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSetImportTasks") is not None:
        import capo_m2.types.data_set_import_task_list

        out["data_set_import_tasks"] = (
            capo_m2.types.data_set_import_task_list.deserialize_json(
                data["dataSetImportTasks"]
            )
        )
    else:
        out["data_set_import_tasks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
