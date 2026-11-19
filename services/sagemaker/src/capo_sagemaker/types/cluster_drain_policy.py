"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterDrainPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_on_drain_timeout
    import capo_sagemaker.types.drain_timeout_in_seconds_value


class ClusterDrainPolicy(TypedDict, closed=True):
    drain_timeout_in_seconds: NotRequired[
        "capo_sagemaker.types.drain_timeout_in_seconds_value.DrainTimeoutInSecondsValue"
    ]
    """<p>The maximum time, in seconds, to wait for the pods on an instance to drain. Valid values are from 0 to 5400 (90 minutes). The default is 3600 (1 hour).</p>"""
    on_drain_timeout: NotRequired[
        "capo_sagemaker.types.cluster_on_drain_timeout.ClusterOnDrainTimeout"
    ]
    """<p>The action to take if the pods on an instance don't drain within <code>DrainTimeoutInSeconds</code>. The default is <code>Skip</code>.</p> <ul> <li> <p> <code>Skip</code>: Doesn't patch the instance. The instance is uncordoned and remains on the previous AMI version. This can leave the instance group partially patched. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.</p> </li> <li> <p> <code>Force</code>: Deletes the remaining pods without respecting Pod Disruption Budgets, and then patches the instance.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterDrainPolicy) -> dict:
    out: dict = {}
    if "drain_timeout_in_seconds" in value:
        out["DrainTimeoutInSeconds"] = value["drain_timeout_in_seconds"]
    if "on_drain_timeout" in value:
        import capo_sagemaker.types.cluster_on_drain_timeout

        out["OnDrainTimeout"] = (
            capo_sagemaker.types.cluster_on_drain_timeout.serialize_aws_json_1_1(
                value["on_drain_timeout"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterDrainPolicy:
    out: ClusterDrainPolicy = {}  # type: ignore[typeddict-item]
    if data.get("DrainTimeoutInSeconds") is not None:
        out["drain_timeout_in_seconds"] = data["DrainTimeoutInSeconds"]
    if data.get("OnDrainTimeout") is not None:
        import capo_sagemaker.types.cluster_on_drain_timeout

        out["on_drain_timeout"] = (
            capo_sagemaker.types.cluster_on_drain_timeout.deserialize_aws_json_1_1(
                data["OnDrainTimeout"]
            )
        )
    return out
