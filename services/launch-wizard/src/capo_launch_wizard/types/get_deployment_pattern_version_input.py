"""Generated from Smithy shape ``com.amazonaws.launchwizard#GetDeploymentPatternVersionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.deployment_pattern_version_name
    import capo_launch_wizard.types.workload_name


class GetDeploymentPatternVersionInput(TypedDict, closed=True):
    workload_name: "capo_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>"""
    deployment_pattern_name: (
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    )
    """<p>The name of the deployment pattern. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter.</p>"""
    deployment_pattern_version_name: "capo_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
    """<p>The name of the deployment pattern version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeploymentPatternVersionInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["deploymentPatternName"] = value["deployment_pattern_name"]
    out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    return out


def deserialize_json(data: dict) -> GetDeploymentPatternVersionInput:
    out: GetDeploymentPatternVersionInput = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError(
            "GetDeploymentPatternVersionInput.workload_name required"
        )
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    else:
        raise DeserializationError(
            "GetDeploymentPatternVersionInput.deployment_pattern_name required"
        )
    if data.get("deploymentPatternVersionName") is not None:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    else:
        raise DeserializationError(
            "GetDeploymentPatternVersionInput.deployment_pattern_version_name required"
        )
    return out
