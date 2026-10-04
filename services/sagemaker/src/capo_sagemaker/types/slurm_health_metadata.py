"""Generated from Smithy shape ``com.amazonaws.sagemaker#SlurmHealthMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.slurm_health_component
    import capo_sagemaker.types.slurm_health_reason
    import capo_sagemaker.types.slurm_health_status


class SlurmHealthMetadata(TypedDict, closed=True):
    component: NotRequired[
        "capo_sagemaker.types.slurm_health_component.SlurmHealthComponent"
    ]
    """<p>The Slurm component that the health information describes. The valid value is <code>Slurmdbd</code>, the Slurm accounting daemon.</p>"""
    status: NotRequired["capo_sagemaker.types.slurm_health_status.SlurmHealthStatus"]
    """<p>The health of the component. Valid values are <code>Healthy</code> and <code>Unhealthy</code>.</p>"""
    reason: NotRequired["capo_sagemaker.types.slurm_health_reason.SlurmHealthReason"]
    """<p>The reason the component is unhealthy. Valid values:</p> <ul> <li> <p> <code>DaemonDown</code>: The daemon is not running, so job accounting records are not being written.</p> </li> <li> <p> <code>DaemonDisabled</code>: The daemon is running and its accounting database is responding, but the daemon is not enabled to start automatically. Job accounting stops the next time the controller node restarts.</p> </li> <li> <p> <code>DbUnreachable</code>: The daemon is running, but its accounting database did not respond. Job accounting records might not be written.</p> </li> </ul> <p>This field is omitted when the component is healthy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlurmHealthMetadata) -> dict:
    out: dict = {}
    if "component" in value:
        import capo_sagemaker.types.slurm_health_component

        out["Component"] = (
            capo_sagemaker.types.slurm_health_component.serialize_aws_json_1_1(
                value["component"]
            )
        )
    if "status" in value:
        import capo_sagemaker.types.slurm_health_status

        out["Status"] = capo_sagemaker.types.slurm_health_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "reason" in value:
        import capo_sagemaker.types.slurm_health_reason

        out["Reason"] = capo_sagemaker.types.slurm_health_reason.serialize_aws_json_1_1(
            value["reason"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SlurmHealthMetadata:
    out: SlurmHealthMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Component") is not None:
        import capo_sagemaker.types.slurm_health_component

        out["component"] = (
            capo_sagemaker.types.slurm_health_component.deserialize_aws_json_1_1(
                data["Component"]
            )
        )
    if data.get("Status") is not None:
        import capo_sagemaker.types.slurm_health_status

        out["status"] = (
            capo_sagemaker.types.slurm_health_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Reason") is not None:
        import capo_sagemaker.types.slurm_health_reason

        out["reason"] = (
            capo_sagemaker.types.slurm_health_reason.deserialize_aws_json_1_1(
                data["Reason"]
            )
        )
    return out
