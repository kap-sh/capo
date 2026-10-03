"""Generated from Smithy shape ``com.amazonaws.launchwizard#CreateDeploymentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_launch_wizard.errors import DeserializationError

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_name
    import capo_launch_wizard.types.deployment_pattern_name
    import capo_launch_wizard.types.deployment_specifications
    import capo_launch_wizard.types.tags
    import capo_launch_wizard.types.workload_name


class CreateDeploymentInput(TypedDict, closed=True):
    workload_name: "capo_launch_wizard.types.workload_name.WorkloadName"
    """<p>The name of the workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloads.html"> <code>ListWorkloads</code> </a> operation to discover supported values for this parameter.</p>"""
    deployment_pattern_name: (
        "capo_launch_wizard.types.deployment_pattern_name.DeploymentPatternName"
    )
    """<p>The name of the deployment pattern supported by a given workload. You can use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_ListWorkloadDeploymentPatterns.html"> <code>ListWorkloadDeploymentPatterns</code> </a> operation to discover supported values for this parameter. </p>"""
    name: "capo_launch_wizard.types.deployment_name.DeploymentName"
    """<p>The name of the deployment.</p>"""
    specifications: (
        "capo_launch_wizard.types.deployment_specifications.DeploymentSpecifications"
    )
    """<p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>"""
    dry_run: "bool"
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tags: NotRequired["capo_launch_wizard.types.tags.Tags"]
    """<p>The tags to add to the deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentInput) -> dict:
    out: dict = {}
    out["workloadName"] = value["workload_name"]
    out["deploymentPatternName"] = value["deployment_pattern_name"]
    out["name"] = value["name"]
    import capo_launch_wizard.types.deployment_specifications

    out["specifications"] = (
        capo_launch_wizard.types.deployment_specifications.serialize_json(
            value["specifications"]
        )
    )
    out["dryRun"] = value.get("dry_run", False)
    if "tags" in value:
        import capo_launch_wizard.types.tags

        out["tags"] = capo_launch_wizard.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDeploymentInput:
    out: CreateDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    else:
        raise DeserializationError("CreateDeploymentInput.workload_name required")
    if data.get("deploymentPatternName") is not None:
        out["deployment_pattern_name"] = data["deploymentPatternName"]
    else:
        raise DeserializationError(
            "CreateDeploymentInput.deployment_pattern_name required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDeploymentInput.name required")
    if data.get("specifications") is not None:
        import capo_launch_wizard.types.deployment_specifications

        out["specifications"] = (
            capo_launch_wizard.types.deployment_specifications.deserialize_json(
                data["specifications"]
            )
        )
    else:
        raise DeserializationError("CreateDeploymentInput.specifications required")
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    if data.get("tags") is not None:
        import capo_launch_wizard.types.tags

        out["tags"] = capo_launch_wizard.types.tags.deserialize_json(data["tags"])
    return out
