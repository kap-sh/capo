"""Generated from Smithy shape ``com.amazonaws.mediastore#PutLifecyclePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.container_name
    import capo_mediastore.types.lifecycle_policy


class PutLifecyclePolicyInput(TypedDict, closed=True):
    container_name: "capo_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that you want to assign the object lifecycle policy to.</p>"""
    lifecycle_policy: "capo_mediastore.types.lifecycle_policy.LifecyclePolicy"
    """<p>The object lifecycle policy to apply to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutLifecyclePolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    out["LifecyclePolicy"] = value["lifecycle_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutLifecyclePolicyInput:
    out: PutLifecyclePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    else:
        out["container_name"] = ""
    if data.get("LifecyclePolicy") is not None:
        out["lifecycle_policy"] = data["LifecyclePolicy"]
    else:
        out["lifecycle_policy"] = ""
    return out
