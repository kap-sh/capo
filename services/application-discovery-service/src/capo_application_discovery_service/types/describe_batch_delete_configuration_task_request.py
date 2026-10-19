"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#DescribeBatchDeleteConfigurationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.uuid


class DescribeBatchDeleteConfigurationTaskRequest(TypedDict, closed=True):
    task_id: "capo_application_discovery_service.types.uuid.UUID"
    """<p> The ID of the task to delete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBatchDeleteConfigurationTaskRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBatchDeleteConfigurationTaskRequest:
    out: DescribeBatchDeleteConfigurationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    return out
