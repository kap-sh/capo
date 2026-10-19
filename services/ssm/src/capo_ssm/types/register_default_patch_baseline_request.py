"""Generated from Smithy shape ``com.amazonaws.ssm#RegisterDefaultPatchBaselineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.baseline_id


class RegisterDefaultPatchBaselineRequest(TypedDict, closed=True):
    baseline_id: "capo_ssm.types.baseline_id.BaselineId"
    """<p>The ID of the patch baseline that should be the default patch baseline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterDefaultPatchBaselineRequest) -> dict:
    out: dict = {}
    out["BaselineId"] = value["baseline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterDefaultPatchBaselineRequest:
    out: RegisterDefaultPatchBaselineRequest = {}  # type: ignore[typeddict-item]
    if data.get("BaselineId") is not None:
        out["baseline_id"] = data["BaselineId"]
    else:
        out["baseline_id"] = ""
    return out
