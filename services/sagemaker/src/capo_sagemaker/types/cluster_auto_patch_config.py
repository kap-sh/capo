"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterAutoPatchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_patch_schedule
    import capo_sagemaker.types.cluster_patching_strategy
    import capo_sagemaker.types.deployment_configuration


class ClusterAutoPatchConfig(TypedDict, closed=True):
    patching_strategy: (
        "capo_sagemaker.types.cluster_patching_strategy.ClusterPatchingStrategy"
    )
    """<p>The strategy for applying patches to instances in the group.</p> <ul> <li> <p> <code>WhenIdle</code>: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.</p> </li> <li> <p> <code>WhenAllIdle</code>: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.</p> </li> </ul>"""
    patch_schedule: NotRequired[
        "capo_sagemaker.types.cluster_patch_schedule.ClusterPatchSchedule"
    ]
    """<p>The schedule for automatic patching, including the next patch date.</p>"""
    deployment_config: NotRequired[
        "capo_sagemaker.types.deployment_configuration.DeploymentConfiguration"
    ]
    """<p>The deployment configuration for rolling patch updates, including rollback settings and batch sizes. Only applicable when using a rolling patching strategy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterAutoPatchConfig) -> dict:
    out: dict = {}
    import capo_sagemaker.types.cluster_patching_strategy

    out["PatchingStrategy"] = (
        capo_sagemaker.types.cluster_patching_strategy.serialize_aws_json_1_1(
            value["patching_strategy"]
        )
    )
    if "patch_schedule" in value:
        import capo_sagemaker.types.cluster_patch_schedule

        out["PatchSchedule"] = (
            capo_sagemaker.types.cluster_patch_schedule.serialize_aws_json_1_1(
                value["patch_schedule"]
            )
        )
    if "deployment_config" in value:
        import capo_sagemaker.types.deployment_configuration

        out["DeploymentConfig"] = (
            capo_sagemaker.types.deployment_configuration.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterAutoPatchConfig:
    out: ClusterAutoPatchConfig = {}  # type: ignore[typeddict-item]
    if data.get("PatchingStrategy") is not None:
        import capo_sagemaker.types.cluster_patching_strategy

        out["patching_strategy"] = (
            capo_sagemaker.types.cluster_patching_strategy.deserialize_aws_json_1_1(
                data["PatchingStrategy"]
            )
        )
    else:
        import typing

        out["patching_strategy"] = typing.cast(
            "capo_sagemaker.types.cluster_patching_strategy.ClusterPatchingStrategy", ""
        )
    if data.get("PatchSchedule") is not None:
        import capo_sagemaker.types.cluster_patch_schedule

        out["patch_schedule"] = (
            capo_sagemaker.types.cluster_patch_schedule.deserialize_aws_json_1_1(
                data["PatchSchedule"]
            )
        )
    if data.get("DeploymentConfig") is not None:
        import capo_sagemaker.types.deployment_configuration

        out["deployment_config"] = (
            capo_sagemaker.types.deployment_configuration.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    return out
