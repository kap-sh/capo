"""Generated from Smithy shape ``com.amazonaws.launchwizard#UpdateDeploymentInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_id
    import capo_launch_wizard.types.deployment_pattern_version_name
    import capo_launch_wizard.types.deployment_specifications
    import capo_launch_wizard.types.workload_version_name


class UpdateDeploymentInput(TypedDict, closed=True):
    deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    specifications: (
        "capo_launch_wizard.types.deployment_specifications.DeploymentSpecifications"
    )
    """<p>The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html">SAP deployment specifications</a>. To retrieve the specifications required to create a deployment for other workloads, use the <a href="https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html"> <code>GetWorkloadDeploymentPattern</code> </a> operation.</p>"""
    workload_version_name: NotRequired[
        "capo_launch_wizard.types.workload_version_name.WorkloadVersionName"
    ]
    """<p>The name of the workload version.</p>"""
    deployment_pattern_version_name: NotRequired[
        "capo_launch_wizard.types.deployment_pattern_version_name.DeploymentPatternVersionName"
    ]
    """<p>The name of the deployment pattern version.</p>"""
    dry_run: NotRequired["bool"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    force: NotRequired["bool"]
    """<p>Forces the update even if validation warnings are present.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    import capo_launch_wizard.types.deployment_specifications

    out["specifications"] = (
        capo_launch_wizard.types.deployment_specifications.serialize_json(
            value["specifications"]
        )
    )
    if "workload_version_name" in value:
        out["workloadVersionName"] = value["workload_version_name"]
    if "deployment_pattern_version_name" in value:
        out["deploymentPatternVersionName"] = value["deployment_pattern_version_name"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_json(data: dict) -> UpdateDeploymentInput:
    out: UpdateDeploymentInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("specifications") is not None:
        import capo_launch_wizard.types.deployment_specifications

        out["specifications"] = (
            capo_launch_wizard.types.deployment_specifications.deserialize_json(
                data["specifications"]
            )
        )
    else:
        out["specifications"] = {}
    if data.get("workloadVersionName") is not None:
        out["workload_version_name"] = data["workloadVersionName"]
    if data.get("deploymentPatternVersionName") is not None:
        out["deployment_pattern_version_name"] = data["deploymentPatternVersionName"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out


def redact_sensitive(value: UpdateDeploymentInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "specifications" in value:
        out["specifications"] = "*** Sensitive Data Redacted ***"
    return out
