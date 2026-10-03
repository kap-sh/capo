"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerResourceRequirements``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_limits
    import capo_batch.types.eks_requests


class EksContainerResourceRequirements(TypedDict, closed=True):
    limits: NotRequired["capo_batch.types.eks_limits.EksLimits"]
    """<p>The type and quantity of the resources to reserve for the container. The values vary based on the <code>name</code> that's specified. Resources can be requested using either the <code>limits</code> or the <code>requests</code> objects.</p> <dl> <dt>memory</dt> <dd> <p>The memory hard limit (in MiB) for the container, using whole integers, with a "Mi" suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. <code>memory</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>memory</code> is specified in both places, then the value that's specified in <code>limits</code> must be equal to the value that's specified in <code>requests</code>.</p> <note> <p>To maximize your resource utilization, provide your jobs with as much memory as possible for the specific instance type that you are using. To learn how, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html">Memory management</a> in the <i>Batch User Guide</i>.</p> </note> </dd> <dt>cpu</dt> <dd> <p>The number of CPUs that's reserved for the container. Values must be an even multiple of <code>0.25</code>. <code>cpu</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>cpu</code> is specified in both places, then the value that's specified in <code>limits</code> must be at least as large as the value that's specified in <code>requests</code>.</p> </dd> <dt>nvidia.com/gpu</dt> <dd> <p>The number of GPUs that's reserved for the container. Values must be a whole integer. <code>memory</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>memory</code> is specified in both places, then the value that's specified in <code>limits</code> must be equal to the value that's specified in <code>requests</code>.</p> </dd> </dl>"""
    requests: NotRequired["capo_batch.types.eks_requests.EksRequests"]
    """<p>The type and quantity of the resources to request for the container. The values vary based on the <code>name</code> that's specified. Resources can be requested by using either the <code>limits</code> or the <code>requests</code> objects.</p> <dl> <dt>memory</dt> <dd> <p>The memory hard limit (in MiB) for the container, using whole integers, with a "Mi" suffix. If your container attempts to exceed the memory specified, the container is terminated. You must specify at least 4 MiB of memory for a job. <code>memory</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>memory</code> is specified in both, then the value that's specified in <code>limits</code> must be equal to the value that's specified in <code>requests</code>.</p> <note> <p>If you're trying to maximize your resource utilization by providing your jobs as much memory as possible for a particular instance type, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/memory-management.html">Memory management</a> in the <i>Batch User Guide</i>.</p> </note> </dd> <dt>cpu</dt> <dd> <p>The number of CPUs that are reserved for the container. Values must be an even multiple of <code>0.25</code>. <code>cpu</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>cpu</code> is specified in both, then the value that's specified in <code>limits</code> must be at least as large as the value that's specified in <code>requests</code>.</p> </dd> <dt>nvidia.com/gpu</dt> <dd> <p>The number of GPUs that are reserved for the container. Values must be a whole integer. <code>nvidia.com/gpu</code> can be specified in <code>limits</code>, <code>requests</code>, or both. If <code>nvidia.com/gpu</code> is specified in both, then the value that's specified in <code>limits</code> must be equal to the value that's specified in <code>requests</code>.</p> </dd> </dl>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerResourceRequirements) -> dict:
    out: dict = {}
    if "limits" in value:
        import capo_batch.types.eks_limits

        out["limits"] = capo_batch.types.eks_limits.serialize_json(value["limits"])
    if "requests" in value:
        import capo_batch.types.eks_requests

        out["requests"] = capo_batch.types.eks_requests.serialize_json(
            value["requests"]
        )
    return out


def deserialize_json(data: dict) -> EksContainerResourceRequirements:
    out: EksContainerResourceRequirements = {}  # type: ignore[typeddict-item]
    if data.get("limits") is not None:
        import capo_batch.types.eks_limits

        out["limits"] = capo_batch.types.eks_limits.deserialize_json(data["limits"])
    if data.get("requests") is not None:
        import capo_batch.types.eks_requests

        out["requests"] = capo_batch.types.eks_requests.deserialize_json(
            data["requests"]
        )
    return out
