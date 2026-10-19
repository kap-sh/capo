"""Generated from Smithy shape ``com.amazonaws.applicationinsights#RemoveWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.component_name
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.workload_id


class RemoveWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "capo_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_id: "capo_application_insights.types.workload_id.WorkloadId"
    """<p>The ID of the workload.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoveWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    out["WorkloadId"] = value["workload_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RemoveWorkloadRequest:
    out: RemoveWorkloadRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceGroupName") is not None:
        out["resource_group_name"] = data["ResourceGroupName"]
    else:
        out["resource_group_name"] = ""
    if data.get("ComponentName") is not None:
        out["component_name"] = data["ComponentName"]
    else:
        out["component_name"] = ""
    if data.get("WorkloadId") is not None:
        out["workload_id"] = data["WorkloadId"]
    else:
        out["workload_id"] = ""
    return out
