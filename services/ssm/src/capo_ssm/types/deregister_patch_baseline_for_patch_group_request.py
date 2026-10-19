"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterPatchBaselineForPatchGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id
    import capo_ssm.types.patch_group


class DeregisterPatchBaselineForPatchGroupRequest(TypedDict, closed=True):
    baseline_id: "capo_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline to deregister the patch group from.</p>"""
    patch_group: "capo_ssm.types.patch_group.PatchGroup"
    """<p>The name of the patch group that should be deregistered from the patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterPatchBaselineForPatchGroupRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    out["PatchGroup"] = value["patch_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterPatchBaselineForPatchGroupRequest:
    out: DeregisterPatchBaselineForPatchGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    else:
        out["baseline_id"] = ""
    if data.get("PatchGroup") is not None:
        out["patch_group"] = data["PatchGroup"]
    else:
        out["patch_group"] = ""
    return out
