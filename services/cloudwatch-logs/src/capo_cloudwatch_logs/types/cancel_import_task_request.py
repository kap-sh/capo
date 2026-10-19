"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CancelImportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.import_id


class CancelImportTaskRequest(TypedDict, closed=True):
    import_id: "capo_cloudwatch_logs.types.import_id.ImportId"
    """<p>The ID of the import task to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelImportTaskRequest) -> dict:
    out: dict = {}
    out["importId"] = value["import_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelImportTaskRequest:
    out: CancelImportTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("importId") is not None:
        out["import_id"] = data["importId"]
    else:
        out["import_id"] = ""
    return out
