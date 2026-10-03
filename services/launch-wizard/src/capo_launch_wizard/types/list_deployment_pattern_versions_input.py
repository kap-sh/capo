"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentPatternVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.filter_list
    import capo_launch_wizard.types.max_workload_results
    import capo_launch_wizard.types.next_token
    import capo_launch_wizard.types.workload_name


class ListDeploymentPatternVersionsInput(TypedDict, closed=True):
    workload_name: "capo_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>"""
    deployment_pattern_name: (
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    )
    """<p>The name of the deployment pattern. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter.</p>"""
    max_results: NotRequired[
        "capo_launch_wizard.types.max_workload_results.MaxWorkloadResults"
    ]
    """<p>The maximum number of deployment pattern versions to list.</p>"""
    next_token: NotRequired["capo_launch_wizard.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    filters: NotRequired["capo_launch_wizard.types.filter_list.FilterList"]
    """<p>Filters to apply when listing deployment pattern versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentPatternVersionsInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["deploymentPatternName"] = value["deployment_pattern_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "filters" in value:
        import capo_launch_wizard.types.filter_list

        out["filters"] = capo_launch_wizard.types.filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListDeploymentPatternVersionsInput:
    out: ListDeploymentPatternVersionsInput = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError(
            "ListDeploymentPatternVersionsInput.workload_name required"
        )
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    else:
        raise DeserializationError(
            "ListDeploymentPatternVersionsInput.deployment_pattern_name required"
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("filters") is not None:
        import capo_launch_wizard.types.filter_list

        out["filters"] = capo_launch_wizard.types.filter_list.deserialize_json(
            data["filters"]
        )
    return out
