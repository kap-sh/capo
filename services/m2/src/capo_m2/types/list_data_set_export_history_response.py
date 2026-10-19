"""Generated from Smithy shape ``com.amazonaws.m2#ListDataSetExportHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.data_set_export_task_list
    import capo_m2.types.next_token


class ListDataSetExportHistoryResponse(TypedDict, closed=True):
    data_set_export_tasks: (
        "capo_m2.types.data_set_export_task_list.DataSetExportTaskList"
    )
    """<p>The data set export tasks.</p>"""
    next_token: NotRequired["capo_m2.types.next_token.NextToken"]
    """<p>If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataSetExportHistoryResponse) -> dict:
    out: dict = {}
    import capo_m2.types.data_set_export_task_list

    out["dataSetExportTasks"] = capo_m2.types.data_set_export_task_list.serialize_json(
        value["data_set_export_tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataSetExportHistoryResponse:
    out: ListDataSetExportHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSetExportTasks") is not None:
        import capo_m2.types.data_set_export_task_list

        out["data_set_export_tasks"] = (
            capo_m2.types.data_set_export_task_list.deserialize_json(
                data["dataSetExportTasks"]
            )
        )
    else:
        out["data_set_export_tasks"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
