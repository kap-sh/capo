"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeWorkloadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_insights.types.account_id
    import capo_application_insights.types.component_name
    import capo_application_insights.types.resource_group_name
    import capo_application_insights.types.workload_id


class DescribeWorkloadRequest(TypedDict, closed=True):
    resource_group_name: (
        "capo_application_insights.types.resource_group_name.ResourceGroupName"
    )
    """<p>The name of the resource group.</p>"""
    component_name: "capo_application_insights.types.component_name.ComponentName"
    """<p>The name of the component.</p>"""
    workload_id: "capo_application_insights.types.workload_id.WorkloadId"
    """<p>The ID of the workload.</p>"""
    account_id: NotRequired["capo_application_insights.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID for the workload owner.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkloadRequest) -> dict:
    out: dict = {}
    out["ResourceGroupName"] = value["resource_group_name"]
    out["ComponentName"] = value["component_name"]
    out["WorkloadId"] = value["workload_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkloadRequest:
    out: DescribeWorkloadRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
