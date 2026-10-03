"""Generated from Smithy shape ``com.amazonaws.batch#EksPodPropertiesOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_container_override_list
    import capo_batch.types.eks_metadata


class EksPodPropertiesOverride(TypedDict, closed=True):
    containers: NotRequired[
        "capo_batch.types.eks_container_override_list.EksContainerOverrideList"
    ]
    """<p>The overrides for the container that's used on the Amazon EKS pod.</p>"""
    init_containers: NotRequired[
        "capo_batch.types.eks_container_override_list.EksContainerOverrideList"
    ]
    """<p>The overrides for the <code>initContainers</code> defined in the Amazon EKS pod. These containers run before application containers, always run to completion, and must complete successfully before the next container starts. These containers are registered with the Amazon EKS Connector agent and persists the registration information in the Kubernetes backend data store. For more information, see <a href="https://kubernetes.io/docs/concepts/workloads/pods/init-containers/">Init Containers</a> in the <i>Kubernetes documentation</i>.</p>"""
    metadata: NotRequired["capo_batch.types.eks_metadata.EksMetadata"]
    """<p>Metadata about the overrides for the container that's used on the Amazon EKS pod.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksPodPropertiesOverride) -> dict:
    out: dict = {}
    if "containers" in value:
        import capo_batch.types.eks_container_override_list

        out["containers"] = capo_batch.types.eks_container_override_list.serialize_json(
            value["containers"]
        )
    if "init_containers" in value:
        import capo_batch.types.eks_container_override_list

        out["initContainers"] = (
            capo_batch.types.eks_container_override_list.serialize_json(
                value["init_containers"]
            )
        )
    if "metadata" in value:
        import capo_batch.types.eks_metadata

        out["metadata"] = capo_batch.types.eks_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> EksPodPropertiesOverride:
    out: EksPodPropertiesOverride = {}  # type: ignore[typeddict-item]
    if data.get("containers") is not None:
        import capo_batch.types.eks_container_override_list

        out["containers"] = (
            capo_batch.types.eks_container_override_list.deserialize_json(
                data["containers"]
            )
        )
    if data.get("initContainers") is not None:
        import capo_batch.types.eks_container_override_list

        out["init_containers"] = (
            capo_batch.types.eks_container_override_list.deserialize_json(
                data["initContainers"]
            )
        )
    if data.get("metadata") is not None:
        import capo_batch.types.eks_metadata

        out["metadata"] = capo_batch.types.eks_metadata.deserialize_json(
            data["metadata"]
        )
    return out
