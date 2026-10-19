"""Generated from Smithy shape ``com.amazonaws.ssm#CancelMaintenanceWindowExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_window_execution_id


class CancelMaintenanceWindowExecutionRequest(TypedDict, closed=True):
    window_execution_id: (
        "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId"
    )
    """<p>The ID of the maintenance window execution to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelMaintenanceWindowExecutionRequest) -> dict:
    out: dict = {}
    out["WindowExecutionId"] = value["window_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelMaintenanceWindowExecutionRequest:
    out: CancelMaintenanceWindowExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("WindowExecutionId") is not None:
        out["window_execution_id"] = data["WindowExecutionId"]
    else:
        out["window_execution_id"] = ""
    return out
