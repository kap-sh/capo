"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetWorkloadDeploymentPatternInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.workload_name


class GetWorkloadDeploymentPatternInput(TypedDict, closed=True):
    workload_name: "capo_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload.</p>"""
    deployment_pattern_name: (
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    )
    """<p>The name of the deployment pattern.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkloadDeploymentPatternInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["deploymentPatternName"] = value["deployment_pattern_name"]
    return out


def deserialize_json(data: dict) -> GetWorkloadDeploymentPatternInput:
    out: GetWorkloadDeploymentPatternInput = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        out["workload_name"] = ""
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    else:
        out["deployment_pattern_name"] = ""
    return out
