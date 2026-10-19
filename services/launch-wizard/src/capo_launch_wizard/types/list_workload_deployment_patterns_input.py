"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListWorkloadDeploymentPatternsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.max_workload_deployment_pattern_results
    import capo_launch_wizard.types.next_token
    import capo_launch_wizard.types.workload_name


class ListWorkloadDeploymentPatternsInput(TypedDict, closed=True):
    workload_name: "capo_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload.</p>"""
    max_results: NotRequired[
        "capo_launch_wizard.types.max_workload_deployment_pattern_results.MaxWorkloadDeploymentPatternResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["capo_launch_wizard.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadDeploymentPatternsInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadDeploymentPatternsInput:
    out: ListWorkloadDeploymentPatternsInput = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        out["workload_name"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
