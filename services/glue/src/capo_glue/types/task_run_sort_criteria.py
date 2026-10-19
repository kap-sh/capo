"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.sort_direction_type
    import capo_glue.types.task_run_sort_column_type


class TaskRunSortCriteria(TypedDict, closed=True):
    column: "capo_glue.types.task_run_sort_column_type.TaskRunSortColumnType"
    """<p>The column to be used to sort the list of task runs for the machine learning transform.</p>"""
    sort_direction: "capo_glue.types.sort_direction_type.SortDirectionType"
    """<p>The sort direction to be used to sort the list of task runs for the machine learning transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunSortCriteria) -> dict:
    out: dict = {}
    import capo_glue.types.task_run_sort_column_type

    out["Column"] = capo_glue.types.task_run_sort_column_type.serialize_aws_json_1_1(
        value["column"]
    )
    import capo_glue.types.sort_direction_type

    out["SortDirection"] = capo_glue.types.sort_direction_type.serialize_aws_json_1_1(
        value["sort_direction"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRunSortCriteria:
    out: TaskRunSortCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Column") is not None:
        import capo_glue.types.task_run_sort_column_type

        out["column"] = (
            capo_glue.types.task_run_sort_column_type.deserialize_aws_json_1_1(
                data["Column"]
            )
        )
    else:
        import typing

        out["column"] = typing.cast(
            "capo_glue.types.task_run_sort_column_type.TaskRunSortColumnType", ""
        )
    if data.get("SortDirection") is not None:
        import capo_glue.types.sort_direction_type

        out["sort_direction"] = (
            capo_glue.types.sort_direction_type.deserialize_aws_json_1_1(
                data["SortDirection"]
            )
        )
    else:
        import typing

        out["sort_direction"] = typing.cast(
            "capo_glue.types.sort_direction_type.SortDirectionType", ""
        )
    return out
