"""Generated from Smithy shape ``com.amazonaws.mediastore#GetContainerPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.container_policy


class GetContainerPolicyOutput(TypedDict, closed=True):
    policy: "capo_mediastore.types.container_policy.ContainerPolicy"
    """<p>The contents of the access policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerPolicyOutput) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerPolicyOutput:
    out: GetContainerPolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
