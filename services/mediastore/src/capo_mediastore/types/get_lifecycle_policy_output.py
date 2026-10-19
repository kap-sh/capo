"""Generated from Smithy shape ``com.amazonaws.mediastore#GetLifecyclePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.lifecycle_policy


class GetLifecyclePolicyOutput(TypedDict, closed=True):
    lifecycle_policy: "capo_mediastore.types.lifecycle_policy.LifecyclePolicy"
    """<p>The object lifecycle policy that is assigned to the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyOutput) -> dict:
    out: dict = {}
    out["LifecyclePolicy"] = value["lifecycle_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyOutput:
    out: GetLifecyclePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("LifecyclePolicy") is not None:
        out["lifecycle_policy"] = data["LifecyclePolicy"]
    else:
        out["lifecycle_policy"] = ""
    return out
