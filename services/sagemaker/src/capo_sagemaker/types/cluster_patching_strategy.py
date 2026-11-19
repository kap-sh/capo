"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterPatchingStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy for applying automatic patches to instances.</p> <ul> <li> <p> <code>WhenIdle</code>: Cordons all instances and patches each instance as it becomes idle (no running jobs). Each instance is uncordoned immediately after patching and becomes available for new jobs. If instances do not become idle, they remain on the previous AMI version. You can then use UpdateClusterSoftware with the desired ImageReleaseVersion to manually update the remaining instances.</p> </li> <li> <p> <code>WhenAllIdle</code>: Cordons all instances and waits for all to become idle before patching. All instances are uncordoned after patching completes. If not all instances become idle, no patching occurs and all instances remain on the previous AMI version.</p> </li> <li> <p> <code>DrainFirst</code>: Designed for workloads that never become idle, such as inference. Cordons instances, evicts the running pods, and then patches each instance in batches. Each instance is uncordoned after patching. Use <code>DrainPolicy</code> to control how long to wait for pods to drain and what happens if the drain times out. Requires <code>MaximumBatchSize</code> in <code>DeploymentConfig</code>. Available only for clusters that use Amazon EKS as the orchestrator.</p> </li> </ul>"""
ClusterPatchingStrategy: TypeAlias = Literal[
    "WhenIdle",
    "WhenAllIdle",
    "DrainFirst",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterPatchingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClusterPatchingStrategy:
    return cast(ClusterPatchingStrategy, data)
