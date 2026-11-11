"""Generated from Smithy shape ``com.amazonaws.batch#EksContainerLinuxCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.eks_container_linux_capability_list


class EksContainerLinuxCapabilities(TypedDict, closed=True):
    add: NotRequired[
        "capo_batch.types.eks_container_linux_capability_list.EksContainerLinuxCapabilityList"
    ]
    """<p>The Linux capabilities to add to the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the <code>CAP_</code> prefix.</p>"""
    drop: NotRequired[
        "capo_batch.types.eks_container_linux_capability_list.EksContainerLinuxCapabilityList"
    ]
    """<p>The Linux capabilities to remove from the default capability set for the container. This parameter contains up to 64 values. Specify capability names without the <code>CAP_</code> prefix.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksContainerLinuxCapabilities) -> dict:
    out: dict = {}
    if "add" in value:
        import capo_batch.types.eks_container_linux_capability_list

        out["add"] = (
            capo_batch.types.eks_container_linux_capability_list.serialize_json(
                value["add"]
            )
        )
    if "drop" in value:
        import capo_batch.types.eks_container_linux_capability_list

        out["drop"] = (
            capo_batch.types.eks_container_linux_capability_list.serialize_json(
                value["drop"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksContainerLinuxCapabilities:
    out: EksContainerLinuxCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("add") is not None:
        import capo_batch.types.eks_container_linux_capability_list

        out["add"] = (
            capo_batch.types.eks_container_linux_capability_list.deserialize_json(
                data["add"]
            )
        )
    if data.get("drop") is not None:
        import capo_batch.types.eks_container_linux_capability_list

        out["drop"] = (
            capo_batch.types.eks_container_linux_capability_list.deserialize_json(
                data["drop"]
            )
        )
    return out
