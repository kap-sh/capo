"""Generated from Smithy shape ``com.amazonaws.datapipeline#ReportTaskProgressInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_data_pipeline.types.field_list
    import capo_data_pipeline.types.task_id


class ReportTaskProgressInput(TypedDict, closed=True):
    task_id: "capo_data_pipeline.types.task_id.taskId"
    """<p>The ID of the task assigned to the task runner. This value is provided in the response for <a>PollForTask</a>.</p>"""
    fields: NotRequired["capo_data_pipeline.types.field_list.fieldList"]
    """<p>Key-value pairs that define the properties of the ReportTaskProgressInput object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportTaskProgressInput) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    if "fields" in value:
        import capo_data_pipeline.types.field_list

        out["fields"] = capo_data_pipeline.types.field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportTaskProgressInput:
    out: ReportTaskProgressInput = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("fields") is not None:
        import capo_data_pipeline.types.field_list

        out["fields"] = capo_data_pipeline.types.field_list.deserialize_aws_json_1_1(
            data["fields"]
        )
    return out
