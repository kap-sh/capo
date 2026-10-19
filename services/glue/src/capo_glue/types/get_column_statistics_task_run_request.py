"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class GetColumnStatisticsTaskRunRequest(TypedDict, closed=True):
    column_statistics_task_run_id: "capo_glue.types.hash_string.HashString"
    """<p>The identifier for the particular column statistics task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskRunRequest) -> dict:
    out: dict = {}
    out["ColumnStatisticsTaskRunId"] = value["column_statistics_task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskRunRequest:
    out: GetColumnStatisticsTaskRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("ColumnStatisticsTaskRunId") is not None:
        out["column_statistics_task_run_id"] = data["ColumnStatisticsTaskRunId"]
    else:
        out["column_statistics_task_run_id"] = ""
    return out
